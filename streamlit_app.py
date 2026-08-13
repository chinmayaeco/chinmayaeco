import streamlit as st
import pandas as pd
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Monopoly Dynamics Engine",
    page_icon="👑",
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
        st.markdown("<p style='text-align: center;'>Enter credential key to deploy the Monopoly Engine.</p>", unsafe_allow_html=True)
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
    st.markdown("### 👑 Monopoly Hub")
    nav_selection = st.radio(
        "Navigation Hub:",
        options=[
            "📌 Market Foundations & Price Searching",
            "⚡ Profit Maximization & Price Discrimination",
            "🔄 Market Inefficiency & Deadweight Loss",
            "🧮 Monopoly Profit & Pricing Power Simulator",
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
        <h2>Monopoly Mastery Index: {round(st.session_state.knowledge_rating, 1)} / 100</h2>
        <p style='color: #FBBF24; margin: 0.25rem 0 0 0;'>
            📝 Monopolistic Market Dynamics Evaluation Active
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE ROUTING ARCHITECTURE
# =====================================================================

# --- SECTION 1: MARKET FOUNDATIONS & PRICE SEARCHING ---
if nav_selection == "📌 Market Foundations & Price Searching":
    st.markdown('<div class="section-header">📌 Foundations of Monopoly Power</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>🏛️ Core Assumptions of Monopoly</h3>
    <p>A <strong>Monopoly</strong> is a market structure characterized by a single seller of a unique product with no close substitutes. The single firm <strong>is</strong> the industry, granting it significant market power as a <strong>price maker</strong>.</p>
    <ul>
        <li><strong>Single Seller:</strong> A single firm controls 100% (or dominant majority) of the market supply.</li>
        <li><strong>Unique Product:</strong> No close substitutes exist; consumers must accept the product or forgo it.</li>
        <li><strong>High Barriers to Entry:</strong> Legal (patents/licenses), natural (economies of scale), or strategic barriers protect pure profits long-term.</li>
        <li><strong>Imperfect Information / Trade Secrets:</strong> Proprietary production technologies or resource control prevent market duplication.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col_found_a, col_found_b = st.columns(2)
    with col_found_a:
        st.markdown(r"""
        <div class="case-study">
        <h4>🎯 The Firm as a Price Maker</h4>
        <p>Because the firm faces the <strong>entire market demand curve</strong> (downward-sloping), to sell a larger quantity ($Q$), it must lower its price ($P$) on <em>all</em> units sold (assuming single-price pricing).</p>
        <ul>
            <li>Demand curve is downward-sloping: $P = f(Q)$.</li>
            <li>Marginal Revenue ($MR$) lies <strong>below</strong> Average Revenue ($AR = P$) for all $Q > 0$.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_found_b:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #10B981;">
        <h4 style="color: #34D399;">📊 Revenue Mechanics for Monopolists</h4>
        <p>Assuming a linear demand function $P = a - bQ$:</p>
        <ul>
            <li><strong>Total Revenue (TR):</strong> $TR = P \times Q = aQ - bQ^2$</li>
            <li><strong>Average Revenue (AR):</strong> $AR = \frac{TR}{Q} = P = a - bQ$</li>
            <li><strong>Marginal Revenue (MR):</strong> $MR = \frac{dTR}{dQ} = a - 2bQ$</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("#### 📐 Fundamental Inequality of a Monopoly")
    st.latex(r"P = AR > MR \quad \text{for all } Q > 0")

# --- SECTION 2: PROFIT MAXIMIZATION & PRICE DISCRIMINATION ---
elif nav_selection == "⚡ Profit Maximization & Price Discrimination":
    st.markdown('<div class="section-header">⚡ Profit Maximization & Price Discrimination</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>⚙️ Profit Maximization Mechanism</h3>
    <p>A profit-maximizing monopolist sets production where <strong>Marginal Revenue equals Marginal Cost ($MR = MC$)</strong> to find optimal output $Q^*$, then projects up to the <strong>Demand curve</strong> to set optimal price $P^*$.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📐 Profit Maximization and Markup Rule")
    st.latex(r"MR = MC \implies P^* \left(1 - \frac{1}{|E_d|}\right) = MC")
    
    col_sr_1, col_sr_2 = st.columns(2)
    with col_sr_1:
        st.markdown(r"""
        <div class="case-study">
        <h4>📈 Lerner Index of Monopoly Power</h4>
        <p>The degree of market power is quantified by the firm's ability to charge a markup over marginal cost:</p>
        <p style="text-align: center; font-weight: bold; font-size: 1.1rem; color: #F59E0B;">
            $L = \frac{P - MC}{P} = \frac{1}{|E_d|}$
        </p>
        <p>Higher price inelasticity of demand ($|E_d| \to 0$) yields greater markup potential.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_sr_2:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #8B5CF6;">
        <h4 style="color: #A78BFA;">🎯 Degrees of Price Discrimination</h4>
        <ul>
            <li><strong>1st Degree (Perfect):</strong> Charges each consumer their exact willingness to pay. Captures 100% of consumer surplus ($MR = P$).</li>
            <li><strong>2nd Degree (Quantity Block):</strong> Charges different rates depending on volume/quantity consumed.</li>
            <li><strong>3rd Degree (Segmented):</strong> Segments markets by elasticity ($MR_1 = MR_2 = MC$).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 3: MARKET INEFFICIENCY & DEADWEIGHT LOSS ---
elif nav_selection == "🔄 Market Inefficiency & Deadweight Loss":
    st.markdown('<div class="section-header">🔄 Social Cost of Monopoly & Inefficiency</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>📉 Deadweight Loss & Economic Welfare</h3>
    <p>Because a single-price monopolist restricts output ($Q_m < Q_c$) and charges a higher price ($P_m > P_c$), price exceeds marginal cost ($P > MC$). This creates a structural loss in total social surplus known as <strong>Deadweight Loss (DWL)</strong>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_lr_1, col_lr_2 = st.columns(2)
    with col_lr_1:
        st.markdown(r"""
        <div class="case-study">
        <h4>⚖️ Competitive vs. Monopoly Equilibrium</h4>
        <ul>
            <li><strong>Perfect Competition:</strong> $P_c = MC$, maximizing Total Social Surplus.</li>
            <li><strong>Monopoly:</strong> Restricts output to $Q_m$ where $MR = MC$, setting price $P_m > MC$.</li>
            <li><strong>Welfare Transfer:</strong> Consumer surplus is partially converted into producer surplus (monopoly profit) and partially destroyed as DWL.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_lr_2:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #EF4444;">
        <h4 style="color: #F87171;">🏛️ Natural Monopoly & Regulation</h4>
        <p>When long-run average costs ($LRATC$) continuously decline over market demand due to massive economies of scale, a single firm operates most efficiently.</p>
        <ul>
            <li><strong>Unregulated:</strong> Sets $MR = MC$, earns high profits, creates DWL.</li>
            <li><strong>Marginal Cost Pricing ($P = MC$):</strong> Efficient output, but firm requires government subsidies (operates at a loss).</li>
            <li><strong>Average Cost Pricing ($P = ATC$):</strong> Zero economic profit, covers costs without subsidies.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("#### 🏛️ Structural Inefficiency Metrics")
    st.latex(r"P > MC \implies \text{Allocatively Inefficient} \quad \text{and} \quad P > \text{Minimum } ATC \implies \text{Productively Inefficient}")
    
    eff_c1, eff_c2 = st.columns(2)
    with eff_c1:
        st.markdown("""
        <div class="metric-card">
            <h3>❌ Allocative Inefficiency</h3>
            <div class="metric-value">P > MC</div>
            <p style="color: #94A3B8; font-size: 0.85rem;">Price exceeds the marginal cost of production, underallocating resources to the good and causing deadweight loss.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with eff_c2:
        st.markdown("""
        <div class="metric-card">
            <h3>❌ Productive Inefficiency</h3>
            <div class="metric-value">P > Minimum ATC</div>
            <p style="color: #94A3B8; font-size: 0.85rem;">Output is not produced at the absolute minimum point of the Average Total Cost curve, wasting productive capacity.</p>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 4: MONOPOLY PROFIT & PRICING POWER SIMULATOR ---
elif nav_selection == "🧮 Monopoly Profit & Pricing Power Simulator":
    st.markdown('<div class="section-header">🧮 Monopoly Profit & Pricing Power Simulator</div>', unsafe_allow_html=True)
    st.markdown("Simulate linear monopoly optimization using demand curve ($P = a - bQ$) and constant marginal cost assumptions.")
    
    sim_col1, sim_col2 = st.columns([1, 1.2])
    
    with sim_col1:
        intercept_a = st.number_input("Demand Price Intercept ($a$):", min_value=10.0, max_value=500.0, value=100.0, step=10.0)
        slope_b = st.number_input("Demand Slope Parameter ($b$):", min_value=0.1, max_value=10.0, value=0.5, step=0.1)
        fixed_cost = st.number_input("Total Fixed Cost ($TFC$):", min_value=0.0, max_value=5000.0, value=1000.0, step=100.0)
        marginal_cost = st.number_input("Constant Marginal Cost ($MC$):", min_value=1.0, max_value=200.0, value=20.0, step=5.0)
        
        # Linear Monopolist Calculations
        # Demand: P = a - b*Q
        # TR = a*Q - b*Q^2 -> MR = a - 2*b*Q
        # Profit Max: MR = MC -> a - 2*b*Q = MC -> Q_m = (a - MC) / (2*b)
        if intercept_a > marginal_cost:
            q_monopoly = (intercept_a - marginal_cost) / (2 * slope_b)
            p_monopoly = intercept_a - (slope_b * q_monopoly)
            
            # Competitive benchmark
            q_comp = (intercept_a - marginal_cost) / slope_b
            p_comp = marginal_cost
            
            total_revenue = p_monopoly * q_monopoly
            total_vc = marginal_cost * q_monopoly
            total_cost = fixed_cost + total_vc
            profit = total_revenue - total_cost
            
            # Deadweight Loss = 0.5 * (P_m - MC) * (Q_c - Q_m)
            dwl = 0.5 * (p_monopoly - marginal_cost) * (q_comp - q_monopoly)
            lerner_index = (p_monopoly - marginal_cost) / p_monopoly
            
            status = "👑 MONOPOLY OPTIMUM REACHED"
            reason = f"Restricting output to Q={q_monopoly:.1f} maximizes monopoly profit while charging P=${p_monopoly:.2f}."
            status_color = "#10B981"
        else:
            q_monopoly = 0.0
            p_monopoly = 0.0
            profit = -fixed_cost
            dwl = 0.0
            lerner_index = 0.0
            status = "🛑 SHUTDOWN / UNFEASIBLE"
            reason = "Marginal cost exceeds maximum willingness to pay (Intercept a)."
            status_color = "#EF4444"
            
    with sim_col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Decision State</h3>
            <div class="metric-value" style="color: {status_color}; font-size: 1.4rem;">{status}</div>
            <p style="color: #E2E8F0; font-size: 0.9rem; margin-top: 0.5rem;">{reason}</p>
        </div>
        """, unsafe_allow_html=True)
        
        metrics_df = pd.DataFrame([
            {"Monopoly Metric": "Optimal Output Quantity (Q_m)", "Value": f"{q_monopoly:,.2f} units"},
            {"Monopoly Metric": "Optimal Market Price (P_m)", "Value": f"${p_monopoly:,.2f}"},
            {"Monopoly Metric": "Competitive Benchmark Quantity (Q_c)", "Value": f"{q_comp:,.2f} units" if intercept_a > marginal_cost else "0.00"},
            {"Monopoly Metric": "Total Revenue (TR)", "Value": f"${total_revenue:,.2f}" if intercept_a > marginal_cost else "$0.00"},
            {"Monopoly Metric": "Total Cost (TC)", "Value": f"${total_cost:,.2f}" if intercept_a > marginal_cost else f"${fixed_cost:,.2f}"},
            {"Monopoly Metric": "Net Economic Profit", "Value": f"${profit:,.2f}"},
            {"Monopoly Metric": "Deadweight Loss (DWL)", "Value": f"${dwl:,.2f}"},
            {"Monopoly Metric": "Lerner Power Index (L)", "Value": f"{lerner_index:.3f}"}
        ])
        
        st.dataframe(metrics_df, use_container_width=True)

# --- SECTION 5: KNOWLEDGE CHECK DECK ---
elif nav_selection == "📝 Knowledge Check Deck":
    st.markdown('<div class="section-header">📝 Monopoly Structure Evaluation</div>', unsafe_allow_html=True)
    st.markdown("Test your economic knowledge of market power, revenue curves, deadweight loss, and price discrimination.")
    
    with st.form("competition_quiz"):
        st.markdown("### 1. Marginal Revenue of a Single-Price Monopolist")
        q1 = st.radio(
            "Why is marginal revenue (MR) strictly less than price (P) for a single-price monopolist?",
            options=[
                "A) Because marginal cost is always falling",
                "B) To sell an additional unit, the firm must lower price on all preceding units",
                "C) Monopolists are price takers bound by market equilibrium",
                "D) Demand is perfectly elastic in monopoly markets"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. Profit Maximization Rule")
        q2 = st.radio(
            "How does a monopolist determine its optimal price after finding MR = MC?",
            options=[
                "A) Charges a price equal to Marginal Cost (P = MC)",
                "B) Charges a price equal to Minimum Average Total Cost",
                "C) Projects the optimal quantity up to the Demand Curve",
                "D) Charges the highest possible price regardless of demand"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Economic Efficiency & Social Surplus")
        q3 = st.radio(
            "Compared to a perfectly competitive market, an unregulated single-price monopoly results in:",
            options=[
                "A) Higher output, lower price, and zero deadweight loss",
                "B) Lower output, higher price, and positive deadweight loss",
                "C) Maximum allocative efficiency where P = MC",
                "D) Total conversion of producer surplus into consumer surplus"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 4. Perfect (1st Degree) Price Discrimination")
        q4 = st.radio(
            "If a monopolist successfully engages in First-Degree (Perfect) Price Discrimination:",
            options=[
                "A) Deadweight loss increases to its maximum possible level",
                "B) Consumer surplus is zero, and output equals the competitive level (P = MC)",
                "C) Marginal revenue remains below price for all units",
                "D) Total profits are reduced to zero"
            ], index=None
        )
        
        eval_quiz = st.form_submit_button("Submit Evaluation", type="primary")
        
        if eval_quiz:
            score_acc = 0.0
            
            if q1 == "B) To sell an additional unit, the firm must lower price on all preceding units":
                score_acc += 25.0; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False
                
            if q2 == "C) Projects the optimal quantity up to the Demand Curve":
                score_acc += 25.0; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False
                
            if q3 == "B) Lower output, higher price, and positive deadweight loss":
                score_acc += 25.0; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False

            if q4 == "B) Consumer surplus is zero, and output equals the competitive level (P = MC)":
                score_acc += 25.0; st.session_state.ans4_ok = True
            else: st.session_state.ans4_ok = False
                
            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Score: {round(st.session_state.knowledge_rating, 1)} / 100 Points")
        
        if not st.session_state.ans1_ok:
            st.error("**Q1 Analysis:** Price must be cut on all previous units to increase sales volume under single pricing, making MR < P.")
        if not st.session_state.ans2_ok:
            st.error("**Q2 Analysis:** The monopolist uses MR = MC to determine optimal quantity Q*, then sets price using consumers' willingness to pay on the Demand curve.")
        if not st.session_state.ans3_ok:
            st.error("**Q3 Analysis:** Monopolies restrict supply and inflate price relative to competitive markets, creating allocative inefficiency and deadweight loss.")
        if not st.session_state.ans4_ok:
            st.error("**Q4 Analysis:** Perfect price discrimination eliminates consumer surplus and converts it to producer surplus while driving output up to the efficient level where MR = P = MC.")

# =====================================================================
# SYSTEM FOOTER DATA TERMINAL
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("🎓 Monopoly Market Dynamics Engine")

with foot_c2:
    st.caption("🚀 Microeconomics & Strategic Pricing Module")

with foot_c3:
    st.caption(f"⏰ System Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
