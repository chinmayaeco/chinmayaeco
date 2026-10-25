from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Macro & Financial Markets Lab: IS-LM & Liquidity Dynamics",
    page_icon="🏛️",
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

    /* Force all headings and general text to remain high-contrast */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #F8FAFC !important;
    }
    
    /* Streamlit widget labels & captions */
    .stMarkdown, .stText, [data-testid="stWidgetLabel"] p {
        color: #F1F5F9 !important;
        font-weight: 500 !important;
    }
    
    .stCaption, [data-testid="stCaptionContainer"] p {
        color: #CBD5E1 !important;
        font-size: 0.88rem !important;
    }

    /* Score banner */
    .score-banner {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.2) 0%, rgba(14, 165, 233, 0.2) 100%);
        border: 1px solid rgba(245, 158, 11, 0.45);
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
    }
    
    /* Metric Cards */
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
    
    /* High-contrast Radio Buttons and Inputs */
    div[data-testid="stRadio"] > div {
        background-color: rgba(15, 23, 42, 0.6);
        padding: 0.8rem;
        border-radius: 8px;
        border: 1px solid rgba(148, 163, 184, 0.25);
    }

    div[data-testid="stRadio"] label span {
        color: #F8FAFC !important;
    }
    
    /* Sliders styling */
    .stSlider [data-baseweb="slider"] {
        color: #38BDF8 !important;
    }

    /* Buttons */
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
if "sim_points" not in st.session_state:
    st.session_state.sim_points = 0
if "sim_completed" not in st.session_state:
    st.session_state.sim_completed = False
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "eval_records" not in st.session_state:
    st.session_state.eval_records = {}

total_final_score = st.session_state.sim_points + st.session_state.quiz_score

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("## 🏛️ Macro & Finance Lab")
    module = st.radio(
        "Select Learning Module:",
        [
            "📈 Module 1: Money & Bond Markets Equilibrium",
            "⚖️ Module 2: The IS-LM Macro Framework",
            "📝 Module 3: Macro-Financial Assessment",
        ],
    )
    st.markdown("---")
    st.markdown("### 🏆 Performance Tracker")
    st.markdown(f"**Interactive Labs:** {st.session_state.sim_points} / 50")
    st.markdown(f"**MCQ Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Aggregate Score:** {total_final_score} / 100")
    
    if total_final_score == 100:
        st.success("🌟 Master of Macro-Finance Achieved!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(
    f"""
<div class="score-banner">
    <h2 style="color: #FBBF24; margin: 0; font-weight: 800;">Macroeconomics & Financial Markets Suite: {total_final_score} / 100</h2>
    <p style="color: #E2E8F0; margin: 0.35rem 0 0 0; font-size: 1rem;">
        Simulation Labs: <b>{st.session_state.sim_points}/50 Pts</b> | Conceptual Assessment: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# MODULE 1: MONEY & BOND MARKETS
# =====================================================================
if module == "📈 Module 1: Money & Bond Markets Equilibrium":
    st.markdown("### 📈 Liquidity Preference, Money Supply & Bond Prices")
    st.markdown(
        r"""
        The money market and the bond market are dual reflections of household portfolio decisions. 
        According to Keynesian theory, total wealth $W$ is split between cash balances and bonds:
        
        $$\frac{M}{P} + B^s = L(Y, r) + B^d$$
        
        When real money supply $\frac{M}{P}$ exceeds money demand $L(Y, r)$, agents purchase bonds, driving bond prices up and interest rates down until:
        $$r^* = \frac{k \cdot Y - \frac{M}{P}}{h}$$
        """
    )

    c1, c2 = st.columns([1, 1.2], gap="large")

    with c1:
        st.subheader("🛠️ Monetary Levers")

        m_nominal = st.slider(
            "1. Nominal Money Supply (M):",
            min_value=400.0,
            max_value=2000.0,
            value=1000.0,
            step=50.0,
            help="Monetary base injected via Central Bank Open Market Operations.",
        )

        p_level = st.slider(
            "2. Price Level Index (P):",
            min_value=1.0,
            max_value=3.0,
            value=1.5,
            step=0.1,
            help="Aggregate price level determining the purchasing power of nominal balances.",
        )

        y_income = st.slider(
            "3. National Real Output (Y):",
            min_value=1000.0,
            max_value=3000.0,
            value=1800.0,
            step=50.0,
            help="Total output determining transaction liquidity demand.",
        )

        h_sensitivity = st.slider(
            "4. Speculative Sensitivity (h):",
            min_value=20.0,
            max_value=120.0,
            value=60.0,
            step=5.0,
            help="Degree to which investors shift between bonds and cash when interest rates change.",
        )

        k_sensitivity = 0.50
        real_money_supply = m_nominal / p_level
        transaction_demand = k_sensitivity * y_income
        r_eq = max(0.1, (transaction_demand - real_money_supply) / h_sensitivity)

        # Theoretical Perpetuity Bond Price: P_bond = Coupon / r
        annual_coupon = 50.0
        bond_price = (annual_coupon / (r_eq / 100))

        st.markdown("---")
        st.markdown("#### 🎯 Monetary Policy Objective")
        st.caption("Calibrate money supply to target a benchmark interest rate between **3.5%** and **5.5%**.")

        if st.button("Submit Portfolio Calibration"):
            if 3.5 <= r_eq <= 5.5:
                st.session_state.sim_points = 50
                st.session_state.sim_completed = True
                st.success(f"🎯 Target rate achieved at r* = {r_eq:.2f}%! (Awarded: 50/50 Pts)")
            else:
                st.session_state.sim_points = 25
                st.session_state.sim_completed = True
                st.warning(f"⚠️ Policy rate at {r_eq:.2f}% is outside the 3.5% - 5.5% corridor. (Awarded: 25/50 Pts)")
            st.rerun()

    with c2:
        st.subheader("📊 Financial Asset Clearings")

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(
                f"""
                <div class="metric-panel">
                    <div class="metric-title">Real Balances (M/P)</div>
                    <div class="metric-val">{real_money_supply:.1f}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with m2:
            st.markdown(
                f"""
                <div class="metric-panel">
                    <div class="metric-title">Equilibrium Yield (r*)</div>
                    <div class="metric-val" style="color: {'#10B981' if 3.5 <= r_eq <= 5.5 else '#F87171'} !important;">{r_eq:.2f}%</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with m3:
            st.markdown(
                f"""
                <div class="metric-panel">
                    <div class="metric-title">Consol Bond Price</div>
                    <div class="metric-val" style="color: #FBBF24 !important;">${bond_price:.1f}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Plot Money Demand Curve vs Supply Line
        r_axis = np.linspace(0.5, 12.0, 40)
        money_demand_curve = transaction_demand - (h_sensitivity * r_axis)

        chart_df = pd.DataFrame({
            "Policy Interest Rate (r %)": np.round(r_axis, 2),
            "Money Demand L(Y,r)": np.round(money_demand_curve, 1),
            "Real Supply M/P": np.round(np.full_like(r_axis, real_money_supply), 1),
        }).set_index("Policy Interest Rate (r %)")

        st.line_chart(chart_df)
        st.caption(f"📌 Equilibrium clearing: Real Cash Stock = {real_money_supply:.1f} | Benchmark Bond Price = ${bond_price:.2f}")

# =====================================================================
# MODULE 2: JOINT IS-LM FRAMEWORK
# =====================================================================
elif module == "⚖️ Module 2: The IS-LM Macro Framework":
    st.markdown("### ⚖️ General Macroeconomic Equilibrium: IS-LM Synthesis")
    st.markdown(
        r"""
        The **IS-LM Model** links the goods market (real economy) with the money market (financial economy):
        - **IS Schedule (Goods Market Equilibrium):** $Y = C(Y - T) + I(r) + G$
        - **LM Schedule (Money Market Equilibrium):** $\frac{M}{P} = kY - hr$
        """
    )

    col_is, col_lm = st.columns(2, gap="large")

    with col_is:
        st.markdown("#### 🏛️ Goods Market Parameters (IS Curve)")
        gov_g = st.slider("Government Spending (G):", 100.0, 600.0, 300.0, 25.0)
        taxes_t = st.slider("Lump-Sum Taxes (T):", 50.0, 400.0, 200.0, 25.0)
        c_mpc = 0.75   # Marginal Propensity to Consume
        i_sens = 30.0  # Investment interest sensitivity (b)
        a_autonomous_c = 150.0
        i_autonomous = 200.0

    with col_lm:
        st.markdown("#### 🏦 Financial Market Parameters (LM Curve)")
        mon_supply_m = st.slider("Nominal Money Supply (M):", 400.0, 1600.0, 900.0, 50.0)
        p_idx = st.slider("Price Level (P):", 1.0, 2.5, 1.5, 0.1)
        k_income_sens = 0.50
        h_spec_sens = 40.0

    # Macroeconomic Algebraic Solution
    # IS: Y = (1 / (1 - c)) * [c_0 - c*T + I_0 - b*r + G]
    # Let Autonomous Expenditure A = c_0 - c*T + I_0 + G
    # IS Equation: Y = alpha * (A - b*r) => r = (A / b) - (Y / (alpha * b))
    # LM Equation: r = (k/h)*Y - (M/P)/h

    alpha = 1.0 / (1.0 - c_mpc)
    autonomous_exp = a_autonomous_c - (c_mpc * taxes_t) + i_autonomous + gov_g
    real_m = mon_supply_m / p_idx

    # Simultaneous Solution:
    # (k/h)*Y - (M/P)/h = (A/i_sens) - Y / (alpha * i_sens)
    # Y * [ (k/h) + 1/(alpha * i_sens) ] = (A / i_sens) + (real_m / h)
    y_mult = (k_income_sens / h_spec_sens) + (1.0 / (alpha * i_sens))
    rhs = (autonomous_exp / i_sens) + (real_m / h_spec_sens)

    y_star = rhs / y_mult
    r_star = (k_income_sens / h_spec_sens) * y_star - (real_m / h_spec_sens)

    st.markdown("---")
    st.subheader("📊 Macroeconomic Equilibrium Coordinates")

    ec1, ec2, ec3 = st.columns(3)
    with ec1:
        st.markdown(
            f"""
            <div class="metric-panel">
                <div class="metric-title">Equilibrium Output (Y*)</div>
                <div class="metric-val">{y_star:.1f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with ec2:
        st.markdown(
            f"""
            <div class="metric-panel">
                <div class="metric-title">Equilibrium Interest Rate (r*)</div>
                <div class="metric-val" style="color: #10B981 !important;">{r_star:.2f}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with ec3:
        st.markdown(
            f"""
            <div class="metric-panel">
                <div class="metric-title">Fiscal Multiplier (Alpha)</div>
                <div class="metric-val" style="color: #FBBF24 !important;">{alpha:.2f}x</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Plot IS-LM Crossing
    y_vals = np.linspace(1000.0, 3200.0, 40)
    r_is = (autonomous_exp / i_sens) - (y_vals / (alpha * i_sens))
    r_lm = (k_income_sens / h_spec_sens) * y_vals - (real_m / h_spec_sens)

    is_lm_df = pd.DataFrame({
        "Output (Y)": np.round(y_vals, 0),
        "IS Curve (Goods Equilibrium)": np.round(r_is, 2),
        "LM Curve (Money Equilibrium)": np.round(r_lm, 2),
    }).set_index("Output (Y)")

    st.line_chart(is_lm_df)
    st.caption("📈 The intersection represents simultaneous clearing in both the goods and money markets.")

# =====================================================================
# MODULE 3: MACRO-FINANCIAL ASSESSMENT
# =====================================================================
elif module == "📝 Module 3: Macro-Financial Assessment":
    st.markdown("### 📝 Macroeconomics & Financial Markets Evaluation")
    st.markdown("Test your structural understanding of asset pricing, central banking, and the IS-LM framework (10 points each).")

    with st.form("macro_finance_quiz"):
        st.markdown("#### 1. Dual Clearing in Bond and Money Markets")
        q1 = st.radio(
            "When the central bank performs an Open Market Purchase of Treasury securities:",
            [
                "A) The money supply contracts, causing bond prices to collapse.",
                "B) Bank reserves rise, bond prices increase, and the equilibrium interest rate falls.",
                "C) The LM curve shifts left, increasing the borrowing cost for private firms.",
                "D) Velocity becomes negative, nullifying the money multiplier.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 2. Fiscal Policy & Financial Crowding-Out")
        q2 = st.radio(
            "Under the IS-LM model, an increase in government deficit spending financed by debt typically causes:",
            [
                "A) The IS curve to shift right, raising both income and interest rates, which dampens private investment.",
                "B) The LM curve to shift left, lowering bond yields.",
                "C) An immediate reduction in aggregate transaction demand for money.",
                "D) Complete neutralization of price levels without any changes in real output.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 3. Slope of the LM Curve and Monetary Transmission")
        q3 = st.radio(
            "When speculative money demand is virtually unresponsive to interest rates (Classical Case, h -> 0):",
            [
                "A) The LM curve is horizontal, making fiscal policy maximally effective.",
                "B) The LM curve is vertical, making monetary policy potent and fiscal policy subject to complete crowding out.",
                "C) Interest rates are pinned at the zero lower bound indefinitely.",
                "D) Bond prices decouple entirely from prevailing interest rates.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 4. The Liquidity Trap & Bond Pricing")
        q4 = st.radio(
            "In a Keynesian Liquidity Trap (interest rates near zero and h approaching infinity):",
            [
                "A) Bond prices are at cyclical lows, and agents anticipate large capital gains.",
                "B) Further injections of liquidity are hoarded as cash; monetary expansion fails to lower interest rates further.",
                "C) The IS curve becomes vertical, rendering fiscal policy completely impotent.",
                "D) The central bank loses control over nominal reserve creation.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 5. Financial Yield Curve Shifts")
        q5 = st.radio(
            "If aggregate prices (P) surge unexpectedly while the nominal money stock is kept rigid:",
            [
                "A) Real money balances (M/P) drop, shifting LM to the left and pushing market interest rates higher.",
                "B) Real money balances expand, boosting corporate bond valuations.",
                "C) The IS curve shifts downward by the full magnitude of the price hike.",
                "D) Transaction demand drops to zero as agents substitute entirely into physical goods.",
            ],
            index=None,
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Grade")

        if submit_quiz:
            correct_keys = {
                "q1": "B) Bank reserves rise, bond prices increase, and the equilibrium interest rate falls.",
                "q2": "A) The IS curve to shift right, raising both income and interest rates, which dampens private investment.",
                "q3": "B) The LM curve is vertical, making monetary policy potent and fiscal policy subject to complete crowding out.",
                "q4": "B) Further injections of liquidity are hoarded as cash; monetary expansion fails to lower interest rates further.",
                "q5": "A) Real money balances (M/P) drop, shifting LM to the left and pushing market interest rates higher.",
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
            st.error("❌ **Q1 Review:** Open market purchases inject reserves, boosting bond prices ($P_{bond} \\uparrow$) and lowering yields ($r \\downarrow$).")
        if not rec.get("q2", False):
            st.error("❌ **Q2 Review:** Higher government spending ($G \\uparrow$) shifts IS rightward. Increased transaction demand drives up interest rates, partially crowding out interest-sensitive private investment ($I(r)$).")
        if not rec.get("q3", False):
            st.error("❌ **Q3 Review:** When $h \\to 0$, $LM$ is vertical. Monetary policy controls output directly, and fiscal expansions simply crowd out equal amounts of private expenditure.")
        if not rec.get("q4", False):
            st.error("❌ **Q4 Review:** In a liquidity trap, money demand is perfectly elastic with respect to the interest rate ($h \\to \\infty$), meaning cash and short-term debt become perfect substitutes.")
        if not rec.get("q5", False):
            st.error("❌ **Q5 Review:** Higher prices deflate real balances $M/P$, causing households to sell bonds for liquidity, which depresses bond prices and drives interest rates up (LM shifts left).")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("🏛️ Macro-Financial Analytics Lab")
with f2:
    st.caption("⚡ Asset Pricing, Money Market Clearing & IS-LM Dynamics")
with f3:
    st.caption(f"⏰ System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
