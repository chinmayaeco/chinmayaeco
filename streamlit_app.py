from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Macro & Financial Markets Lab: Capital, Money & Equilibrium Dynamics",
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
    
    /* Concept Info Cards */
    .concept-card {
        background: rgba(15, 23, 42, 0.65);
        border-left: 4px solid #38BDF8;
        border-radius: 0 8px 8px 0;
        padding: 1rem;
        margin-bottom: 1rem;
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
if "market_points" not in st.session_state:
    st.session_state.market_points = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "eval_records" not in st.session_state:
    st.session_state.eval_records = {}

total_final_score = (
    st.session_state.sim_points
    + st.session_state.market_points
    + st.session_state.quiz_score
)

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("## 🏛️ Financial Architecture Lab")
    module = st.radio(
        "Select Learning Module:",
        [
            "🏢 Module 1: Financial Markets (Primary & Secondary)",
            "📈 Module 2: Money & Bond Markets Equilibrium",
            "⚖️ Module 3: The IS-LM Macro Framework",
            "📝 Module 4: Integrated Macro-Finance Assessment",
        ],
    )
    st.markdown("---")
    st.markdown("### 🏆 Performance Tracker")
    st.markdown(f"**Market Structure Lab:** {st.session_state.market_points} / 25")
    st.markdown(f"**Monetary Labs:** {st.session_state.sim_points} / 25")
    st.markdown(f"**Evaluation Quiz:** {st.session_state.quiz_score} / 50")
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
        Primary/Secondary Lab: <b>{st.session_state.market_points}/25 Pts</b> | Monetary Lab: <b>{st.session_state.sim_points}/25 Pts</b> | Conceptual Assessment: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# MODULE 1: FINANCIAL MARKETS, PRIMARY & SECONDARY
# =====================================================================
if module == "🏢 Module 1: Financial Markets (Primary & Secondary)":
    st.markdown("### 🏢 Financial Markets Architecture: Capital Allocation & Liquidity")
    st.markdown(
        """
        Financial markets channel surplus funds from savers (households, institutions) to deficit entities 
        (firms, governments) for capital formation. Financial assets exist across two major dimensions:
        """
    )

    t1, t2 = st.tabs(["🏛️ Institutional Taxonomy", "🔬 Primary vs. Secondary Deep Dive"])

    with t1:
        st.markdown(
            """
            | Dimension | **Money Market** | **Capital Market** |
            | :--- | :--- | :--- |
            | **Maturity Profile** | Short-term ($\le$ 1 Year) | Long-term (> 1 Year or Perpetual) |
            | **Primary Instruments** | Treasury Bills, Commercial Paper, Repos, CDs | Common Equities, Corporate Bonds, Sovereign Gilts |
            | **Primary Function** | Managing working capital & institutional liquidity | Funding real assets, long-term capex, growth |
            | **Risk / Return** | Low default risk, low yields, high price stability | Higher duration & equity risk, higher expected return |
            """
        )

    with t2:
        col_p, col_s = st.columns(2, gap="medium")
        with col_p:
            st.markdown(
                """
                <div class="concept-card">
                    <h4 style="color: #38BDF8; margin: 0 0 0.5rem 0;">1. Primary Market (Capital Creation)</h4>
                    <p style="font-size: 0.9rem;">
                        Where newly issued securities are born. Capital flows <b>directly from investors to the issuer</b> (corporate or sovereign).
                    </p>
                    <ul style="font-size: 0.85rem; color: #CBD5E1;">
                        <li><b>Mechanisms:</b> Initial Public Offerings (IPOs), Follow-on Offerings (FPOs), Rights Issues, Private Placements.</li>
                        <li><b>Key Intermediaries:</b> Investment banks, underwriters, bookrunners.</li>
                        <li><b>Economic Impact:</b> Expands real capital stock ($I$ in GDP).</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col_s:
            st.markdown(
                """
                <div class="concept-card">
                    <h4 style="color: #FBBF24; margin: 0 0 0.5rem 0;">2. Secondary Market (Liquidity & Price Discovery)</h4>
                    <p style="font-size: 0.9rem;">
                        Where pre-existing securities are exchanged <b>between investors</b>. The original issuer receives zero proceeds.
                    </p>
                    <ul style="font-size: 0.85rem; color: #CBD5E1;">
                        <li><b>Mechanisms:</b> Central Limit Order Books (Exchanges like NYSE, NASDAQ), Over-the-Counter (OTC) dealer networks.</li>
                        <li><b>Key Intermediaries:</b> Market makers, broker-dealers, clearinghouses.</li>
                        <li><b>Economic Impact:</b> Lowers liquidity risk, lowering the cost of capital for future primary issuances.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.subheader("🛠️ Interactive Labs: Primary Dilution & Secondary Market Order Book")

    lab_mode = st.radio(
        "Choose Lab Component:",
        ["1. Primary Market: IPO Pricing, Capital Raised & Dilution", "2. Secondary Market: Bid-Ask Spread & Liquidity Depth"],
        horizontal=True,
    )

    if lab_mode == "1. Primary Market: IPO Pricing, Capital Raised & Dilution":
        c_ipo1, c_ipo2 = st.columns([1, 1.2], gap="large")

        with c_ipo1:
            st.markdown("#### 🎯 Issuer IPO Parameters")
            pre_shares = st.slider("Existing Pre-IPO Shares (Millions):", 10.0, 100.0, 50.0, 5.0)
            shares_issued = st.slider("New Primary Shares Issued (Millions):", 5.0, 50.0, 15.0, 1.0)
            offer_price = st.slider("IPO Offer Price per Share ($):", 10.0, 100.0, 40.0, 2.0)
            underwriting_fee_pct = st.slider("Underwriting Spread / Discount (%):", 1.0, 10.0, 5.0, 0.5)

            gross_proceeds = shares_issued * offer_price
            fees = gross_proceeds * (underwriting_fee_pct / 100.0)
            net_proceeds = gross_proceeds - fees
            post_shares = pre_shares + shares_issued
            dilution_pct = (shares_issued / post_shares) * 100.0
            post_money_mkt_cap = post_shares * offer_price

            st.markdown("---")
            st.markdown("#### 🎯 Primary Capital Objective")
            st.caption("Structure an issuance that raises **$\ge$ $500M in Net Capital** while keeping founder dilution **$\le$ 25%**.")

            if st.button("Submit IPO Capital Plan"):
                if net_proceeds >= 500.0 and dilution_pct <= 25.0:
                    st.session_state.market_points = 25
                    st.success(f"🎯 Optimal Offering! Net proceeds: ${net_proceeds:.1f}M, Dilution: {dilution_pct:.1f}% (Awarded: 25/25 Pts)")
                else:
                    st.session_state.market_points = 10
                    st.warning(f"⚠️ Conditions missed: Net proceeds ${net_proceeds:.1f}M (Target $\ge$500M) or Dilution {dilution_pct:.1f}% (Target $\le$25%). (Awarded: 10/25 Pts)")
                st.rerun()

        with c_ipo2:
            st.markdown("#### 📊 Offering Economics & Ownership Shift")
            p_m1, p_m2, p_m3 = st.columns(3)
            with p_m1:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Net Capital Raised</div>
                        <div class="metric-val" style="color: {'#10B981' if net_proceeds >= 500 else '#38BDF8'} !important;">${net_proceeds:.1f}M</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with p_m2:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Founder Dilution</div>
                        <div class="metric-val" style="color: {'#10B981' if dilution_pct <= 25 else '#F87171'} !important;">{dilution_pct:.1f}%</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with p_m3:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Post-Money Cap</div>
                        <div class="metric-val" style="color: #FBBF24 !important;">${post_money_mkt_cap:.1f}M</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Cap Table Breakdown chart
            cap_df = pd.DataFrame(
                {
                    "Stakeholder": ["Original Shareholders", "New Public Investors"],
                    "Equity Stake (%)": [100.0 - dilution_pct, dilution_pct],
                }
            ).set_index("Stakeholder")
            st.bar_chart(cap_df)
            st.caption(f"📌 Gross Proceeds: ${gross_proceeds:.1f}M | Underwriting Commission: ${fees:.2f}M.")

    else:
        # Secondary Market Simulator
        c_sec1, c_sec2 = st.columns([1, 1.2], gap="large")

        with c_sec1:
            st.markdown("#### 🔄 Order Book & Microstructure")
            mid_price = st.slider("Benchmark Fair Value ($):", 50.0, 200.0, 100.0, 5.0)
            spread_bps = st.slider("Bid-Ask Half-Spread (Basis Points):", 5, 100, 20, 5)
            depth_multiplier = st.slider("Market Maker Liquidity Depth Index:", 1.0, 5.0, 2.5, 0.5)

            half_spread_dollars = mid_price * (spread_bps / 10000.0)
            bid = mid_price - half_spread_dollars
            ask = mid_price + half_spread_dollars

            st.markdown(
                f"""
                - **Top-of-Book Bid:** ${bid:.2f} *(Buyers willing to pay)*
                - **Top-of-Book Ask:** ${ask:.2f} *(Sellers willing to accept)*
                - **Total Quoted Spread:** ${(ask - bid):.3f} ({(spread_bps * 2)} bps)
                """
            )
            st.caption("Tight bid-ask spreads indicate high liquidity, reducing transaction frictions and lowering the issuer's future cost of capital.")

        with c_sec2:
            st.markdown("#### 📊 Cumulative Depth Chart (Secondary Liquidity)")
            levels = np.array([3, 2, 1, 1, 2, 3])
            price_offsets = np.array([-3, -2, -1, 1, 2, 3]) * half_spread_dollars * 1.5
            prices = mid_price + price_offsets
            sizes = np.array([800, 500, 200, 250, 450, 900]) * depth_multiplier

            depth_df = pd.DataFrame(
                {
                    "Order Type": ["Bid (Buy)", "Bid (Buy)", "Bid (Buy)", "Ask (Sell)", "Ask (Sell)", "Ask (Sell)"],
                    "Price Level ($)": np.round(prices, 2),
                    "Shares Available": np.round(sizes, 0),
                }
            )
            st.dataframe(depth_df, use_container_width=True)
            st.caption("💡 Secondary markets do not allocate funds to the firm; they provide liquidity that enables primary market investors to exit at predictable market prices.")

# =====================================================================
# MODULE 2: MONEY & BOND MARKETS (ORIGINAL MODULE 1)
# =====================================================================
elif module == "📈 Module 2: Money & Bond Markets Equilibrium":
    st.markdown("### 📈 Liquidity Preference, Money Supply & Bond Prices")
    st.markdown(
        r"""
        The money market and the bond market are dual reflections of household portfolio decisions. 
        According to Keynesian theory, total financial wealth $W$ is split between cash balances and bonds:
        
        $$\frac{M}{P} + B^s = L(Y, r) + B^d$$
        
        When real money supply $\frac{M}{P}$ exceeds money demand $L(Y, r)$, agents purchase bonds in the secondary debt market, driving bond prices up and interest rates down until:
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
        bond_price = annual_coupon / (r_eq / 100)

        st.markdown("---")
        st.markdown("#### 🎯 Monetary Policy Objective")
        st.caption("Calibrate money supply to target a benchmark interest rate between **3.5%** and **5.5%**.")

        if st.button("Submit Portfolio Calibration"):
            if 3.5 <= r_eq <= 5.5:
                st.session_state.sim_points = 25
                st.success(f"🎯 Target rate achieved at r* = {r_eq:.2f}%! (Awarded: 25/25 Pts)")
            else:
                st.session_state.sim_points = 10
                st.warning(f"⚠️ Policy rate at {r_eq:.2f}% is outside the 3.5% - 5.5% corridor. (Awarded: 10/25 Pts)")
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

        r_axis = np.linspace(0.5, 12.0, 40)
        money_demand_curve = transaction_demand - (h_sensitivity * r_axis)

        chart_df = pd.DataFrame(
            {
                "Policy Interest Rate (r %)": np.round(r_axis, 2),
                "Money Demand L(Y,r)": np.round(money_demand_curve, 1),
                "Real Supply M/P": np.round(np.full_like(r_axis, real_money_supply), 1),
            }
        ).set_index("Policy Interest Rate (r %)")

        st.line_chart(chart_df)
        st.caption(f"📌 Equilibrium clearing: Real Cash Stock = {real_money_supply:.1f} | Benchmark Bond Price = ${bond_price:.2f}")

# =====================================================================
# MODULE 3: JOINT IS-LM FRAMEWORK (ORIGINAL MODULE 2)
# =====================================================================
elif module == "⚖️ Module 3: The IS-LM Macro Framework":
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
        c_mpc = 0.75
        i_sens = 30.0
        a_autonomous_c = 150.0
        i_autonomous = 200.0

    with col_lm:
        st.markdown("#### 🏦 Financial Market Parameters (LM Curve)")
        mon_supply_m = st.slider("Nominal Money Supply (M):", 400.0, 1600.0, 900.0, 50.0)
        p_idx = st.slider("Price Level (P):", 1.0, 2.5, 1.5, 0.1)
        k_income_sens = 0.50
        h_spec_sens = 40.0

    alpha = 1.0 / (1.0 - c_mpc)
    autonomous_exp = a_autonomous_c - (c_mpc * taxes_t) + i_autonomous + gov_g
    real_m = mon_supply_m / p_idx

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

    y_vals = np.linspace(1000.0, 3200.0, 40)
    r_is = (autonomous_exp / i_sens) - (y_vals / (alpha * i_sens))
    r_lm = (k_income_sens / h_spec_sens) * y_vals - (real_m / h_spec_sens)

    is_lm_df = pd.DataFrame(
        {
            "Output (Y)": np.round(y_vals, 0),
            "IS Curve (Goods Equilibrium)": np.round(r_is, 2),
            "LM Curve (Money Equilibrium)": np.round(r_lm, 2),
        }
    ).set_index("Output (Y)")

    st.line_chart(is_lm_df)
    st.caption("📈 The intersection represents simultaneous clearing in both the goods and money markets.")

# =====================================================================
# MODULE 4: MACRO-FINANCIAL ASSESSMENT (EXPANDED TO 50 PTS)
# =====================================================================
elif module == "📝 Module 4: Integrated Macro-Finance Assessment":
    st.markdown("### 📝 Integrated Macro-Finance & Capital Markets Evaluation")
    st.markdown("Test your structural understanding of primary/secondary markets, asset pricing, central banking, and the IS-LM framework (10 points each).")

    with st.form("macro_finance_quiz"):
        st.markdown("#### 1. Primary vs. Secondary Market Mechanism")
        q1 = st.radio(
            "When an investor buys shares of Apple Inc. on the NASDAQ exchange:",
            [
                "A) Apple receives equity financing to construct new semiconductor fabrication plants.",
                "B) The transaction occurs on the secondary market; liquidity and ownership transfer without cash flowing to Apple.",
                "C) The money supply contracts as liquidity is absorbed by corporate balance sheets.",
                "D) The primary market clears through an underwriting syndicate.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 2. Dual Clearing in Bond and Money Markets")
        q2 = st.radio(
            "When the central bank performs an Open Market Purchase of Treasury securities:",
            [
                "A) The money supply contracts, causing bond prices to collapse.",
                "B) Bank reserves rise, bond prices increase, and the equilibrium interest rate falls.",
                "C) The LM curve shifts left, increasing borrowing costs for private firms.",
                "D) Velocity becomes negative, nullifying the money multiplier.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 3. Interconnection between Primary and Secondary Markets")
        q3 = st.radio(
            "Why is a deep, highly liquid secondary bond market vital for corporate primary debt issuance?",
            [
                "A) It eliminates default risk entirely from the borrowing corporation.",
                "B) Investors accept lower required yields in the primary market because they can easily liquidate bonds later.",
                "C) It prevents the central bank from targeting interest rates.",
                "D) It converts long-term debt into short-term money market instruments.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 4. Fiscal Policy & Financial Crowding-Out")
        q4 = st.radio(
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
        st.markdown("#### 5. Liquidity Trap Dynamics")
        q5 = st.radio(
            "In a Keynesian Liquidity Trap (interest rates near zero and h approaching infinity):",
            [
                "A) Bond prices are at cyclical lows, and agents anticipate large capital gains.",
                "B) Further injections of liquidity are hoarded as cash; monetary expansion fails to lower interest rates further.",
                "C) The IS curve becomes vertical, rendering fiscal policy completely impotent.",
                "D) The central bank loses control over nominal reserve creation.",
            ],
            index=None,
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Grade")

        if submit_quiz:
            correct_keys = {
                "q1": "B) The transaction occurs on the secondary market; liquidity and ownership transfer without cash flowing to Apple.",
                "q2": "B) Bank reserves rise, bond prices increase, and the equilibrium interest rate falls.",
                "q3": "B) Investors accept lower required yields in the primary market because they can easily liquidate bonds later.",
                "q4": "A) The IS curve to shift right, raising both income and interest rates, which dampens private investment.",
                "q5": "B) Further injections of liquidity are hoarded as cash; monetary expansion fails to lower interest rates further.",
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
            st.error("❌ **Q1 Review:** Secondary market exchanges happen between market participants; no fresh capital goes to the underlying company.")
        if not rec.get("q2", False):
            st.error("❌ **Q2 Review:** Open market purchases inject reserves, boosting bond prices ($P_{bond} \\uparrow$) and lowering yields ($r \\downarrow$).")
        if not rec.get("q3", False):
            st.error("❌ **Q3 Review:** Secondary market liquidity reduces the liquidity risk premium demanded by primary market investors, lowering the cost of capital.")
        if not rec.get("q4", False):
            st.error("❌ **Q4 Review:** Higher government spending ($G \\uparrow$) shifts IS rightward. Increased transaction demand drives up interest rates, partially crowding out private investment ($I(r)$).")
        if not rec.get("q5", False):
            st.error("❌ **Q5 Review:** In a liquidity trap, money demand is perfectly elastic with respect to the interest rate ($h \\to \\infty$), meaning cash and short-term debt become perfect substitutes.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("🏛️ Financial Architecture & Macro Lab")
with f2:
    st.caption("⚡ Primary/Secondary Allocation, Bond Pricing & IS-LM Dynamics")
with f3:
    st.caption(f"⏰ System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
