from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Financial Asset Valuation: Bonds, DDM & CAPM",
    page_icon="📊",
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
    st.markdown("## 📊 Asset Valuation Lab")
    module = st.radio(
        "Select Learning Module:",
        [
            "🏛️ Module 1: Fixed Income, DDM & CAPM Analytics",
            "📝 Module 2: Valuation Theory Assessment",
        ],
    )
    st.markdown("---")
    st.markdown("### 🏆 Performance Tracker")
    st.markdown(f"**Interactive Lab:** {st.session_state.lab_points} / 50")
    st.markdown(f"**Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Aggregate Score:** {total_final_score} / 100")

    if total_final_score == 100:
        st.success("🌟 Certified Valuation & Asset Pricing Specialist!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(
    f"""
<div class="score-banner">
    <h2 style="color: #FBBF24; margin: 0; font-weight: 800;">Asset Pricing & Valuation Suite: {total_final_score} / 100</h2>
    <p style="color: #E2E8F0; margin: 0.35rem 0 0 0; font-size: 1rem;">
        Simulation Lab: <b>{st.session_state.lab_points}/50 Pts</b> | Conceptual Assessment: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# MODULE 1: VALUATION SIMULATION LAB
# =====================================================================
if module == "🏛️ Module 1: Fixed Income, DDM & CAPM Analytics":
    st.markdown("### 🏛️ Intrinsic Valuation: Bond Pricing, Equity DDM, and CAPM Hurdle Rates")
    st.markdown(
        "Asset valuation discounts expected future cash flows using an appropriate risk-adjusted rate. "
        "The **Capital Asset Pricing Model (CAPM)** formalizes systematic risk to establish required equity returns ($r_e$), "
        "which subsequently parameterize discounted cash flow structures like the **Gordon Growth Model (DDM)**."
    )

    tab_overview, tab_deep = st.tabs(["📚 Core Framework", "🔬 Mathematical Foundations"])

    with tab_overview:
        st.markdown(
            """
| Model | Closed-Form Expression | Core Variables | Underlying Economic Principle |
| :--- | :--- | :--- | :--- |
| **Bond Pricing** | $P_0 = \\sum_{t=1}^n \\frac{C}{(1+y)^t} + \\frac{M}{(1+y)^n}$ | Coupon ($C$), Face Value ($M$), YTM ($y$), Maturity ($n$) | Present value of deterministic contractual cash flows; inverse convex price-yield relationship. |
| **CAPM Cost of Equity** | $\\mathbb{E}[R_i] = R_f + \\beta_i \\left(\\mathbb{E}[R_m] - R_f\\right)$ | Risk-Free Rate ($R_f$), Beta ($\\beta$), Market Premium ($ERP$) | Only non-diversifiable systematic risk receives compensation in equilibrium. |
| **Gordon Growth DDM** | $P_0 = \\frac{D_1}{r_e - g} = \\frac{D_0 (1+g)}{r_e - g}$ | Expected Dividend ($D_1$), Discount Rate ($r_e$), Growth ($g$) | Infinite-horizon stream of perpetual dividends expanding at a steady long-term rate ($r_e > g$). |
| **Multi-Stage DDM** | $P_0 = \\sum_{t=1}^T \\frac{D_t}{(1+r_e)^t} + \\frac{P_T}{(1+r_e)^T}$ | High Growth ($g_s$), Stable Growth ($g_n$), Horizon ($T$) | Accommodates competitive life-cycle decay from supernormal expansion into steady state. |
            """
        )

    with tab_deep:
        col_m1, col_m2 = st.columns(2, gap="medium")
        with col_m1:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #38BDF8; margin: 0 0 0.5rem 0;">1. Duration & Convexity Mechanics</h4>
    <p style="font-size: 0.9rem;">
        Bonds trade at a premium when the coupon rate exceeds yield-to-maturity (YTM) and at a discount when YTM exceeds the coupon.
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li><b>Modified Duration ($D^*$):</b> Measures the percentage price sensitivity relative to shifts in yield: $D^* = -\\frac{1}{P} \\frac{dP}{dy}$.</li>
        <li><b>Convexity:</b> Accounts for the curvature of the price-yield function, cushioning losses during rising rates and enhancing gains when yields decline.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col_m2:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #FBBF24; margin: 0 0 0.5rem 0;">2. The Security Market Line (SML) & DDM Convergence</h4>
    <p style="font-size: 0.9rem;">
        CAPM maps systematic covariance ($\\beta = \\frac{\\text{Cov}(R_i, R_m)}{\\sigma_m^2}$) onto the Security Market Line:
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li><b>Alpha Generation ($\\alpha$):</b> Stocks plotted above the SML are underpriced; those below are overpriced.</li>
        <li><b>Terminal Rate Constraint:</b> In the Gordon model, $g$ must strictly stay below the economy's nominal GDP growth and hurdle rate $r_e$. If $g \\ge r_e$, the model destabilizes mathematically.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.subheader("🛠️ Interactive Labs: Asset Pricing & Sensitivity Engines")

    lab_mode = st.radio(
        "Choose Lab Component:",
        [
            "1. Bond Pricing Engine: Yield Curve & Sensitivity Dynamics",
            "2. Integrated Equity Lab: CAPM Hurdle & Gordon Growth Valuation",
        ],
        horizontal=True,
    )

    if lab_mode == "1. Bond Pricing Engine: Yield Curve & Sensitivity Dynamics":
        c_bond1, c_bond2 = st.columns([1, 1.2], gap="large")

        with c_bond1:
            st.markdown("#### Bond Specification")
            face_val = st.slider("Face Value ($M$ in $):", 500.0, 5000.0, 1000.0, 100.0)
            coupon_rate = st.slider("Annual Coupon Rate (%):", 0.0, 15.0, 6.0, 0.25) / 100.0
            years_to_mat = st.slider("Years to Maturity ($n$):", 1, 30, 10, 1)
            ytm = st.slider("Yield to Maturity (YTM %):", 0.5, 18.0, 5.0, 0.25) / 100.0

            annual_coupon = face_val * coupon_rate
            periods = np.arange(1, years_to_mat + 1)
            discount_factors = (1.0 + ytm) ** periods
            pv_coupons = np.sum(annual_coupon / discount_factors)
            pv_face = face_val / ((1.0 + ytm) ** years_to_mat)
            bond_price = pv_coupons + pv_face

            # Macaulay Duration & Modified Duration
            pv_cf = (annual_coupon / discount_factors)
            pv_cf[-1] += pv_face
            mac_duration = np.sum(periods * pv_cf) / bond_price
            mod_duration = mac_duration / (1.0 + ytm)

            st.markdown("---")
            st.markdown("#### Target Pricing Challenge")
            st.caption(
                "Adjust terms to construct a **Discount Bond priced between $800 and $900** with a **Modified Duration of at least 6.5 years**."
            )

            if st.button("Evaluate Bond Constraints"):
                if 800.0 <= bond_price <= 900.0 and mod_duration >= 6.5:
                    st.session_state.lab_points = 50
                    st.success(f"Target matched! Price: ${bond_price:.2f}, Mod Duration: {mod_duration:.2f} yrs (Awarded: 50/50 Pts)")
                else:
                    st.session_state.lab_points = 25
                    st.warning(
                        f"Target missed: Bond Price is ${bond_price:.2f} (Target: $800-$900) or Mod Duration is {mod_duration:.2f} yrs (Target: 6.5+ yrs). (Awarded: 25/50 Pts)"
                    )
                st.rerun()

        with c_bond2:
            st.markdown("#### Valuation & Sensitivity Metrics")
            m1, m2, m3 = st.columns(3)
            with m1:
                p_status = "PAR" if abs(bond_price - face_val) < 0.5 else ("PREMIUM" if bond_price > face_val else "DISCOUNT")
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Price ({p_status})</div>
                        <div class="metric-val" style="color: {'#10B981' if 800 <= bond_price <= 900 else '#38BDF8'} !important;">${bond_price:.2f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m2:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Modified Duration</div>
                        <div class="metric-val" style="color: {'#10B981' if mod_duration >= 6.5 else '#FBBF24'} !important;">{mod_duration:.2f} yrs</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m3:
                dollar_duration = (mod_duration * bond_price) / 100.0
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">DV01 (1bp Shift)</div>
                        <div class="metric-val" style="color: #38BDF8 !important;">${dollar_duration / 100.0:.3f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Convex Price-Yield Curve
            ytm_domain = np.linspace(0.01, 0.18, 50)
            price_curve = [
                np.sum((face_val * coupon_rate) / ((1.0 + y) ** periods)) + (face_val / ((1.0 + y) ** years_to_mat))
                for y in ytm_domain
            ]

            chart_data = pd.DataFrame(
                {
                    "Yield to Maturity (%)": np.round(ytm_domain * 100, 2),
                    "Theoretical Bond Price ($)": np.round(price_curve, 2),
                }
            ).set_index("Yield to Maturity (%)")

            st.line_chart(chart_data)
            st.caption(
                f"Current Market Position: Yield = {ytm*100:.2f}%, Price = ${bond_price:.2f}. "
                "Notice the upward curvature (convexity), demonstrating that prices gain more when rates drop than they lose when rates rise by equal magnitude."
            )

    else:
        c_eq1, c_eq2 = st.columns([1, 1.2], gap="large")

        with c_eq1:
            st.markdown("#### CAPM Parameters")
            rf_rate = st.slider("Risk-Free Rate ($R_f$ %):", 1.0, 7.0, 4.0, 0.25) / 100.0
            beta_val = st.slider("Equity Systematic Risk (Beta $\\beta$):", 0.2, 2.5, 1.15, 0.05)
            market_risk_prem = st.slider("Market Risk Premium ($E[R_m] - R_f$ %):", 3.0, 10.0, 5.5, 0.25) / 100.0

            # Hurdle rate via CAPM
            cost_of_equity = rf_rate + (beta_val * market_risk_prem)

            st.markdown("#### Dividend Growth (DDM) Setup")
            last_div = st.slider("Current Annual Dividend ($D_0$ in $):", 0.5, 20.0, 3.50, 0.25)
            div_growth = st.slider("Constant Dividend Growth ($g$ %):", 0.5, 12.0, 3.5, 0.25) / 100.0

            st.markdown("---")
            if div_growth >= cost_of_equity:
                st.error("Constraint Violation: $g \\ge r_e$. The Gordon Growth model diverges when dividend growth equals or exceeds the cost of equity.")
                fair_stock_price = np.nan
            else:
                next_div = last_div * (1.0 + div_growth)
                fair_stock_price = next_div / (cost_of_equity - div_growth)
                st.markdown(
                    f"""
                    - **CAPM Hurdle Rate ($r_e$):** `{cost_of_equity*100:.2f}%`
                    - **Expected Next Dividend ($D_1$):** `${next_div:.2f}$`
                    - **Intrinsic Target Price:** `${fair_stock_price:.2f}$`
                    """
                )

            st.caption(
                "According to CAPM, high-beta equities demand a higher cost of equity, which penalizes the discounted present value of expected cash flows."
            )

        with c_eq2:
            st.markdown("#### Security Market Line (SML) & Risk Positioning")
            beta_domain = np.linspace(0.0, 2.5, 50)
            sml_returns = (rf_rate + (beta_domain * market_risk_prem)) * 100

            sml_chart_df = pd.DataFrame(
                {
                    "Systematic Beta": np.round(beta_domain, 2),
                    "Expected Return / Hurdle Rate (%)": np.round(sml_returns, 2),
                }
            ).set_index("Systematic Beta")

            st.line_chart(sml_chart_df)
            st.caption(
                f"Asset Placement: At $\\beta = {beta_val:.2f}$, the expected equity return is {cost_of_equity*100:.2f}%. "
                "Any investment yielding below this threshold destroys shareholder value relative to systematic market risk."
            )

            st.markdown("#### Dividend Growth vs. Fair Value Horizon")
            valid_g = np.linspace(0.01, min(cost_of_equity - 0.005, 0.10), 30)
            val_curve = [(last_div * (1.0 + g)) / (cost_of_equity - g) for g in valid_g]

            ddm_chart_df = pd.DataFrame(
                {
                    "Growth Rate (%)": np.round(valid_g * 100, 2),
                    "Implied Intrinsic Stock Value ($)": np.round(val_curve, 2),
                }
            ).set_index("Growth Rate (%)")

            st.line_chart(ddm_chart_df)
            st.caption(
                "As the perpetual growth rate approaches the required rate of return, intrinsic valuation exhibits asymptotic sensitivity."
            )

# =====================================================================
# MODULE 2: VALUATION & PRICING ASSESSMENT
# =====================================================================
elif module == "📝 Module 2: Valuation Theory Assessment":
    st.markdown("### 📝 Asset Pricing, Fixed Income & Equity Assessment")
    st.markdown("Test your mastery of bond analytics, duration dynamics, Gordon growth constraints, and CAPM mechanics (10 points each).")

    with st.form("valuation_theory_quiz"):
        st.markdown("#### 1. Price-Yield Relationship and Convexity")
        q1 = st.radio(
            "Due to the convexity of conventional fixed-rate coupon bonds, when market yields shift by equal increments:",
            [
                "A) Price appreciation resulting from a 100 bp rate decrease exceeds price depreciation from a 100 bp rate increase.",
                "B) Price depreciation resulting from a 100 bp rate decrease exceeds price appreciation from a 100 bp rate increase.",
                "C) The modified duration shifts linearly, leaving percentage price changes perfectly symmetric.",
                "D) Bond prices only alter if the coupon rate itself adjusts dynamically with market yields.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 2. Modified Duration Interpretation")
        q2 = st.radio(
            "If an investment-grade corporate bond possesses a Modified Duration of 7.2 years and market yields fall by 50 basis points (0.50%):",
            [
                "A) The bond's price will fall by approximately 7.20%.",
                "B) The bond's price will rise by approximately 3.60%.",
                "C) The bond's annual coupon distribution expands by 3.60%.",
                "D) The maturity of the bond contracts by exactly 0.50 years.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 3. Capital Asset Pricing Model (CAPM) Assumptions")
        q3 = st.radio(
            "According to the CAPM framework, why does the market portfolio only compensate investors for systematic risk (Beta) and not unsystematic risk?",
            [
                "A) Unsystematic risk is unquantifiable by institutional investors.",
                "B) Regulators mandate that all equities maintain identical idiosyncratic risk profiles.",
                "C) Unsystematic risk can be eliminated costlessly through proper portfolio diversification.",
                "D) High beta assets are legally guaranteed higher cash dividends.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 4. Gordon Growth Model Mathematical Limits")
        q4 = st.radio(
            "What happens analytically within the constant dividend growth model ($P_0 = \\frac{D_1}{r_e - g}$) if perpetual growth ($g$) equals the discount rate ($r_e$)?",
            [
                "A) The equity price approaches zero because future cash flows are rendered worthless.",
                "B) The formula becomes mathematically undefined (division by zero), implying infinite valuation as growth matches capital cost.",
                "C) The valuation defaults to the current book value of shareholders' equity.",
                "D) The cost of equity resets to the risk-free rate of return.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 5. Security Market Line (SML) Disequilibrium")
        q5 = st.radio(
            "An analyst calculates that a stock with $\\beta = 1.2$ offers an expected return of 14%, while CAPM projects a required return of 11%. How should this asset be classified?",
            [
                "A) Overpriced with negative alpha ($\\alpha = -3\\%$); it plots below the SML.",
                "B) Underpriced with positive alpha ($\\alpha = +3\\%$); it plots above the SML.",
                "C) In equilibrium; beta compensates for the difference via arbitrage.",
                "D) Distressed; because its hurdle rate is lower than the expected return.",
            ],
            index=None,
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Grade")

        if submit_quiz:
            correct_keys = {
                "q1": "A) Price appreciation resulting from a 100 bp rate decrease exceeds price depreciation from a 100 bp rate increase.",
                "q2": "B) The bond's price will rise by approximately 3.60%.",
                "q3": "C) Unsystematic risk can be eliminated costlessly through proper portfolio diversification.",
                "q4": "B) The formula becomes mathematically undefined (division by zero), implying infinite valuation as growth matches capital cost.",
                "q5": "B) Underpriced with positive alpha ($\\alpha = +3\\%$); it plots above the SML.",
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
            st.error("Q1 Review: Convexity creates an asymmetric return profile: bond prices gain more when market yields decline than they lose when yields rise by an equal amount.")
        if not rec.get("q2", False):
            st.error("Q2 Review: $\\Delta P/P \\approx -D^* \\times \\Delta y = -7.2 \\times (-0.0050) = +0.036$ or $+3.60\\%$. Falling yields boost bond prices.")
        if not rec.get("q3", False):
            st.error("Q3 Review: Investors can diversify idiosyncratic firm-specific risks across large portfolios. Therefore, the market only prices non-diversifiable systematic risk (Beta).")
        if not rec.get("q4", False):
            st.error("Q4 Review: If $g \\ge r_e$, the denominator becomes zero or negative, breaking the convergence of the infinite geometric series of discounted dividends.")
        if not rec.get("q5", False):
            st.error("Q5 Review: When expected return exceeds required return ($14\\% > 11\\%$, $\\alpha = +3\\%$), the stock trades at an attractive discount (underpriced) and plots above the SML.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("Quantitative Asset Valuation Suite")
with f2:
    st.caption("Fixed Income, DDM & CAPM Capital Markets Analytics")
with f3:
    st.caption(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
