from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="FX Dynamics & International Trade Economics",
    page_icon="💱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# High-Contrast Dark Slate, Emerald, and Amber Theme
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at 10% 20%, #061e1f 0%, #07171d 50%, #030a10 100%);
        color: #F8FAFC !important;
    }

    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #F8FAFC !important;
    }
    
    .stMarkdown, .stText, [data-testid="stWidgetLabel"] p {
        color: #F1F5F9 !important;
        font-weight: 500 !important;
    }
    
    .stCaption, [data-testid="stCaptionContainer"] p {
        color: #94A3B8 !important;
        font-size: 0.88rem !important;
    }

    .score-banner {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(14, 165, 233, 0.2) 100%);
        border: 1px solid rgba(16, 185, 129, 0.45);
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
    }
    
    .metric-panel {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(16, 185, 129, 0.35);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }
    
    .metric-title {
        color: #94A3B8 !important;
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .metric-val {
        color: #34D399 !important;
        font-size: 1.6rem;
        font-weight: 800;
        margin-top: 0.3rem;
    }
    
    .concept-card {
        background: rgba(15, 23, 42, 0.65);
        border-left: 4px solid #34D399;
        border-radius: 0 8px 8px 0;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    div[data-testid="stRadio"] > div {
        background-color: rgba(15, 23, 42, 0.6);
        padding: 0.8rem;
        border-radius: 8px;
        border: 1px solid rgba(148, 163, 184, 0.25);
    }

    div[data-testid="stRadio"] label span {
        color: #F8FAFC !important;
    }
    
    .stSlider [data-baseweb="slider"] {
        color: #34D399 !important;
    }

    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid #34D399 !important;
        padding: 0.6rem 1.6rem !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease-in-out;
    }

    .stButton > button:hover, .stFormSubmitButton > button:hover {
        background: linear-gradient(135deg, #047857 0%, #065F46 100%) !important;
        border-color: #6EE7B7 !important;
        color: #FFFFFF !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# SESSION STATE ENGINE
# =====================================================================
if "lab_points" not in st.session_state:
    st.session_state.lab_points = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "eval_records" not in st.session_state:
    st.session_state.eval_records = {}

total_final_score = st.session_state.lab_points + st.session_state.quiz_score

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("## 💱 FX & Trade Macro Lab")
    module = st.radio(
        "Select Learning Module:",
        [
            "🌐 Module 1: FX Fluctuations, Elasticity & J-Curve Simulation",
            "📝 Module 2: FX Theory & Trade Elasticity Assessment",
        ],
    )
    st.markdown("---")
    st.markdown("### 🏆 Performance Tracker")
    st.markdown(f"**Interactive Simulation:** {st.session_state.lab_points} / 50")
    st.markdown(f"**Macro Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Aggregate Score:** {total_final_score} / 100")

    if total_final_score == 100:
        st.success("🌟 Certified International Macro & FX Trade Strategist!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(
    f"""
<div class="score-banner">
    <h2 style="color: #34D399; margin: 0; font-weight: 800;">International FX & Trade Suite: {total_final_score} / 100</h2>
    <p style="color: #E2E8F0; margin: 0.35rem 0 0 0; font-size: 1rem;">
        Simulation Lab: <b>{st.session_state.lab_points}/50 Pts</b> | Theoretical Assessment: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# MODULE 1: FX FLUCTUATIONS & TRADE SIMULATION LAB
# =====================================================================
if module == "🌐 Module 1: FX Fluctuations, Elasticity & J-Curve Simulation":
    st.markdown("### 🌐 Currency Shocks: Marshall-Lerner Dynamics, J-Curve Trajectory & Real Exchange Rates")
    st.markdown(
        "Exchange rate movements generate price and volume shocks across domestic and international markets. "
        "The **Marshall-Lerner Condition** dictates whether currency depreciation ultimately restores trade equilibrium, "
        "while nominal shifts translate into competitiveness through the **Real Effective Exchange Rate (REER)**."
    )

    tab_overview, tab_deep = st.tabs(["📚 Core Framework", "🔬 Mathematical Foundations"])

    with tab_overview:
        st.markdown(
            """
| Analytical Model | Formulation | Primary Variables | Economic Transmission Mechanism |
| :--- | :--- | :--- | :--- |
| **Real Exchange Rate ($q$)** | $q = E \\cdot \\frac{P^*}{P}$ | Nominal FX ($E$, domestic/foreign), Foreign Prices ($P^*$), Domestic Prices ($P$) | Quantifies international relative purchasing power and true competitive terms of trade. |
| **Marshall-Lerner Condition** | $|\\epsilon_x| + |\\epsilon_m| > 1$ | Export Price Elasticity ($\\epsilon_x$), Import Price Elasticity ($\\epsilon_m$) | Real depreciation enhances the current account balance only if total export-import price elasticities exceed unity. |
| **J-Curve Dynamic Horizon** | $TB_t = P_x(t) X(t) - E(t) P_m^*(t) M(t)$ | Time Horizon ($t$), Sticky Contracts, Staggered Volume Elasticities | In the short run, rigid trade volumes cause depreciation to worsen the trade deficit before elastic volume adjustments take hold. |
| **Exchange Rate Pass-Through (ERPT)** | $\\beta_{PT} = \\frac{\\partial \\ln P^{imp}}{\\partial \\ln E}$ | Border/Import Prices ($P^{imp}$), Local Currency FX ($E$) | Incomplete pass-through ($\\beta_{PT} < 1$) blunts relative price adjustments due to local currency pricing (LCP) and distribution markups. |
            """
        )

    with tab_deep:
        col_m1, col_m2 = st.columns(2, gap="medium")
        with col_m1:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #34D399; margin: 0 0 0.5rem 0;">1. J-Curve Dynamic Pass-Through</h4>
    <p style="font-size: 0.9rem;">
        Currency depreciation alters export-import value balances via two conflicting pressures:
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li><b>Price Valuation Effect (Immediate):</b> Import bills in domestic currency rise instantly because existing contracts are invoiced in foreign currencies.</li>
        <li><b>Volume Adjustment Effect (Delayed):</b> As production lines and supply chains adjust, export volumes expand and import volumes contract, reversing the initial deficit.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col_m2:
            st.markdown(
                """
<div class="concept-card" style="border-left-color: #FBBF24;">
    <h4 style="color: #FBBF24; margin: 0 0 0.5rem 0;">2. Marshall-Lerner Threshold & Terms of Trade</h4>
    <p style="font-size: 0.9rem;">
        Assuming initial balanced trade ($TB = 0$):
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li><b>Condition:</b> $\\frac{\\partial TB}{\\partial E} > 0 \\iff |\\epsilon_x| + |\\epsilon_m| > 1$.</li>
        <li><b>Inelastic Failure:</b> If demand is highly inelastic ($|\\epsilon_x| + |\\epsilon_m| < 1$, e.g., essential energy or raw commodities), currency depreciation permanently deteriorates the balance of trade.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.subheader("🛠️ Interactive Labs: FX Macro & Trade Sensitivity Engines")

    lab_mode = st.radio(
        "Choose Lab Component:",
        [
            "1. J-Curve & Trade Balance Simulation: Post-Depreciation Dynamics",
            "2. Real Exchange Rate (RER) & Elasticity Sensitivity Suite",
        ],
        horizontal=True,
    )

    if lab_mode == "1. J-Curve & Trade Balance Simulation: Post-Depreciation Dynamics":
        c_fx1, c_fx2 = st.columns([1, 1.2], gap="large")

        with c_fx1:
            st.markdown("#### Depreciation Shock & Trade Profile")
            deprec_pct = st.slider("Domestic Currency Depreciation (%):", 5.0, 50.0, 20.0, 1.0) / 100.0
            init_export_val = st.slider("Base Export Volume ($B):", 50.0, 500.0, 200.0, 10.0)
            init_import_val = st.slider("Base Import Volume ($B):", 50.0, 500.0, 200.0, 10.0)

            st.markdown("#### Long-Run Elasticity Parameters")
            elas_x = st.slider("Long-Run Export Demand Elasticity ($|\\epsilon_x|$):", 0.1, 2.0, 0.75, 0.05)
            elas_m = st.slider("Long-Run Import Demand Elasticity ($|\\epsilon_m|$):", 0.1, 2.0, 0.65, 0.05)
            adjust_speed = st.slider("Quarterly Elasticity Convergence Speed ($k$):", 0.2, 1.0, 0.5, 0.05)

            ml_sum = elas_x + elas_m
            ml_satisfied = ml_sum > 1.0

            st.markdown("---")
            st.markdown("#### Policy Target Challenge")
            st.caption(
                "Tune elasticity and depreciation to construct a viable recovery where **ML condition holds ($|\\epsilon_x| + |\\epsilon_m| > 1.3$)** "
                "and **Year-End Trade Surplus exceeds $15B**."
            )

            # J-Curve Quarter Trajectory (Quarters 0 to 8)
            quarters = np.arange(0, 9)
            # Elasticities start low (short run stickiness) and rise asymptotically
            realized_ex = elas_x * (1.0 - np.exp(-adjust_speed * quarters))
            realized_em = elas_m * (1.0 - np.exp(-adjust_speed * quarters))

            # Prices & Volumes over time:
            # Foreign currency import price = 1; in domestic currency: (1 + deprec_pct)
            # Exports volume grows with realized_ex: init_export_val * (1 + realized_ex * deprec_pct)
            # Import volume drops with realized_em: init_import_val * (1 - realized_em * deprec_pct)
            export_revenues = init_export_val * (1.0 + realized_ex * deprec_pct)
            import_expenditures = (init_import_val * (1.0 + deprec_pct)) * (1.0 - realized_em * deprec_pct)
            net_trade_balance = export_revenues - import_expenditures

            terminal_tb = net_trade_balance[-1]

            if st.button("Evaluate Trade Adjustment Profile"):
                if ml_sum > 1.3 and terminal_tb >= 15.0:
                    st.session_state.lab_points = 50
                    st.success(f"Target matched! $\\Sigma \\epsilon = {ml_sum:.2f}$, 8Q Net Trade: ${terminal_tb:.2f}B (Awarded: 50/50 Pts)")
                else:
                    st.session_state.lab_points = 25
                    st.warning(
                        f"Target missed: Total Elasticity is {ml_sum:.2f} (Target: >1.3) or 8Q Balance is ${terminal_tb:.2f}B (Target: >=$15B). (Awarded: 25/50 Pts)"
                    )
                st.rerun()

        with c_fx2:
            st.markdown("#### Valuation & Dynamic Trajectory")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Marshall-Lerner</div>
                        <div class="metric-val" style="color: {'#10B981' if ml_satisfied else '#EF4444'} !important;">{ml_sum:.2f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m2:
                initial_trough = float(np.min(net_trade_balance))
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Initial Trough</div>
                        <div class="metric-val" style="color: {'#EF4444' if initial_trough < 0 else '#34D399'} !important;">${initial_trough:.1f}B</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m3:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Terminal Trade Balance</div>
                        <div class="metric-val" style="color: {'#10B981' if terminal_tb > 0 else '#EF4444'} !important;">${terminal_tb:.1f}B</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # J-Curve Chart
            j_curve_df = pd.DataFrame(
                {
                    "Quarters Post-Devaluation": quarters,
                    "Trade Balance ($B)": np.round(net_trade_balance, 2),
                    "Baseline Equilibrium": 0.0,
                }
            ).set_index("Quarters Post-Devaluation")

            st.line_chart(j_curve_df)
            st.caption(
                f"Trajectory shows the J-Curve phenomenon: Depreciation immediately deepens the initial trade deficit to ${initial_trough:.2f}B "
                "before structural volume substitutions take effect and re-establish a trade surplus."
            )

    else:
        c_reer1, c_reer2 = st.columns([1, 1.2], gap="large")

        with c_reer1:
            st.markdown("#### Price & Nominal FX Inputs")
            nom_rate = st.slider("Nominal Exchange Rate ($E$, Domestic/Foreign):", 0.5, 3.0, 1.20, 0.05)
            p_domestic = st.slider("Domestic Price Index ($P$):", 80.0, 180.0, 105.0, 1.0)
            p_foreign = st.slider("Foreign Partner Price Index ($P^*$):", 80.0, 180.0, 100.0, 1.0)

            # Real Exchange Rate calculation: q = E * (P* / P)
            # Higher q denotes foreign goods are more expensive relative to domestic goods (real depreciation)
            rer = nom_rate * (p_foreign / p_domestic)

            st.markdown("---")
            st.markdown(
                f"""
                - **Nominal FX ($E$):** `{nom_rate:.2f}`
                - **Relative Price Ratio ($P^*/P$):** `{(p_foreign/p_domestic):.3f}`
                - **Real Exchange Rate ($q$):** `{rer:.3f}`
                """
            )
            if rer > nom_rate:
                st.info("💡 Real Exchange Rate is more depreciated than nominal due to lower domestic inflation relative to trading partners.")
            else:
                st.warning("⚠️ High domestic inflation offsets nominal depreciation, causing real currency appreciation and eroding export competitiveness.")

        with c_reer2:
            st.markdown("#### Real Exchange Rate Competitiveness Horizon")
            inf_spread = np.linspace(-0.10, 0.10, 40)
            implied_rer = [nom_rate * ((p_foreign * (1 + spread)) / p_domestic) for spread in inf_spread]

            rer_chart_df = pd.DataFrame(
                {
                    "Foreign Inflation Differential (%)": np.round(inf_spread * 100, 2),
                    "Resulting Real Exchange Rate (q)": np.round(implied_rer, 3),
                }
            ).set_index("Foreign Inflation Differential (%)")

            st.line_chart(rer_chart_df)
            st.caption(
                "When foreign price levels rise faster than domestic prices (positive inflation differential), "
                "the real exchange rate depreciates ($q$ rises), making domestic exports more price-competitive abroad."
            )

# =====================================================================
# MODULE 2: ASSESSMENT
# =====================================================================
elif module == "📝 Module 2: FX Theory & Trade Elasticity Assessment":
    st.markdown("### 📝 FX Fluctuations & International Trade Assessment")
    st.markdown("Test your mastery of exchange rate pass-through, the Marshall-Lerner condition, J-Curve dynamics, and purchasing power parity (10 points each).")

    with st.form("fx_trade_quiz"):
        st.markdown("#### 1. The Marshall-Lerner Condition Mechanics")
        q1 = st.radio(
            "Under the Marshall-Lerner framework, a real currency depreciation succeeds in improving the net trade balance only if:",
            [
                "A) The sum of price elasticities of demand for exports and imports strictly exceeds unity ($|\\epsilon_x| + |\\epsilon_m| > 1$).",
                "B) Both export and import demand curves are perfectly price-inelastic.",
                "C) The domestic central bank raises benchmark interest rates to equal foreign rates.",
                "D) The country runs a continuous capital account deficit.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 2. The J-Curve Dynamic Horizon")
        q2 = st.radio(
            "Why does a nominal exchange rate depreciation frequently worsen a nation's trade balance in the short run?",
            [
                "A) Domestic consumers immediately increase savings and cease purchasing domestic goods.",
                "B) Existing contracts lock in import orders, causing the domestic currency cost of imports to rise before quantities can adjust.",
                "C) Exporters immediately reduce manufacturing production due to deflationary pressures.",
                "D) Foreign partners immediately impose countervailing tariffs on all exported goods.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 3. Real Effective Exchange Rate (REER) Determination")
        q3 = st.radio(
            "If a country's domestic inflation runs at 12% while foreign inflation is 2%, and the nominal exchange rate remains fixed:",
            [
                "A) The Real Exchange Rate depreciates, boosting domestic export competitiveness.",
                "B) The Real Exchange Rate appreciates, making domestic exports less competitive and imports cheaper.",
                "C) Net trade balances immediately shift into an expanding surplus.",
                "D) Purchasing Power Parity (PPP) remains strictly in permanent balance.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 4. Incomplete Exchange Rate Pass-Through (ERPT)")
        q4 = st.radio(
            "Which factor explains why a 15% currency depreciation rarely translates into a full 15% increase in consumer import prices?",
            [
                "A) Foreign firms compress profit margins to preserve market share (pricing-to-market) and local distribution costs remain fixed.",
                "B) Central banks enforce legal price caps on all imported consumer products.",
                "C) The Marshall-Lerner condition requires pass-through to equal zero by definition.",
                "D) Importers automatically swap contracts into the domestic currency at par.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 5. Currency Appreciation and Terms of Trade")
        q5 = st.radio(
            "When a domestic currency experiences a sustained nominal and real appreciation, the expected trade impact is:",
            [
                "A) Exports become cheaper in foreign currency, widening the trade surplus.",
                "B) Foreign imports become cheaper domestically, while domestic exports become more expensive abroad, exerting downward pressure on the trade balance.",
                "C) Domestic aggregate demand shifts permanently toward domestic goods over imports.",
                "D) Import quantities contract instantaneously due to wealth effects.",
            ],
            index=None,
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Grade")

        if submit_quiz:
            correct_keys = {
                "q1": "A) The sum of price elasticities of demand for exports and imports strictly exceeds unity ($|\\epsilon_x| + |\\epsilon_m| > 1$).",
                "q2": "B) Existing contracts lock in import orders, causing the domestic currency cost of imports to rise before quantities can adjust.",
                "q3": "B) The Real Exchange Rate appreciates, making domestic exports less competitive and imports cheaper.",
                "q4": "A) Foreign firms compress profit margins to preserve market share (pricing-to-market) and local distribution costs remain fixed.",
                "q5": "B) Foreign imports become cheaper domestically, while domestic exports become more expensive abroad, exerting downward pressure on the trade balance.",
            }

            records = {
                "q1": (q1 == correct_keys["q1"]),
                "q2": (q2 == correct_keys["q2"]),
                "q3": (q3 == correct_keys["q3"]),
                "q4": (q4 == correct_keys["q4"]),
                "q5": (q5 == correct_keys["q5"]),
            }

            st.session_state.quiz_score = sum(records.values()) * 10
            st.session_state.quiz_submitted = True
            st.session_state.eval_records = records
            st.rerun()

    if st.session_state.quiz_submitted:
        st.markdown("---")
        st.markdown(f"### Assessment Score: **{st.session_state.quiz_score} / 50 Points**")

        rec = st.session_state.eval_records
        if not rec.get("q1", False):
            st.error("Q1 Review: The Marshall-Lerner condition states that depreciation improves the trade balance only if the absolute sum of demand elasticities for exports and imports exceeds 1 ($|\\epsilon_x| + |\\epsilon_m| > 1$).")
        if not rec.get("q2", False):
            st.error("Q2 Review: J-Curve dynamics stem from sticky trade contracts. The price valuation effect is immediate (imports cost more), while volume substitutions require time to materialize.")
        if not rec.get("q3", False):
            st.error("Q3 Review: Higher domestic inflation without compensatory nominal depreciation leads to real appreciation ($q = E \\cdot P^*/P$ drops), pricing domestic producers out of foreign markets.")
        if not rec.get("q4", False):
            st.error("Q4 Review: Incomplete pass-through occurs because foreign exporters absorb currency swings via markups (pricing-to-market) and local distribution/marketing costs remain denominated in local currency.")
        if not rec.get("q5", False):
            st.error("Q5 Review: Currency appreciation makes exports more expensive for foreign buyers and foreign products cheaper for domestic consumers, typically reducing net exports.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("Quantitative FX & Trade Macro Suite")
with f2:
    st.caption("Marshall-Lerner, J-Curve & Elasticity Analytics")
with f3:
    st.caption(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
