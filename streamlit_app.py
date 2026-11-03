from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Currency Movements & Net Exports (NX)",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Deep Slate, Emerald, and Amber Theme
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

    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid #34D399 !important;
        padding: 0.6rem 1.6rem !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease-in-out;
    }
</style>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# SESSION STATE ENGINE
# =====================================================================
if "nx_points" not in st.session_state:
    st.session_state.nx_points = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "eval_records" not in st.session_state:
    st.session_state.eval_records = {}

total_score = st.session_state.nx_points + st.session_state.quiz_score

# =====================================================================
# SIDEBAR
# =====================================================================
with st.sidebar:
    st.markdown("## 📊 FX & Net Exports Suite")
    nav_mode = st.radio(
        "Select Section:",
        [
            "🔬 Simulation: Appreciation vs. Depreciation",
            "📝 Assessment: FX & Trade Theory",
        ],
    )
    st.markdown("---")
    st.markdown("### 🏆 Performance Tracker")
    st.markdown(f"**Interactive Lab:** {st.session_state.nx_points} / 50")
    st.markdown(f"**Theory Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Aggregate Score:** {total_score} / 100")

# =====================================================================
# BANNER
# =====================================================================
st.markdown(
    f"""
<div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(14, 165, 233, 0.2) 100%);
            border: 1px solid rgba(16, 185, 129, 0.45); border-radius: 12px; padding: 1.2rem; margin-bottom: 1.5rem; text-align: center;">
    <h2 style="color: #34D399; margin: 0; font-weight: 800;">Currency Valuation & Net Exports Engine: {total_score} / 100</h2>
    <p style="color: #E2E8F0; margin: 0.35rem 0 0 0; font-size: 1rem;">
        Simulation Lab: <b>{st.session_state.nx_points}/50 Pts</b> | Conceptual Assessment: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# SECTION 1: SIMULATION LAB
# =====================================================================
if nav_mode == "🔬 Simulation: Appreciation vs. Depreciation":
    st.markdown("### 🌐 Currency Fluctuations & Net Exports: $NX = X - M$")
    st.markdown(
        "An **appreciation** makes domestic goods more expensive abroad and foreign imports cheaper domestically, "
        "tending to lower Net Exports ($NX$). A **depreciation** creates the inverse incentive, but real-world "
        "outcomes depend on price elasticities of demand ($|\\epsilon_x| + |\\epsilon_m|$) and time-horizon contract stickiness."
    )

    tab_model, tab_math = st.tabs(["📚 Core Framework", "🔬 Mathematical Relations"])

    with tab_model:
        st.markdown(
            """
| Movement | Relative Export Price | Relative Import Price | Quantity Effect | Value Effect on Net Exports ($NX$) |
| :--- | :--- | :--- | :--- | :--- |
| **Appreciation** ($\\%\\Delta E < 0$) | More expensive abroad | Cheaper domestically | $X \\downarrow, M \\uparrow$ | Deteriorates $NX$ when demand is elastic. |
| **Depreciation** ($\\%\\Delta E > 0$) | Cheaper abroad | More expensive domestically | $X \\uparrow, M \\downarrow$ | Improves $NX$ in the long run if Marshall-Lerner ($|\\epsilon_x| + |\\epsilon_m| > 1$) holds. |
            """
        )

    with tab_math:
        col_c1, col_c2 = st.columns(2, gap="medium")
        with col_c1:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #34D399; margin: 0 0 0.5rem 0;">1. Net Export Formula with Elasticities</h4>
    <p style="font-size: 0.88rem; color: #E2E8F0;">
        Let $E$ denote the nominal exchange rate (units of domestic currency per foreign currency, so an increase is a depreciation):
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li>$X = X_0 \\cdot \\left(1 + |\\epsilon_x| \\cdot \\%\\Delta E\\right)$</li>
        <li>$M_{qty} = M_0 \\cdot \\left(1 - |\\epsilon_m| \\cdot \\%\\Delta E\\right)$</li>
        <li>$M_{val} = M_{qty} \\cdot \\left(1 + \\%\\Delta E\\right)$</li>
        <li>$NX = X - M_{val}$</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col_c2:
            st.markdown(
                """
<div class="concept-card" style="border-left-color: #FBBF24;">
    <h4 style="color: #FBBF24; margin: 0 0 0.5rem 0;">2. Marshall-Lerner Criterion</h4>
    <p style="font-size: 0.88rem; color: #E2E8F0;">
        Starting from balanced trade ($X = M$):
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li>$\\frac{d(NX)}{dE} > 0 \\iff |\\epsilon_x| + |\\epsilon_m| > 1$</li>
        <li>If $|\\epsilon_x| + |\\epsilon_m| < 1$, depreciation paradoxically <b>worsens</b> $NX$ because volume changes fail to offset higher per-unit import expenditures.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.subheader("🛠️ Interactive Sensitivity & Scenario Engine")

    col_in, col_out = st.columns([1, 1.2], gap="large")

    with col_in:
        st.markdown("#### Scenario Controls")
        fx_shock_type = st.radio(
            "Select Currency Shock Direction:",
            ["Domestic Currency Depreciation", "Domestic Currency Appreciation"],
            horizontal=True,
        )
        pct_magnitude = st.slider("Shock Magnitude (%):", 1.0, 40.0, 15.0, 1.0) / 100.0

        # Sign convention: positive delta_e = depreciation, negative = appreciation
        delta_e = pct_magnitude if fx_shock_type == "Domestic Currency Depreciation" else -pct_magnitude

        st.markdown("#### Trade Parameters")
        base_x = st.slider("Baseline Exports ($B):", 50.0, 500.0, 200.0, 10.0)
        base_m = st.slider("Baseline Imports ($B):", 50.0, 500.0, 200.0, 10.0)
        elas_x = st.slider("Export Price Elasticity ($|\\epsilon_x|$):", 0.05, 2.0, 0.75, 0.05)
        elas_m = st.slider("Import Price Elasticity ($|\\epsilon_m|$):", 0.05, 2.0, 0.65, 0.05)

        base_nx = base_x - base_m
        ml_condition = (elas_x + elas_m) > 1.0

        # Post-shock values
        post_x = base_x * (1.0 + elas_x * delta_e)
        post_m_vol = base_m * (1.0 - elas_m * delta_e)
        post_m_val = post_m_vol * (1.0 + delta_e)
        post_nx = post_x - post_m_val
        delta_nx = post_nx - base_nx

        st.markdown("---")
        st.markdown("#### Target Exercise")
        st.caption(
            "Configure a scenario where currency depreciation generates a **net improvement in trade ($\\Delta NX \\ge \\$10\\text{B}$)** "
            "with **Marshall-Lerner condition satisfied**."
        )

        if st.button("Evaluate Net Export Target"):
            if delta_e > 0 and ml_condition and delta_nx >= 10.0:
                st.session_state.nx_points = 50
                st.success(f"Target achieved! $\\Delta NX = +\\${delta_nx:.2f}B$ with $\\Sigma \\epsilon = {elas_x + elas_m:.2f}$. (Awarded: 50/50 Pts)")
            else:
                st.session_state.nx_points = 20
                st.warning(
                    f"Target missed: Requires Depreciation (current: {fx_shock_type}), ML > 1.0 (current: {elas_x + elas_m:.2f}), "
                    f"and $\\Delta NX \\ge \\$10B$ (current: ${delta_nx:.2f}B). (Awarded: 20/50 Pts)"
                )
            st.rerun()

    with col_out:
        st.markdown("#### Impact Analysis")
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(
                f"""
                <div class="metric-panel">
                    <div class="metric-title">New Exports ($X$)</div>
                    <div class="metric-val">${post_x:.1f}B</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with m2:
            st.markdown(
                f"""
                <div class="metric-panel">
                    <div class="metric-title">New Imports ($M$)</div>
                    <div class="metric-val">${post_m_val:.1f}B</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with m3:
            nx_color = "#10B981" if delta_nx >= 0 else "#EF4444"
            st.markdown(
                f"""
                <div class="metric-panel">
                    <div class="metric-title">Change in NX ($\\Delta NX$)</div>
                    <div class="metric-val" style="color: {nx_color} !important;">
                        {'+' if delta_nx > 0 else ''}{delta_nx:.1f}B
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Sensitivity curve: FX Shift vs NX across a range (-30% to +30%)
        fx_range = np.linspace(-0.30, 0.30, 41)
        sim_nx = []
        for shift in fx_range:
            sim_x = base_x * (1.0 + elas_x * shift)
            sim_m = (base_m * (1.0 - elas_m * shift)) * (1.0 + shift)
            sim_nx.append(sim_x - sim_m)

        chart_df = pd.DataFrame(
            {
                "Currency Movement (% Shift)": np.round(fx_range * 100, 1),
                "Implied Net Exports ($B)": np.round(sim_nx, 2),
                "Baseline NX ($B)": base_nx,
            }
        ).set_index("Currency Movement (% Shift)")

        st.line_chart(chart_df)
        st.caption(
            "Negative axis represents currency appreciation (stronger domestic currency); "
            "positive axis represents depreciation (weaker domestic currency). "
            f"Slope is {'positive' if ml_condition else 'negative'} because $|\\epsilon_x| + |\\epsilon_m| = {elas_x + elas_m:.2f} "
            f"({'Marshall-Lerner satisfied' if ml_condition else 'Marshall-Lerner violated'})."
        )

# =====================================================================
# SECTION 2: ASSESSMENT
# =====================================================================
elif nav_mode == "📝 Assessment: FX & Trade Theory":
    st.markdown("### 📝 Currency Valuation & Net Exports Assessment")
    st.markdown("Test your understanding of currency appreciation, depreciation, exchange rate pass-through, and trade balances (10 points each).")

    with st.form("trade_assessment_form"):
        st.markdown("#### 1. Mechanism of Currency Appreciation")
        q1 = st.radio(
            "When a nation's currency appreciates significantly, holding all else constant:",
            [
                "A) Foreign goods become more expensive for domestic buyers, reducing total imports.",
                "B) Domestic export prices in foreign currency rise, reducing export demand abroad, while imports become cheaper.",
                "C) Net exports unconditionally expand across both the short run and long run.",
                "D) The country's physical export volumes expand to meet higher foreign demand.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 2. The Marshall-Lerner Rule")
        q2 = st.radio(
            "If the sum of price elasticities of demand for exports and imports equals 0.65 ($|\\epsilon_x| + |\\epsilon_m| = 0.65$), a currency depreciation will:",
            [
                "A) Improve the trade balance by expanding export revenue above import expenditure.",
                "B) Leave the trade balance unchanged because supply equals demand in equilibrium.",
                "C) Deteriorate the trade balance because volume adjustments fail to compensate for more expensive imports.",
                "D) Force domestic inflation to instantly drop to zero.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 3. Real Exchange Rate Formulation")
        q3 = st.radio(
            "The Real Exchange Rate ($q = E \\cdot \\frac{P^*}{P}$) tracks relative international prices. If domestic price inflation ($P$) outpaces foreign inflation ($P^*$) while the nominal rate ($E$) stays flat:",
            [
                "A) The real exchange rate appreciates, eroding domestic export price competitiveness.",
                "B) The real exchange rate depreciates, increasing international market share.",
                "C) Domestic exporters gain an automatic price advantage over foreign competitors.",
                "D) Net exports increase systematically.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 4. The J-Curve Dynamic")
        q4 = st.radio(
            "In the initial months following an unexpected currency depreciation, net exports frequently drop before improving because:",
            [
                "A) Foreign buyers cancel contracts immediately due to currency regulations.",
                "B) Trade contracts are fixed in the short term; import prices in domestic currency spike before volumes can substitute.",
                "C) Domestic firms voluntarily stop producing export products.",
                "D) Central banks prohibit capital flows until the trade balance resets.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 5. Macroeconomic Aggregate Demand Link")
        q5 = st.radio(
            "In the national income accounting identity ($Y = C + I + G + NX$), a sustained increase in Net Exports ($NX$) from a successful depreciation directly:",
            [
                "A) Reduces aggregate domestic output ($Y$).",
                "B) Increases Aggregate Demand and puts upward pressure on domestic output and the price level.",
                "C) Guarantees an immediate reduction in total government tax revenue.",
                "D) Eliminates the national debt without any monetary intervention.",
            ],
            index=None,
        )

        submit_btn = st.form_submit_button("Submit Assessment & Grade")

        if submit_btn:
            correct_answers = {
                "q1": "B) Domestic export prices in foreign currency rise, reducing export demand abroad, while imports become cheaper.",
                "q2": "C) Deteriorate the trade balance because volume adjustments fail to compensate for more expensive imports.",
                "q3": "A) The real exchange rate appreciates, eroding domestic export price competitiveness.",
                "q4": "B) Trade contracts are fixed in the short term; import prices in domestic currency spike before volumes can substitute.",
                "q5": "B) Increases Aggregate Demand and puts upward pressure on domestic output and the price level.",
            }

            results = {
                "q1": (q1 == correct_answers["q1"]),
                "q2": (q2 == correct_answers["q2"]),
                "q3": (q3 == correct_answers["q3"]),
                "q4": (q4 == correct_answers["q4"]),
                "q5": (q5 == correct_answers["q5"]),
            }

            st.session_state.quiz_score = sum(results.values()) * 10
            st.session_state.quiz_submitted = True
            st.session_state.eval_records = results
            st.rerun()

    if st.session_state.quiz_submitted:
        st.markdown("---")
        st.markdown(f"### Assessment Score: **{st.session_state.quiz_score} / 50 Points**")

        rec = st.session_state.eval_records
        if not rec.get("q1", False):
            st.error("Q1 Review: Appreciation strengthens domestic purchasing power abroad (cheaper imports), but makes domestic exports less attractive to foreign consumers.")
        if not rec.get("q2", False):
            st.error("Q2 Review: When $|\\epsilon_x| + |\\epsilon_m| < 1$, the volume shift is too weak to offset the valuation loss from higher import costs, worsening the trade balance.")
        if not rec.get("q3", False):
            st.error("Q3 Review: When domestic inflation exceeds trading partners under a constant nominal rate, domestic goods become relatively more expensive (real appreciation).")
        if not rec.get("q4", False):
            st.error("Q4 Review: The J-Curve reflects short-run contract stickiness: import costs increase in local currency immediately, whereas volume adjustments take several quarters.")
        if not rec.get("q5", False):
            st.error("Q5 Review: Because $NX$ is an additive component of aggregate output, an improvement in $NX$ raises aggregate demand ($AD$), expanding output and potentially inducing demand-pull inflation.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("International Trade & Macro Valuation Engine")
with f2:
    st.caption("Net Exports, Marshall-Lerner & Exchange Rate Sensitivity")
with f3:
    st.caption(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
