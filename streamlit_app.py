import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Scale, Scope & Learning Dynamics Engine",
    page_icon="🏗️",
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
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Operations Engine Security</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Enter credential key to deploy the Scale, Scope & Learning Engine.</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.text_input("Security Password", type="password", on_change=password_entered, key="password")
        return False
    
    elif not st.session_state["password_correct"]:
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Operations Engine Security</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.text_input("Security Password", type="password", on_change=password_entered, key="password")
            st.error("😕 Access denied. Invalid token key.")
        return False
    
    return True

if not check_password():
    st.stop()

# =====================================================================
# CORE DESIGN SYSTEM (SLATE, COBALT & AMBER METROPOLIS THEME)
# =====================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Main Background & Core Canvas Layout */
    .stApp { background: linear-gradient(135deg, #0F172A 0%, #1E293B 40%, #0F172A 100%); }
    
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
def init_system_state():
    defaults = {
        'knowledge_rating': 0.0,
        'quiz_done': False,
        'ans1_ok': False, 'ans2_ok': False, 'ans3_ok': False, 'ans4_ok': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_system_state()

# =====================================================================
# SIDEBAR CONTROL DECK
# =====================================================================
with st.sidebar:
    st.markdown("### 🏗️ Operations Hub")
    nav_selection = st.radio(
        "Navigation Hub:",
        options=[
            "⚖️ Economies & Diseconomies of Scale",
            "🔀 Economies & Diseconomies of Scope",
            "📈 Learning Curve & Experience Dynamics",
            "📝 Knowledge Check Deck"
        ]
    )

# =====================================================================
# LIVE SCORE TRACKING ENGINE
# =====================================================================
score_container = st.container()
with score_container:
    st.markdown(f"""
    <div class="score-banner">
        <h2>Operational Knowledge Rating: {round(st.session_state.knowledge_rating, 1)} / 100 Index</h2>
        <p style='color: #FBBF24; margin: 0.25rem 0 0 0;'>
            📝 Concept Mastery Evaluation Active
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE ROUTING ARCHITECTURE
# =====================================================================

# --- SECTION 1: ECONOMIES & DISECONOMIES OF SCALE ---
if nav_selection == "⚖️ Economies & Diseconomies of Scale":
    st.markdown('<div class="section-header">⚖️ Economies & Diseconomies of Scale</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>📉 Understanding Scale Dynamics</h3>
    <p><strong>Scale Dynamics</strong> examine how per-unit costs change as a firm scales up total output volume ($Q$) in a single product line over the long run.</p>
    <ul>
        <li><strong>Economies of Scale:</strong> Occurs when Long-Run Average Cost ($LRAC$) <em>declines</em> as output ($Q$) increases.</li>
        <li><strong>Diseconomies of Scale:</strong> Occurs when $LRAC$ <em>rises</em> as output continues to expand beyond the Minimum Efficient Scale ($MES$).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col_eos_a, col_eos_b = st.columns(2)
    with col_eos_a:
        st.markdown(r"""
        <div class="case-study">
        <h4>💡 Key Drivers of Economies of Scale ($LRAC \downarrow$)</h4>
        <ul>
            <li><strong>Technical & Physical Rules:</strong> The "Square-Cube Law" (doubling a container's surface area increases volume 8x, lowering per-unit storage cost).</li>
            <li><strong>Specialization of Labor:</strong> Complex processes broken down into micro-tasks lead to higher efficiency and expertise.</li>
            <li><strong>Indivisibilities:</strong> Spreading large non-divisible fixed costs (e.g., massive machinery, high-cost R&D) over more units.</li>
            <li><strong>Bulk Procurement:</strong> Higher bargaining power yields purchasing discounts on raw materials.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_eos_b:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #EF4444;">
        <h4 style="color: #F87171;">🚨 Drivers of Diseconomies of Scale ($LRAC \uparrow$)</h4>
        <ul>
            <li><strong>Managerial & Coordination Friction:</strong> Bureaucratic bloat, communication lag, and hierarchical latency in massive organizations.</li>
            <li><strong>Principal-Agent Misalignment:</strong> Reduced employee monitoring effectiveness leading to lower morale and productivity.</li>
            <li><strong>Input Supply Bottlenecks:</strong> Regional resource depletion bidding up factor input prices ($w$ or $r$).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("#### 📐 Mathematical Condition for Scale Elasticity")
    st.latex(r"E_C = \frac{\% \Delta TC}{\% \Delta Q} = \frac{MC}{AC}")
    st.markdown(r"""
    <p style='text-align: center;'>
        If $E_C < 1$ (or $MC < AC$), <strong>Economies of Scale</strong> exist.<br>
        If $E_C = 1$ (or $MC = AC$), <strong>Constant Costs</strong> exist.<br>
        If $E_C > 1$ (or $MC > AC$), <strong>Diseconomies of Scale</strong> exist.
    </p>
    """, unsafe_allow_html=True)

# --- SECTION 2: ECONOMIES & DISECONOMIES OF SCOPE ---
elif nav_selection == "🔀 Economies & Diseconomies of Scope":
    st.markdown('<div class="section-header">🔀 Economies & Diseconomies of Scope</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>🔀 Understanding Scope Dynamics</h3>
    <p>While <em>Scale</em> measures cost savings from volume in a single product, <strong>Scope</strong> measures cost savings achieved by producing <strong>multiple distinct products joint-together</strong> using shared infrastructure, operational assets, or capabilities.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📐 Degree of Economies of Scope Formula ($S$)")
    st.latex(r"S = \frac{TC(Q_1, 0) + TC(0, Q_2) - TC(Q_1, Q_2)}{TC(Q_1, Q_2)}")
    
    col_scope_1, col_scope_2 = st.columns(2)
    with col_scope_1:
        st.markdown(r"""
        <div class="case-study">
        <h4>✅ Scope Economies ($S > 0$)</h4>
        <p>Joint production is <strong>cheaper</strong> than standalone production.</p>
        <ul>
            <li><strong>Shared Technological Platforms:</strong> Car manufacturers using one underlying chassis for sedans and SUVs.</li>
            <li><strong>By-Product Utilization:</strong> Sawmills utilizing timber for wood products and converting residual sawdust into particleboard.</li>
            <li><strong>Shared Distribution & Marketing:</strong> Using a single sales force or logistical network to distribute multiple product lines.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_scope_2:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #EF4444;">
        <h4 style="color: #F87171;">❌ Scope Diseconomies ($S < 0$)</h4>
        <p>Joint production is <strong>more expensive</strong> than standalone production.</p>
        <ul>
            <li><strong>Operational Interference:</strong> Running custom high-precision manufacturing in the same line as high-speed mass production leads to machine setup bottlenecks.</li>
            <li><strong>Managerial Complexity:</strong> Managing fundamentally opposing business models under one roof dilutes operational focus.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🧮 Interactive Scope Economies Calculator")
    sc_col1, sc_col2 = st.columns([1, 1.2])
    
    with sc_col1:
        cost_p1 = st.number_input("Standalone Cost for Product 1 ($TC(Q_1, 0)$):", min_value=1.0, value=100000.0, step=5000.0)
        cost_p2 = st.number_input("Standalone Cost for Product 2 ($TC(0, Q_2)$):", min_value=1.0, value=80000.0, step=5000.0)
        cost_joint = st.number_input("Joint Production Cost ($TC(Q_1, Q_2)$):", min_value=1.0, value=150000.0, step=5000.0)
        
    with sc_col2:
        s_value = (cost_p1 + cost_p2 - cost_joint) / cost_joint
        savings_pct = round(s_value * 100, 2)
        
        if s_value > 0:
            status_text = f"✅ Positive Economies of Scope ($S = {round(s_value, 4)}$)"
            sub_text = f"Joint production saves **{savings_pct}%** compared to standalone operations."
        elif s_value < 0:
            status_text = f"❌ Diseconomies of Scope ($S = {round(s_value, 4)}$)"
            sub_text = f"Joint production costs **{abs(savings_pct)}%** more than producing separately."
        else:
            status_text = "⚖️ Neutral Scope Effect ($S = 0$)"
            sub_text = "No cost difference between joint and separate production."
            
        st.markdown(f"""
        <div class="metric-card">
            <h3>Degree of Scope Measure (S)</h3>
            <div class="metric-value">{round(s_value, 4)}</div>
            <p style="color: #60A5FA; font-size: 0.95rem;">{status_text}</p>
            <p style="color: #94A3B8; font-size: 0.85rem;">{sub_text}</p>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 3: LEARNING CURVE & EXPERIENCE DYNAMICS ---
elif nav_selection == "📈 Learning Curve & Experience Dynamics":
    st.markdown('<div class="section-header">📈 Learning Curve & Experience Dynamics</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>📈 Learning Curve (Experience Effect)</h3>
    <p><strong>Scale vs. Learning Distinguishability:</strong> Scale economies depend on the <em>rate of production per time period</em> ($Q$). The <strong>Learning Curve</strong> depends on the <em>cumulative past output</em> ($N$) produced over time.</p>
    <p>As cumulative output doubles, labor input per unit drops by a predictable percentage (the <strong>Learning Rate</strong>).</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📐 Power-Law Learning Curve Equation")
    st.latex(r"L(N) = A \cdot N^{-b}")
    st.markdown(r"""
    <p style='font-size:0.9rem;'>Where $L(N)$ is the labor requirement for unit $N$, $A$ is the labor requirement for the 1st unit, $N$ is cumulative output, and $b$ is the learning elasticity parameter ($b = \frac{-\log(\text{Learning Rate})}{\log(2)}$).</p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🧮 Interactive Learning Curve Cost Simulator")
    
    lc_col1, lc_col2 = st.columns([1, 1.2])
    with lc_col1:
        base_hours = st.number_input("Labor Hours for 1st Unit ($A$):", min_value=10.0, max_value=5000.0, value=100.0, step=10.0)
        learn_pct = st.slider("Learning Rate (% labor hours retained upon doubling cumulative output):", min_value=50, max_value=95, value=80, step=5)
        target_units = st.slider("Select Cumulative Unit Number ($N$):", min_value=1, max_value=128, value=16, step=1)
        
        b_param = - (np.log(learn_pct / 100.0) / np.log(2.0))
        hours_nth = base_hours * (target_units ** (-b_param))
        
    with lc_col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Labor Requirement for Unit #{target_units}</h3>
            <div class="metric-value">{round(hours_nth, 2)} Hours</div>
            <p style="color: #64748B; font-size: 0.85rem;">Elasticity Parameter ($b$): {round(b_param, 4)}</p>
        </div>
        """, unsafe_allow_html=True)
        
        doublings = [1, 2, 4, 8, 16, 32, 64, 128]
        table_data = []
        for d in doublings:
            h = base_hours * (d ** (-b_param))
            table_data.append({
                "Cumulative Output (N)": d, 
                "Labor Hours / Unit": round(h, 2), 
                "Cost Reduction vs Unit #1": f"{round((1 - h/base_hours)*100, 1)}%"
            })
        
        st.dataframe(pd.DataFrame(table_data), use_container_width=True)

# --- SECTION 4: KNOWLEDGE CHECK DECK ---
elif nav_selection == "📝 Knowledge Check Deck":
    st.markdown('<div class="section-header">📝 Scale, Scope & Learning Knowledge Evaluation</div>', unsafe_allow_html=True)
    st.markdown("Test your operational understanding of scale economies, scope economies, and learning curves.")
    
    with st.form("operations_quiz"):
        st.markdown("### 1. Scale Elasticity Parameter Interpretation")
        q1 = st.radio(
            "If a plant's cost elasticity parameter Ec = (MC / AC) is equal to 0.75, which operational state is the plant experiencing?",
            options=[
                "A) Diseconomies of Scale (LRAC is rising)",
                "B) Minimum Efficient Scale (LRAC is at its absolute floor)",
                "C) Economies of Scale (LRAC is declining as output increases)",
                "D) Scope Diseconomies"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. Scale vs. Learning Distinction")
        q2 = st.radio(
            "What is the key difference between Economies of Scale and the Learning Curve?",
            options=[
                "A) Scale depends on cumulative production over time; Learning depends on current output rate per period.",
                "B) Scale depends on output rate per period (Q); Learning depends on cumulative volume (N) over time.",
                "C) Scale applies only to labor, while Learning applies only to capital.",
                "D) Scale causes costs to rise, while Learning causes costs to drop."
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Degree of Economies of Scope Calculation")
        q3 = st.radio(
            "A company produces Product A separately for $90k and Product B separately for $50k. Producing both together costs $120k. What is the degree of scope economy?",
            options=[
                "A) S = -0.167 (Diseconomies of Scope)",
                "B) S = 0.167 (Positive Economies of Scope)",
                "C) S = 0.833 (Scale Economies)",
                "D) S = 0.000 (Neutral Scope)"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 4. Learning Curve Calculation")
        q4 = st.radio(
            "A factory operates on an 80% Learning Curve. If Unit #1 required 100 hours, how many labor hours will Unit #4 require?",
            options=[
                "A) 80 hours",
                "B) 64 hours",
                "C) 50 hours",
                "D) 40 hours"
            ], index=None
        )
        
        eval_quiz = st.form_submit_button("Submit Evaluation", type="primary")
        
        if eval_quiz:
            score_acc = 0.0
            
            if q1 == "C) Economies of Scale (LRAC is declining as output increases)":
                score_acc += 25.0; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False
                
            if q2 == "B) Scale depends on output rate per period (Q); Learning depends on cumulative volume (N) over time.":
                score_acc += 25.0; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False
                
            if q3 == "B) S = 0.167 (Positive Economies of Scope)":
                score_acc += 25.0; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False

            if q4 == "B) 64 hours":
                score_acc += 25.0; st.session_state.ans4_ok = True
            else: st.session_state.ans4_ok = False
                
            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Score: {round(st.session_state.knowledge_rating, 1)} / 100 Points")
        
        if not st.session_state.ans1_ok:
            st.error("**Q1 Analysis:** When $E_C = MC/AC < 1$, Marginal Cost is below Average Cost, pulling the $LRAC$ curve downward (Economies of Scale).")
        if not st.session_state.ans2_ok:
            st.error("**Q2 Analysis:** Scale economies relate to production rate per period ($Q$). Learning curves relate to accumulated experience over time ($N$).")
        if not st.session_state.ans3_ok:
            st.error("**Q3 Analysis:** $S = (90k + 50k - 120k) / 120k = 20k / 120k = +0.167 > 0$, indicating positive cost savings from joint production.")
        if not st.session_state.ans4_ok:
            st.error("**Q4 Analysis:** With an 80% curve: Unit #1 = 100 hrs. Unit #2 (1st doubling) = 100 * 0.80 = 80 hrs. Unit #4 (2nd doubling) = 80 * 0.80 = 64 hrs.")

# =====================================================================
# SYSTEM FOOTER DATA TERMINAL
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("🎓 Scale, Scope & Learning Dynamics Engine")

with foot_c2:
    st.caption("🚀 Operations Strategy Module Active")

with foot_c3:
    st.caption(f"⏰ System Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
