import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# CONFIGURATION & GLOBAL PALETTE
# =====================================================================
st.set_page_config(
    page_title="Macroeconomic Capital & Policy Simulator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Design: Midnight Obsidian + Emerald + Electric Cyan
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .stApp {
        background: radial-gradient(circle at 15% 15%, #0d1b2a 0%, #050c14 60%, #010408 100%);
        color: #E2E8F0;
    }
    
    .header-box {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.12) 0%, rgba(14, 165, 233, 0.12) 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 12px;
        padding: 1.3rem;
        margin-bottom: 1.5rem;
    }
    
    .metric-panel {
        background: rgba(13, 27, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .metric-title {
        color: #94A3B8;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .metric-val {
        color: #38BDF8;
        font-size: 1.7rem;
        font-weight: 800;
        margin-top: 0.3rem;
    }
    
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.65rem 1.6rem !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SESSION STATE ENGINE
# =====================================================================
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "eval_records" not in st.session_state:
    st.session_state.eval_records = {}

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("## 🏛️ Macroeconomic Nexus")
    module = st.radio(
        "Select Operating Plane:",
        ["⚡ Policy Simulation Lab", "🎯 High-Stakes Assessment Deck"]
    )
    st.markdown("---")
    st.markdown("**Core Framework:**")
    st.caption("• Classical Loanable Funds Clearing\n• Fiscal Deficit Crowding-Out\n• Fisherian Interest Mechanics\n• Keynesian Liquidity Traps")

# =====================================================================
# MODULE 1: SIMULATION LAB
# =====================================================================
if module == "⚡ Policy Simulation Lab":
    st.markdown("""
    <div class="header-box">
        <h2 style="color: #38BDF8; margin: 0;">Loanable Funds Equilibrium & Crowding-Out Engine</h2>
        <p style="color: #94A3B8; margin: 0.3rem 0 0 0;">
            Simulate the interaction between National Saving (Supply) and Physical Investment Demand under varying macroeconomic regimes.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_ctrl, col_viz = st.columns([1, 1.3], gap="medium")

    with col_ctrl:
        st.subheader("🛠️ Policy Shock Vectors")
        
        fiscal_deficit = st.slider(
            "Fiscal Deficit (G - T):", 
            min_value=-150.0, max_value=300.0, value=60.0, step=10.0, 
            help="Positive = Budget Deficit; Negative = Surplus."
        )
        
        autonomous_saving = st.slider(
            "Autonomous Private Thriftiness (S₀):", 
            min_value=50.0, max_value=400.0, value=200.0, step=10.0,
            help="Structural shift in private baseline propensity to save."
        )
        
        capital_productivity = st.slider(
            "Capital Productivity & Optimism (I₀):", 
            min_value=200.0, max_value=600.0, value=400.0, step=10.0,
            help="Autonomous firm willingness to invest given technological returns."
        )
        
        nco_inflows = st.slider(
            "Net Foreign Capital Inflow (Imports - Exports):", 
            min_value=-100.0, max_value=200.0, value=20.0, step=10.0,
            help="Net inflow of international loanable capital."
        )

        st.subheader("📈 Structural Elasticities")
        s_elasticity = st.slider("Interest Elasticity of Saving (dS/dr):", 10.0, 60.0, 30.0, 5.0)
        i_elasticity = st.slider("Interest Elasticity of Investment (dI/dr):", 10.0, 60.0, 35.0, 5.0)

        # Baseline parameters
        base_s0, base_i0, base_def = 200.0, 400.0, 0.0
        r_base = (base_i0 - (base_s0 - base_def)) / (s_elasticity + i_elasticity)
        vol_base = base_i0 - (i_elasticity * r_base)

        effective_saving_intercept = (autonomous_saving - fiscal_deficit + nco_inflows)
        r_eq = (capital_productivity - effective_saving_intercept) / (s_elasticity + i_elasticity)
        r_eq = max(0.2, r_eq)
        vol_eq = max(10.0, capital_productivity - (i_elasticity * r_eq))

        investment_displacement = vol_base - vol_eq

    with col_viz:
        st.subheader("📊 Dynamic Market Clearance")
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Equilibrium Rate (r*)</div>
                <div class="metric-val">{r_eq:.2f}%</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Cleared Volume (S* = I*)</div>
                <div class="metric-val" style="color: #10B981;">${vol_eq:,.1f}B</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            displacement_color = "#F87171" if investment_displacement > 0 else "#34D399"
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Capital Displaced</div>
                <div class="metric-val" style="color: {displacement_color};">${abs(investment_displacement):,.1f}B</div>
            </div>
            """, unsafe_allow_html=True)

        rates = np.linspace(1.0, 12.0, 50)
        s_curve = effective_saving_intercept + (s_elasticity * rates)
        i_curve = capital_productivity - (i_elasticity * rates)

        chart_data = pd.DataFrame({
            "Real Interest Rate (r%)": np.round(rates, 2),
            "National Saving Supply [S]": s_curve,
            "Investment Demand [I]": i_curve
        }).set_index("Real Interest Rate (r%)")

        st.line_chart(chart_data)
        st.caption(f"📍 Current Equilibrium Point: r* = {r_eq:.2f}% | Cleared Volume = ${vol_eq:,.1f}B")

# =====================================================================
# MODULE 2: HIGH-STAKES ASSESSMENT DECK
# =====================================================================
elif module == "🎯 High-Stakes Assessment Deck":
    st.markdown("""
    <div class="header-box">
        <h2 style="color: #38BDF8; margin: 0;">Advanced Macroeconomic Evaluation</h2>
        <p style="color: #94A3B8; margin: 0.3rem 0 0 0;">
            Rigorous scenarios on saving-investment coordination, portfolio substitution, and open-market interactions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("hardcore_macro_quiz"):
        st.markdown("#### Question 1: The Paradox of Thrift with Induced Investment")
        q1 = st.radio(
            "In a Keynesian macroeconomic framework where investment is not merely autonomous but also depends positively on aggregate income (I = I₀ + dY), "
            "what is the impact of an exogenous increase in the private marginal propensity to save?",
            [
                "A) Realized aggregate saving increases because higher saving reduces the real interest rate in the money market.",
                "B) Realized national saving remains strictly invariant, as saving must balance autonomous investment at the new equilibrium output.",
                "C) Realized aggregate national saving paradoxically falls, while aggregate output contracts by more than in the fixed-investment case.",
                "D) Aggregate output declines, but realized national saving rises to equalize the increased steady-state capital stock."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### Question 2: Barro-Ricardo Equivalence & Public Debt Dynamics")
        q2 = st.radio(
            "Under the assumptions of Ricardian Equivalence (infinite horizons, non-distortionary taxes, perfect capital markets), "
            "if the government enacts a temporary debt-financed tax cut while holding the path of public expenditures constant:",
            [
                "A) The supply of loanable funds contracts because the government borrows from the public, driving the real interest rate higher.",
                "B) Private saving expands by exactly the amount of the tax cut, neutralizing the public dissaving and keeping the real rate unchanged.",
                "C) Real interest rates decrease because consumer liquidity surges, driving up commercial bank reserve holdings.",
                "D) Aggregate demand expands via permanent income wealth effects, triggering demand-pull inflation."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### Question 3: The Mundell-Tobin Effect & The Fisher Identity")
        q3 = st.radio(
            "According to the Mundell-Tobin effect, how does an increase in anticipated inflation (πᵉ) alter the classical Fisher equation (i = r + πᵉ)?",
            [
                "A) The nominal rate (i) rises by more than 1:1 with πᵉ because lenders demand an inflation risk premium.",
                "B) The nominal rate rises by less than 1:1 with πᵉ because rising inflation lowers real money balances, inducing households to hold physical capital, which depresses the equilibrium real rate (r).",
                "C) The real rate (r) remains strictly fixed because money is neutral in the long run across all asset structures.",
                "D) The real rate (r) spikes upward because inflation accelerates the capital depreciation rate."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### Question 4: Open-Economy Fiscal Transmission (Mundell-Fleming)")
        q4 = st.radio(
            "In a small open economy characterized by perfect capital mobility and floating exchange rates, "
            "what is the true mechanism of 'crowding out' following an expansionary fiscal deficit (G > T)?",
            [
                "A) Domestic real interest rates rise above the world rate (r > r*), choking off domestic corporate capital expenditures.",
                "B) Domestic interest rates remain pinned to the world interest rate (r = r*); the exchange rate appreciates, crowding out Net Exports (NX) completely.",
                "C) Capital flight occurs, causing the currency to sharply depreciate and driving inflation to statutory maximums.",
                "D) Domestic saving surges via compulsory import taxes, generating a permanent trade surplus."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### Question 5: Capital Market Clearing at the Zero Lower Bound")
        q5 = st.radio(
            "In an economy trapped at the Zero Lower Bound (nominal rate i = 0) with lingering deflation (π < 0), "
            "why can the market for loanable funds fail to automatically clear at full employment?",
            [
                "A) The nominal interest rate cannot turn negative, meaning expected deflation forces the ex-ante real rate (r = i - πᵉ) to remain elevated, suppressing investment below full-employment saving.",
                "B) At the zero lower bound, private investment demand becomes infinitely interest-elastic, depleting the banking sector.",
                "C) Household saving collapses to zero because zero nominal yields eliminate any financial incentive to defer consumption.",
                "D) The central bank loses the legal authority to conduct quantitative asset purchases."
            ], index=None
        )

        submitted = st.form_submit_button("Submit Assessment & Reveal Diagnostics")

        if submitted:
            correct_answers = {
                "q1": "C) Realized aggregate national saving paradoxically falls, while aggregate output contracts by more than in the fixed-investment case.",
                "q2": "B) Private saving expands by exactly the amount of the tax cut, neutralizing the public dissaving and keeping the real rate unchanged.",
                "q3": "B) The nominal rate rises by less than 1:1 with πᵉ because rising inflation lowers real money balances, inducing households to hold physical capital, which depresses the equilibrium real rate (r).",
                "q4": "B) Domestic interest rates remain pinned to the world interest rate (r = r*); the exchange rate appreciates, crowding out Net Exports (NX) completely.",
                "q5": "A) The nominal interest rate cannot turn negative, meaning expected deflation forces the ex-ante real rate (r = i - πᵉ) to remain elevated, suppressing investment below full-employment saving."
            }
            
            records = {
                "q1": (q1 == correct_answers["q1"]),
                "q2": (q2 == correct_answers["q2"]),
                "q3": (q3 == correct_answers["q3"]),
                "q4": (q4 == correct_answers["q4"]),
                "q5": (q5 == correct_answers["q5"])
            }

            st.session_state.quiz_score = sum(records.values()) * 20
            st.session_state.quiz_submitted = True
            st.session_state.eval_records = records
            st.rerun()

    if st.session_state.quiz_submitted:
        st.markdown("---")
        score = st.session_state.quiz_score
        color = "#10B981" if score >= 80 else ("#F59E0B" if score >= 40 else "#EF4444")
        st.markdown(f"### Performance Grade: <span style='color: {color};'>{score} / 100</span>", unsafe_allow_html=True)

        rec = st.session_state.eval_records
        if not rec.get("q1", False):
            st.error("**Q1 Clarification (Paradox of Thrift):** In the presence of an induced investment function (I = I₀ + dY), higher thrift cuts output, which directly reduces investment. Because realized S must equal realized I in equilibrium, total realized saving must *fall*, not just stay constant.")
        if not rec.get("q2", False):
            st.error("**Q2 Clarification (Ricardian Equivalence):** Rational forward-looking agents realize debt issued today is future taxes in disguise. Hence, the marginal propensity to consume out of a debt-financed tax rebate is 0. Private saving rises by 100% of the cut, fully offsetting public dissaving.")
        if not rec.get("q3", False):
            st.error("**Q3 Clarification (Mundell-Tobin Effect):** Anticipated inflation penalizes cash holdings. Wealth is shifted out of money balances into physical productive capital, driving up the capital-labor ratio, reducing the marginal product of capital, and reducing the equilibrium real rate.")
        if not rec.get("q4", False):
            st.error("**Q4 Clarification (Mundell-Fleming Crowding-Out):** Perfect capital mobility ties domestic interest rates to world rates (r = r*). Fiscal expansion triggers incipient capital inflows that appreciate the exchange rate, totally displacing Net Exports rather than domestic investment.")
        if not rec.get("q5", False):
            st.error("**Q5 Clarification (Zero Lower Bound Trap):** When i = 0, deflation (πᵉ < 0) implies r = 0 - (-|πᵉ|) = +|πᵉ| > 0. The real rate is mechanically wedged above zero, preventing investment from expanding to clear the excess supply of savings.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
st.caption(f"⚡ Policy & Capital Clearing Engine | Platform System Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
