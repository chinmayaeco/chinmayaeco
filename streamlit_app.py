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
# PREMIUM DESIGN SYSTEM
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
    
    .case-study strong {
        color: #86EFAC;
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
        'current_round': 0
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
    # =========================================================
    # SECTION 1: THE MARKET SIMULATION GAME
    # =========================================================
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
            
            # Game inputs
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
                # Economic Model: Demand Calculation
                # Base demand driven by marketing
                base_demand = 1000 + (marketing_budget / 20)
                # Price sensitivity reduced by R&D (better product)
                price_sensitivity = 20 - (rd_budget / 10000)
                
                # Calculate actual demand (cannot be negative)
                calculated_demand = max(0, int(base_demand - (price_sensitivity * price)))
                
                # Financials
                revenue = calculated_demand * price
                fixed_costs = 100000 # The budget
                variable_costs = calculated_demand * 15 # $15 to make each unit
                total_costs = fixed_costs + variable_costs
                profit = revenue - total_costs
                
                st.session_state.profit = profit
                st.session_state.revenue = revenue
                st.session_state.costs = total_costs
                st.session_state.demand = calculated_demand
                st.session_state.current_round += 1
                
                # Store history
                st.session_state.game_history.append({
                    'round': st.session_state.current_round,
                    'price': price,
                    'marketing': budget_allocation,
                    'profit': profit,
                    'demand': calculated_demand
                })
                
                # Calculate game score based on hitting a good profit threshold (e.g., > $50k gets max points)
                normalized_score = max(0, min(50, (profit / 80000) * 50))
                st.session_state.game_score = normalized_score
                st.session_state.game_played = True
                
                st.rerun()
    
    # =========================================================
    # SECTION 2: GAME RESULTS & ANALYSIS
    # =========================================================
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
            
            # Visualizations
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
                <p><strong>Trade-offs:</strong> Your budget allocation forced a choice between building brand awareness (Marketing) and reducing price sensitivity (R&D). This is <em>Opportunity Cost</em> in action.</p>
                <p><strong>Prices & Markets:</strong> If your profit is low, you likely hit the elastic part of the demand curve, where a high price collapsed your unit sales, or you priced too low to cover your fixed costs.</p>
                <p><strong>Theories & Models:</strong> The backend of this game relies on a simplified linear demand curve model. It ignores competitor responses (Ceteris Paribus assumption).</p>
                </div>
                """, unsafe_allow_html=True)

elif learning_path == "📖 Conceptual Deep Dive":
    st.markdown('<div class="section-header">📚 Managerial Economics Concepts</div>', unsafe_allow_html=True)
    
    concept_tabs = st.tabs(["Trade-offs & Opportunity Cost", "Prices & Markets", "Theories & Models", "Positive vs. Normative"])
    
    with concept_tabs[0]:
        st.markdown("""
        <div class="concept-note">
        <h3>⚖️ Trade-offs & Opportunity Cost</h3>
        <p><strong>Definition:</strong> Scarcity dictates that resources (time, money, labor) are limited. Choosing one path inherently means sacrificing another. The value of the next best alternative given up is the <strong>Opportunity Cost</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="case-study">
        <h4>🏢 Case Study: Capital Allocation in Big Tech</h4>
        <p><strong>The Situation:</strong> A tech company has $5B in surplus cash.</p>
        <p><strong>The Trade-off:</strong> They can either issue a special dividend to shareholders OR invest in a new AI research division.</p>
        <p><strong>The Lesson:</strong> If they choose the dividend, the opportunity cost is the potential future monopoly profits from the AI division. Managers must calculate the Expected Value of both paths to ensure resources flow to their most productive use.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with concept_tabs[1]:
        st.markdown("""
        <div class="concept-note">
        <h3>🛒 Prices, Markets, and Equilibrium</h3>
        <p><strong>Definition:</strong> Markets are mechanisms where buyers and sellers interact. Prices act as signals, communicating scarcity and directing resources. Equilibrium occurs when supply matches demand.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="case-study">
        <h4>🚕 Case Study: Uber's Surge Pricing</h4>
        <p><strong>The Mechanism:</strong> When demand for rides spikes (e.g., after a concert), standard prices lead to a shortage (Quantity Demanded > Quantity Supplied).</p>
        <p><strong>The Solution:</strong> Uber's algorithm dynamically raises the price. This accomplishes two market functions simultaneously:</p>
        <ul>
            <li><strong>Suppresses Demand:</strong> Price-sensitive riders wait or take the bus.</li>
            <li><strong>Incentivizes Supply:</strong> Off-duty drivers log on to capture the premium.</li>
        </ul>
        <p><strong>The Lesson:</strong> Dynamic pricing forces the market back into equilibrium rapidly.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with concept_tabs[2]:
        st.markdown("""
        <div class="concept-note">
        <h3>📐 Theories and Models</h3>
        <p><strong>Definition:</strong> Economic models are deliberate simplifications of a complex reality. They strip away "noise" to focus on the core variables driving behavior (e.g., assuming <em>Ceteris Paribus</em> - all other things being equal).</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="managerial-lesson">
        <h4>💼 Why Managers Use Simplified Models</h4>
        <p>A map that is perfectly true to scale is useless because it's as big as the territory it represents. Models work the same way.</p>
        <ul>
            <li><strong>Demand Forecasting Models:</strong> Isolate price and income, ignoring weather or minor fads.</li>
            <li><strong>Cost-Volume-Profit (CVP) Analysis:</strong> Assumes linear costs to easily calculate break-even points.</li>
        </ul>
        <p><em>Rule of thumb for leaders: "All models are wrong, but some are useful." (George Box)</em></p>
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
        
        st.markdown("""
        <div class="real-world-app">
        <h4>📊 Spotting the Difference in the Boardroom</h4>
        <p><strong>Scenario: Minimum Wage Increases</strong></p>
        <ul>
            <li><strong>Manager A (Positive):</strong> "If the minimum wage rises to $15/hr, our payroll costs will increase by 12%, and we will need to automate 3 cashier roles to maintain our current margin." <em>(Testable forecasting)</em></li>
            <li><strong>Manager B (Normative):</strong> "We should voluntarily raise our starting wage to $15/hr because it's the fair thing to do for our community, even if it hurts short-term profits." <em>(Moral judgment)</em></li>
        </ul>
        <p><strong>Managerial Application:</strong> Effective leaders use Positive economics to understand reality, and Normative economics to set the organization's mission and values.</p>
        </div>
        """, unsafe_allow_html=True)

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
        <p>Prices are not just math; they are communication. If your inventory is sitting, the market is signaling your price is too high for the perceived value.</p>
        <p><strong>3. Use Models Safely</strong></p>
        <p>Rely on economic models for directional guidance, but know their blind spots. Understand the assumptions (Ceteris Paribus) baked into your data.</p>
        <p><strong>4. Separate Facts from Values</strong></p>
        <p>Clearly distinguish between positive statements (data) and normative statements (strategy/ethics) during executive debates to avoid endless circular arguments.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with exec_col2:
        st.markdown("""
        <div class="real-world-app">
        <h4>📊 Strategic Impact Matrix</h4>
        <p>Integrating these concepts yields tangible corporate results:</p>
        <ul>
            <li><strong>Opportunity Cost Analysis:</strong> Eliminates "pet projects" and optimizes capital ROI (+15-20% CapEx efficiency).</li>
            <li><strong>Dynamic Pricing Models:</strong> Captures consumer surplus, directly lifting gross margins.</li>
            <li><strong>Positive Fact-Finding:</strong> Reduces executive bias in forecasting.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif learning_path == "🛠️ Implementation Guide":
    st.markdown('<div class="section-header">🛠️ Implementation Guide: Economic Thinking in Practice</div>', unsafe_allow_html=True)
    
    impl_tabs = st.tabs(["Decision Frameworks", "Meeting Interventions", "Common Pitfalls"])
    
    with impl_tabs[0]:
        st.markdown("""
        <div class="managerial-lesson">
        <h4>📅 The Marginal Analysis Framework</h4>
        <p>How to apply economic thinking to your next major project:</p>
        <ul>
            <li><strong>Step 1: Ignore Sunk Costs.</strong> Look only at future costs and future revenues.</li>
            <li><strong>Step 2: Calculate Marginal Revenue (MR).</strong> How much *extra* revenue will this one specific unit/project bring?</li>
            <li><strong>Step 3: Calculate Marginal Cost (MC).</strong> How much *extra* cost will this incur?</li>
            <li><strong>Step 4: The Golden Rule.</strong> As long as MR > MC, expand operations. Stop exactly where MR = MC.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with impl_tabs[1]:
        st.markdown("""
        <div class="real-world-app">
        <h4>🗣️ Intervening in Meetings</h4>
        <p>Use these phrases to steer your team toward sound economic thinking:</p>
        <ul>
            <li><strong>To surface Trade-offs:</strong> "I love this initiative. If we commit $50k to it, which of our current projects are we pausing to free up that budget?"</li>
            <li><strong>To check Models:</strong> "This revenue forecast looks great. What are the two biggest assumptions we are making, and what happens if they are wrong?"</li>
            <li><strong>To clarify Positive vs Normative:</strong> "Let's pause. Are we arguing about what the data *is* (positive), or are we disagreeing on what our goal *should* be (normative)?"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with impl_tabs[2]:
        st.markdown("""
        <div class="case-study">
        <h4>⚠️ Common Pitfalls to Avoid</h4>
        <p><strong>Pitfall 1: Ignoring the Secondary Effects</strong></p>
        <ul>
            <li>❌ "Cutting our price by 10% will increase our sales volume." (Forgetting competitors will likely cut their prices too).</li>
            <li>✅ Build game theory into your models.</li>
        </ul>
        <p><strong>Pitfall 2: Confusing Accounting Profit with Economic Profit</strong></p>
        <ul>
            <li>❌ Celebrating a $100k profit on a project that tied up $2M in capital for a year.</li>
            <li>✅ Always subtract the Opportunity Cost of capital (e.g., 5% risk-free rate) to find true Economic Profit.</li>
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
