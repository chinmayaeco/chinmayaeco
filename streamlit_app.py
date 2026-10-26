from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Financial Markets Lab: Primary & Secondary Markets",
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
    st.markdown("## 🏛️ Financial Markets Lab")
    module = st.radio(
        "Select Learning Module:",
        [
            "🏢 Module 1: Primary & Secondary Markets",
            "📝 Module 2: Financial Markets Assessment",
        ],
    )
    st.markdown("---")
    st.markdown("### 🏆 Performance Tracker")
    st.markdown(f"**Interactive Lab:** {st.session_state.market_points} / 50")
    st.markdown(f"**Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Aggregate Score:** {total_final_score} / 100")

    if total_final_score == 100:
        st.success("🌟 Market Specialist Status Achieved!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(
    f"""
<div class="score-banner">
    <h2 style="color: #FBBF24; margin: 0; font-weight: 800;">Financial Markets Learning Suite: {total_final_score} / 100</h2>
    <p style="color: #E2E8F0; margin: 0.35rem 0 0 0; font-size: 1rem;">
        Simulation Lab: <b>{st.session_state.market_points}/50 Pts</b> | Conceptual Assessment: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# MODULE 1: FINANCIAL MARKETS, PRIMARY & SECONDARY
# =====================================================================
if module == "🏢 Module 1: Primary & Secondary Markets":
    st.markdown("### 🏢 Financial Markets Architecture: Capital Allocation & Liquidity")
    st.markdown(
        "Financial markets channel surplus capital from savers to deficit entities "
        "(corporations, public bodies) for capital formation."
    )

    tab_tax, tab_deep = st.tabs(["🏛️ Institutional Overview", "🔬 Primary vs. Secondary Deep Dive"])

    with tab_tax:
        st.markdown(
            """
| Dimension | Money Market | Capital Market |
| :--- | :--- | :--- |
| **Maturity Profile** | Short-term (under 1 Year) | Long-term (over 1 Year or Perpetual) |
| **Primary Instruments** | Treasury Bills, Commercial Paper, Repos, CDs | Common Equities, Corporate Debt, Sovereign Bonds |
| **Primary Function** | Managing working capital & institutional liquidity | Funding real assets, long-term capex, expansion |
| **Risk / Return** | Low default risk, low yields, price stability | Higher duration & equity risk, higher return |
            """
        )

    with tab_deep:
        col_p, col_s = st.columns(2, gap="medium")
        with col_p:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #38BDF8; margin: 0 0 0.5rem 0;">1. Primary Market (Capital Creation)</h4>
    <p style="font-size: 0.9rem;">
        Where newly minted securities are issued. Capital flows <b>directly from investors to the issuer</b>.
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li><b>Mechanisms:</b> Initial Public Offerings (IPOs), Rights Offerings, Private Placements.</li>
        <li><b>Key Intermediaries:</b> Investment banks, underwriting syndicates, bookrunners.</li>
        <li><b>Economic Role:</b> Increases aggregate real investment and physical capital stock.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col_s:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #FBBF24; margin: 0 0 0.5rem 0;">2. Secondary Market (Liquidity & Discovery)</h4>
    <p style="font-size: 0.9rem;">
        Where existing securities are traded <b>between market participants</b>. The issuing firm receives zero capital.
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li><b>Mechanisms:</b> Central Limit Order Books (NYSE, NASDAQ), Over-the-Counter (OTC) networks.</li>
        <li><b>Key Intermediaries:</b> Market makers, broker-dealers, clearinghouses.</li>
        <li><b>Economic Role:</b> Continuous pricing, immediate exit liquidity, reducing cost of capital.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.subheader("🛠️ Interactive Labs: Primary Dilution & Secondary Market Order Book")

    lab_mode = st.radio(
        "Choose Lab Component:",
        [
            "1. Primary Market: IPO Pricing, Capital Raised & Dilution",
            "2. Secondary Market: Bid-Ask Spread & Liquidity Depth",
        ],
        horizontal=True,
    )

    if lab_mode == "1. Primary Market: IPO Pricing, Capital Raised & Dilution":
        c_ipo1, c_ipo2 = st.columns([1, 1.2], gap="large")

        with c_ipo1:
            st.markdown("#### Primary IPO Configuration")
            pre_shares = st.slider("Existing Pre-IPO Shares (Millions):", 10.0, 100.0, 50.0, 5.0)
            shares_issued = st.slider("New Shares to Issue (Millions):", 5.0, 50.0, 15.0, 1.0)
            offer_price = st.slider("Offer Price per Share (USD):", 10.0, 100.0, 40.0, 2.0)
            underwriting_fee_pct = st.slider("Underwriting Spread / Discount (%):", 1.0, 10.0, 5.0, 0.5)

            gross_proceeds = shares_issued * offer_price
            fees = gross_proceeds * (underwriting_fee_pct / 100.0)
            net_proceeds = gross_proceeds - fees
            post_shares = pre_shares + shares_issued
            dilution_pct = (shares_issued / post_shares) * 100.0
            post_money_mkt_cap = post_shares * offer_price

            st.markdown("---")
            st.markdown("#### Capital Allocation Objective")
            st.caption("Structure an issuance that raises at least **500M USD Net Capital** while keeping founder dilution **under 25%**.")

            if st.button("Submit IPO Capital Plan"):
                if net_proceeds >= 500.0 and dilution_pct <= 25.0:
                    st.session_state.market_points = 50
                    st.success(f"Target reached! Net proceeds: {net_proceeds:.1f}M USD, Dilution: {dilution_pct:.1f}% (Awarded: 50/50 Pts)")
                else:
                    st.session_state.market_points = 25
                    st.warning(f"Target criteria missed: Net proceeds {net_proceeds:.1f}M USD (Target: 500M+ USD) or Dilution {dilution_pct:.1f}% (Target: 25% or less). (Awarded: 25/50 Pts)")
                st.rerun()

        with c_ipo2:
            st.markdown("#### Offering Economics & Ownership Breakdown")
            p_m1, p_m2, p_m3 = st.columns(3)
            with p_m1:
                st.markdown(
                    f"""
                    <div class="metric-panel">
                        <div class="metric-title">Net Capital Raised</div>
                        <div class="metric-val" style="color: {'#10B981' if net_proceeds >= 500 else '#38BDF8'} !important;">{net_proceeds:.1f}M USD</div>
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
                        <div class="metric-val" style="color: #FBBF24 !important;">{post_money_mkt_cap:.1f}M USD</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            cap_df = pd.DataFrame(
                {
                    "Stakeholder": ["Original Shareholders", "New Public Investors"],
                    "Ownership Percentage": [100.0 - dilution_pct, dilution_pct],
                }
            ).set_index("Stakeholder")
            st.bar_chart(cap_df)
            st.caption(f"Gross Proceeds: {gross_proceeds:.1f}M USD | Underwriting Fees: {fees:.2f}M USD")

    else:
        c_sec1, c_sec2 = st.columns([1, 1.2], gap="large")

        with c_sec1:
            st.markdown("#### Order Book Microstructure")
            mid_price = st.slider("Benchmark Price (USD):", 50.0, 200.0, 100.0, 5.0)
            spread_bps = st.slider("Bid-Ask Half-Spread (Basis Points):", 5, 100, 20, 5)
            depth_multiplier = st.slider("Market Depth Index:", 1.0, 5.0, 2.5, 0.5)

            half_spread_dollars = mid_price * (spread_bps / 10000.0)
            bid = mid_price - half_spread_dollars
            ask = mid_price + half_spread_dollars

            st.markdown(
                f"""
                - **Top-of-Book Bid:** {bid:.2f} USD *(Buyers willing to pay)*
                - **Top-of-Book Ask:** {ask:.2f} USD *(Sellers willing to accept)*
                - **Total Quoted Spread:** {(ask - bid):.3f} USD ({(spread_bps * 2)} bps)
                """
            )
            st.caption("A tight bid-ask spread signals high liquidity, reducing transaction frictions for investors.")

        with c_sec2:
            st.markdown("#### Secondary Market Liquidity Depth")
            price_offsets = np.array([-3, -2, -1, 1, 2, 3]) * half_spread_dollars * 1.5
            prices = mid_price + price_offsets
            sizes = np.array([800, 500, 200, 250, 450, 900]) * depth_multiplier

            depth_df = pd.DataFrame(
                {
                    "Order Side": ["Bid (Buy)", "Bid (Buy)", "Bid (Buy)", "Ask (Sell)", "Ask (Sell)", "Ask (Sell)"],
                    "Price Level (USD)": np.round(prices, 2),
                    "Shares Depth": np.round(sizes, 0),
                }
            )
            st.dataframe(depth_df, use_container_width=True)
            st.caption("Notice: Trades in the secondary market redistribute shares among investors without directly funding corporate operations.")

# =====================================================================
# MODULE 2: ASSESSMENT (FORMERLY MODULE 4)
# =====================================================================
elif module == "📝 Module 2: Financial Markets Assessment":
    st.markdown("### 📝 Financial Markets Knowledge Evaluation")
    st.markdown("Test your structural understanding of primary vs. secondary capital markets (10 points each).")

    with st.form("market_structure_quiz"):
        st.markdown("#### 1. Primary vs. Secondary Market Mechanism")
        q1 = st.radio(
            "When an investor purchases shares of a publicly listed company on an open exchange like NASDAQ:",
            [
                "A) The company receives direct equity capital to build factories.",
                "B) The transaction is in the secondary market; ownership transfers without funding the firm directly.",
                "C) Total outstanding shares in the company automatically increase.",
                "D) The primary market clears the trade via an underwriting syndicate.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 2. Capital Market vs. Money Market Classification")
        q2 = st.radio(
            "Which of the following is strictly a Money Market instrument?",
            [
                "A) 30-Year Sovereign Treasury Bond",
                "B) Common Stock",
                "C) 90-Day Commercial Paper",
                "D) Corporate Debenture",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 3. Interconnection Between Primary and Secondary Markets")
        q3 = st.radio(
            "Why is a liquid secondary market essential for an issuer's primary market offerings?",
            [
                "A) It completely eliminates the issuer's credit risk.",
                "B) Investors accept lower yields in the primary market because they can easily liquidate holdings later.",
                "C) It prevents prices from fluctuating in the primary market.",
                "D) It turns equity securities into guaranteed short-term deposits.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 4. Primary Market Issuance Mechanics")
        q4 = st.radio(
            "What is the primary role of an investment bank acting as an underwriter in an IPO?",
            [
                "A) Guaranteeing post-IPO secondary market stock performance for 10 years.",
                "B) Assisting the firm in pricing, regulatory filings, and absorbing or placing the new issue.",
                "C) Managing day-to-day corporate treasury operations post-listing.",
                "D) Regulating exchange bid-ask quotes on open trading venues.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 5. Secondary Market Liquidity Signals")
        q5 = st.radio(
            "A security market characterized by an extremely narrow bid-ask spread and heavy order book depth indicates:",
            [
                "A) High liquidity, low transaction costs, and rapid price discovery.",
                "B) Significant liquidity risk and elevated cost of capital.",
                "C) A total absence of institutional market makers.",
                "D) The complete collapse of secondary market volume.",
            ],
            index=None,
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Grade")

        if submit_quiz:
            correct_keys = {
                "q1": "B) The transaction is in the secondary market; ownership transfers without funding the firm directly.",
                "q2": "C) 90-Day Commercial Paper",
                "q3": "B) Investors accept lower yields in the primary market because they can easily liquidate holdings later.",
                "q4": "B) Assisting the firm in pricing, regulatory filings, and absorbing or placing the new issue.",
                "q5": "A) High liquidity, low transaction costs, and rapid price discovery.",
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
            st.error("Q1 Review: Secondary market transactions occur strictly between investors; no new funds flow to the underlying company.")
        if not rec.get("q2", False):
            st.error("Q2 Review: Commercial paper is a short-term, unsecured debt instrument maturing in 270 days or less, making it a money market instrument.")
        if not rec.get("q3", False):
            st.error("Q3 Review: Liquidity in the secondary market reduces the liquidity risk premium demanded by primary buyers, reducing the issuer's cost of capital.")
        if not rec.get("q4", False):
            st.error("Q4 Review: Underwriters conduct due diligence, value the firm, structure the offering, and syndicate shares to primary investors.")
        if not rec.get("q5", False):
            st.error("Q5 Review: Narrow spreads and deep order books reflect robust liquidity and active market participation.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("Financial Architecture Lab")
with f2:
    st.caption("Primary Allocation & Secondary Liquidity Dynamics")
with f3:
    st.caption(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
