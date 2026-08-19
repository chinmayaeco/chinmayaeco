import streamlit as st
import pandas as pd
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Advanced Pricing & Price Discrimination Engine",
    page_icon="🏷️",
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
        st.markdown("<p style='text-align: center;'>Enter credential key to deploy the Pricing Strategy Engine.</p>", unsafe_allow_html=True)
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
    
    .stApp { background: linear-gradient(135deg, #0F172A 0%, #1E293B 40%, #0F172A 100%); }
    
    .score-banner {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid rgba(59, 130, 246, 0.3);
        color: #FFFFFF; padding: 1.5rem; border-radius: 12px; text-align: center; margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    }
    .score-banner h2 { color: #60A5FA !important; margin: 0 !important; font-weight: 700; font-size: 1.6rem; }
    
    .stContainer, .stForm {
        background: rgba(30, 41, 59, 0.7) !important; 
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px; padding: 1.75rem; margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25); backdrop-filter: blur(12px);
    }
    
    .section-header {
        color: #FBBF24; font-weight: 700; font-size: 1.4rem; margin-bottom: 1.25rem;
        padding-bottom: 0.75rem; border-bottom: 1px solid rgba(251, 191, 36, 0.2);
    }
    
    .concept-note, .case-study { padding: 1.25rem; border-radius: 8px; margin: 1.2rem 0; }
    .concept-note { background: rgba(59, 130, 246, 0.08); border-left: 4px solid #3B82F6; }
    .concept-note h3 { color: #60A5FA; margin-top: 0 !important; font-size: 1.2rem; }
    .case-study { background: rgba(217, 119, 6, 0.08); border-left: 4px solid #D97706; }
    .case-study h4 { color: #F59E0B; margin-top: 0 !important; font-size: 1.2rem; }
    
    .metric-card {
        background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 1.25rem; border-radius: 8px; text-align: center;
    }
    .metric-card h3 { color: #94A3B8; font-size: 1.05rem; margin: 0 0 0.5rem 0; }
    .metric-value { color: #FBBF24; font-size: 1.8rem; font-weight: 700; margin: 0.25rem 0; }
    
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important; color: white !important;
        border: none !important; padding: 0.65rem 1.75rem !important; border-radius: 6px !important;
        font-weight: 600 !important; transition: all 0.2s ease !important;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover { 
        transform: translateY(-1px) !important; 
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4) !important; 
    }
    
    .stMarkdown, p, li { color: #E2E8F0 !important; font-size: 0.98rem; line-height: 1.6; }
    .stSidebar { background: #0F172A !important; border-right: 1px solid rgba(255, 255, 255, 0.05); }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SESSION STATE MANAGEMENT
# =====================================================================
def init_system_state():
    defaults = {
        'knowledge_rating': 0.0,
        'quiz_done': False,
        'ans1_ok': False, 'ans2_ok': False, 'ans3_ok': False, 'ans4_ok': False, 'ans5_ok': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_system_state()

# =====================================================================
# SIDEBAR CONTROL DECK
# =====================================================================
with st.sidebar:
    st.markdown("### 👑 Pricing Architecture")
    nav_selection = st.radio(
        "Navigation Hub:",
        options=[
            "📌 Prerequisites for Price Discrimination",
            "🎯 1st, 2nd & 3rd Degree Discrimination",
            "⏳ Intertemporal vs. Peak-Load Pricing",
            "🧮 Multi-Market Pricing Strategy Simulator",
            "📝 Pricing Strategy Knowledge Deck"
        ]
    )

# =====================================================================
# LIVE SCORE TRACKING ENGINE
# =====================================================================
score_container = st.container()
with score_container:
    st.markdown(f"""
    <div class="score-banner">
        <h2>Pricing Power Mastery Index: {round(st.session_state.knowledge_rating, 1)} / 100</h2>
        <p style='color: #FBBF24; margin: 0.25rem 0 0 0;'>
            🏷️ Microeconomic Pricing Strategies & Revenue Extraction Engine
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE ROUTING ARCHITECTURE
# =====================================================================

# --- SECTION 1: PREREQUISITES ---
if nav_selection == "📌 Prerequisites for Price Discrimination":
    st.markdown('<div class="section-header">📌 Necessary Conditions for Price Discrimination</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>⚙️ Essential Market Conditions</h3>
    <p>Price discrimination occurs when a firm charges different prices for identical goods or services, where price differences do not reflect cost differences. To practice it successfully, three conditions must hold:</p>
    <ul>
        <li><strong>Market Power:</strong> The firm must be a price maker facing a downward-sloping demand curve ($P > MC$). Perfectly competitive price-takers cannot discriminate.</li>
        <li><strong>Market Identification / Segmentation:</strong> The firm must be able to identify differences in willingness to pay (WTP) or price elasticity of demand across consumer segments.</li>
        <li><strong>Prevention of Resale (Arbitrage Elimination):</strong> Consumers buying at a discounted rate must be unable to resell the good to consumers facing higher prices.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="case-study">
        <h4>🛡️ Arbitrage Friction Mechanisms</h4>
        <ul>
            <li><strong>Non-transferable Services:</strong> Medical services, haircuts, legal consultations.</li>
            <li><strong>Legal/Identity Verification:</strong> Student IDs, senior discounts, passport checks for airline tickets.</li>
            <li><strong>Transaction & Transportation Costs:</strong> Tariffs, regional geoblocking, regional hardware locking.</li>
            <li><strong>Contractual Restrictions:</strong> Enterprise software non-resale clauses.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #10B981;">
        <h4 style="color: #34D399;">📈 The Welfare Mechanism</h4>
        <p>Under uniform pricing, consumer surplus ($CS$) is uncaptured and output is restricted ($Q_m < Q_c$), causing deadweight loss ($DWL$).</p>
        <p>Through price discrimination, the firm aims to convert:</p>
        <ol>
            <li><strong>Consumer Surplus ($CS$) $\to$ Producer Profit ($\Pi$)</strong></li>
            <li><strong>Deadweight Loss ($DWL$) $\to$ Producer Profit ($\Pi$)</strong></li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 2: 1ST, 2ND & 3RD DEGREE ---
elif nav_selection == "🎯 1st, 2nd & 3rd Degree Discrimination":
    st.markdown('<div class="section-header">🎯 Classic Pigouvian Degrees of Price Discrimination</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "1st Degree (Perfect)",
        "2nd Degree (Self-Selection / Volume)",
        "3rd Degree (Market Segmentation)"
    ])
    
    with tab1:
        st.markdown(r"""
        <div class="concept-note">
        <h3>🥇 First-Degree (Perfect) Price Discrimination</h3>
        <p>The firm charges each individual consumer their exact <strong>maximum willingness to pay (reservation price)</strong>.</p>
        <ul>
            <li><strong>Demand equals Marginal Revenue:</strong> Since price is lowered only for the marginal unit without discounting prior units, $MR = P = D(Q)$.</li>
            <li><strong>Efficiency:</strong> Output expands until $P = MC$ ($Q_{1st} = Q_{comp}$). Total Social Welfare is maximized ($DWL = 0$).</li>
            <li><strong>Surplus Distribution:</strong> Consumer Surplus ($CS$) is completely reduced to $0$, fully absorbed into Producer Surplus ($PS$).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"MR(Q) = P(Q) \implies Q^* \text{ where } P(Q^*) = MC \quad (CS = 0, \, DWL = 0)")

    with tab2:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #8B5CF6;">
        <h3 style="color: #A78BFA;">🥈 Second-Degree Price Discrimination (Non-Linear Pricing)</h3>
        <p>The firm cannot directly observe individual valuations, so it designs pricing menus or volume tiers that induce consumers to <strong>self-select</strong> according to their preferences.</p>
        <ul>
            <li><strong>Block Pricing / Volume Discounts:</strong> Charging lower per-unit rates for higher quantities purchased (e.g., utility tiers, bulk wholesale).</li>
            <li><strong>Two-Part Tariffs:</strong> Charging a fixed entry fee ($T$) plus a per-unit usage fee ($P$). When consumers are identical: $P = MC$ and $T = CS$.</li>
            <li><strong>Version-Based Discrimination:</strong> Damaged-goods strategy, software feature gating (Basic vs. Pro), seat classes on trains.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"\text{Two-Part Tariff: } \text{Total Outlay } E(q) = T + P \cdot q")

    with tab3:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #F59E0B;">
        <h3 style="color: #FBBF24;">🥉 Third-Degree Price Discrimination (Market Segmentation)</h3>
        <p>The firm partitions buyers into distinct observable groups with different price elasticities of demand ($|E_1| \ne |E_2|$) and charges different uniform prices to each group.</p>
        <ul>
            <li><strong>Equimarginal Rule:</strong> The firm sets output across sub-markets such that marginal revenue is equalized across all groups and matches total marginal cost: $MR_1 = MR_2 = \dots = MC$.</li>
            <li><strong>Inverse Elasticity Pricing Rule:</strong> The sub-market with more inelastic demand is charged a higher price:</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"P_1 \left(1 - \frac{1}{|E_1|}\right) = P_2 \left(1 - \frac{1}{|E_2|}\right) = MC \implies \text{If } |E_1| < |E_2|, \text{ then } P_1 > P_2")

# --- SECTION 3: INTERTEMPORAL VS PEAK-LOAD ---
elif nav_selection == "⏳ Intertemporal vs. Peak-Load Pricing":
    st.markdown('<div class="section-header">⏳ Dynamic Pricing: Intertemporal vs. Peak-Load</div>', unsafe_allow_html=True)
    
    col_it, col_pl = st.columns(2)
    
    with col_it:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #3B82F6;">
        <h3>⏱️ Intertemporal Price Discrimination</h3>
        <p><strong>Core Concept:</strong> Charging different prices across distinct points in time to capture different consumer segments separated by their patience and valuation.</p>
        <ul>
            <li><strong>Phase 1 (High Price):</strong> Target high-valuation, low-patience early adopters (inelastic demand).</li>
            <li><strong>Phase 2 (Price Drops):</strong> Target price-sensitive, patient mass consumers (elastic demand).</li>
            <li><strong>Cost Structure:</strong> Production costs are constant or identical across time periods. Price changes purely due to demand segmentation.</li>
            <li><strong>Examples:</strong> Hardcover releases vs. paperbacks, flagship smartphone launches, movie theater theatrical runs vs. streaming release.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_pl:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #EF4444;">
        <h3 style="color: #F87171;">⚡ Peak-Load Pricing</h3>
        <p><strong>Core Concept:</strong> Charging different prices at different time intervals due to shifts in demand that run against fixed physical capacity constraints.</p>
        <ul>
            <li><strong>Capacity Limits:</strong> Because capacity is fixed in the short run, marginal costs ($MC$) sharply increase or become vertical during peak periods.</li>
            <li><strong>Cost-Driven:</strong> Unlike pure price discrimination, price differentials in peak-load pricing reflect <strong>actual differences in marginal costs</strong> ($MC_{peak} > MC_{off-peak}$).</li>
            <li><strong>Efficiency Criterion:</strong> $P_{peak} = MC_{peak}$ and $P_{off} = MC_{off}$, shifting non-urgent demand to off-peak periods and covering capacity capital costs.</li>
            <li><strong>Examples:</strong> Electricity grids during summer afternoons, toll lanes during rush hour, hotel rooms during holiday weekends.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("#### ⚖️ Structural Comparison")
    comp_df = pd.DataFrame([
        {"Dimension": "Primary Driver", "Intertemporal Pricing": "Differences in willingness to pay & patience", "Peak-Load Pricing": "Differences in marginal operating/capacity costs"},
        {"Dimension": "Marginal Cost Equality", "Intertemporal Pricing": "MC is identical across both time periods", "Peak-Load Pricing": "MC is significantly higher during peak periods"},
        {"Dimension": "Objective", "Intertemporal Pricing": "Maximize revenue via intertemporal consumer sorting", "Peak-Load Pricing": "Ration fixed capacity and balance operational load"},
        {"Dimension": "Classification", "Intertemporal Pricing": "Price discrimination (same cost, different prices)", "Peak-Load Pricing": "Cost-reflective pricing (different costs, different prices)"}
    ])
    st.dataframe(comp_df, use_container_width=True)

# --- SECTION 4: SIMULATOR ---
elif nav_selection == "🧮 Multi-Market Pricing Strategy Simulator":
    st.markdown('<div class="section-header">🧮 Third-Degree Price Discrimination Simulator</div>', unsafe_allow_html=True)
    st.markdown("Simulate pricing across two distinct market segments (e.g., Business vs. Leisure travelers) with constant marginal cost.")
    
    sim_col1, sim_col2 = st.columns([1, 1.2])
    
    with sim_col1:
        st.markdown("#### Market 1 (Inelastic Segment - e.g., Enterprise)")
        a1 = st.number_input("Market 1 Intercept ($a_1$):", min_value=20.0, max_value=500.0, value=120.0, step=10.0)
        b1 = st.number_input("Market 1 Slope ($b_1$):", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
        
        st.markdown("#### Market 2 (Elastic Segment - e.g., Students/Leisure)")
        a2 = st.number_input("Market 2 Intercept ($a_2$):", min_value=10.0, max_value=500.0, value=80.0, step=10.0)
        b2 = st.number_input("Market 2 Slope ($b_2$):", min_value=0.1, max_value=5.0, value=0.5, step=0.1)
        
        st.markdown("#### Production Cost Structure")
        mc = st.number_input("Constant Marginal Cost ($MC$):", min_value=1.0, max_value=100.0, value=20.0, step=5.0)
        
        # Calculations: 3rd Degree
        # Market 1: P1 = a1 - b1*Q1 -> MR1 = a1 - 2*b1*Q1 = MC -> Q1 = (a1 - MC)/(2*b1)
        q1 = max(0.0, (a1 - mc) / (2 * b1)) if a1 > mc else 0.0
        p1 = a1 - (b1 * q1) if q1 > 0 else 0.0
        tr1 = p1 * q1
        profit1 = tr1 - (mc * q1)
        
        # Market 2: P2 = a2 - b2*Q2 -> MR2 = a2 - 2*b2*Q2 = MC -> Q2 = (a2 - MC)/(2*b2)
        q2 = max(0.0, (a2 - mc) / (2 * b2)) if a2 > mc else 0.0
        p2 = a2 - (b2 * q2) if q2 > 0 else 0.0
        tr2 = p2 * q2
        profit2 = tr2 - (mc * q2)
        
        total_discrim_profit = profit1 + profit2
        total_discrim_q = q1 + q2

    with sim_col2:
        st.markdown("#### 📊 Optimal Segmented Equilibrium")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Market 1 (Inelastic)</h3>
                <div class="metric-value">${p1:,.2f}</div>
                <p style="color: #94A3B8; font-size: 0.85rem;">Volume: {q1:.1f} units<br>Segment Profit: ${profit1:,.2f}</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Market 2 (Elastic)</h3>
                <div class="metric-value">${p2:,.2f}</div>
                <p style="color: #94A3B8; font-size: 0.85rem;">Volume: {q2:.1f} units<br>Segment Profit: ${profit2:,.2f}</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("---")
        
        sim_summary = pd.DataFrame([
            {"Metric": "Market 1 Price ($P_1$)", "Discriminated": f"${p1:,.2f}"},
            {"Metric": "Market 2 Price ($P_2$)", "Discriminated": f"${p2:,.2f}"},
            {"Metric": "Market 1 Output ($Q_1$)", "Discriminated": f"{q1:,.2f}"},
            {"Metric": "Market 2 Output ($Q_2$)", "Discriminated": f"{q2:,.2f}"},
            {"Metric": "Total Combined Output", "Discriminated": f"{total_discrim_q:,.2f}"},
            {"Metric": "Total Economic Profit ($\Pi$)", "Discriminated": f"${total_discrim_profit:,.2f}"}
        ])
        st.dataframe(sim_summary, use_container_width=True)

# --- SECTION 5: QUIZ DECK ---
elif nav_selection == "📝 Pricing Strategy Knowledge Deck":
    st.markdown('<div class="section-header">📝 Pricing Strategy & Price Discrimination Evaluation</div>', unsafe_allow_html=True)
    st.markdown("Evaluate your understanding of degrees of price discrimination, intertemporal sorting, and peak-load mechanisms.")
    
    with st.form("pricing_quiz"):
        st.markdown("### 1. First-Degree (Perfect) Price Discrimination Welfare")
        q1 = st.radio(
            "Under perfect (1st degree) price discrimination, what happens to Deadweight Loss (DWL) and Consumer Surplus (CS)?",
            options=[
                "A) DWL is maximized, and CS is maximized",
                "B) DWL is zero, and CS is zero",
                "C) DWL is positive, and CS equals total profit",
                "D) DWL is zero, and CS is maximized"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. Second-Degree Price Discrimination")
        q2 = st.radio(
            "Which of the following is a classic example of second-degree price discrimination?",
            options=[
                "A) Charging students 20% less based on student ID presentation",
                "B) Offering tiered discounts for bulk quantity purchases (e.g., $10 for 1, $16 for 2)",
                "C) Charging higher rates for electricity during evening peak hours",
                "D) Bargaining 1-on-1 with every individual customer to extract reservation price"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Third-Degree Price Discrimination Rule")
        q3 = st.radio(
            "In 3rd degree price discrimination across two distinct markets, which market receives the higher price?",
            options=[
                "A) The market with higher price elasticity of demand (|E_d| is larger)",
                "B) The market with lower price elasticity of demand (|E_d| is smaller)",
                "C) The market with the lowest total willingness to pay",
                "D) Both markets are charged identical prices because MC is equal"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 4. Peak-Load Pricing vs. Intertemporal Pricing")
        q4 = st.radio(
            "Why is peak-load pricing NOT considered pure price discrimination in the strict microeconomic sense?",
            options=[
                "A) Because consumer surplus is completely eliminated during off-peak times",
                "B) Because the firm does not possess market power during off-peak periods",
                "C) Because the price differences reflect variations in marginal costs due to capacity constraints",
                "D) Because arbitrage is physically impossible between day and night"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 5. Two-Part Tariffs")
        q5 = st.radio(
            "For a monopoly facing identical consumers, how should it set a two-part tariff (Entry fee T, Usage fee P) to maximize profit?",
            options=[
                "A) Set P = Monopoly Price and T = 0",
                "B) Set P = MC and set T equal to the entire Consumer Surplus generated at that price",
                "C) Set P = 0 and T = Minimum Average Total Cost",
                "D) Set P above MC and T equal to Deadweight Loss"
            ], index=None
        )
        
        eval_quiz = st.form_submit_button("Submit Pricing Strategy Evaluation", type="primary")
        
        if eval_quiz:
            score_acc = 0.0
            
            if q1 == "B) DWL is zero, and CS is zero":
                score_acc += 20.0; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False
                
            if q2 == "B) Offering tiered discounts for bulk quantity purchases (e.g., $10 for 1, $16 for 2)":
                score_acc += 20.0; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False
                
            if q3 == "B) The market with lower price elasticity of demand (|E_d| is smaller)":
                score_acc += 20.0; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False

            if q4 == "C) Because the price differences reflect variations in marginal costs due to capacity constraints":
                score_acc += 20.0; st.session_state.ans4_ok = True
            else: st.session_state.ans4_ok = False

            if q5 == "B) Set P = MC and set T equal to the entire Consumer Surplus generated at that price":
                score_acc += 20.0; st.session_state.ans5_ok = True
            else: st.session_state.ans5_ok = False
                
            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Score: {round(st.session_state.knowledge_rating, 1)} / 100 Points")
        
        if not st.session_state.ans1_ok:
            st.error("**Q1 Analysis:** 1st-degree price discrimination extracts all consumer surplus ($CS=0$) while producing output up to $P=MC$, eliminating deadweight loss ($DWL=0$).")
        if not st.session_state.ans2_ok:
            st.error("**Q2 Analysis:** 2nd-degree price discrimination relies on self-selection menus, such as quantity block discounts or two-part tariffs.")
        if not st.session_state.ans3_ok:
            st.error("**Q3 Analysis:** Under 3rd-degree discrimination, the pricing markup rule $P(1 - 1/|E|) = MC$ dictates that less price-sensitive (more inelastic) consumers face higher prices.")
        if not st.session_state.ans4_ok:
            st.error("**Q4 Analysis:** Price discrimination requires charging different prices not justified by costs. Peak-load pricing reflects higher marginal costs of serving capacity at peak times.")
        if not st.session_state.ans5_ok:
            st.error("**Q5 Analysis:** With identical consumers, setting per-unit price $P=MC$ maximizes social surplus, which is then fully extracted via fixed entry fee $T=CS$.")

# =====================================================================
# SYSTEM FOOTER
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("🎓 Advanced Pricing Dynamics Engine")

with foot_c2:
    st.caption("🚀 Price Discrimination & Peak-Load Frameworks")

with foot_c3:
    st.caption(f"⏰ System Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
