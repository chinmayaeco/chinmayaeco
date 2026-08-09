import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Perfect Competition Dynamics Engine",
    page_icon="⚖️",
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
        st.markdown("<p style='text-align: center;'>Enter credential key to deploy the Perfect Competition Engine.</p>", unsafe_allow_html=True)
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
    
    /* Content Blocks (Containers/Forms) */
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
    
    /* Global Text Adjustments */
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
    st.markdown("### ⚖️ Competition Hub")
    nav_selection = st.radio(
        "Navigation Hub:",
        options=[
            "📌 Market Foundations & Price Taking",
            "⚡ Short-Run Equilibrium & Shutdown Rules",
            "🔄 Long-Run Equilibrium & Industry Efficiency",
            "🧮 Interactive Firm & Market Simulator",
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
        <h2>Perfect Competition Mastery Index: {round(st.session_state.knowledge_rating, 1)} / 100</h2>
        <p style='color: #FBBF24; margin: 0.25rem 0 0 0;'>
            📝 Competitive Dynamics Evaluation Active
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE ROUTING ARCHITECTURE
# =====================================================================

# --- SECTION 1: MARKET FOUNDATIONS & PRICE TAKING ---
if nav_selection == "📌 Market Foundations & Price Taking":
    st.markdown('<div class="section-header">📌 Foundations of Perfect Competition</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>🏛️ Core Assumptions of Perfect Competition</h3>
    <p>A <strong>Perfectly Competitive Market</strong> is an idealized market structure where price is determined purely by aggregate market demand and market supply. Individual firms are <strong>price takers</strong> with zero market power.</p>
    <ul>
        <li><strong>Many Buyers and Sellers:</strong> No single economic actor can influence the market price.</li>
        <li><strong>Homogeneous Products:</strong> Goods offered by sellers are perfect substitutes.</li>
        <li><strong>Free Entry and Exit:</strong> No barriers to entry or exit in the long run.</li>
        <li><strong>Perfect Information:</strong> Buyers and sellers have full knowledge of prices, quality, and technology.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col_found_a, col_found_b = st.columns(2)
    with col_found_a:
        st.markdown(r"""
        <div class="case-study">
        <h4>🎯 The Firm as a Price Taker</h4>
        <p>Because products are identical and sellers are small relative to the market, an individual firm faces a <strong>perfectly elastic horizontal demand curve</strong> at the prevailing market price ($P^*$).</p>
        <ul>
            <li>If a firm charges $P > P^*$, demand falls to <strong>zero</strong>.</li>
            <li>If a firm charges $P \le P^*$, it can sell all output it produces without dropping the price.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_found_b:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #10B981;">
        <h4 style="color: #34D399;">📊 Revenue Identities under Price Taking</h4>
        <p>When price ($P$) is constant regardless of output quantity ($q$):</p>
        <ul>
            <li><strong>Total Revenue:</strong> $TR(q) = P \cdot q$</li>
            <li><strong>Average Revenue:</strong> $AR(q) = \frac{TR}{q} = P$</li>
            <li><strong>Marginal Revenue:</strong> $MR(q) = \frac{dTR}{dq} = P$</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("#### 📐 Fundamental Identity of the Price-Taking Firm")
    st.latex(r"P = AR = MR = \text{Individual Firm Demand } (d)")

# --- SECTION 2: SHORT-RUN EQUILIBRIUM & SHUTDOWN RULES ---
elif nav_selection == "⚡ Short-Run Equilibrium & Shutdown Rules":
    st.markdown('<div class="section-header">⚡ Short-Run Profit Maximization & Shutdown Rules</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>⚙️ Profit Maximization Condition</h3>
    <p>In the short run, capital is fixed while variable inputs (like labor) can adjust. The firm maximizes economic profit ($\pi$) where marginal revenue equals marginal cost, provided $MC$ is rising.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📐 Profit Maximization Rule")
    st.latex(r"M\pi = MR - MC = 0 \implies P = MC(q^*) \quad \text{where } \frac{dMC}{dq} > 0")
    
    col_sr_1, col_sr_2 = st.columns(2)
    with col_sr_1:
        st.markdown(r"""
        <div class="case-study">
        <h4>📈 Short-Run Profitability States</h4>
        <ul>
            <li><strong>Economic Profit ($\pi > 0$):</strong> $P > ATC(q^*)$</li>
            <li><strong>Break-Even ($\pi = 0$):</strong> $P = \min ATC$</li>
            <li><strong>Operating Loss ($\pi < 0$):</strong> $AVC(q^*) \le P < ATC(q^*)$ (Loss is less than Fixed Cost)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_sr_2:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #EF4444;">
        <h4 style="color: #F87171;">🛑 Short-Run Shutdown Rule</h4>
        <p>A firm will <strong>shut down operations immediately</strong> ($q^* = 0$) if total revenue cannot even cover variable costs:</p>
        <p style="text-align: center; font-weight: bold; font-size: 1.1rem; color: #F87171;">
            $P < \min AVC$
        </p>
        <p>If $P \ge \min AVC$, the firm continues producing in the short run to minimize losses by covering all variable costs and a portion of fixed costs.</p>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 3: LONG-RUN EQUILIBRIUM & INDUSTRY EFFICIENCY ---
elif nav_selection == "🔄 Long-Run Equilibrium & Industry Efficiency":
    st.markdown('<div class="section-header">🔄 Long-Run Dynamics & Economic Efficiency</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>🔄 Free Entry and Exit Dynamics</h3>
    <p>In the long run, all inputs are variable and firms can freely enter or exit the market. Unconstrained entry and exit eliminate positive or negative economic profits across the industry.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_lr_1, col_lr_2 = st.columns(2)
    with col_lr_1:
        st.markdown(r"""
        <div class="case-study">
        <h4>➡️ Short-Run Profit $\implies$ Market Entry</h4>
        <p>When $P > \min ATC$ in the short run:</p>
        <ol>
            <li>Incumbent firms earn positive economic profit ($\pi > 0$).</li>
            <li>New firms enter the industry.</li>
            <li>Market supply curve shifts <strong>right</strong> ($S \to S'$).</li>
            <li>Market price drops until $P^* = \min ATC$ and $\pi = 0$.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    with col_lr_2:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #EF4444;">
        <h4 style="color: #F87171;">⬅️ Short-Run Loss $\implies$ Market Exit</h4>
        <p>When $P < \min ATC$ in the short run:</p>
        <ol>
            <li>Incumbent firms incur economic losses ($\pi < 0$).</li>
            <li>Firms exit the industry over time.</li>
            <li>Market supply curve shifts <strong>left</strong> ($S \to S''$).</li>
            <li>Market price rises until $P^* = \min ATC$ and $\pi = 0$.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("#### 🏛️ Economic Efficiency Benchmarks")
    st.latex(r"P = MC = \min LRATC")
    
    eff_c1, eff_c2 = st.columns(2)
    with eff_c1:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Allocative Efficiency</h3>
            <div class="metric-value">P = MC</div>
            <p style="color: #94A3B8; font-size: 0.85rem;">Price reflects marginal benefit to consumers. Total surplus (Consumer + Producer) is maximized with zero deadweight loss.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with eff_c2:
        st.markdown("""
        <div class="metric-card">
            <h3>⚙️ Productive Efficiency</h3>
            <div class="metric-value">P = min LRATC</div>
            <p style="color: #94A3B8; font-size: 0.85rem;">Goods are produced at the lowest possible per-unit cost in the long run. Resources are utilized at maximum productivity.</p>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 4: INTERACTIVE FIRM & MARKET SIMULATOR ---
elif nav_selection == "🧮 Interactive Firm & Market Simulator":
    st.markdown('<div class="section-header">🧮 Interactive Firm Production & Cost Simulator</div>', unsafe_allow_html=True)
    st.markdown("Model a price-taking firm with cost function $TC(q) = FC + a \cdot q + b \cdot q^2$.")
    
    sim_col1, sim_col2 = st.columns([1, 1.2])
    
    with sim_col1:
        price = st.number_input("Market Price ($P$):", min_value=1.0, max_value=200.0, value=50.0, step=5.0)
        fixed_cost = st.number_input("Fixed Cost ($FC$):", min_value=10.0, max_value=1000.0, value=100.0, step=10.0)
        param_a = st.number_input("Linear Variable Cost Coeff ($a$):", min_value=0.0, max_value=50.0, value=10.0, step=1.0)
        param_b = st.number_input("Quadratic Cost Coeff ($b$):", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
        
        # Mathematical Derivations:
        # TC(q) = FC + a*q + b*q^2
        # VC(q) = a*q + b*q^2
        # MC(q) = a + 2*b*q
        # AVC(q) = a + b*q
        # ATC(q) = FC/q + a + b*q
        
        min_avc = param_a  # min AVC occurs as q -> 0 for quadratic VC
        min_atc = param_a + 2 * np.sqrt(fixed_cost * param_b)
        q_atc_min = np.sqrt(fixed_cost / param_b)
        
        # Profit Maximization: P = MC = a + 2*b*q => q* = (P - a) / (2*b)
        if price < min_avc:
            q_opt = 0.0
            status = "🛑 SHUT DOWN IMMEDIATELY (P < min AVC)"
            status_color = "#EF4444"
        else:
            q_opt = max(0.0, (price - param_a) / (2 * param_b))
            if price > min_atc:
                status = "🟢 OPERATING WITH ECONOMIC PROFIT (P > min ATC)"
                status_color = "#10B981"
            elif abs(price - min_atc) < 1e-3:
                status = "⚖️ BREAK-EVEN / LONG-RUN EQUILIBRIUM (P = min ATC)"
                status_color = "#FBBF24"
            else:
                status = "🟡 OPERATING AT LOSS IN SHORT RUN (min AVC <= P < min ATC)"
                status_color = "#F59E0B"
                
        tr = price * q_opt
        tc = fixed_cost + param_a * q_opt + param_b * (q_opt ** 2) if q_opt > 0 else fixed_cost
        profit = tr - tc if q_opt > 0 else -fixed_cost
        
    with sim_col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Optimal Output ($q^*$)</h3>
            <div class="metric-value">{round(q_opt, 2)} Units</div>
            <p style="color: {status_color}; font-weight: 600; font-size: 0.95rem;">{status}</p>
        </div>
        """, unsafe_allow_html=True)
        
        metrics_df = pd.DataFrame([
            {"Metric": "Market Price (P)", "Value": f"${round(price, 2)}"},
            {"Metric": "Optimal Output (q*)", "Value": f"{round(q_opt, 2)} units"},
            {"Metric": "Total Revenue (TR)", "Value": f"${round(tr, 2)}"},
            {"Metric": "Total Cost (TC)", "Value": f"${round(tc, 2)}"},
            {"Metric": "Economic Profit / Loss (π)", "Value": f"${round(profit, 2)}"},
            {"Metric": "Break-Even Price (min ATC)", "Value": f"${round(min_atc, 2)} at q={round(q_atc_min, 2)}"},
            {"Metric": "Shutdown Price Threshold (min AVC)", "Value": f"${round(min_avc, 2)}"}
        ])
        
        st.dataframe(metrics_df, use_container_width=True)

# --- SECTION 5: KNOWLEDGE CHECK DECK ---
elif nav_selection == "📝 Knowledge Check Deck":
    st.markdown('<div class="section-header">📝 Perfect Competition Knowledge Evaluation</div>', unsafe_allow_html=True)
    st.markdown("Test your economic knowledge of market structures, short-run profit rules, and long-run adjustments.")
    
    with st.form("competition_quiz"):
        st.markdown("### 1. Demand Curve Faced by a Price Taker")
        q1 = st.radio(
            "What is the elasticity of the demand curve faced by an individual firm in a perfectly competitive market?",
            options=[
                "A) Perfectly Inelastic (Vertical)",
                "B) Unit Elastic",
                "C) Perfectly Elastic (Horizontal at market price)",
                "D) Downward Sloping with finite price elasticity"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. Short-Run Shutdown Decision")
        q2 = st.radio(
            "Under what condition should a competitive firm shut down immediately in the short run?",
            options=[
                "A) Market Price falls below Average Total Cost (P < ATC)",
                "B) Market Price falls below Average Variable Cost (P < AVC)",
                "C) Total Profit becomes equal to zero (π = 0)",
                "D) Marginal Cost is equal to Marginal Revenue (MC = MR)"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Long-Run Competitive Equilibrium")
        q3 = st.radio(
            "In the long run, free entry and exit ensure that every firm in a competitive industry earns:",
            options=[
                "A) Positive economic profit (π > 0)",
                "B) Zero economic profit (P = min ATC)",
                "C) Zero accounting profit",
                "D) Monopoly rents"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 4. Economic Efficiency Conditions")
        q4 = st.radio(
            "Which pair of equations represents allocative and productive efficiency respectively in long-run competitive equilibrium?",
            options=[
                "A) Allocative: P = MC ; Productive: P = min ATC",
                "B) Allocative: P = min ATC ; Productive: P = MC",
                "C) Allocative: MR = MC ; Productive: TR = TC",
                "D) Allocative: P > MC ; Productive: P = AVC"
            ], index=None
        )
        
        eval_quiz = st.form_submit_button("Submit Evaluation", type="primary")
        
        if eval_quiz:
            score_acc = 0.0
            
            if q1 == "C) Perfectly Elastic (Horizontal at market price)":
                score_acc += 25.0; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False
                
            if q2 == "B) Market Price falls below Average Variable Cost (P < AVC)":
                score_acc += 25.0; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False
                
            if q3 == "B) Zero economic profit (P = min ATC)":
                score_acc += 25.0; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False

            if q4 == "A) Allocative: P = MC ; Productive: P = min ATC":
                score_acc += 25.0; st.session_state.ans4_ok = True
            else: st.session_state.ans4_ok = False
                
            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Score: {round(st.session_state.knowledge_rating, 1)} / 100 Points")
        
        if not st.session_state.ans1_ok:
            st.error("**Q1 Analysis:** An individual firm in perfect competition is a price taker, facing a horizontal (perfectly elastic) demand curve at $P^*$.")
        if not st.session_state.ans2_ok:
            st.error("**Q2 Analysis:** In the short run, if $P < AVC$, total revenue cannot cover variable costs, so shutting down minimizes loss to fixed costs.")
        if not st.session_state.ans3_ok:
            st.error("**Q3 Analysis:** Free entry/exit drives economic profit down to zero ($\pi = 0$) in the long run, where $P = \min ATC$.")
        if not st.session_state.ans4_ok:
            st.error("**Q4 Analysis:** Allocative efficiency occurs where $P = MC$ (price equals marginal cost), and productive efficiency occurs where $P = \min ATC$.")

# =====================================================================
# SYSTEM FOOTER DATA TERMINAL
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("🎓 Perfectly Competitive Market Dynamics Engine")

with foot_c2:
    st.caption("🚀 Microeconomics & Operations Strategy Module")

with foot_c3:
    st.caption(f"⏰ System Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
