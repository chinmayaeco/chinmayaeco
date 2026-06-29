import streamlit as st
import random
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION & THEME
# =====================================================================
st.set_page_config(
    page_title="Managerial Economics Simulator",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# PREMIUM DESIGN SYSTEM (Same as previous)
# =====================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F172A 100%);
    }
    
    /* Header styling */
    .header-gradient {
        background: linear-gradient(135deg, #2563EB 0%, #7C3AED 50%, #DB2777 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(37, 99, 235, 0.15);
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
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 2px solid #3B82F6;
        color: white;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.2);
    }
    
    .score-banner h2 {
        color: #60A5FA !important;
        margin: 0 !important;
        font-weight: 700;
        font-size: 1.8rem;
    }
    
    .score-banner p {
        color: rgba(255, 255, 255, 0.8);
        margin: 0.5rem 0 0 0 !important;
        font-size: 1rem;
    }
    
    /* Container styling */
    .stContainer {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }
    
    /* Section headers */
    .section-header {
        color: #60A5FA;
        font-weight: 700;
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid rgba(96, 165, 250, 0.3);
    }
    
    /* Concept note box */
    .concept-note {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
        border-left: 4px solid #3B82F6;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .concept-note h3 {
        color: #3B82F6;
        margin-top: 0 !important;
    }
    
    .concept-note p {
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.6;
    }
    
    /* Case study */
    .case-study {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(34, 197, 94, 0.05) 100%);
        border-left: 4px solid #22C55E;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .case-study h4 {
        color: #22C55E;
        margin-top: 0 !important;
    }
    
    .case-study p {
        color: rgba(255, 255, 255, 0.85);
        line-height: 1.6;
    }
    
    /* Managerial lesson */
    .managerial-lesson {
        background: linear-gradient(135deg, rgba(249, 115, 22, 0.1) 0%, rgba(249, 115, 22, 0.05) 100%);
        border-left: 4px solid #F97316;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .managerial-lesson h4 {
        color: #FB923C;
        margin-top: 0 !important;
    }
    
    .managerial-lesson p {
        color: rgba(255, 255, 255, 0.85);
        line-height: 1.6;
    }
    
    /* Real-world application */
    .real-world-app {
        background: linear-gradient(135deg, rgba(236, 72, 153, 0.1) 0%, rgba(236, 72, 153, 0.05) 100%);
        border-left: 4px solid #EC4899;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .real-world-app h4 {
        color: #EC4899;
        margin-top: 0 !important;
    }
    
    .real-world-app p {
        color: rgba(255, 255, 255, 0.85);
        line-height: 1.6;
    }
    
    /* Key metrics */
    .metric-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(96, 165, 250, 0.3);
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
    }
    
    .metric-card h3 {
        color: #60A5FA;
        font-size: 1.2rem;
        margin: 0 0 0.5rem 0;
    }
    
    .metric-value {
        color: #10B981;
        font-size: 2rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3) !important;
    }
    
    .stButton > button:hover {
        box-shadow: 0 8px 24px rgba(37, 99, 235, 0.5) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(30, 41, 59, 0.5);
        border-bottom: 2px solid rgba(96, 165, 250, 0.2);
    }
    
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #2563EB !important;
    }
    
    /* Text colors */
    .stMarkdown {
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Sidebar */
    .stSidebar {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
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
        'profit': 0.0,
        'revenue': 0.0,
        'costs': 0.0,
        'demand': 0,
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
            "📝 Knowledge Check",
            "💼 Executive Summary",
            "🛠️ Implementation Guide"
        ]
    )

# =====================================================================
# HEADER SECTION
# =====================================================================
st.markdown("""
<div class="header-gradient">
    <h1>📈 Managerial Economics Simulator</h1>
    <p>Master strategic decision-making through resource trade-offs, market pricing dynamics, and applied economic models.</p>
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
        <h2>Your Managerial Acumen Score: {total_score} / 100</h2>
        <p>🎮 Simulation Score: {round(st.session_state.game_score)}/50 | 📝 Quiz Score: {round(st.session_state.quiz_score)}/50</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# MAIN CONTENT ROUTING
# =====================================================================

if learning_path == "🎮 Play & Learn":
    game_section = st.container()
    with game_section:
        st.markdown('<div class="section-header">🎮 Phase 1: The Product Launch Simulation</div>', unsafe_allow_html=True)
        
        col_concept, col_game = st.columns([1, 1.2])
        
        with col_concept:
            st.markdown("""
            <div class="concept-note">
            <h3>📌 The Manager's Dilemma</h3>
            <p><strong>Scenario:</strong> You are launching a new smart gadget. You face two core economic decisions based on standard <strong>Theories and Models</strong>.</p>
            <ul>
                <li><strong>1. Trade-offs (Resource Allocation):</strong> You have a $100k budget. Every dollar spent on Marketing (increases base demand) is a dollar taken away from R&D (justifies a higher price). This is your <em>Opportunity Cost</em>.</li>
                <li><strong>2. Prices and Markets:</strong> Set your product price. According to the law of demand, higher prices yield lower unit sales, but higher margins.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="managerial-lesson">
            <h4>💡 Positive vs. Normative Decisions</h4>
            <p><strong>Positive Economics:</strong> "If we price at $50, our model predicts 2,000 units sold." (Fact-based, testable)</p>
            <p><strong>Normative Economics:</strong> "We <em>should</em> price lower so more students can afford our gadget." (Value-based, opinion)</p>
            <p><em>In this simulation, optimize purely for Profit (Positive).</em></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_game:
            st.markdown("""
            <div class="concept-note">
            <h3>🎯 Your Decision Board</h3>
            <p>Allocate your resources and set your price to maximize profit.</p>
            </div>
            """, unsafe_allow_html=True)
            
            budget_allocation = st.slider(
                "⚖️ Budget Trade-off (Total: $100k)",
                min_value=0, max_value=100, value=50, step=10,
                help="0 = 100% R&D | 100 = 100% Marketing"
            )
            
            marketing_budget = budget_allocation * 1000
            rd_budget = (100 - budget_allocation) * 1000
            
            st.caption(f"📊 Allocation: ${marketing_budget:,} Marketing | ${rd_budget:,} R&D")
            
            price = st.slider(
                "🏷️ Set Product Price",
                min_value=10, max_value=150, value=50, step=5
            )
            
            col_btn1, col_btn2 = st.columns([1, 2])
            with col_btn1:
                submit_game = st.button("▶️ Run Market Model", type="primary", use_container_width=True)
            
            if submit_game:
                base_demand = 1000 + (marketing_budget / 20)
                price_sensitivity = 20 - (rd_budget / 10000)
                calculated_demand = max(0, int(base_demand - (price_sensitivity * price)))
                
                revenue = calculated_demand * price
                fixed_costs = 100000
                variable_costs = calculated_demand * 15
                total_costs = fixed_costs + variable_costs
                profit = revenue - total_costs
                
                st.session_state.profit = profit
                st.session_state.revenue = revenue
                st.session_state.costs = total_costs
                st.session_state.demand = calculated_demand
                st.session_state.current_round += 1
                
                st.session_state.game_history.append({
                    'round': st.session_state.current_round,
                    'price': price,
                    'marketing': budget_allocation,
                    'profit': profit,
                    'demand': calculated_demand
                })
                
                normalized_score = max(0, min(50, (profit / 80000) * 50))
                st.session_state.game_score = normalized_score
                st.session_state.game_played = True
                
                st.rerun()

    if st.session_state.game_played:
        results_section = st.container()
        with results_section:
            st.markdown('<div class="section-header">📊 Market Results & Economic Analysis</div>', unsafe_allow_html=True)
            metric_cols = st.columns(4)
            
            with metric_cols[0]:
                profit_color = "#10B981" if st.session_state.profit > 0 else "#EF4444"
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Net Profit</h3>
                    <div class="metric-value" style="color: {profit_color};">${st.session_state.profit:,.0f}</div>
                    <p style="color: #60A5FA; font-size: 0.9rem;">The Ultimate Metric</p>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_cols[1]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Units Sold (Demand)</h3>
                    <div class="metric-value">{st.session_state.demand:,}</div>
                    <p style="color: #60A5FA; font-size: 0.9rem;">Market Clearance</p>
                </div>
                """, unsafe_allow_html=True)
                
            with metric_cols[2]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Total Revenue</h3>
                    <div class="metric-value">${st.session_state.revenue:,.0f}</div>
                    <p style="color: #60A5FA; font-size: 0.9rem;">Price × Quantity</p>
                </div>
                """, unsafe_allow_html=True)
                
            with metric_cols[3]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Total Costs</h3>
                    <div class="metric-value">${st.session_state.costs:,.0f}</div>
                    <p style="color: #60A5FA; font-size: 0.9rem;">Fixed + Variable</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            viz_col1, viz_col2 = st.columns(2)
            
            with viz_col1:
                if len(st.session_state.game_history) > 0:
                    st.markdown("### 📈 Profit Trajectory Over Rounds")
                    history_df = pd.DataFrame(st.session_state.game_history)
                    st.line_chart(
                        history_df.set_index('round')['profit'],
                        color="#10B981"
                    )
            
            with viz_col2:
                st.markdown("""
                <div class="real-world-app">
                <h4>🔍 Economic Deconstruction</h4>
                <p><strong>Trade-offs:</strong> Your budget allocation forced a choice between building brand awareness and reducing price sensitivity. This is <em>Opportunity Cost</em>.</p>
                <p><strong>Prices & Markets:</strong> If profit is low, you likely hit the elastic part of the demand curve where high prices collapsed sales, or you priced too low to cover fixed costs.</p>
                </div>
                """, unsafe_allow_html=True)

elif learning_path == "📖 Conceptual Deep Dive":
    st.markdown('<div class="section-header">📚 Managerial Economics Concepts</div>', unsafe_allow_html=True)
    concept_tabs = st.tabs(["Trade-offs & Opportunity Cost", "Prices & Markets", "Theories & Models", "Positive vs. Normative"])
    
    with concept_tabs[0]:
        st.markdown("""
        <div class="concept-note">
        <h3>⚖️ Trade-offs & Opportunity Cost</h3>
        <p><strong>Definition:</strong> Scarcity dictates that resources are limited. Choosing one path inherently means sacrificing another. The value of the next best alternative given up is the <strong>Opportunity Cost</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with concept_tabs[1]:
        st.markdown("""
        <div class="concept-note">
        <h3>🛒 Prices, Markets, and Equilibrium</h3>
        <p><strong>Definition:</strong> Markets are mechanisms where buyers and sellers interact. Prices act as signals, communicating scarcity and directing resources. Equilibrium occurs when supply matches demand.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with concept_tabs[2]:
        st.markdown("""
        <div class="concept-note">
        <h3>📐 Theories and Models</h3>
        <p><strong>Definition:</strong> Economic models are deliberate simplifications of a complex reality. They strip away "noise" to focus on the core variables driving behavior.</p>
        </div>
        """, unsafe_allow_html=True)

    with concept_tabs[3]:
        st.markdown("""
        <div class="concept-note">
        <h3>🔍 Positive vs. Normative Economics</h3>
        <p><strong>Positive Economics:</strong> Objective and fact-based. "What is." Can be tested or verified with data.</p>
        <p><strong>Normative Economics:</strong> Subjective and value-based. "What ought to be." Rooted in ethics or policy goals.</p>
        </div>
        """, unsafe_allow_html=True)

elif learning_path == "📝 Knowledge Check":
    st.markdown('<div class="section-header">📝 Check Your Managerial Acumen</div>', unsafe_allow_html=True)
    st.markdown("Test your understanding of the four core themes. Each correct answer adds **12.5 points** to your total score.")
    
    with st.form("quiz_form"):
        # Theme 1: Trade-offs
        st.markdown("### 1. Trade-offs & Opportunity Cost")
        q1 = st.radio(
            "If a manager chooses to spend $50,000 on new software instead of a marketing campaign that would have reliably generated $60,000 in revenue, what is the opportunity cost of the software?",
            options=[
                "A) $50,000",
                "B) $60,000 in lost revenue",
                "C) $10,000",
                "D) The cost of training employees on the new software"
            ],
            index=None
        )
        
        # Theme 2: Prices and Markets
        st.markdown("---")
        st.markdown("### 2. Prices and Markets")
        q2 = st.radio(
            "When a rideshare app implements 'surge pricing' during a rainstorm, which market mechanisms are primarily at work to restore equilibrium?",
            options=[
                "A) It suppresses driver supply and increases rider demand.",
                "B) It relies on normative economics to make the market fair.",
                "C) It suppresses rider demand and incentivizes driver supply.",
                "D) It sets a government-mandated price floor."
            ],
            index=None
        )
        
        # Theme 3: Theories and Models
        st.markdown("---")
        st.markdown("### 3. Theories and Models")
        q3 = st.radio(
            "Why do economic models frequently rely on the assumption of 'Ceteris Paribus' (all other things being equal)?",
            options=[
                "A) Because real-world markets never change.",
                "B) To isolate the effect of a single variable by holding other disruptive factors constant.",
                "C) To calculate accounting profit rather than economic profit.",
                "D) It proves that normative economic statements are factually correct."
            ],
            index=None
        )
        
        # Theme 4: Positive vs. Normative
        st.markdown("---")
        st.markdown("### 4. Positive vs. Normative Economics")
        q4 = st.radio(
            "Which of the following boardroom statements is an example of Positive Economics?",
            options=[
                "A) 'We ought to prioritize green energy to protect the environment.'",
                "B) 'It is unfair that our competitors are paying minimum wage.'",
                "C) 'The government must step in and regulate tech monopolies.'",
                "D) 'Increasing our product price by 10% will likely reduce unit sales by 15%.'"
            ],
            index=None
        )
        
        submit_quiz = st.form_submit_button("Submit Answers", type="primary")
        
        if submit_quiz:
            score = 0.0
            
            # Check Q1
            if q1 == "B) $60,000 in lost revenue":
                score += 12.5
                st.session_state.q1_correct = True
            else:
                st.session_state.q1_correct = False
                
            # Check Q2
            if q2 == "C) It suppresses rider demand and incentivizes driver supply.":
                score += 12.5
                st.session_state.q2_correct = True
            else:
                st.session_state.q2_correct = False
                
            # Check Q3
            if q3 == "B) To isolate the effect of a single variable by holding other disruptive factors constant.":
                score += 12.5
                st.session_state.q3_correct = True
            else:
                st.session_state.q3_correct = False
                
            # Check Q4
            if q4 == "D) 'Increasing our product price by 10% will likely reduce unit sales by 15%.'":
                score += 12.5
                st.session_state.q4_correct = True
            else:
                st.session_state.q4_correct = False
                
            st.session_state.quiz_score = score
            st.session_state.quiz_submitted = True
            st.rerun()

    # Show Results after submission
    if st.session_state.quiz_submitted:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Results: {st.session_state.quiz_score}/50 points")
        
        if not st.session_state.q1_correct:
            st.error("**Q1 Incorrect:** The opportunity cost is the value of the next best alternative given up, which was the $60,000 in revenue.")
        if not st.session_state.q2_correct:
            st.error("**Q2 Incorrect:** Surge pricing raises prices to suppress excess rider demand while incentivizing more drivers to log on and supply rides.")
        if not st.session_state.q3_correct:
            st.error("**Q3 Incorrect:** Ceteris Paribus is used in models to strip away noise and see exactly how one variable (like price) affects another (like demand) in isolation.")
        if not st.session_state.q4_correct:
            st.error("**Q4 Incorrect:** Positive economics is about testable, objective facts (e.g., forecasting sales volume drops based on price hikes).")
            
        if st.session_state.quiz_score == 50:
            st.success("Perfect score! You have a strong grasp of foundational managerial economics.")

elif learning_path == "💼 Executive Summary":
    st.markdown('<div class="section-header">💼 Executive Summary: The Economic Leader</div>', unsafe_allow_html=True)
    exec_col1, exec_col2 = st.columns(2)
    with exec_col1:
        st.markdown("""
        <div class="managerial-lesson">
        <h4>🎯 Four Pillars of Economic Decision Making</h4>
        <p><strong>1. Embrace Opportunity Cost</strong></p>
        <p>Never look at an investment in isolation. Always ask: "What are we giving up to do this?"</p>
        <p><strong>2. Respect Market Signals</strong></p>
        <p>Prices are not just math; they are communication.</p>
        </div>
        """, unsafe_allow_html=True)

elif learning_path == "🛠️ Implementation Guide":
    st.markdown('<div class="section-header">🛠️ Implementation Guide: Economic Thinking in Practice</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="managerial-lesson">
    <h4>📅 The Marginal Analysis Framework</h4>
    <ul>
        <li><strong>Step 1: Ignore Sunk Costs.</strong> Look only at future costs and future revenues.</li>
        <li><strong>Step 2: Calculate Marginal Revenue (MR).</strong></li>
        <li><strong>Step 3: Calculate Marginal Cost (MC).</strong></li>
        <li><strong>Step 4: The Golden Rule.</strong> As long as MR > MC, expand operations.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.caption("🎓 Built for Managerial Economics | Powered by Streamlit")

with footer_col2:
    total_score = min(100, round(st.session_state.game_score + st.session_state.quiz_score))
    st.caption(f"📈 Managerial Acumen: {total_score}/100")

with footer_col3:
    st.caption(f"⏰ Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
