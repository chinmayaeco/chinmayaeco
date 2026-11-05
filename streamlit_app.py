from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Open Economy Macro: Exchange Rates & Mundell-Fleming",
    page_icon="🌐",
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
if "sim_points" not in st.session_state:
    st.session_state.sim_points = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "eval_records" not in st.session_state:
    st.session_state.eval_records = {}

total_score = st.session_state.sim_points + st.session_state.quiz_score

# =====================================================================
# SIDEBAR
# =====================================================================
with st.sidebar:
    st.markdown("## 🌐 International Macro & FX Suite")
    nav_mode = st.radio(
        "Select Section:",
        [
            "🔬 Simulation: Mundell-Fleming Lab",
            "📝 Assessment: Open Economy Policy & LM*",
        ],
    )
    st.markdown("---")
    st.markdown("### 🏆 Performance Tracker")
    st.markdown(f"**Interactive Lab:** {st.session_state.sim_points} / 50")
    st.markdown(f"**Theory Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Aggregate Score:** {total_score} / 100")

# =====================================================================
# BANNER
# =====================================================================
st.markdown(
    f"""
<div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(14, 165, 233, 0.2) 100%);
            border: 1px solid rgba(16, 185, 129, 0.45); border-radius: 12px; padding: 1.2rem; margin-bottom: 1.5rem; text-align: center;">
    <h2 style="color: #34D399; margin: 0; font-weight: 800;">Mundell-Fleming & Open Economy Equilibrium: {total_score} / 100</h2>
    <p style="color: #E2E8F0; margin: 0.35rem 0 0 0; font-size: 1rem;">
        Simulation Lab: <b>{st.session_state.sim_points}/50 Pts</b> | Conceptual Assessment: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# SECTION 1: SIMULATION LAB
# =====================================================================
if nav_mode == "🔬 Simulation: Mundell-Fleming Lab":
    st.markdown("### ⚖️ Mundell-Fleming Dynamics with Perfect Capital Mobility")
    st.markdown(
        "In a small open economy with perfect capital mobility, domestic interest rates are pinned to world rates ($r = r^*$). "
        "In $(Y, e)$ space, the money market equilibrium condition ($M/P = L(r^*, Y)$) yields a **vertical $LM^*$ curve**, "
        "rendering output determined exclusively by the money supply under floating rates."
    )

    tab_model, tab_math = st.tabs(["📚 Regime Comparison", "🔬 Open Economy Multipliers"])

    with tab_model:
        st.markdown(
            """
| Regime | Policy Levers | Monetary Policy Impact | Fiscal Policy Impact | Trade Policy Restrictions |
| :--- | :--- | :--- | :--- | :--- |
| **Flexible Rates** | Independent $M$; Exchange rate $e$ floats | **Completely Potent**: Shifts $LM^*$; changes $Y$ via currency depreciation/appreciation. | **Completely Impotent**: Crowded out 100% through exchange rate appreciation ($NX \\downarrow$). | **Impotent on Output**: Currency appreciates, canceling out the tariff/import protection. |
| **Fixed Rates** | $e = \\bar{e}$; Central bank pegs via FX reserves | **Completely Impotent**: Endogenous money supply ($M$) must defend parity; loss of monetary autonomy. | **Maximum Potency**: Fiscal shift triggers reserve inflows, expanding $M$ and shifting $LM^*$ right. | **Expansive**: Increases net exports, forcing central bank to inject reserves to maintain $\\bar{e}$. |
            """
        )

    with tab_math:
        col_c1, col_c2 = st.columns(2, gap="medium")
        with col_c1:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #34D399; margin: 0 0 0.5rem 0;">1. The Vertical LM* Equation</h4>
    <p style="font-size: 0.88rem; color: #E2E8F0;">
        Equilibrium in the domestic money market under $r = r^*$:
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li>$\\frac{M}{P} = L(r^*, Y) = kY - h r^*$</li>
        <li>$Y = \\frac{1}{k}\\left(\\frac{M}{P} + h r^*\\right)$</li>
        <li>Notice the nominal/real exchange rate ($e$) does <b>not</b> appear in this equation: $LM^*$ is perfectly vertical in $(Y, e)$ space.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col_c2:
            st.markdown(
                """
<div class="concept-card" style="border-left-color: #FBBF24;">
    <h4 style="color: #FBBF24; margin: 0 0 0.5rem 0;">2. Downward-Sloping IS* Equation</h4>
    <p style="font-size: 0.88rem; color: #E2E8F0;">
        Goods market equilibrium where net exports depend inversely on the exchange rate:
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li>$Y = C(Y - T) + I(r^*) + G + NX(e)$</li>
        <li>$NX(e) = NX_0 - q \\cdot e$</li>
        <li>Higher $e$ (appreciation) makes domestic goods more expensive, reducing net exports and aggregate output.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("---")
        st.subheader("🛠️ Policy Shock & Regime Simulator")

        col_in, col_out = st.columns([1, 1.2], gap="large")

        with col_in:
            st.markdown("#### Regime & Exogenous Parameters")
            regime = st.selectbox("Exchange Rate Regime:", ["Flexible Exchange Rate", "Fixed Exchange Rate"])
            r_star = st.slider("World Interest Rate ($r^*$ in %):", 1.0, 10.0, 4.0, 0.5) / 100.0
            gov_spending = st.slider("Fiscal Policy: Government Spending ($G$):", 50.0, 300.0, 150.0, 10.0)
            money_supply = st.slider("Monetary Policy: Money Supply ($M$):", 100.0, 500.0, 250.0, 10.0)
            target_fixed_e = 100.0  # Baseline peg parity

            # Structural model coefficients
            P = 1.0
            k = 0.5   # Money demand income sensitivity
            h = 250.0 # Money demand interest sensitivity
            c_mpc = 0.6
            tax = 100.0
            I_base = 120.0
            q_nx = 1.5
            nx_base = 180.0

            # Structural Equations
            # LM*: M/P = kY - h*r* => Y_lm = (M/P + h*r*) / k
            # IS*: Y = c_mpc*(Y - T) + I_base - 100*r* + G + nx_base - q_nx*e
            # (1 - c_mpc)*Y = -c_mpc*tax + I_base - 100*r* + G + nx_base - q_nx*e
            A = -c_mpc * tax + I_base - 100.0 * r_star + gov_spending + nx_base

            if regime == "Flexible Exchange Rate":
                # LM* determines output directly
                eq_Y = (money_supply / P + h * r_star) / k
                # IS* clears exchange rate
                eq_e = (A - (1.0 - c_mpc) * eq_Y) / q_nx
                effective_M = money_supply
            else:
                # Fixed rate pins e = target_fixed_e, IS* determines output
                eq_e = target_fixed_e
                eq_Y = (A - q_nx * eq_e) / (1.0 - c_mpc)
                # Central bank money supply must adjust endogenously to validate LM*
                effective_M = (k * eq_Y - h * r_star) * P

            eq_nx = nx_base - q_nx * eq_e

            st.markdown("---")
            st.markdown("#### Policy Target Challenge")
            st.caption(
                "Achieve a target output **$Y \\ge 650$** while avoiding severe currency depreciation "
                "(maintain **$e \\ge 85.0$**) under your chosen regime."
            )

            if st.button("Evaluate Policy Target"):
                if eq_Y >= 650.0 and eq_e >= 85.0:
                    st.session_state.sim_points = 50
                    st.success(f"Target achieved! $Y = {eq_Y:.1f}$, $e = {eq_e:.1f}$. (Awarded: 50/50 Pts)")
                else:
                    st.session_state.sim_points = 20
                    st.warning(
                        f"Target missed: Requires $Y \\ge 650$ (current: {eq_Y:.1f}) and $e \\ge 85.0$ (current: {eq_e:.1f}). "
                        f"(Awarded: 20/50 Pts)"
                    )
                st.rerun()

        with col_out:
            st.markdown("#### Open Economy Equilibrium State")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Equilibrium Output ($Y$)</div>
                        <div class="metric-val">{eq_Y:.1f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m2:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Exchange Rate ($e$)</div>
                        <div class="metric-val">{eq_e:.1f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m3:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Endogenous Reserves/Money ($M$)</div>
                        <div class="metric-val" style="color: #38BDF8 !important;">{effective_M:.1f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Chart IS*-LM* Curve Representation in (Y, e) space
            e_vals = np.linspace(50.0, 150.0, 30)
            y_is = (A - q_nx * e_vals) / (1.0 - c_mpc)
            y_lm = np.full_like(e_vals, (effective_M / P + h * r_star) / k)

            chart_df = pd.DataFrame(
                {
                    "Exchange Rate (e)": np.round(e_vals, 1),
                    "IS* Curve (Goods Market)": np.round(y_is, 1),
                    "Vertical LM* Curve (Money Market)": np.round(y_lm, 1),
                }
            ).set_index("Exchange Rate (e)")

            st.line_chart(chart_df)
            st.caption(
                f"Equilibrium Net Exports: **${eq_nx:.1f}B**. Under floating rates, fiscal policy shifts IS* vertically along the vertical LM*, "
                f"altering only $e$. Under fixed rates, the central bank adjusts money supply to **${effective_M:.1f}** to defend parity."
            )

# =====================================================================
# SECTION 2: ASSESSMENT
# =====================================================================
elif nav_mode == "📝 Assessment: Open Economy Policy & LM*":
    st.markdown("### 📝 Open Economy & Mundell-Fleming Theory Assessment")
    st.markdown("Test your mastery of exchange rate systems, capital mobility, monetary autonomy, and the LM* curve (10 points each).")

    with st.form("open_econ_assessment_form"):
        st.markdown("#### 1. Geometry of the LM* Curve")
        q1 = st.radio(
            "In the Mundell-Fleming model for a small open economy with perfect capital mobility, why is the $LM^*$ curve vertical in $(Y, e)$ space?",
            [
                "A) The exchange rate directly determines central bank reserve ratios.",
                "B) Domestic interest rates are pinned to $r^*$, meaning the money market equation $M/P = L(r^*, Y)$ determines $Y$ independently of $e$.",
                "C) Net exports have infinite elasticity with respect to domestic prices.",
                "D) Commercial banks refuse to lend foreign currency to domestic households.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 2. Fiscal Policy under Floating Rates")
        q2 = st.radio(
            "Under a flexible exchange rate regime, how does an expansionary fiscal policy shock ($\\Delta G > 0$) affect equilibrium aggregate income ($Y$)?",
            [
                "A) Output expands via the Keynesian government spending multiplier.",
                "B) Output falls sharply because the central bank contracts the base money supply.",
                "C) Output is unchanged because complete currency appreciation crowds out net exports 100%.",
                "D) The LM* curve shifts rightward to accommodate lower taxes.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 3. Monetary Policy under Fixed Rates")
        q3 = st.radio(
            "If a central bank maintains a credible fixed exchange rate peg and attempts an open market purchase of bonds to expand the money supply:",
            [
                "A) Downward pressure on domestic interest rates triggers capital flight, forcing the central bank to sell foreign reserves, restoring $M$ to its original level.",
                "B) Domestic output permanently expands as net exports rise.",
                "C) The exchange rate instantly depreciates without central bank intervention.",
                "D) World interest rates ($r^*$) adjust downward to match domestic rates.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 4. The Monetary Policy Trilemma")
        q4 = st.radio(
            "According to the Open Economy Trilemma (Impossible Trinity), a country cannot simultaneously maintain:",
            [
                "A) A balanced budget, low unemployment, and price stability.",
                "B) Free capital mobility, a fixed exchange rate, and an independent monetary policy.",
                "C) High exports, a floating exchange rate, and a positive current account balance.",
                "D) Fractional reserve banking, currency in circulation, and deposit insurance.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 5. Import Restrictions / Tariffs under Floating Rates")
        q5 = st.radio(
            "Under flexible exchange rates and perfect capital mobility, introducing an import quota or tariff shifts the $IS^*$ curve right. The resulting equilibrium displays:",
            [
                "A) Higher output ($Y$) and higher net exports ($NX$).",
                "B) Higher output ($Y$) with an unchanged exchange rate ($e$).",
                "C) Unchanged output ($Y$), an appreciated exchange rate ($e$), and unchanged total net exports ($NX$).",
                "D) A downward shift in the vertical $LM^*$ curve.",
            ],
            index=None,
        )

        submit_btn = st.form_submit_button("Submit Assessment & Grade")

        if submit_btn:
            correct_answers = {
                "q1": "B) Domestic interest rates are pinned to $r^*$, meaning the money market equation $M/P = L(r^*, Y)$ determines $Y$ independently of $e$.",
                "q2": "C) Output is unchanged because complete currency appreciation crowds out net exports 100%.",
                "q3": "A) Downward pressure on domestic interest rates triggers capital flight, forcing the central bank to sell foreign reserves, restoring $M$ to its original level.",
                "q4": "B) Free capital mobility, a fixed exchange rate, and an independent monetary policy.",
                "q5": "C) Unchanged output ($Y$), an appreciated exchange rate ($e$), and unchanged total net exports ($NX$).",
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
            st.error("Q1 Review: Because $r = r^*$, money equilibrium $\\frac{M}{P} = L(r^*, Y)$ pins down $Y$ uniquely. Because $e$ does not enter money demand, $LM^*$ is strictly vertical.")
        if not rec.get("q2", False):
            st.error("Q2 Review: $\\Delta G > 0$ attempts to raise interest rates, attracting foreign capital inflows. The resulting currency appreciation cuts net exports until aggregate demand returns exactly to its starting point.")
        if not rec.get("q3", False):
            st.error("Q3 Review: Monetary policy is completely impotent under fixed rates. Domestic liquidity expansion creates downward rate pressure, triggering capital outflow and drain of FX reserves until $M$ contracts back.")
        if not rec.get("q4", False):
            st.error("Q4 Review: The Trilemma dictates that an open economy can pick at most two of: (1) Free capital mobility, (2) Fixed exchange rate, and (3) Independent domestic monetary policy.")
        if not rec.get("q5", False):
            st.error("Q5 Review: Tariffs shift $IS^*$ rightward, but because $LM^*$ is vertical, $Y$ cannot change. The exchange rate appreciates by enough to counteract the tariff, leaving aggregate $NX$ and $Y$ unchanged.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("International Macroeconomics & Mundell-Fleming Engine")
with f2:
    st.caption("Capital Mobility, Trilemma Mechanics & Vertical LM*")
with f3:
    st.caption(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
