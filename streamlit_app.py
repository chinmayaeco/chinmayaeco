import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Oligopoly Markets & Kinked Demand Engine",
    page_icon="♟️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# SECURE ACCESS SYSTEM
# =====================================================================
def check_password():
    """Returns `True` if the user enters the correct security key."""
    def password_entered():
        if st.session_state["password"] == "OLIGO2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Operations Engine Security</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Enter credential key to deploy the Oligopoly Strategy Engine.</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.text_input("Security Password (Use 'OLIGO2026')", type="password", on_change=password_entered, key="password")
        return False
    
    elif not st.session_state["password_correct"]:
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Operations Engine Security</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.text_input("Security Password (Use 'OLIGO2026')", type="password", on_change=password_entered, key="password")
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
    st.markdown("### ♟️ Market Structure Deck")
    nav_selection = st.radio(
        "Navigation Hub:",
        options=[
            "📌 Oligopoly Foundations & Characteristics",
            "📉 Sweezy Kinked Demand Curve Model",
            "⚔️ Non-Collusive Duopoly: Cournot vs. Bertrand vs. Stackelberg",
            "🤝 Collusion, Cartels & Game Theory (Prisoner's Dilemma)",
            "🧮 Kinked Demand & Price Rigidity Simulator",
            "📝 Oligopoly Mastery Knowledge Deck"
        ]
    )

# =====================================================================
# LIVE SCORE TRACKING ENGINE
# =====================================================================
score_container = st.container()
with score_container:
    st.markdown(f"""
    <div class="score-banner">
        <h2>Oligopoly & Strategic Pricing Mastery Index: {round(st.session_state.knowledge_rating, 1)} / 100</h2>
        <p style='color: #FBBF24; margin: 0.25rem 0 0 0;'>
            ♟️ Strategic Interdependence, Sweezy Price Rigidity & Game Theoretic Equilibria
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE ROUTING ARCHITECTURE
# =====================================================================

# --- SECTION 1: FOUNDATIONS ---
if nav_selection == "📌 Oligopoly Foundations & Characteristics":
    st.markdown('<div class="section-header">📌 Fundamentals of Oligopolistic Markets</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>⚙️ Defining Characteristics of an Oligopoly</h3>
    <p>An oligopoly is an imperfect market structure dominated by a small number of large, strategically interdependent firms. Key structural attributes include:</p>
    <ul>
        <li><strong>Few Dominant Sellers:</strong> A small group of firms accounts for the vast majority of industry output ($CR_4 > 60\%$ or high $HHI$).</li>
        <li><strong>Mutual Interdependence:</strong> No single firm can set price or output in isolation. Every strategic action triggers a counter-response from rivals.</li>
        <li><strong>High Barriers to Entry:</strong> Substantial capital requirements, economies of scale, patents, and predatory strategies prevent rapid competitor ingress.</li>
        <li><strong>Product Nature:</strong> Can be homogeneous (pure oligopoly: steel, cement, crude oil) or differentiated (differentiated oligopoly: commercial aircraft, smartphones, automobiles).</li>
        <li><strong>Non-Price Competition:</strong> Heavy reliance on branding, product differentiation, warranties, and advertising to avoid destructive price wars.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(r"""
        <div class="case-study">
        <h4>📊 Concentration Metrics</h4>
        <p>Economists measure oligopolistic concentration using two primary tools:</p>
        <ul>
            <li><strong>Four-Firm Concentration Ratio ($CR_4$):</strong>
                $$CR_4 = \sum_{i=1}^{4} S_i$$
                where $S_i$ is the market share of the $i$-th largest firm. A ratio exceeding $60\%$ generally denotes an oligopoly.
            </li>
            <li><strong>Herfindahl-Hirschman Index ($HHI$):</strong>
                $$HHI = \sum_{i=1}^{n} (S_i)^2$$
                An $HHI > 1{,}800$ indicates a highly concentrated market under US DOJ/FTC horizontal merger guidelines.
            </li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #10B981;">
        <h4 style="color: #34D399;">🎯 Strategic Dilemma: Collude vs. Compete</h4>
        <p>Firms in an oligopoly face two opposing forces:</p>
        <ol>
            <li><strong>Cooperation Incentive (Joint Profit Maximization):</strong> Agreeing to act as a shared monopoly to restrict output and elevate prices ($P \to P_{mono}$).</li>
            <li><strong>Cheating Incentive (Individual Gain):</strong> Secretly undercutting the agreed price or overproducing to capture market share from rivals.</li>
        </ol>
        <p>This structural tension often leads to <em>price rigidity</em> or sudden, aggressive <em>price wars</em>.</p>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 2: KINKED DEMAND CURVE ---
elif nav_selection == "📉 Sweezy Kinked Demand Curve Model":
    st.markdown('<div class="section-header">📉 Sweezy Kinked Demand Curve & Price Rigidity</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="concept-note">
    <h3>🔍 The Sweezy Asymmetric Reaction Hypothesis (Paul Sweezy, 1939)</h3>
    <p>The Kinked Demand Curve model explains why prices in oligopolistic markets remain <strong>rigid (sticky)</strong> over time, even when underlying input costs ($MC$) fluctuate.</p>
    <p>The model rests on an asymmetrical behavioral assumption regarding how rivals react to price alterations from an established prevailing price $P^*$:</p>
    <ul>
        <li><strong>If a firm RAISES its price ($P > P^*$):</strong> Rivals will <em>ignore</em> the price hike to capture the firm's defecting customers. Consequently, demand is <strong>highly elastic (flat)</strong> above the kink ($|E_d| > 1$). A price increase leads to a sharp loss in total revenue.</li>
        <li><strong>If a firm LOWERS its price ($P < P^*$):</strong> Rivals will <em>immediately match</em> the price cut to prevent losing their market share. Consequently, demand is <strong>highly inelastic (steep)</strong> below the kink ($|E_d| < 1$). A price cut triggers a price war with negligible quantity gains, decreasing total revenue.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(r"""
        <div class="case-study">
        <h4>⚡ Marginal Revenue Discontinuity (The Vertical Gap)</h4>
        <p>Because the demand curve changes slope abruptly at the established output $Q^*$, the associated Marginal Revenue ($MR$) curve consists of two separate segments with a <strong>vertical discontinuity gap</strong> at $Q^*$:</p>
        <ul>
            <li><strong>Upper $MR$ ($MR_{elastic}$):</strong> Shallow downward slope corresponding to the elastic segment.</li>
            <li><strong>Lower $MR$ ($MR_{inelastic}$):</strong> Steep downward slope corresponding to the inelastic segment.</li>
            <li><strong>The Gap ($AB$):</strong> A vertical jump directly below the kink at $Q^*$.</li>
        </ul>
        <p>As long as the firm's Marginal Cost ($MC$) curve shifts within this vertical gap ($MC_1$ to $MC_2$), the profit-maximizing condition $MR = MC$ continues to intersect the vertical segment at exactly the same output $Q^*$ and price $P^*$.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #EF4444;">
        <h4 style="color: #F87171;">⚠️ Limitations of the Sweezy Model</h4>
        <p>While the Kinked Demand Curve model provides intuition for price rigidity, it faces major microeconomic critiques:</p>
        <ol>
            <li><strong>Exogenous Kink:</strong> It explains why prices remain <em>rigid</em> once established, but fails to explain how the prevailing price-quantity coordinate $(P^*, Q^*)$ was determined in the first place.</li>
            <li><strong>Empirical Mixed Evidence:</strong> George Stigler's empirical tests showed that oligopolists frequently match price increases during inflationary periods and do not always follow asymmetric patterns.</li>
            <li><strong>Ignored Collusion:</strong> It does not capture dynamic game-theoretic repeated interactions or tacit collusion mechanisms.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 3: CLASSIC DUOPOLY MODELS ---
elif nav_selection == "⚔️ Non-Collusive Duopoly: Cournot vs. Bertrand vs. Stackelberg":
    st.markdown('<div class="section-header">⚔️ Classic Non-Collusive Duopoly Models</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "Cournot (Simultaneous Quantity)",
        "Bertrand (Simultaneous Price)",
        "Stackelberg (Sequential Quantity)"
    ])
    
    with tab1:
        st.markdown(r"""
        <div class="concept-note">
        <h3>📦 Cournot Duopoly Model (Antoine Augustin Cournot, 1838)</h3>
        <p>Firms choose their <strong>output quantities simultaneously</strong>, treating the competitor's output as fixed.</p>
        <ul>
            <li><strong>Decision Variable:</strong> Output quantities $q_1, q_2$. Market clearing price is determined by aggregate output: $P = P(Q) = P(q_1 + q_2)$.</li>
            <li><strong>Best-Response Functions:</strong> Firm 1 derives reaction curve $q_1^*(q_2)$ by maximizing $\pi_1 = P(q_1 + q_2)q_1 - C_1(q_1)$.</li>
            <li><strong>Equilibrium:</strong> Intersection of reaction curves yields the Cournot-Nash Equilibrium.</li>
            <li><strong>Welfare Hierarchy:</strong> $P_{Monopoly} > P_{Cournot} > P_{PerfectComp}$ and $Q_{Monopoly} < Q_{Cournot} < Q_{PerfectComp}$.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"\text{Linear Case } P = a - b(q_1+q_2), \, MC=c \implies q_1^* = q_2^* = \frac{a - c}{3b}, \quad P^* = \frac{a + 2c}{3}")

    with tab2:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #8B5CF6;">
        <h3 style="color: #A78BFA;">🏷️ Bertrand Duopoly Model (Joseph Bertrand, 1883)</h3>
        <p>Firms produce homogeneous goods and compete by choosing <strong>prices simultaneously</strong>.</p>
        <ul>
            <li><strong>Strategic Incentive:</strong> Since goods are identical, consumers purchase entirely from the lower-priced firm. If $P_1 < P_2$, Firm 1 captures 100% of the market.</li>
            <li><strong>The Bertrand Paradox:</strong> Both firms engage in iterative price undercutting until neither can undercut further without making economic losses.</li>
            <li><strong>Nash Equilibrium:</strong> $P_1^* = P_2^* = MC$. Even with only <strong>two firms</strong>, the market achieves the perfectly competitive outcome ($\Pi_1 = \Pi_2 = 0$).</li>
            <li><strong>Resolutions to the Paradox:</strong> Capacity constraints (Edgeworth model), product differentiation, or repeated interaction tacit collusion.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"P_1^* = P_2^* = MC \implies Q^* = Q_{comp}, \quad \text{Economic Profit } \Pi = 0")

    with tab3:
        st.markdown(r"""
        <div class="concept-note" style="border-left-color: #F59E0B;">
        <h3 style="color: #FBBF24;">👑 Stackelberg Leadership Model (Heinrich von Stackelberg, 1934)</h3>
        <p>A sequential game where a <strong>dominant Leader firm (Firm 1)</strong> sets its output first, and the <strong>Follower firm (Firm 2)</strong> observes and responds.</p>
        <ul>
            <li><strong>Backward Induction:</strong> The Leader anticipates the Follower's reaction function $q_2^*(q_1)$ and substitutes it directly into its own profit function before setting $q_1$.</li>
            <li><strong>First-Mover Advantage:</strong> The Leader produces a larger output and earns higher profits than in the Cournot equilibrium by committing to high capacity early.</li>
            <li><strong>Follower's Outcome:</strong> The Follower is forced to produce a smaller quantity and earns strictly lower profits than under Cournot.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"q_{Leader}^* = \frac{a - c}{2b}, \quad q_{Follower}^* = \frac{a - c}{4b}, \quad Q_{Stackelberg} = \frac{3(a-c)}{4b}")

# --- SECTION 4: COLLUSION & GAME THEORY ---
elif nav_selection == "🤝 Collusion, Cartels & Game Theory (Prisoner's Dilemma)":
    st.markdown('<div class="section-header">🤝 Collusive Oligopoly & Strategic Game Theory</div>', unsafe_allow_html=True)
    
    col_gt1, col_gt2 = st.columns(2)
    
    with col_gt1:
        st.markdown(r"""
        <div class="concept-note">
        <h3>🏛️ Cartels & Explicit Collusion</h3>
        <p>A <strong>Cartel</strong> is a formal organization of producers that coordinate output quotas and price agreements to act as a shared multi-plant monopoly.</p>
        <ul>
            <li><strong>Joint Profit Maximization:</strong> Sets total industry output $Q$ such that $\sum MR(Q) = MC_i$ for all member firms.</li>
            <li><strong>Inherent Instability:</strong> For any individual firm $i$, price exceeds its marginal cost ($P > MC_i$). Thus, each member faces a continuous unilateral incentive to cheat by expanding quota:
            $$\frac{\partial \pi_i}{\partial q_i} > 0 \quad \text{at the cartel agreement}$$</li>
            <li><strong>Enforcement Enablers:</strong> Cartels survive when there are few firms, high market transparency, low cost variance, and credible punishment strategies (e.g., Grim Trigger, Tit-for-Tat).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_gt2:
        st.markdown(r"""
        <div class="case-study">
        <h4>🎮 Duopoly as a Prisoner's Dilemma</h4>
        <p>Consider two symmetrical duopolists deciding whether to Collude (High Price) or Cheat (Low Price):</p>
        </div>
        """, unsafe_allow_html=True)
        
        payoff_matrix = pd.DataFrame({
            "Firm 2: Collude (High Price)": ["Firm 1: $50M, Firm 2: $50M (Joint Max)", "Firm 1: $70M, Firm 2: $10M (Firm 1 Cheats)"],
            "Firm 2: Cheat (Low Price)": ["Firm 1: $10M, Firm 2: $70M (Firm 2 Cheats)", "Firm 1: $25M, Firm 2: $25M (Nash Equilibrium)"]
        }, index=["Firm 1: Collude (High Price)", "Firm 1: Cheat (Low Price)"])
        
        st.dataframe(payoff_matrix, use_container_width=True)
        st.markdown(r"""
        <p style='font-size: 0.9rem; color: #CBD5E1;'>
        • <strong>Dominant Strategy:</strong> "Cheat (Low Price)" is the strictly dominant strategy for both firms.<br>
        • <strong>Nash Equilibrium:</strong> Both cheat ($25M, $25M), yielding an outcome strictly inferior to mutual cooperation ($50M, $50M).
        </p>
        """, unsafe_allow_html=True)

# --- SECTION 5: KINKED DEMAND SIMULATOR ---
elif nav_selection == "🧮 Kinked Demand & Price Rigidity Simulator":
    st.markdown('<div class="section-header">🧮 Sweezy Kinked Demand & Discontinuous MR Simulator</div>', unsafe_allow_html=True)
    st.markdown("Interact with the parameters of the Sweezy model to observe how the **Marginal Revenue discontinuity gap** creates **price rigidity** despite shifting marginal costs ($MC$).")
    
    sim_col1, sim_col2 = st.columns([1, 1.3])
    
    with sim_col1:
        st.markdown("#### Kink Coordinates (Current Market Equilibrium)")
        p_kink = st.slider("Established Rigid Price ($P^*$):", min_value=50.0, max_value=200.0, value=100.0, step=5.0)
        q_kink = st.slider("Established Output ($Q^*$):", min_value=20.0, max_value=100.0, value=50.0, step=5.0)
        
        st.markdown("#### Segment Elasticities (Slopes)")
        b_upper = st.slider("Upper Segment Slope $b_1$ (Elastic - Flat):", min_value=0.2, max_value=1.5, value=0.5, step=0.1)
        b_lower = st.slider("Lower Segment Slope $b_2$ (Inelastic - Steep):", min_value=1.6, max_value=5.0, value=2.5, step=0.1)
        
        st.markdown("#### Firm Cost Dynamics")
        mc_val = st.slider("Current Marginal Cost ($MC$):", min_value=10.0, max_value=120.0, value=45.0, step=2.0)
        
        # Upper Demand: P = a1 - b_upper * Q  => passing through (q_kink, p_kink) => a1 = p_kink + b_upper * q_kink
        a1 = p_kink + (b_upper * q_kink)
        # Lower Demand: P = a2 - b_lower * Q  => passing through (q_kink, p_kink) => a2 = p_kink + b_lower * q_kink
        a2 = p_kink + (b_lower * q_kink)
        
        # MR Upper at Q*: MR1 = a1 - 2*b_upper*Q* = p_kink + b_upper*q_kink - 2*b_upper*q_kink = p_kink - b_upper*q_kink
        mr_top = p_kink - (b_upper * q_kink)
        # MR Lower at Q*: MR2 = a2 - 2*b_lower*Q* = p_kink + b_lower*q_kink - 2*b_lower*q_kink = p_kink - b_lower*q_kink
        mr_bottom = p_kink - (b_lower * q_kink)
        
        # Check if MC is inside the gap
        inside_gap = mr_bottom <= mc_val <= mr_top

    with sim_col2:
        st.markdown("#### 📊 Marginal Revenue Gap & Rigidity State")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Upper MR Bound ($MR_{{top}}$)</h3>
                <div class="metric-value">${mr_top:,.2f}</div>
                <p style="color: #94A3B8; font-size: 0.85rem;">Limit of elastic demand revenue</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Lower MR Bound ($MR_{{bottom}}$)</h3>
                <div class="metric-value">${mr_bottom:,.2f}</div>
                <p style="color: #94A3B8; font-size: 0.85rem;">Limit of inelastic demand revenue</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        if inside_gap:
            st.success(f"✅ **Price Rigidity Holds:** Marginal Cost ($MC = \${mc_val:,.2f}$) intersects within the vertical gap $[\\${mr_bottom:,.2f}, \\${mr_top:,.2f}]$. The optimal price remains **\\${p_kink:,.2f}** and output remains **{q_kink:.1f} units**.")
        elif mc_val > mr_top:
            st.warning(f"⚠️ **MC Exceeds MR Gap:** Marginal Cost ($MC = \${mc_val:,.2f}$) is above $\\${mr_top:,.2f}$. The firm must contract output ($Q < {q_kink:.1f}$) and raise price along the elastic curve.")
        else:
            st.info(f"ℹ️ **MC Below MR Gap:** Marginal Cost ($MC = \${mc_val:,.2f}$) is below $\\${mr_bottom:,.2f}$. The firm has incentive to expand output ($Q > {q_kink:.1f}$) into the inelastic segment.")
        
        # Generate chart data for visual inspection
        q_range = np.linspace(5, q_kink * 2, 80)
        p_demand = []
        mr_curve = []
        
        for q in q_range:
            if q <= q_kink:
                p_demand.append(a1 - b_upper * q)
                mr_curve.append(a1 - 2 * b_upper * q)
            else:
                p_demand.append(a2 - b_lower * q)
                mr_curve.append(a2 - 2 * b_lower * q)
                
        plot_df = pd.DataFrame({
            "Quantity": q_range,
            "Demand Curve (P)": [max(0, p) for p in p_demand],
            "Marginal Revenue (MR)": mr_curve,
            "Marginal Cost (MC)": [mc_val] * len(q_range)
        }).set_index("Quantity")
        
        st.line_chart(plot_df)
        
        sim_summary = pd.DataFrame([
            {"Parameter / Metric": "Equilibrium Price ($P^*$)", "Value": f"${p_kink:,.2f}"},
            {"Parameter / Metric": "Equilibrium Quantity ($Q^*$)", "Value": f"{q_kink:,.2f} units"},
            {"Parameter / Metric": "Vertical Discontinuity Gap Span", "Value": f"${(mr_top - mr_bottom):,.2f}"},
            {"Parameter / Metric": "Current Marginal Cost ($MC$)", "Value": f"${mc_val:,.2f}"},
            {"Parameter / Metric": "Equilibrium Condition Met?", "Value": "Rigid at Kink" if inside_gap else "Break from Kink"}
        ])
        st.dataframe(sim_summary, use_container_width=True)

# --- SECTION 6: QUIZ DECK ---
elif nav_selection == "📝 Oligopoly Mastery Knowledge Deck":
    st.markdown('<div class="section-header">📝 Oligopoly & Strategic Pricing Evaluation</div>', unsafe_allow_html=True)
    st.markdown("Test your command over oligopolistic market structures, the Sweezy kinked demand model, and non-collusive game-theoretic duopolies.")
    
    with st.form("oligopoly_quiz"):
        st.markdown("### 1. The Sweezy Kinked Demand Asymmetry")
        q1 = st.radio(
            "In the Sweezy Kinked Demand Curve model, what is the behavioral assumption regarding rival firms' reactions?",
            options=[
                "A) Rivals match both price increases and price decreases equally.",
                "B) Rivals ignore price increases, but match price decreases.",
                "C) Rivals match price increases, but ignore price decreases.",
                "D) Rivals merge to form a monopoly whenever price changes."
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. Discontinuous Marginal Revenue & Price Rigidity")
        q2 = st.radio(
            "Why does the market price remain rigid in the Sweezy model even if input costs (MC) fluctuate?",
            options=[
                "A) Because government price controls prohibit oligopolists from altering price.",
                "B) Because the MC curve passes through the vertical discontinuity gap in the MR curve.",
                "C) Because the firm's Average Total Cost is perfectly horizontal at all outputs.",
                "D) Because consumers sign long-term fixed-price contracts."
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Cournot vs. Bertrand Duopoly Paradox")
        q3 = st.radio(
            "Under the Bertrand duopoly model with homogeneous goods and identical constant MC, what is the resulting equilibrium price?",
            options=[
                "A) The monopoly price, maximizing joint profits.",
                "B) Equal to Marginal Cost (P = MC), yielding zero economic profit.",
                "C) Halfway between the Cournot price and the Monopoly price.",
                "D) Undefined, because no equilibrium exists."
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 4. Stackelberg First-Mover Advantage")
        q4 = st.radio(
            "In a Stackelberg sequential quantity game, why does the Leader achieve higher profit than in Cournot equilibrium?",
            options=[
                "A) The Leader commits to a larger output first, forcing the Follower to contract along its reaction curve.",
                "B) The Leader possesses lower production technology costs than the Follower.",
                "C) The Follower is legally barred from competing in the same geographic territory.",
                "D) The Leader sets the price while the Follower sets the quantity."
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 5. Cartel Instability & Game Theory")
        q5 = st.radio(
            "Why do explicit cartels (like OPEC) frequently experience cheating among member nations?",
            options=[
                "A) Because cartels are only profitable when all firms cheat simultaneously.",
                "B) Because at the agreed collusive output, the market price exceeds each individual firm's marginal cost (P > MC), creating an incentive to secretly expand quota.",
                "C) Because cartels eliminate barriers to entry automatically.",
                "D) Because consumer demand becomes perfectly elastic under collusive agreements."
            ], index=None
        )
        
        eval_quiz = st.form_submit_button("Submit Oligopoly Strategy Evaluation", type="primary")
        
        if eval_quiz:
            score_acc = 0.0
            
            if q1 == "B) Rivals ignore price increases, but match price decreases.":
                score_acc += 20.0; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False
                
            if q2 == "B) Because the MC curve passes through the vertical discontinuity gap in the MR curve.":
                score_acc += 20.0; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False
                
            if q3 == "B) Equal to Marginal Cost (P = MC), yielding zero economic profit.":
                score_acc += 20.0; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False

            if q4 == "A) The Leader commits to a larger output first, forcing the Follower to contract along its reaction curve.":
                score_acc += 20.0; st.session_state.ans4_ok = True
            else: st.session_state.ans4_ok = False

            if q5 == "B) Because at the agreed collusive output, the market price exceeds each individual firm's marginal cost (P > MC), creating an incentive to secretly expand quota.":
                score_acc += 20.0; st.session_state.ans5_ok = True
            else: st.session_state.ans5_ok = False
                
            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Score: {round(st.session_state.knowledge_rating, 1)} / 100 Points")
        
        if not st.session_state.ans1_ok:
            st.error("**Q1 Analysis:** The Sweezy model assumes asymmetric expectations: raising price loses substantial market share (elastic), while lowering price triggers immediate matching price wars (inelastic).")
        if not st.session_state.ans2_ok:
            st.error("**Q2 Analysis:** Because the slope changes sharply at the kink, the MR curve drops vertically. Any MC shifts within this vertical gap satisfy $MR = MC$ at the unchanged price $P^*$ and output $Q^*$.")
        if not st.session_state.ans3_ok:
            st.error("**Q3 Analysis:** The Bertrand Paradox demonstrates that with homogeneous products and price competition, firms undercut each other until $P = MC$, yielding competitive zero economic profit.")
        if not st.session_state.ans4_ok:
            st.error("**Q4 Analysis:** The Stackelberg Leader exploits first-mover commitment, choosing a large output knowing the Follower will optimally reduce output along its downward-sloping reaction function.")
        if not st.session_state.ans5_ok:
            st.error("**Q5 Analysis:** At the collusive output, $P > MC$, meaning producing an additional unit adds more to revenue than cost. Each firm faces a Prisoner's Dilemma incentive to defect and overproduce.")

# =====================================================================
# SYSTEM FOOTER
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("♟️ Oligopoly & Strategic Game Theory Engine")

with foot_c2:
    st.caption("📉 Sweezy Kinked Demand & Duopoly Equilibria")

with foot_c3:
    st.caption(f"⏰ System Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
