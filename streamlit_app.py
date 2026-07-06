import streamlit as st
import random
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Supply & Demand Simulator",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# PASSWORD PROTECTION SYSTEM
# =====================================================================
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        if st.session_state["password"] == "Supply2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.markdown("<h1 style='text-align: center; color: #10B981;'>🔒 Secure Access</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Please enter the password to access the simulator.</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
        return False
    
    elif not st.session_state["password_correct"]:
        # Password incorrect, show input + error.
        st.markdown("<h1 style='text-align: center; color: #10B981;'>🔒 Secure Access</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            st.error("😕 Password incorrect. Please try again.")
        return False
    
    return True

if not check_password():
    st.stop()

# =====================================================================
# PREMIUM DESIGN SYSTEM (EMERALD & GOLD THEME)
# =====================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #022C22 0%, #064E3B 50%, #022C22 100%);
    }
    
    /* Header styling */
    .header-gradient {
        background: linear-gradient(135deg, #047857 0%, #10B981 50%, #F59E0B 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.15);
    }
    
    .header-gradient h1 {
        color: white !important;
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .header-gradient p {
        color: rgba(255, 255, 255, 0.95) !important;
        font-size: 1.1rem !important;
        margin: 0.5rem 0 0 0 !important;
    }
    
    /* Score banner */
    .score-banner {
        background: linear-gradient(135deg, #064E3B 0%, #065F46 100%);
        border: 2px solid #10B981;
        color: white;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(16, 185, 129, 0.2);
    }
    
    .score-banner h2 {
        color: #34D399 !important;
        margin: 0 !important;
        font-weight: 700;
        font-size: 1.8rem;
    }
    
    /* Container styling */
    .stContainer, .stForm {
        background: rgba(6, 78, 59, 0.8);
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }
    
    /* Section headers */
    .section-header {
        color: #FCD34D;
        font-weight: 700;
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid rgba(252, 211, 77, 0.3);
    }
    
    /* Concept note box */
    .concept-note, .case-study, .managerial-lesson, .real-world-app {
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .concept-note {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(52, 211, 153, 0.1) 100%);
        border-left: 4px solid #10B981;
    }
    .concept-note h3 { color: #34D399; margin-top: 0 !important; }
    
    .case-study {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(251, 191, 36, 0.05) 100%);
        border-left: 4px solid #F59E0B;
    }
    .case-study h4 { color: #FBBF24; margin-top: 0 !important; }
    
    /* Key metrics */
    .metric-card {
        background: rgba(2, 44, 34, 0.6);
        border: 1px solid rgba(52, 211, 153, 0.3);
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
    }
    
    .metric-card h3 {
        color: #6EE7B7;
        font-size: 1.2rem;
        margin: 0 0 0.5rem 0;
    }
    
    .metric-value {
        color: #FCD34D;
        font-size: 2rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    /* Buttons */
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #059669 0%, #10B981 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3) !important;
    }
    
    .stButton > button:hover, .stFormSubmitButton > button:hover {
        box-shadow: 0 8px 24px rgba(16, 185, 129, 0.5) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(6, 78, 59, 0.5);
        border-bottom: 2px solid rgba(16, 185, 129, 0.2);
    }
    
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #10B981 !important;
    }
    
    /* Text colors */
    .stMarkdown, p, li {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    .stRadio p, .stRadio label, div[role="radiogroup"] p {
        color: rgba(255, 255, 255, 0.95) !important;
        font-size: 1.05rem;
    }
    
    /* Sidebar */
    .stSidebar {
        background: linear-gradient(180deg, #022C22 0%, #064E3B 100%);
    }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SESSION STATE INITIALIZATION
# =====================================================================
def initialize_session_state():
    defaults = {
        'game_played': False,
        'game_score': 0.0,
        'quiz_score': 0.0,
        'qd': 0,
        'qs': 0,
        'price_set': 0,
        'status': "",
        'gap': 0,
        'game_history': [],
        'current_round': 0,
        'q1_answered': False, 'q1_correct': False,
        'q2_answered': False, 'q2_correct': False,
        'q3_answered': False, 'q3_correct': False,
        'q4_answered': False, 'q4_correct': False,
        'quiz_submitted': False
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()

# =====================================================================
# SIDEBAR: LEARNING PATH & NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("### 📚 Learning Path")
    learning_path = st.radio(
        "Select your focus:",
        options=[
            "🎮 Play & Learn",
            "📖 Conceptual Deep Dive",
            "📈 Price Elasticity",
            "📝 Knowledge Check",
            "💼 Executive Summary"
        ]
    )

# =====================================================================
# HEADER SECTION
# =====================================================================
st.markdown("""
<div class="header-gradient">
    <h1>⚖️ Supply & Demand Simulator</h1>
    <p>Master the fundamental laws of economics by finding market equilibrium, managing prices, and clearing the market.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# PERFORMANCE DASHBOARD
# =====================================================================
dashboard_col = st.container()
with dashboard_col:
    total_score = min(100, round(st.session_state.game_score + st.session_state.quiz_score))
    
    st.markdown(f"""
    <div class="score-banner">
        <h2>Overall Economics Score: {total_score} / 100</h2>
        <p style='color: #FCD34D;'>🎮 Market Efficiency Score: {round(st.session_state.game_score)}/50 | 📝 Quiz Score: {round(st.session_state.quiz_score)}/50</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# MAIN CONTENT ROUTING
# =====================================================================

if learning_path == "🎮 Play & Learn":
    game_section = st.container()
    with game_section:
        st.markdown('<div class="section-header">🎮 Phase 1: Find the Market Equilibrium</div>', unsafe_allow_html=True)
        
        col_concept, col_game = st.columns([1, 1.2])
        
        with col_concept:
            st.markdown("""
            <div class="concept-note">
            <h3>📌 Simulation Instructions</h3>
            <p><strong>Your Role:</strong> You are analyzing the market for a new <em>Eco-Friendly Smart Thermostat</em>. Your goal is to find the exact price that "clears the market."</p>
            <p><strong>The Rules:</strong></p>
            <ul>
                <li><strong>Law of Demand:</strong> As you raise the price, consumers will want to buy fewer units.</li>
                <li><strong>Law of Supply:</strong> As you raise the price, manufacturers are willing to produce more units.</li>
            </ul>
            <p><strong>Objective:</strong> Adjust the price until Quantity Demanded ($Q_d$) exactly equals Quantity Supplied ($Q_s$). If you price too high, you get a <em>Surplus</em>. If you price too low, you get a <em>Shortage</em>. The closer the gap is to zero, the higher your score!</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_game:
            st.markdown("""
            <div class="case-study">
            <h4>🎯 The Market Dashboard</h4>
            <p>Set your market price to bring buyers and sellers into harmony.</p>
            </div>
            """, unsafe_allow_html=True)
            
            price = st.slider(
                "🏷️ Set Market Price ($)",
                min_value=10, max_value=120, value=20, step=2
            )
            
            submit_game = st.button("▶️ Test Market Price", type="primary", use_container_width=True)
            
            if submit_game:
                # Underlying Economic Equations
                # Demand: Qd = 5000 - 40P
                # Supply: Qs = -1000 + 60P
                # Equilibrium is at P = 60, Q = 2600
                
                qd = max(0, 5000 - (40 * price))
                qs = max(0, -1000 + (60 * price))
                
                st.session_state.qd = qd
                st.session_state.qs = qs
                st.session_state.price_set = price
                
                gap = abs(qd - qs)
                st.session_state.gap = gap
                
                if qd > qs:
                    st.session_state.status = f"SHORTAGE of {gap:,} units"
                elif qs > qd:
                    st.session_state.status = f"SURPLUS of {gap:,} units"
                else:
                    st.session_state.status = "MARKET CLEARED! Equilibrium Found."
                
                st.session_state.current_round += 1
                
                st.session_state.game_history.append({
                    'round': st.session_state.current_round,
                    'price': price,
                    'qd': qd,
                    'qs': qs,
                    'gap': gap
                })
                
                # Score Calculation: Max score is 50. You lose points based on the size of the gap.
                max_possible_gap = 5000 # Roughly the gap at extreme prices
                penalty = (gap / max_possible_gap) * 50
                st.session_state.game_score = max(0, 50 - penalty)
                st.session_state.game_played = True
                
                st.rerun()

    if st.session_state.game_played:
        results_section = st.container()
        with results_section:
            st.markdown('<div class="section-header">📊 Market Results & Efficiency</div>', unsafe_allow_html=True)
            metric_cols = st.columns(3)
            
            with metric_cols[0]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Quantity Demanded ($Q_d$)</h3>
                    <div class="metric-value">{st.session_state.qd:,}</div>
                    <p style="color: #6EE7B7; font-size: 0.9rem;">What consumers want</p>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_cols[1]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Quantity Supplied ($Q_s$)</h3>
                    <div class="metric-value">{st.session_state.qs:,}</div>
                    <p style="color: #6EE7B7; font-size: 0.9rem;">What producers make</p>
                </div>
                """, unsafe_allow_html=True)
                
            with metric_cols[2]:
                status_color = "#10B981" if st.session_state.gap == 0 else "#F59E0B"
                st.markdown(f"""
                <div class="metric-card" style="border-color: {status_color};">
                    <h3 style="color: {status_color};">Market Status</h3>
                    <div class="metric-value" style="font-size: 1.5rem; color: {status_color}; margin-top: 1rem;">
                        {st.session_state.status}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            viz_col1, viz_col2 = st.columns(2)
            
            with viz_col1:
                if len(st.session_state.game_history) > 0:
                    st.markdown("### 📉 Market Gap Over Time (Lower is Better)")
                    history_df = pd.DataFrame(st.session_state.game_history)
                    st.line_chart(
                        history_df.set_index('round')['gap'],
                        color="#FCD34D"
                    )
            
            with viz_col2:
                st.markdown("""
                <div class="case-
