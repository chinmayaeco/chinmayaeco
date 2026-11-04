from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Money Creation & Monetary Aggregates",
    page_icon="🏦",
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
    st.markdown("## 🏛️ Central Banking & Liquidity Suite")
    nav_mode = st.radio(
        "Select Section:",
        [
            "🔬 Simulation: Deposit Multiplier & Expansion",
            "📝 Assessment: Monetary Theory & Aggregates",
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
    <h2 style="color: #34D399; margin: 0; font-weight: 800;">Money Creation & Liquidity Expansion Engine: {total_score} / 100</h2>
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
if nav_mode == "🔬 Simulation: Deposit Multiplier & Expansion":
    st.markdown("### 🏦 Fractional Reserve Banking & Money Multipliers")
    st.markdown(
        "When commercial banks receive new cash reserves, they retain required regulatory reserves and lend out "
        "the remainder. Real-world credit expansion is attenuated by **excess reserve holdings** ($e$) and **currency "
        "drain into public circulation** ($c$)."
    )

    tab_model, tab_math = st.tabs(["📚 Aggregates Hierarchy", "🔬 Multiplier Mechanics"])

    with tab_model:
        st.markdown(
            """
| Aggregate | Core Components | Degree of Liquidity | Economic Role |
| :--- | :--- | :--- | :--- |
| **Monetary Base ($M_0$ / $B$)** | Physical Currency in Circulation ($C$) + Bank Reserves ($R$) | Direct central bank liability | Foundation for broad money creation |
| **Narrow Money ($M_1$)** | Physical Currency ($C$) + Demand/Checking Deposits ($D$) | Ultra-high (immediate medium of exchange) | Transactional balances and consumer payments |
| **Broad Money ($M_2$)** | $M_1$ + Savings Deposits + Retail Money Market Funds + Small CDs | Moderate to high | Transactional liquidity plus close near-monies |
            """
        )

    with tab_math:
        col_c1, col_c2 = st.columns(2, gap="medium")
        with col_c1:
            st.markdown(
                """
<div class="concept-card">
    <h4 style="color: #34D399; margin: 0 0 0.5rem 0;">1. Simple Theoretical Multiplier</h4>
    <p style="font-size: 0.88rem; color: #E2E8F0;">
        Assumes zero currency drain ($c = 0$) and zero excess reserve preference ($e = 0$):
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li>$m_{simple} = \\frac{1}{rr}$</li>
        <li>$\\Delta D_{max} = \\frac{\\Delta R}{rr}$</li>
        <li>Where $rr$ is the central bank's statutory Reserve Requirement Ratio.</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )
        with col_c2:
            st.markdown(
                """
<div class="concept-card" style="border-left-color: #FBBF24;">
    <h4 style="color: #FBBF24; margin: 0 0 0.5rem 0;">2. Realistic Money Multiplier ($m$)</h4>
    <p style="font-size: 0.88rem; color: #E2E8F0;">
        Incorporating Currency Drain ($c = C/D$) and Excess Reserves ($e = ER/D$):
    </p>
    <ul style="font-size: 0.85rem; color: #CBD5E1;">
        <li>$m = \\frac{1 + c}{rr + e + c}$</li>
        <li>$M_1 = m \\cdot M_0 = m \\cdot (C + R)$</li>
        <li>$\\lim_{(c+e) \\to \\infty} m = 1$ (eliminates credit amplification)</li>
    </ul>
</div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.subheader("🛠️ Interactive Reserve Injection & Multiplier Lab")

    col_in, col_out = st.columns([1, 1.2], gap="large")

    with col_in:
        st.markdown("#### Policy & Behavioral Controls")
        delta_reserves = st.slider("Central Bank Open Market Purchase ($\\Delta R$, $B):", 5.0, 100.0, 20.0, 5.0)
        req_ratio = st.slider("Required Reserve Ratio ($rr$):", 0.02, 0.30, 0.10, 0.01)
        curr_ratio = st.slider("Currency Drain Ratio ($c = C/D$):", 0.0, 0.50, 0.15, 0.01)
        excess_ratio = st.slider("Excess Reserve Holding ($e = ER/D$):", 0.0, 0.40, 0.05, 0.01)

        # Multiplier Calculations
        simple_mult = 1.0 / req_ratio
        realistic_mult = (1.0 + curr_ratio) / (req_ratio + excess_ratio + curr_ratio)

        delta_m1_simple = delta_reserves * simple_mult
        delta_m1_real = delta_reserves * realistic_mult
        leakage_loss = delta_m1_simple - delta_m1_real

        st.markdown("---")
        st.markdown("#### Target Exercise")
        st.caption(
            "Target an effective broad money expansion of **$\\Delta M_1 \\ge \\$75\\text{B}$** "
            "while maintaining an effective multiplier **$m \\ge 3.0$**."
        )

        if st.button("Evaluate Expansion Target"):
            if delta_m1_real >= 75.0 and realistic_mult >= 3.0:
                st.session_state.sim_points = 50
                st.success(f"Target achieved! $\\Delta M_1 = \\${delta_m1_real:.2f}B$ with $m = {realistic_mult:.2f}$. (Awarded: 50/50 Pts)")
            else:
                st.session_state.sim_points = 20
                st.warning(
                    f"Target missed: Requires $\\Delta M_1 \\ge \\$75B$ (current: ${delta_m1_real:.2f}B) "
                    f"and $m \\ge 3.0$ (current: {realistic_mult:.2f}). (Awarded: 20/50 Pts)"
                )
            st.rerun()

    with col_out:
        st.markdown("#### Money Supply Impact")
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(
                f"""
                <div class="metric-panel">
                    <div class="metric-title">Effective Multiplier ($m$)</div>
                    <div class="metric-val">{realistic_mult:.2f}x</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with m2:
            st.markdown(
                f"""
                <div class="metric-panel">
                    <div class="metric-title">Realistic Expansion ($\\Delta M_1$)</div>
                    <div class="metric-val">${delta_m1_real:.1f}B</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with m3:
            st.markdown(
                f"""
                <div class="metric-panel">
                    <div class="metric-title">Leakage Penalty</div>
                    <div class="metric-val" style="color: #EF4444 !important;">-${leakage_loss:.1f}B</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Iterative credit expansion rounds
        rounds = np.arange(1, 11)
        retention_ratio = (1.0 - req_ratio - excess_ratio) / (1.0 + curr_ratio)
        retention_ratio = max(0.0, retention_ratio)
        round_lending = [delta_reserves * (retention_ratio ** (r - 1)) for r in rounds]
        cumulative_m1 = np.cumsum(round_lending)

        chart_df = pd.DataFrame(
            {
                "Expansion Round": rounds,
                "New Loans Disbursed ($B)": np.round(round_lending, 2),
                "Cumulative Money Created ($B)": np.round(cumulative_m1, 2),
            }
        ).set_index("Expansion Round")

        st.line_chart(chart_df)
        st.caption(
            f"Lending rounds converge asymptotically. Theoretical maximum simple ceiling: **${delta_m1_simple:.1f}B**; "
            f"Attenuated realistic equilibrium: **${delta_m1_real:.1f}B**."
        )

# =====================================================================
# SECTION 2: ASSESSMENT
# =====================================================================
elif nav_mode == "📝 Assessment: Monetary Theory & Aggregates":
    st.markdown("### 📝 Monetary Economics & Multiplier Assessment")
    st.markdown("Test your understanding of monetary aggregates, fractional reserves, leakages, and open market operations (10 points each).")

    with st.form("money_assessment_form"):
        st.markdown("#### 1. Composition of Monetary Aggregates")
        q1 = st.radio(
            "Which of the following items is included in Broad Money ($M_2$) but excluded from Narrow Money ($M_1$)?",
            [
                "A) Physical paper banknotes and coins held by the non-bank public.",
                "B) Commercial bank vault cash.",
                "C) Retail savings deposits and non-institutional money market funds.",
                "D) Demand and checking deposits at commercial depository institutions.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 2. Central Bank Balance Sheet Mechanics")
        q2 = st.radio(
            "When a central bank carries out an Open Market Purchase of sovereign bonds from commercial banks:",
            [
                "A) Commercial bank reserves expand at the central bank, increasing the Monetary Base ($M_0$).",
                "B) The required reserve ratio automatically climbs to absorb liquidity.",
                "C) The money multiplier immediately drops to zero.",
                "D) Commercial banks are legally prohibited from extending further credit.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 3. Mathematical Impact of Cash Drain")
        q3 = st.radio(
            "If the non-bank public suddenly prefers to hold a larger fraction of their money as physical cash (an increase in $c = C/D$):",
            [
                "A) Commercial banks gain additional reserves to lend.",
                "B) The realistic money multiplier decreases because reserves leak from the credit creation cycle.",
                "C) The simple deposit multiplier formula ($1/rr$) increases proportionately.",
                "D) Total demand deposits expand exponentially.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 4. Excess Reserves and the Liquidity Trap")
        q4 = st.radio(
            "During severe financial distress, commercial banks frequently accumulate substantial excess reserves ($e \\uparrow$). Holding all else constant, this leads to:",
            [
                "A) Hyperinflation caused by uncontrolled credit acceleration.",
                "B) A breakdown in credit transmission where additions to $M_0$ fail to stimulate $M_1$ and $M_2$.",
                "C) An automatic increase in the velocity of money ($V$).",
                "D) An immediate legal default of the fractional reserve framework.",
            ],
            index=None,
        )

        st.markdown("---")
        st.markdown("#### 5. Simple Multiplier Arithmetic")
        q5 = st.radio(
            "Assuming no currency drain and zero excess reserves, if the statutory required reserve ratio ($rr$) is set at 5% (0.05), an initial reserve injection of $10 million yields a maximum theoretical deposit expansion of:",
            [
                "A) $50 million.",
                "B) $100 million.",
                "C) $200 million.",
                "D) $500 million.",
            ],
            index=None,
        )

        submit_btn = st.form_submit_button("Submit Assessment & Grade")

        if submit_btn:
            correct_answers = {
                "q1": "C) Retail savings deposits and non-institutional money market funds.",
                "q2": "A) Commercial bank reserves expand at the central bank, increasing the Monetary Base ($M_0$).",
                "q3": "B) The realistic money multiplier decreases because reserves leak from the credit creation cycle.",
                "q4": "B) A breakdown in credit transmission where additions to $M_0$ fail to stimulate $M_1$ and $M_2$.",
                "q5": "C) $200 million.",
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
            st.error("Q1 Review: $M_1$ tracks immediate media of exchange (currency + checking deposits). Savings accounts and small-denomination time deposits enter at the $M_2$ boundary.")
        if not rec.get("q2", False):
            st.error("Q2 Review: Central bank open-market asset purchases credit commercial bank reserve accounts, expanding base money ($M_0$).")
        if not rec.get("q3", False):
            st.error("Q3 Review: Cash drain removes high-powered reserves from commercial vaults/central balances, cutting off subsequent rounds of re-lending.")
        if not rec.get("q4", False):
            st.error("Q4 Review: If banks hoard excess reserves rather than disbursing new credit, the money multiplier contracts, decoupling monetary base growth from broad money.")
        if not rec.get("q5", False):
            st.error("Q5 Review: Theoretical expansion equals $\\Delta D = \\Delta R \\times (1/rr) = \\$10\\text{M} \\times (1 / 0.05) = \\$10\\text{M} \\times 20 = \\$200\\text{M}$.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("Monetary Economics & Banking Policy Engine")
with f2:
    st.caption("Deposit Multiplication, Reserve Ratios & Liquidity Tiers")
with f3:
    st.caption(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
