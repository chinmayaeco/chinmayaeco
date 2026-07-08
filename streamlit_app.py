import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Consumer Choice Optimizer",
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
        if st.session_state["password"] == "PED2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #10B981;'>🔒 Secure Access</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Please enter the password to access the simulator.</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    
    elif not st.session_state["password_correct"]:
        st.markdown("<h1 style='text-align: center; color: #10B981;'>🔒 Secure Access</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Password", type="password", on_change=password_entered, key="password")
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
    
    * { font-family: 'Inter', sans-serif; }
    
    /* Main background */
    .stApp { background: linear-gradient(135deg, #022C22 0%, #064E3B 50%, #022C22 100%); }
    
    /* Header styling */
    .header-gradient {
        background: linear-gradient(135deg, #047857 0%, #10B981 50%, #F59E0B 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.15);
    }
    .header-gradient h1 { color: white !important; font-size: 2.5rem !important; font-weight: 800 !important; margin: 0 !important; text-shadow: 0 2px 8px rgba(0, 0, 0, 0.2); }
    .header-gradient p { color: rgba(255, 255, 255, 0.95) !important; font-size: 1.1rem !important; margin: 0.5rem 0 0 0 !important; }
    
    /* Score banner */
    .score-banner {
        background: linear-gradient(135deg, #064E3B 0%, #065F46 100%);
        border: 2px solid #10B981;
        color: white; padding: 2rem; border-radius: 12px; text-align: center; margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(16, 185, 129, 0.2);
    }
    .score-banner h2 { color: #34D399 !important; margin: 0 !important; font-weight: 700; font-size: 1.8rem; }
    
    /* Container styling */
    .stContainer, .stForm {
        background: rgba(6, 78, 59, 0.8); border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 12px; padding: 2rem; margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2); backdrop-filter: blur(10px);
    }
    
    /* Section headers */
    .section-header {
        color: #FCD34D; font-weight: 700; font-size: 1.5rem; margin-bottom: 1.5rem;
        padding-bottom: 1rem; border-bottom: 2px solid rgba(252, 211, 77, 0.3);
    }
    
    /* Concept note box */
    .concept-note, .case-study { padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; }
    .concept-note { background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(52, 211, 153, 0.1) 100%); border-left: 4px solid #10B981; }
    .concept-note h3 { color: #34D399; margin-top: 0 !important; }
    .case-study { background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(251, 191, 36, 0.05) 100%); border-left: 4px solid #F59E0B; }
    .case-study h4 { color: #FBBF24; margin-top: 0 !important; }
    
    /* Key metrics */
    .metric-card {
        background: rgba(2, 44, 34, 0.6); border: 1px solid rgba(52, 211, 153, 0.3);
        padding: 1.5rem; border-radius: 8px; text-align: center;
    }
    .metric-card h3 { color: #6EE7B7; font-size: 1.2rem; margin: 0 0 0.5rem 0; }
    .metric-value { color: #FCD34D; font-size: 2rem; font-weight: 700; margin: 0.5rem 0; }
    
    /* Buttons */
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #059669 0%, #10B981 100%) !important; color: white !important;
        border: none !important; padding: 0.75rem 2rem !important; border-radius: 8px !important;
        font-weight: 600 !important; transition: all 0.3s ease !important; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3) !important;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover { box-shadow: 0 8px 24px rgba(16, 185, 129, 0.5) !important; transform: translateY(-2px) !important; }
    
    /* Tabs & Text */
    .stTabs [data-baseweb="tab-list"] { background: rgba(6, 78, 59, 0.5); border-bottom: 2px solid rgba(16, 185, 129, 0.2); }
    .stTabs [aria-selected="true"] { border-bottom: 3px solid #10B981 !important; }
    .stMarkdown, p, li { color: rgba(255, 255, 255, 0.9) !important; }
    .stRadio p, .stRadio label, div[role="radiogroup"] p { color: rgba(255, 255, 255, 0.95) !important; font-size: 1.05rem; }
    .stSidebar { background: linear-gradient(180deg, #022C22 0%, #064E3B 100%); }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SESSION STATE INITIALIZATION
# =====================================================================
def initialize_session_state():
    defaults = {
        'game_played': False,
        'sim_score': 0.0,
        'quiz_score': 0.0,
        'sim_history': [],
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
    st.markdown("### 📚 Consumer Choice Path")
    learning_path = st.radio(
        "Select your focus:",
        options=[
            "🎮 Utility Optimization Simulator",
            "📖 Conceptual Deep Dive",
            "📈 Real-World Market Applications",
            "📝 Knowledge Check",
            "💼 Executive Summary"
        ]
    )

# =====================================================================
# HEADER SECTION
# =====================================================================
st.markdown("""
<div class="header-gradient">
    <h1>⚖️ Consumer Choice Theory</h1>
    <p>Analyze how individuals achieve optimal satisfaction. Master the strategic equilibrium where budgetary constraints perfectly align with subjective consumer utility.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# PERFORMANCE DASHBOARD (ANTI-100% PERFECT SCORE MECHANIC)
# =====================================================================
dashboard_col = st.container()
with dashboard_col:
    # A structural ceiling cap and dynamic friction penalty ensures the absolute maximum score sits around 96-98, preventing anyone from hitting 100.
    raw_total = st.session_state.sim_score + st.session_state.quiz_score
    friction_penalty = 2.5 if raw_total > 80 else (0.03 * raw_total)
    total_score = max(0.0, min(97.5, round(raw_total - friction_penalty, 1)))
    
    st.markdown(f"""
    <div class="score-banner">
        <h2>Overall Microeconomic Mastery: {total_score} / 100</h2>
        <p style='color: #FCD34D;'>🎮 Optimization Score: {round(st.session_state.sim_score, 1)}/50 | 📝 Quiz Score: {round(st.session_state.quiz_score, 1)}/50</p>
        <small style='color: #a7f3d0;'>⚠️ Dynamic market friction applied. Universal perfect efficiency (100%) is structurally impossible in a scarce resource reality.</small>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# MAIN CONTENT ROUTING
# =====================================================================

if learning_path == "🎮 Utility Optimization Simulator":
    game_section = st.container()
    with game_section:
        st.markdown('<div class="section-header">🎮 The Optimal Bundle Constrained Simulator</div>', unsafe_allow_html=True)
        
        col_concept, col_game = st.columns([1, 1.2])
        
        with col_concept:
            st.markdown("""
            <div class="concept-note">
            <h3>📌 Your Mission: Maximize Total Utility</h3>
            <p><strong>Your Scenario:</strong> An individual allocates a strict budget between two goods: <strong>Premium Coffee (Good X)</strong> and <strong>Streaming Subscriptions (Good Y)</strong>.</p>
            <p><strong>The Constraint:</strong> You cannot exceed your budget. Spending less than your budget leaves utility unmaximized.</p>
            <p><strong>The Rule of Optimality:</strong> True consumer equilibrium occurs precisely where the Budget Constraint is tangent to the highest attainable Indifference Curve. At this unique mathematical intersection:</p>
            <p style='text-align: center; font-weight: bold; color: #FCD34D;'>MRS = Price Ratio<br><code>(MU_x / MU_y) = (P_x / P_y)</code></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_game:
            st.markdown("""
            <div class="case-study">
            <h4>🎯 Budget & Market Parameters</h4>
            </div>
            """, unsafe_allow_html=True)
            
            # Constants for simulator
            income = 200
            price_x = 20
            price_y = 40
            
            st.write(f"💰 **Total Disposable Income:** ${income}")
            st.write(f"☕ **Price of Premium Coffee (Good X):** ${price_x} per unit")
            st.write(f"🎬 **Price of Streaming (Good Y):** ${price_y} per unit")
            
            # User picks quantities
            qty_x = st.slider("Select Quantity of Premium Coffee (X)", min_value=0, max_value=12, value=4, step=1)
            qty_y = st.slider("Select Quantity of Streaming (Y)", min_value=0, max_value=8, value=2, step=1)
            
            submit_sim = st.button("⚖️ Calculate Consumer Equilibrium", type="primary", use_container_width=True)
            
            if submit_sim:
                total_spent = (qty_x * price_x) + (qty_y * price_y)
                
                # Cobb-Douglas derived utility simulation: U = X^0.5 * Y^0.5 scaled up
                # Theoretical optimal bundle is X=5, Y=2.5. Since integer selection: X=5, Y=2 gives total_spent = 180 (underbudget)
                # Let's reward high allocations that balance MRS near price ratio (20/40 = 0.5)
                utility = float(round((qty_x ** 0.5) * (qty_y ** 0.5) * 20, 2)) if (qty_x > 0 and qty_y > 0) else 0.0
                
                # Process outcome and calculate points
                if total_spent > income:
                    status = "Budget Violated! ❌ (Bankruptcy)"
                    score_add = 0.0
                elif total_spent == income:
                    # Perfect balance evaluation
                    mrs = (qty_y / qty_x) if qty_x > 0 else 0
                    price_ratio = price_x / price_y # 0.5
                    
                    if abs(mrs - price_ratio) < 0.01:
                        status = "Absolute Consumer Equilibrium Achieved! 🌟"
                        score_add = 46.5 # Cap strictly under 50 to prevent 100/100 matching rules
                    else:
                        status = "Affordable but Inefficient Bundle ➖ (MRS ≠ Price Ratio)"
                        score_add = 30.0
                else:
                    status = "Inefficient Allocation 📉 (Leftover Income Unspent)"
                    score_add = max(5.0, utility - 5.0)

                st.session_state.current_round += 1
                st.session_state.sim_score = min(46.5, score_add)
                
                st.session_state.sim_history.append({
                    'round': st.session_state.current_round,
                    'qty_x': qty_x,
                    'qty_y': qty_y,
                    'spent': total_spent,
                    'utility': utility,
                    'status': status
                })
                
                st.session_state.game_played = True
                st.rerun()

    if st.session_state.game_played:
        results_section = st.container()
        with results_section:
            st.markdown('<div class="section-header">📊 Optimization Metrics Result</div>', unsafe_allow_html=True)
            
            latest_result = st.session_state.sim_history[-1]
            metric_cols = st.columns(3)
            
            with metric_cols[0]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Total Capital Spent</h3>
                    <div class="metric-value">${latest_result['spent']}</div>
                    <p style="color: #6EE7B7; font-size: 0.9rem;">Budget Limit: $200</p>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_cols[1]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Subjective Utility Yielded</h3>
                    <div class="metric-value">{latest_result['utility']} Utils</div>
                    <p style="color: #6EE7B7; font-size: 0.9rem;">Calculated via Preference Curves</p>
                </div>
                """, unsafe_allow_html=True)
                
            with metric_cols[2]:
                is_ok = "🌟" in latest_result['status'] or "Inefficient" in latest_result['status'] and "Leftover" not in latest_result['status']
                status_color = "#10B981" if is_ok else "#EF4444"
                
                st.markdown(f"""
                <div class="metric-card" style="border-color: {status_color};">
                    <h3 style="color: {status_color};">Equilibrium State</h3>
                    <div class="metric-value" style="font-size: 1.5rem; color: {status_color};">{latest_result['status']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("### 📈 Visualizing Consumer Constraints vs. Preferences")
            
            # Generate numerical values to render Budget Line & Indifference Curves
            x_vals = np.linspace(0.1, 12, 20)
            budget_y = (200 - (20 * x_vals)) / 40
            budget_y = np.clip(budget_y, 0, None)
            
            # Create interactive standard DataFrame for user visualization
            chart_data = pd.DataFrame({
                'Good X (Coffee)': x_vals,
                'Budget Line Constraint': budget_y,
            })
            st.line_chart(chart_data.set_index('Good X (Coffee)'), color="#FCD34D")

elif learning_path == "📖 Conceptual Deep Dive":
    st.markdown('<div class="section-header">📚 Foundations of Rational Choice Theory</div>', unsafe_allow_html=True)
    concept_tabs = st.tabs(["Indifference Curves", "Budget Constraints", "The Optimal Points Condition"])
    
    with concept_tabs[0]:
        st.markdown("""
        <div class="concept-note">
        <h3>📊 Indifference Curves (Preferences)</h3>
        <p>An <strong>Indifference Curve</strong> represents all combinations of two goods that provide a consumer with the exact same level of total satisfaction or utility.</p>
        <p><strong>Core Mathematical Properties:</strong></p>
        <ul>
            <li><strong>Downward Sloping:</strong> To get more of Good X, a consumer must sacrifice some of Good Y to maintain identical happiness.</li>
            <li><strong>Convex to the Origin:</strong> Due to the law of diminishing marginal utility, as you acquire more of a good, your willingness to trade away another good for it decreases. This slope is the <strong>Marginal Rate of Substitution (MRS)</strong>.</li>
            <li><strong>Non-Intersecting:</strong> Higher curves correspond to superior levels of utility ($U_3 > U_2 > U_1$).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with concept_tabs[1]:
        st.markdown("""
        <div class="concept-note">
        <h3>💰 Budget Constraints (Scarcity)</h3>
        <p>While Indifference Curves illustrate what a consumer <em>wants</em> to do, the <strong>Budget Constraint</strong> establishes what they <em>can</em> do based on limited purchasing power.</p>
        <p>The standard algebraic equation represents market equilibrium across available bundles:</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"P_x \cdot X + P_y \cdot Y = I")
        st.markdown("""
        <p>Where $I$ equals absolute disposable income. The absolute slope of this budget constraint represents the market exchange option rate, structurally defined as the relative price ratio:</p>
        """, unsafe_allow_html=True)
        st.latex(r"\text{Slope} = \frac{P_x}{P_y}")

    with concept_tabs[2]:
        st.markdown("""
        <div class="concept-note">
        <h3>⚖️ The Tangency Optimality Rule</h3>
        <p>A utility-maximizing consumer picks the exact bundle along their budget constraint that touches the highest possible indifference curve.</p>
        <p>This optimal point is mathematically reached where the slope of the indifference curve matches the slope of the budget line perfectly:</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"\text{MRS} = \frac{MU_x}{MU_y} = \frac{P_x}{P_y}")
        st.markdown("""
        <p>Rearranging this formula gives the **Equi-Marginal Principle**, proving optimal allocation requires that the utility gained per dollar spent must be uniform across all commodities:</p>
        """, unsafe_allow_html=True)
        st.latex(r"\frac{MU_x}{P_x} = \frac{MU_y}{P_y}")

elif learning_path == "📈 Real-World Market Applications":
    st.markdown('<div class="section-header">📈 Strategic Consumption Behavioral Shifts</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="case-study">
    <h4>📉 The Income Effect vs. Substitution Effect</h4>
    <p>When the price of a critical item declines, consumer choice parameters react to two structural phenomena:</p>
    <ul>
        <li><strong>Substitution Effect:</strong> The item is now relatively cheaper compared to alternatives. Consumers adjust behavior to purchase more of it, pivoting along the same indifference curve.</li>
        <li><strong>Income Effect:</strong> The price decline effectively frees up absolute purchasing power. The budget constraint shifts outward, allowing the consumer to cross into a higher, premium indifference curve entirely.</li>
    </ul>
    </div>
    
    <div class="case-study">
    <h4>🍿 Indian F&B Bundling Patterns (Multiplex Strategy)</h4>
    <p>Cinema operations leverage consumer constraints by designing combined combos (Popcorn + Drinks). By altering the relative internal bundle prices, they manipulate the slope of the consumer's short-term internal budget line, pushing consumers toward higher spending thresholds that optimization formulas show capture maximum consumer surplus.</p>
    </div>
    """, unsafe_allow_html=True)

elif learning_path == "📝 Knowledge Check":
    st.markdown('<div class="section-header">📝 Analytical Knowledge Evaluation</div>', unsafe_allow_html=True)
    st.markdown("Validate your microeconomic proficiency. Note: Performance factors undergo systemic friction penalties to reflect dynamic market realities.")
    
    with st.form("quiz_form"):
        st.markdown("### 1. The Core Meaning of MRS")
        q1 = st.radio(
            "What does the Marginal Rate of Substitution (MRS) represent along an Indifference Curve?",
            options=[
                "A) The exact financial market cost ratio of Good X to Good Y.",
                "B) The rate at which a consumer is willing to exchange one good for another while maintaining constant total utility.",
                "C) The total cash remaining in a consumer's bank balance.",
                "D) The structural shift of a budget line when income changes."
            ],
            index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. General Optimality Framework")
        q2 = st.radio(
            "When a consumer maximizes utility subject to a standard budget constraint, what structural relationship must hold true?",
            options=[
                "A) The indifference curve must be completely vertical.",
                "B) Total spending must equal exactly double the user's available assets.",
                "C) The Marginal Rate of Substitution must equal the relative price ratio (MU_x/MU_y = P_x/P_y).",
                "D) Marginal Utility for both goods must decrease down to absolute zero."
            ],
            index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Price Ratio Manipulations")
        q3 = st.radio(
            "If the market price of Good X doubles while the price of Good Y and total nominal income stay completely identical, what happens to the budget line?",
            options=[
                "A) The budget line shifts outward in a parallel line.",
                "B) The budget line rotates inward along the horizontal X-axis, making it steeper.",
                "C) The line rotates outward along the vertical Y-axis only.",
                "D) The budget line remains completely static and unchanged."
            ],
            index=None
        )
        
        st.markdown("---")
        st.markdown("### 4. Over-Allocation Realities")
        q4 = st.radio(
            "If a consumer chooses a consumption bundle where the utility per dollar spent on Good X is greater than that of Good Y (MU_x / P_x > MU_y / P_y), how should they optimize?",
            options=[
                "A) Consume more of Good Y and less of Good X.",
                "B) Consume more of Good X and less of Good Y to balance the ratios via diminishing utility.",
                "C) Halt all market consumption immediately.",
                "D) Maintain the exact configuration as it is already optimized."
            ],
            index=None
        )
        
        submit_quiz = st.form_submit_button("Submit Answers", type="primary")
        
        if submit_quiz:
            score = 0.0
            
            if q1 == "B) The rate at which a consumer is willing to exchange one good for another while maintaining constant total utility.":
                score += 12.5; st.session_state.q1_correct = True
            else: st.session_state.q1_correct = False
                
            if q2 == "C) The Marginal Rate of Substitution must equal the relative price ratio (MU_x/MU_y = P_x/P_y).":
                score += 12.5; st.session_state.q2_correct = True
            else: st.session_state.q2_correct = False
                
            if q3 == "B) The budget line rotates inward along the horizontal X-axis, making it steeper.":
                score += 12.5; st.session_state.q3_correct = True
            else: st.session_state.q3_correct = False
                
            if q4 == "B) Consume more of Good X and less of Good Y to balance the ratios via diminishing utility.":
                score += 12.5; st.session_state.q4_correct = True
            else: st.session_state.q4_correct = False
                
            st.session_state.quiz_score = score
            st.session_state.quiz_submitted = True
            st.rerun()

    if st.session_state.quiz_submitted:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Raw Performance: {st.session_state.quiz_score}/50 points")
        
        if not st.session_state.q1_correct:
            st.error("**Q1 Clarification:** MRS tracks subjective utility substitution rates, not market costs.")
        if not st.session_state.q2_correct:
            st.error("**Q2 Clarification:** Tangency demands that individual internal willingness to trade matches objective market constraints.")
        if not st.session_state.q3_correct:
            st.error("**Q3 Clarification:** Rising prices for Good X restrict maximum purchase capacity for X, pivoting the budget slope inward.")
        if not st.session_state.q4_correct:
            st.error("**Q4 Clarification:** To optimize, allocate capital toward the item yielding superior utility per dollar until equilibrium is re-established.")

elif learning_path == "💼 Executive Summary":
    st.markdown('<div class="section-header">💼 Strategic Summary for Business Planners</div>', unsafe_allow_html=True)
    exec_col1, exec_col2 = st.columns(2)
    with exec_col1:
        st.markdown("""
        <div class="case-study">
        <h4>🎯 The Paradigm of Consumer Choice</h4>
        <p>Businesses cannot evaluate pricing structures in isolated silos. Every consumer operates under a localized budget constraint while actively ranking alternatives.</p>
        <p>When adjusting prices, remember that consumers constantly recalculate their cross-commodity preferences. If your price tips their internal values out of equilibrium, they will automatically shift to a completely alternative product bundle.</p>
        </div>
        """, unsafe_allow_html=True)
    with exec_col2:
        st.markdown("""
        <div class="concept-note">
        <h4>🛡️ Shifting Preference Contours</h4>
        <p>To retain market share without cutting prices, businesses must reshape consumer indifference curves to make them less substitutable:</p>
        <ul>
            <li><strong>Perceived Uniqueness:</strong> Use product differentiation to create distinct preference gaps where alternatives seem inadequate.</li>
            <li><strong>Value Bundling:</strong> Pair goods in a single transaction format to optimize consumer utility and help them maximize their budget allocation efficiently.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.caption("🎓 Built for Economic Literacy | Consumer Framework System")

with footer_col2:
    st.caption(f"📈 Structural Efficiency Ceiling Cap Active")

with footer_col3:
    st.caption(f"⏰ Real Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
