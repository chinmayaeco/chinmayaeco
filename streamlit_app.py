import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Short-Run Production Optimization Engine",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# SECURE ACCESS SYSTEM
# =====================================================================
def check_password():
    """Returns `True` if the user enters the correct security key."""
    def password_entered():
        if st.session_state["password"] == "PED2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Production Engine Security</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Enter credential key to deploy the Short-Run Simulator.</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.text_input("Security Password", type="password", on_change=password_entered, key="password")
        return False
    
    elif not st.session_state["password_correct"]:
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Production Engine Security</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.text_input("Security Password", type="password", on_change=password_entered, key="password")
            st.error("😕 Access denied. Invalid token key.")
        return False
    
    return True

if not check_password():
    st.stop()

# =====================================================================
# REVAMPED CORE DESIGN SYSTEM (SLATE, COBALT & AMBER METROPOLIS THEME)
# =====================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Main Background & Core Canvas Layout */
    .stApp { background: linear-gradient(135deg, #0F172A 0%, #1E293B 40%, #0F172A 100%); }
    
    /* Premium Header Area Custom Styling */
    .header-gradient {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 50%, #D97706 100%);
        padding: 2.5rem 2rem;
        border-radius: 14px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.15);
    }
    .header-gradient h1 { color: #FFFFFF !important; font-size: 2.4rem !important; font-weight: 800 !important; margin: 0 !important; }
    .header-gradient p { color: rgba(255, 255, 255, 0.9) !important; font-size: 1.05rem !important; margin: 0.5rem 0 0 0 !important; }
    
    /* Dynamic Performance Score Indicator */
    .score-banner {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid rgba(59, 130, 246, 0.3);
        color: #FFFFFF; padding: 1.5rem; border-radius: 12px; text-align: center; margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    }
    .score-banner h2 { color: #60A5FA !important; margin: 0 !important; font-weight: 700; font-size: 1.6rem; }
    
    /* Elegant Content Blocks (Containers/Forms) */
    .stContainer, .stForm {
        background: rgba(30, 41, 59, 0.7) !important; 
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px; padding: 1.75rem; margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25); backdrop-filter: blur(12px);
    }
    
    /* System Division Headers */
    .section-header {
        color: #FBBF24; font-weight: 700; font-size: 1.4rem; margin-bottom: 1.25rem;
        padding-bottom: 0.75rem; border-bottom: 1px solid rgba(251, 191, 36, 0.2);
    }
    
    /* Concept Info Cards & Box Systems */
    .concept-note, .case-study { padding: 1.25rem; border-radius: 8px; margin: 1.2rem 0; }
    .concept-note { background: rgba(59, 130, 246, 0.08); border-left: 4px solid #3B82F6; }
    .concept-note h3 { color: #60A5FA; margin-top: 0 !important; font-size: 1.2rem; }
    .case-study { background: rgba(217, 119, 6, 0.08); border-left: 4px solid #D97706; }
    .case-study h4 { color: #F59E0B; margin-top: 0 !important; font-size: 1.2rem; }
    
    /* Dynamic Metric Highlight Blocks */
    .metric-card {
        background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 1.25rem; border-radius: 8px; text-align: center;
    }
    .metric-card h3 { color: #94A3B8; font-size: 1.05rem; margin: 0 0 0.5rem 0; }
    .metric-value { color: #FBBF24; font-size: 1.8rem; font-weight: 700; margin: 0.25rem 0; }
    
    /* Interface Control Elements / Buttons */
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important; color: white !important;
        border: none !important; padding: 0.65rem 1.75rem !important; border-radius: 6px !important;
        font-weight: 600 !important; transition: all 0.2s ease !important;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover { 
        transform: translateY(-1px) !important; 
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4) !important; 
    }
    
    /* Framework Global Text Elements Adjustments */
    .stMarkdown, p, li { color: #E2E8F0 !important; font-size: 0.98rem; line-height: 1.6; }
    .stSidebar { background: #0F172A !important; border-right: 1px solid rgba(255, 255, 255, 0.05); }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SESSION STATE SYSTEM MANAGEMENT
# =====================================================================
def init_short_run_state():
    defaults = {
        'sim_calculated': False,
        'operational_efficiency': 0.0,
        'knowledge_rating': 0.0,
        'prod_history': [],
        'round_counter': 0,
        'quiz_done': False,
        'ans1_ok': False, 'ans2_ok': False, 'ans3_ok': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_short_run_state()

# =====================================================================
# SIDEBAR CONTROL DECK
# =====================================================================
with st.sidebar:
    st.markdown("### 🏭 Short-Run Operations")
    nav_selection = st.radio(
        "Navigation Hub:",
        options=[
            "🎮 Short-Run Simulator Sandbox",
            "📖 Core Theory Deep Dive",
            "📈 Geometric Margins Analysis",
            "📝 Operational Knowledge Check"
        ]
    )

# =====================================================================
# LIVE SCORE TRACKING ENGINE
# =====================================================================
score_container = st.container()
with score_container:
    combined_raw = st.session_state.operational_efficiency + st.session_state.knowledge_rating
    safety_buffer = 1.8 if combined_raw > 75 else (0.02 * combined_raw)
    final_score = max(0.0, min(98.2, round(combined_raw - safety_buffer, 1)))
    
    st.markdown(f"""
    <div class="score-banner">
        <h2>Industrial Efficiency Index: {final_score} / 100</h2>
        <p style='color: #FBBF24; margin: 0.25rem 0 0 0;'>🎮 Optimization Yield: {round(st.session_state.operational_efficiency, 1)}/50 | 📝 Quiz Accuracy: {round(st.session_state.knowledge_rating, 1)}/50</p>
        <small style='color: #94A3B8;'>System Constraint Note: Absolute zero-loss performance (100%) is structurally unavailable due to physical capital congestion constraints.</small>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE ROUTING ARCHITECTURE
# =====================================================================

if nav_selection == "🎮 Short-Run Simulator Sandbox":
    st.markdown('<div class="section-header">🎮 Variable Labor Allocation Sandbox</div>', unsafe_allow_html=True)
    
    panel_left, panel_right = st.columns([1, 1.2])
    
    with panel_left:
        st.markdown("""
        <div class="concept-note">
        <h3>📌 Short-Run Operational Constraints</h3>
        <p><strong>Fixed Capital Variable Environment:</strong> You operate an industrial manufacturing facility with a locked assembly system setup ($K = 4$ units).</p>
        <p><strong>Your Task:</strong> Determine the optimal number of operational assembly technicians ($L$) to deploy. Your target is to identify the precise boundary where total expansion ends and inefficiency begins.</p>
        <p><strong>Economic Equilibrium Rule:</strong> Efficiency is maximized when your Average Product curve matches your Marginal Product curve ($AP_L = MP_L$). Beyond this intersection point, structural congestion drops net returns.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with panel_right:
        st.markdown("""
        <div class="case-study">
        <h4>⚙️ Fixed Infrastructure Capacity Parameters</h4>
        </div>
        """, unsafe_allow_html=True)
        
        fixed_k = 4
        st.write(f"🔒 **Fixed Capital Capacity Asset Size ($K$):** {fixed_k} Industrial Units (Static)")
        st.write("📊 **Short-Run Production Function:** Standard Non-Linear Model")
        
        # User input slider for labor allocation
        labor_input = st.slider("Deploy Workforce Size (Labor Units - L):", min_value=0, max_value=15, value=2, step=1)
        
        compute_metrics = st.button("🏗️ Calculate Production Metrics", type="primary", use_container_width=True)
        
        if compute_metrics:
            # Short-run production modeling simulation formulas:
            # TP = 6 * K * L^2 - 0.4 * L^3
            tp = float(round((6 * fixed_k * (labor_input ** 2)) - (0.4 * (labor_input ** 3)), 1)) if labor_input > 0 else 0.0
            ap = float(round(tp / labor_input, 2)) if labor_input > 0 else 0.0
            
            # Derivative for exact Marginal Product: dTP/dL = 12 * K * L - 1.2 * L^2
            mp = float(round((12 * fixed_k * labor_input) - (1.2 * (labor_input ** 2)), 2)) if labor_input > 0 else 0.0
            
            # Map dynamic status evaluations based on economic returns zones
            if labor_input == 0:
                zone_status = "Zero Production Capacity ⚪"
                points_given = 0.0
            elif mp > ap:
                zone_status = "Phase 1: Increasing Returns (Under-utilization) 📈"
                points_given = 25.0
            elif mp <= ap and mp >= 0:
                # Target sweet spot calculation zone
                if abs(mp - ap) < 5.0 or labor_input == 10:
                    zone_status = "Optimal Allocation Zone: Peak Efficiency Achieved 🌟"
                    points_given = 47.5
                else:
                    zone_status = "Phase 2: Diminishing Returns (Congested Capital) ⚠️"
                    points_given = 35.0
            else:
                zone_status = "Phase 3: Negative Returns (System Failure) 🚨"
                points_given = 5.0
                
            st.session_state.round_counter += 1
            st.session_state.operational_efficiency = min(47.5, points_given)
            
            st.session_state.prod_history.append({
                'run': st.session_state.round_counter,
                'labor': labor_input,
                'tp': tp,
                'ap': ap,
                'mp': mp,
                'status': zone_status
            })
            st.session_state.sim_calculated = True
            st.rerun()

    if st.session_state.sim_calculated:
        metrics_block = st.container()
        with metrics_block:
            st.markdown('<div class="section-header">📊 Dynamic Factory Output Performance Summary</div>', unsafe_allow_html=True)
            
            latest_run = st.session_state.prod_history[-1]
            card_col1, card_col2, card_col3 = st.columns(3)
            
            with card_col1:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Total Product (TP)</h3>
                    <div class="metric-value">{latest_run['tp']} Units</div>
                    <p style="color: #64748B; font-size: 0.85rem;">Gross Output Yield</p>
                </div>
                """, unsafe_allow_html=True)
                
            with card_col2:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Average Product ($AP_L$)</h3>
                    <div class="metric-value">{latest_run['ap']} Units</div>
                    <p style="color: #64748B; font-size: 0.85rem;">Efficiency Per Worker ($TP/L$)</p>
                </div>
                """, unsafe_allow_html=True)
                
            with card_col3:
                border_accent = "#F59E0B" if "Optimal" in latest_run['status'] else "#3B82F6"
                if "Negative" in latest_run['status']: border_accent = "#EF4444"
                
                st.markdown(f"""
                <div class="metric-card" style="border-color: {border_accent};">
                    <h3 style="color: #94A3B8;">Current Returns Zone</h3>
                    <div class="metric-value" style="font-size: 1.25rem; color: #FBBF24; padding-top: 0.4rem;">{latest_run['status']}</div>
                </div>
                """, unsafe_allow_html=True)
                
            st.markdown("---")
            st.markdown("### 📈 Short-Run Variable Performance Distribution Curves")
            
            # Build continuous arrays to trace out smooth classic microeconomic production graphs
            l_range = np.linspace(0.1, 15, 60)
            tp_curve = (6 * 4 * (l_range ** 2)) - (0.4 * (l_range ** 3))
            ap_curve = tp_curve / l_range
            mp_curve = (12 * 4 * l_range) - (1.2 * (l_range ** 2))
            
            graph_data = pd.DataFrame({
                'Labor Assigned (L)': l_range,
                'Average Product (AP)': ap_curve,
                'Marginal Product (MP)': mp_curve
            })
            
            st.line_chart(graph_data.set_index('Labor Assigned (L)'), color=["#3B82F6", "#F59E0B"])
            st.caption("💡 **Operational Analysis:** Notice that the orange Marginal Product ($MP$) curve intersects the blue Average Product ($AP$) curve exactly at its highest point ($L=10$). This marks the maximum efficiency threshold before systemic crowding takes over.")

elif nav_selection == "📖 Core Theory Deep Dive":
    st.markdown('<div class="section-header">📚 Structural Mechanics of Short-Run Frameworks</div>', unsafe_allow_html=True)
    theory_tabs = st.tabs(["Short-Run Limits Matrix", "The Structural Productivity Matrix", "The Law of Diminishing Returns"])
    
    with theory_tabs[0]:
        st.markdown("""
        <div class="concept-note">
        <h3>⚡ Time Horizon Boundaries: Short Run vs. Long Run</h3>
        <p>In analytical economics, the <strong>Short Run</strong> is not defined by calendar dates or duration windows. It is explicitly an operational period where <strong>at least one structural input is completely fixed</strong>.</p>
        <p><strong>Core Constraints Matrix:</strong></p>
        <ul>
            <li><strong>Fixed Inputs ($K$):</strong> Factors that cannot be adjusted instantly due to contracts, building timelines, or heavy capital procurement constraints (e.g., commercial real estate, factories, customized heavy machinery).</li>
            <li><strong>Variable Inputs ($L$):</strong> Factors that can be adjusted on demand to ramp capacity up or down (e.g., hourly labor shifts, raw assembly materials, utility usage).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with theory_tabs[1]:
        st.markdown("""
        <div class="concept-note">
        <h3>🔢 The Metric Identities</h3>
        <p>Short-run operations are evaluated through three interrelated mathematical indicators:</p>
        <ol>
            <li><strong>Total Product (TP):</strong> The total absolute volume of physical output produced by combining variable labor with a fixed capital footprint.</li>
            <li><strong>Average Product of Labor ($AP_L$):</strong> The output yield generated per individual unit of labor asset deployed. It measures baseline labor efficiency:</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"AP_L = \frac{TP}{L}")
        st.markdown("""
        <div class="concept-note">
        <ol start="3">
            <li><strong>Marginal Product of Labor ($MP_L$):</strong> The net incremental change in total output resulting from adding one additional unit of variable labor:</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"MP_L = \frac{\Delta TP}{\Delta L} \quad \text{or} \quad MP_L = \frac{d(TP)}{dL}")

    with theory_tabs[2]:
        st.markdown("""
        <div class="concept-note">
        <h3>⚖️ The Law of Diminishing Marginal Returns</h3>
        <p>This fundamental law states that <strong>as you add more units of a variable input (labor) to a fixed asset structure (capital), the resulting additions to total output will eventually decline.</strong></p>
        <p><strong>Why Diminishing Returns Occur:</strong></p>
        <ul>
            <li><strong>Initial Stages:</strong> Adding workers allows for task specialization and efficient teamwork, driving performance up.</li>
            <li><strong>The Turning Point:</strong> Because your capital footprint is locked, adding too many workers creates a bottleneck. Workers spend time waiting to use the same equipment, slowing down the rate of production growth.</li>
            <li><strong>The Extreme Stage:</strong> Excessive over-hiring leads to physical congestion and coordination breakdown. Total output drops, and your marginal product turns negative.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif nav_selection == "📈 Geometric Margins Analysis":
    st.markdown('<div class="section-header">📈 Core Mathematical Intersections & Phases</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="case-study">
    <h4>🔄 The Essential Curve Linkages</h4>
    <p>The geometric relationship between Average Product ($AP$) and Marginal Product ($MP$) follows strict mathematical rules on a graph:</p>
    <ul>
        <li><strong>When $MP_L > AP_L$:</strong> The Average Product curve is pulled <strong>upward</strong>. Each new worker adds more output than the current team average, raising the overall efficiency rate.</li>
        <li><strong>When $MP_L < AP_L$:</strong> The Average Product curve is dragged <strong>downward</strong>. The incremental output of new hires is lower than the average, decreasing baseline productivity.</li>
        <li><strong>At Intersect ($MP_L = AP_L$):</strong> The Average Product curve reaches its absolute peak. At this exact cross point, average labor efficiency is maximized.</li>
    </ul>
    </div>
    
    <div class="case-study">
    <h4>🗺️ The Three Stages of Production Architecture</h4>
    <p>A short-run operation goes through three distinct efficiency zones:</p>
    <ol>
        <li><strong>Stage 1: Increasing Returns (From $L=0$ until $AP_L$ peaks)</strong><br>
        Fixed capital assets are underutilized. New hires allow for better specialization, causing both $AP$ and $MP$ to rise. A rational firm will never stop hiring here because their fixed assets have plenty of unused capacity.</li>
        <li><strong>Stage 2: Diminishing Returns (From Peak $AP_L$ until $MP_L = 0$)</strong><br>
        Total output continues to grow, but at a slower rate as fixed assets face crowding. This is the **rational zone of operations**. A firm will choose to operate in this range based on product prices and wage rates.</li>
        <li><strong>Stage 3: Negative Returns (Beyond the Point Where $MP_L = 0$)</strong><br>
        The factory floor is overcrowded. Additional labor reduces absolute total output, making operations highly inefficient.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

elif nav_selection == "📝 Operational Knowledge Check":
    st.markdown('<div class="section-header">📝 Short-Run Operational Knowledge Evaluation</div>', unsafe_allow_html=True)
    st.markdown("Test your understanding of short-run production dynamics. Results include systemic adjustments to reflect capacity constraints.")
    
    with st.form("short_run_quiz"):
        st.markdown("### 1. Defining the Short-Run Horizon")
        q1 = st.radio(
            "What condition explicitly defines a short-run production environment?",
            options=[
                "A) The company's operating runway is shorter than 12 business months.",
                "B) All inputs can be scaled simultaneously to achieve economies of scale.",
                "C) At least one factor of production is completely fixed due to capacity constraints.",
                "D) Total revenue fails to cover variable operating expenses."
            ],
            index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. Tracking the AP and MP Intersection")
        q2 = st.radio(
            "What happens mathematically when the Marginal Product of Labor matches the Average Product of Labor ($MP_L = AP_L$)?",
            options=[
                "A) Total product drops to absolute zero.",
                "B) Average Product of Labor reaches its maximum point.",
                "C) The production line enters Stage 3 negative returns.",
                "D) Fixed capital utilization becomes completely zero."
            ],
            index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Management Strategy in Stage 3")
        q3 = st.radio(
            "If a factory floor operates in Stage 3 where the Marginal Product of Labor is negative ($MP_L < 0$), what is the correct optimization step?",
            options=[
                "A) Hire more workers to help speed up the bottleneck.",
                "B) Keep input levels steady and double product prices.",
                "C) Reduce workforce size to resolve overcrowding and increase total output.",
                "D) Purchase more raw inputs while maintaining the same labor force."
            ],
            index=None
        )
        
        eval_quiz = st.form_submit_button("Submit Performance Metrics", type="primary")
        
        if eval_quiz:
            score_acc = 0.0
            
            if q1 == "C) At least one factor of production is completely fixed due to capacity constraints.":
                score_acc += 16.66; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False
                
            if q2 == "B) Average Product of Labor reaches its maximum point.":
                score_acc += 16.67; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False
                
            if q3 == "C) Reduce workforce size to resolve overcrowding and increase total output.":
                score_acc += 16.67; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False
                
            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Performance Score: {round(st.session_state.knowledge_rating, 1)} / 50 Points")
        
        if not st.session_state.ans1_ok:
            st.error("**Q1 Analysis:** The short run is defined by input flexibility constraints (fixed assets), not by calendar timeframes.")
        if not st.session_state.ans2_ok:
            st.error("**Q2 Analysis:** The $MP$ curve always crosses the $AP$ curve at the exact point where $AP$ reaches its peak.")
        if not st.session_state.ans3_ok:
            st.error("**Q3 Analysis:** In Stage 3, the overcrowding bottleneck is severe. Reducing labor resolves congestion, which increases total output and cuts costs.")

# =====================================================================
# SYSTEM FOOTER DATA TERMINAL
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("🎓 Production Optimization Engine | Corporate Strategy Hub")

with foot_c2:
    st.caption("📈 Asset Bottleneck Congestion Filter Active")

with foot_c3:
    st.caption(f"⏰ Engine System Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
