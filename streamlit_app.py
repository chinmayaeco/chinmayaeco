from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Macroeconomic Lab: Money Market & LM Curve",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# High-Contrast Dark Slate, Cyan, and Amber Theme
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at 10% 20%, #0c192c 0%, #070e1b 50%, #030712 100%);
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
        color: #CBD5E1 !important;
        font-size: 0.88rem !important;
    }

    .score-banner {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.2) 0%, rgba(14, 165, 233, 0.2) 100%);
        border: 1px solid rgba(245, 158, 11, 0.45);
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
    }
    
    .metric-panel {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }
    
    .metric-title {
        color: #CBD5E1 !important;
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .metric-val {
        color: #38BDF8 !important;
        font-size: 1.6rem;
        font-weight: 800;
        margin-top: 0.3rem;
    }
    
    .concept-card {
        background: rgba(15, 23, 42, 0.65);
        border-left: 4px solid #38BDF8;
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
        color: #38BDF8 !important;
    }

    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid #38BDF8 !important;
        padding: 0.6rem 1.6rem !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease-in-out;
    }

    .stButton > button:hover, .stFormSubmitButton > button:hover {
        background: linear-gradient(135deg, #0369A1 0%, #075985 100%) !important;
        border-color: #7DD3FC !important;
        color: #FFFFFF !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# SESSION STATE ENGINE
# =====================================================================
if "market_points" not in st.session_state:
    st.session_state.market_points = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "eval_records" not in st.session_state:
    st.session_state.eval_records = {}

total_final_score = st.session_state.market_points + st.session_state.quiz_score

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("## 📈 Macroeconomic Lab")
    module = st.radio(
        "Select Learning Module:",
        [
            "🏛️ Module 1: Money Market & LM Curve Mechanics",
            "📝 Module 2: Monetary Theory Assessment",
        ],
    )
    st.markdown("---")
    st.markdown("### 🏆 Performance Tracker")
    st.markdown(f"**Interactive Lab:** {st.session_state.market_points} / 50")
    st.markdown(f"**Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Aggregate Score:** {total_final_score} / 100")

    if total_final_score == 100:
        st.success("🌟 Monetary Macro Specialist Status Achieved!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(
    f"""
<div class="score-banner">
    <h2 style="color: #FBBF24; margin: 0; font-weight: 800;">Liquidity Preference & LM Suite: {total_final_score} / 100</h2>
    <p style="color: #E2E8F0; margin: 0.35rem 0 0 0; font-size: 1rem;">
        Simulation Lab: <b>{st.session_state.market_points}/50 Pts</b> | Conceptual Assessment: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# MODULE 1: MONEY DEMAND, MONEY SUPPLY & THE LM CURVE
# =====================================================================
if module == "🏛️ Module 1: Money Market & LM Curve Mechanics":
    st.markdown("### 🏛️ Money Market Equilibrium: Keynesian Liquidity Preference to the LM Curve")
    st.markdown(
        "The money market equilibrates the demand for real money balances with the real money supply set by the central bank. "
        "The **LM (Liquidity-Money) curve** charts all combinations of national income ($Y$) and interest rates ($r$) where the money market clears."
    )

    tab_overview, tab_deep = st.tabs(["📚 Core Framework", "🔬 Microfoundations & Transmission"])

    with tab_overview:
        st.markdown(
            """
| Component | Analytical Form | Primary Determinants | Behavioral Rationale |
| :--- | :--- | :--- | :--- |
| **Real Money Demand ($L$)** | $L(Y, r) = kY - hr$ | Output ($Y$), Nominal Interest Rate ($r$) | Transactions & precautionary demand scale with income; speculative demand declines with interest rates (opportunity cost). |
| **Real Money Supply ($M/P$)** | $\\bar{M} / \\bar{P}$ | Nominal Money Stock ($M$), Price Level ($P$) | Exogenously set by the central bank and institutional reserve architecture in the short run. |
| **Equilibrium Condition** | $\\bar{M}/\\bar{P} = kY - hr$ | Asset market clearing | Interest rates adjust continuously to eliminate excess cash or bond demand. |
| **LM Equation** | $r = \\frac{k}{h}Y - \\frac{1}{h}\\left(\\frac{M}{P}\\right)$ | Slope $= k/h$, Shift $= -\\frac{1}{h}\\Delta(M/P)$ | Higher income raises transaction demand, requiring higher interest rates to choke off speculative balances and restore equilibrium. |
            """
        )

    with tab_deep:
        col_md, col_ms = st.columns(2, gap="medium")
        with col_md:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #38BDF8; margin: 0 0 0.5rem 0;">1. Keynesian Motives for Holding Money</h4>
    <p style="font-size: 0.9rem;">
        Money yields liquidity services rather than financial returns. The demand for real balances balances transaction needs against opportunity cost.
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li><b>Transactions Motive:</b> Cash held for day-to-day payments; scales positively with real output ($kY$).</li>
        <li><b>Precautionary Motive:</b> Safety margin against unexpected expenditures; scales with real output.</li>
        <li><b>Speculative Motive:</b> Inverse sensitivity to rate of return on alternative assets (bonds). Governed by $-hr$.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col_ms:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #FBBF24; margin: 0 0 0.5rem 0;">2. Policy Shocks & Curve Shifts</h4>
    <p style="font-size: 0.9rem;">
        The position and slope of the LM curve determine monetary policy potency:
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li><b>Expansionary Policy:</b> Central bank raises $M$ $\\rightarrow$ Excess liquidity drops $r$ at any given $Y$ $\\rightarrow$ <b>LM shifts right/down</b>.</li>
        <li><b>Price Surges ($P\\uparrow$):</b> Erodes real money balances $(M/P)\\downarrow$ $\\rightarrow$ <b>LM shifts left/up</b>.</li>
        <li><b>Liquidity Trap ($h \\to \\infty$):</b> Absolute elasticity at zero lower bound $\\rightarrow$ Flat LM curve; monetary policy cannot lower rates further.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.subheader("🛠️ Interactive Labs: Money Market Clearing & LM Derivation")

    lab_mode = st.radio(
        "Choose Lab Component:",
        [
            "1. Money Market Equilibrium: Rate Determination & Policy Shock",
            "2. LM Curve Constructor: Income Variation & Monetary Shift",
        ],
        horizontal=True,
    )

    if lab_mode == "1. Money Market Equilibrium: Rate Determination & Policy Shock":
        c_sim1, c_sim2 = st.columns([1, 1.2], gap="large")

        with c_sim1:
            st.markdown("#### Money Market Calibration")
            nominal_m = st.slider("Nominal Money Supply ($M$ in Billions):", 200.0, 1200.0, 600.0, 50.0)
            price_p = st.slider("Price Level Index ($P$):", 0.5, 3.0, 1.0, 0.1)
            real_income_y = st.slider("Real Aggregate Income ($Y$):", 1000.0, 4000.0, 2000.0, 100.0)
            k_param = st.slider("Transaction Sensitivity ($k$):", 0.1, 0.6, 0.35, 0.05)
            h_param = st.slider("Interest Rate Sensitivity ($h$):", 20.0, 150.0, 60.0, 5.0)

            # Mathematical derivations
            real_ms = nominal_m / price_p
            # Equilibrium: real_ms = k*Y - h*r  =>  h*r = k*Y - real_ms  => r = (k*Y - real_ms)/h
            eq_rate = (k_param * real_income_y - real_ms) / h_param
            eq_rate_clamped = max(eq_rate, 0.0)

            st.markdown("---")
            st.markdown("#### Stabilization Challenge")
            st.caption(
                "Adjust policy variables ($M$ or assume a targeted $Y$) to hit an **Equilibrium Policy Interest Rate between 3.0% and 5.0%** with a **Real Money Stock of at least 500 Billion**."
            )

            if st.button("Evaluate Equilibrium Target"):
                if 3.0 <= eq_rate <= 5.0 and real_ms >= 500.0:
                    st.session_state.market_points = 50
                    st.success(f"Equilibrium achieved! Target rate: {eq_rate:.2f}%, Real M/P: {real_ms:.1f}B (Awarded: 50/50 Pts)")
                else:
                    st.session_state.market_points = 25
                    st.warning(
                        f"Target missed: Equilibrium Rate is {eq_rate:.2f}% (Target: 3.0-5.0%) or Real Supply is {real_ms:.1f}B (Target: 500B+). (Awarded: 25/50 Pts)"
                    )
                st.rerun()

        with c_sim2:
            st.markdown("#### Money Market State & Allocations")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Real Money Supply (M/P)</div>
                        <div class="metric-val" style="color: {'#10B981' if real_ms >= 500 else '#38BDF8'} !important;">{real_ms:.1f}B</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m2:
                rate_color = "#10B981" if 3.0 <= eq_rate <= 5.0 else ("#F87171" if eq_rate < 0 else "#FBBF24")
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Equilibrium Interest Rate</div>
                        <div class="metric-val" style="color: {rate_color} !important;">{eq_rate:.2f}%</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m3:
                transaction_share = (k_param * real_income_y)
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Transaction Balances (k·Y)</div>
                        <div class="metric-val" style="color: #38BDF8 !important;">{transaction_share:.1f}B</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Generate Money Demand Curve across an interest rate spectrum
            rate_domain = np.linspace(0.5, 12.0, 50)
            demand_values = (k_param * real_income_y) - (h_param * rate_domain)

            chart_data = pd.DataFrame(
                {
                    "Interest Rate (%)": rate_domain,
                    "Real Money Demand (L)": demand_values,
                    "Real Money Supply (M/P)": np.full_like(rate_domain, real_ms),
                }
            ).set_index("Interest Rate (%)")

            st.line_chart(chart_data)
            st.caption(
                f"Equilibrium clearing point: r* = {eq_rate:.2f}%. Notice that if r < r*, there is excess demand for money, driving bond sales and pushing yields back up."
            )

    else:
        c_lm1, c_lm2 = st.columns([1, 1.2], gap="large")

        with c_lm1:
            st.markdown("#### LM Parameterization")
            nominal_m_lm = st.slider("Monetary Base ($M$):", 200.0, 1000.0, 500.0, 50.0, key="lm_m")
            p_lm = st.slider("Price Level ($P$):", 0.8, 2.0, 1.0, 0.1, key="lm_p")
            k_lm = st.slider("Transaction Coefficient ($k$):", 0.1, 0.5, 0.25, 0.05, key="lm_k")
            h_lm = st.slider("Speculative Sensitivity ($h$):", 20.0, 100.0, 50.0, 5.0, key="lm_h")

            real_balance = nominal_m_lm / p_lm
            lm_slope = k_lm / h_lm
            lm_intercept = -real_balance / h_lm

            st.markdown(
                f"""
                - **LM Slope ($k/h$):** `{lm_slope:.4f}`
                - **Horizontal Shift Factor:** `${real_balance:.1f}B$` real balances
                - **Equation:** $r = {lm_slope:.4f} \\cdot Y - {abs(lm_intercept):.2f}$
                """
            )
            st.caption(
                "A steeper LM curve reflects high sensitivity to income (k) or low sensitivity to interest rates (h), making monetary policy more influential over rates."
            )

        with c_lm2:
            st.markdown("#### The LM Curve in (Y, r) Space")
            y_domain = np.linspace(1000.0, 4000.0, 50)
            r_lm_baseline = (k_lm * y_domain - real_balance) / h_lm
            # Show a monetary expansion comparison (+20% Money Supply)
            r_lm_expanded = (k_lm * y_domain - (real_balance * 1.25)) / h_lm

            lm_chart_df = pd.DataFrame(
                {
                    "Aggregate Income (Y)": np.round(y_domain, 0),
                    "Baseline LM [r (%)]": np.round(r_lm_baseline, 2),
                    "Expanded Money Supply (+25%) [r (%)]": np.round(r_lm_expanded, 2),
                }
            ).set_index("Aggregate Income (Y)")

            st.line_chart(lm_chart_df)
            st.caption(
                "Notice: An increase in the money supply shifts the LM curve downwards/rightwards, reducing the interest rate associated with every level of income."
            )

# =====================================================================
# MODULE 2: ASSESSMENT
# =====================================================================
elif module == "📝 Module 2: Monetary Theory Assessment":
    st.markdown("### 📝 Money Market & LM Curve Knowledge Evaluation")
    st.markdown("Test your structural understanding of money demand, supply mechanics, and LM equilibrium shifts (10 points each).")

    with st.form("monetary_theory_quiz"):
        st.markdown("#### 1. Speculative Demand for Money")
        q1 = st.radio(
            "According to Keynesian liquidity preference, why does money demand decrease when interest rates rise?",
            [
                "A) The opportunity cost of holding non-interest-bearing cash balances increases, prompting shifts into bonds.",
                "B) Higher interest rates mechanically shrink the physical currency stock printed by the treasury.",
                "C) Households experience an immediate drop in aggregate disposable income.",
                "D) Commercial banks are legally prohibited from extending credit during high-rate regimes.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 2. Slope of the LM Curve")
        q2 = st.radio(
            "Under standard LM formulation ($r = \\frac{k}{h}Y - \\frac{M/P}{h}$), what makes the LM curve steeper?",
            [
                "A) An increase in interest rate sensitivity ($h$) or decrease in income sensitivity ($k$).",
                "B) A high income sensitivity of money demand ($k$) and a low interest responsiveness ($h$).",
                "C) A simultaneous doubling of the nominal money stock ($M$) and price index ($P$).",
                "D) The economy entering a classical liquidity trap where interest elasticity approaches infinity.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 3. Real Balances and Price Level Shocks")
        q3 = st.radio(
            "If the aggregate price level ($P$) increases while nominal money supply ($M$) remains fixed:",
            [
                "A) Real money supply increases, shifting the LM curve down and right.",
                "B) The LM curve remains unaffected because nominal balances are unchanged.",
                "C) Real money balances ($M/P$) decline, shifting the LM curve upward and leftward.",
                "D) Interest rates fall for any given level of real national income.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 4. The Liquidity Trap Dynamic")
        q4 = st.radio(
            "What characterizes the LM curve within a Keynesian Liquidity Trap?",
            [
                "A) It becomes vertical because money demand is completely unresponsive to output changes.",
                "B) It becomes completely horizontal at the nominal zero lower bound as speculative demand becomes infinitely interest-elastic.",
                "C) It shifts violently to the left whenever the central bank conducts open market purchases.",
                "D) The LM slope becomes infinite ($k/h \\to \\infty$).",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 5. Open Market Operations Transmission")
        q5 = st.radio(
            "When the Central Bank conducts an open market purchase of government securities:",
            [
                "A) It absorbs commercial bank reserves, lowering bank deposits and raising money market rates.",
                "B) It expands bank reserves and nominal money supply ($M$), shifting the LM curve to the right.",
                "C) The real transaction demand parameter ($k$) immediately resets to zero.",
                "D) The yield on bonds rises immediately to eliminate money market excess liquidity.",
            ],
            index=None,
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Grade")

        if submit_quiz:
            correct_keys = {
                "q1": "A) The opportunity cost of holding non-interest-bearing cash balances increases, prompting shifts into bonds.",
                "q2": "B) A high income sensitivity of money demand ($k$) and a low interest responsiveness ($h$).",
                "q3": "C) Real money balances ($M/P$) decline, shifting the LM curve upward and leftward.",
                "q4": "B) It becomes completely horizontal at the nominal zero lower bound as speculative demand becomes infinitely interest-elastic.",
                "q5": "B) It expands bank reserves and nominal money supply ($M$), shifting the LM curve to the right.",
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
            st.error("Q1 Review: Interest is the opportunity cost of holding cash. When $r$ rises, holding zero-interest money becomes costlier, decreasing cash demand in favor of bonds.")
        if not rec.get("q2", False):
            st.error("Q2 Review: Slope equals $k/h$. A larger $k$ (large transaction demand per unit of $Y$) or smaller $h$ (weak rate responsiveness) steepens the LM curve.")
        if not rec.get("q3", False):
            st.error("Q3 Review: Higher $P$ reduces real balances $M/P$. At any income level, less real cash is available, requiring higher interest rates to balance the market (LM shifts left/up).")
        if not rec.get("q4", False):
            st.error("Q4 Review: In a liquidity trap, investors are indifferent between bonds and cash ($h \\to \\infty$). The LM curve flattens completely horizontally at low rates.")
        if not rec.get("q5", False):
            st.error("Q5 Review: Central bank bond purchases inject high-powered money into the banking sector, expanding $M$ and shifting LM rightward.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("Macroeconomic Architecture Lab")
with f2:
    st.caption("Liquidity Preference & LM Equilibrium Dynamics")
with f3:
    st.caption(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
