import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Loanable Funds & Interest Rate Policy Simulator",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# CORE DESIGN SYSTEM
# =====================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }

    .stApp { 
        background: radial-gradient(circle at top right, #0B192C 0%, #06101E 50%, #030712 100%);
    }

    .score-banner {
        background: linear-gradient(135deg, #0F2744 0%, #16325B 100%);
        border: 1px solid rgba(56, 189, 248, 0.35);
        color: #FFFFFF; 
        padding: 1.5rem; 
        border-radius: 14px; 
        text-align: center; 
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    }
    .score-banner h2 { 
        color: #38BDF8 !important; 
        margin: 0 !important; 
        font-weight: 700; 
        font-size: 1.6rem; 
    }

    .metric-card {
        background: rgba(6, 16, 30, 0.7); 
        border: 1px solid rgba(56, 189, 248, 0.18);
        padding: 1.25rem; 
        border-radius: 10px; 
        text-align: center;
    }
    .metric-card h3 { 
        color: #94A3B8; 
        font-size: 0.95rem; 
        margin: 0 0 0.5rem 0; 
        font-weight: 500;
    }
    .metric-value { 
        color: #38BDF8; 
        font-size: 1.85rem; 
        font-weight: 700; 
        margin: 0.25rem 0; 
    }

    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important; 
        color: white !important;
        border: none !important; 
        padding: 0.65rem 1.8rem !important; 
        border-radius: 8px !important;
        font-weight: 600 !important; 
    }

    .stMarkdown, p, li { 
        color: #CBD5E1 !important; 
        font-size: 0.98rem; 
        line-height: 1.65; 
    }
    .stSidebar { 
        background: #06101E !important; 
        border-right: 1px solid rgba(56, 189, 248, 0.12); 
    }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SESSION STATE INITIALIZATION
# =====================================================================
def init_system_state():
    defaults = {
        'knowledge_rating': 0.0,
        'quiz_done': False,
        'ans1_ok': False, 'ans2_ok': False, 'ans3_ok': False, 'ans4_ok': False, 'ans5_ok': False
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

init_system_state()

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("### 🏛️ Policy & Capital Markets")
    nav_selection = st.radio(
        "Module Navigation:",
        options=[
            "🎛️ Loanable Funds Policy Simulator",
            "📝 Rigorous Macroeconomic Assessment"
        ]
    )

# =====================================================================
# PERFORMANCE SCOREBOARD
# =====================================================================
score_container = st.container()
with score_container:
    st.markdown(f"""
    <div class="score-banner">
        <h2>Saving-Investment Equilibrium Mastery: {round(st.session_state.knowledge_rating, 1)} / 100</h2>
        <p style='color: #34D399; margin: 0.25rem 0 0 0;'>
            Classical Clearing | Crowding Out | IS Elasticity | Ricardian Equivalence | Fisher Relation
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# MODULE 1: POLICY SIMULATOR
# =====================================================================
if nav_selection == "🎛️ Loanable Funds Policy Simulator":
    st.markdown("### 🎛️ Macroeconomic Policy Shock Simulator: Saving, Investment & Equilibrium Rates")
    st.markdown("""
    Evaluate how fiscal shocks, private thriftiness shifts, capital productivity taxes, and open-economy capital flows 
    determine the real interest rate ($r^*$) and total volume of capital accumulation ($S^* = I^*$).
    """)

    sim_c1, sim_c2 = st.columns([1, 1.4])

    with sim_c1:
        st.markdown("#### 🏛️ Fiscal & Structural Controls")
        g_deficit = st.slider("Fiscal Deficit (G - T, Crowding-Out Pressure):", min_value=-200.0, max_value=400.0, value=100.0, step=10.0)
        private_thrift = st.slider("Marginal Propensity to Save Shift (Autonomous Saving):", min_value=-150.0, max_value=250.0, value=50.0, step=10.0)
        biz_confidence = st.slider("Capital Productivity & Animal Spirits (Autonomous I):", min_value=200.0, max_value=800.0, value=500.0, step=25.0)
        nco_inflow = st.slider("Net Capital Inflow from Abroad (Net Imports / NFI):", min_value=-100.0, max_value=200.0, value=0.0, step=10.0)
        
        st.markdown("#### 📐 Elasticity Parameters")
        s_slope = st.slider("Interest Elasticity of Saving (dS/dr):", min_value=10.0, max_value=80.0, value=35.0, step=5.0)
        i_slope = st.slider("Interest Sensitivity of Investment (dI/dr):", min_value=15.0, max_value=90.0, value=45.0, step=5.0)

        numerator = biz_confidence - (private_thrift - g_deficit + nco_inflow)
        denominator = s_slope + i_slope
        r_eq = max(0.25, numerator / denominator)
        funds_eq = biz_confidence - (i_slope * r_eq)
        crowding_out = max(0.0, g_deficit)

    with sim_c2:
        st.markdown("#### 📊 Real-Time Market Clearing")
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Equilibrium Real Rate (r*)</h3>
                <div class="metric-value">{r_eq:.2f}%</div>
                <p style="color: #94A3B8; font-size: 0.8rem;">Price of Loanable Funds</p>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Cleared Capital (S* = I*)</h3>
                <div class="metric-value" style="color: #34D399;">${funds_eq:,.1f}B</div>
                <p style="color: #94A3B8; font-size: 0.8rem;">Physical Capital Additions</p>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Fiscal Deficit Displacement</h3>
                <div class="metric-value" style="color: #F87171;">${crowding_out:,.1f}B</div>
                <p style="color: #94A3B8; font-size: 0.8rem;">Public Claim on Savings</p>
            </div>
            """, unsafe_allow_html=True)

        rates = np.linspace(0.5, 15.0, 100)
        s_curve = (private_thrift - g_deficit + nco_inflow) + (s_slope * rates)
        i_curve = biz_confidence - (i_slope * rates)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=s_curve, y=rates, mode='lines', name='National Saving (Supply)', line=dict(color='#38BDF8', width=3)))
        fig.add_trace(go.Scatter(x=i_curve, y=rates, mode='lines', name='Gross Investment (Demand)', line=dict(color='#FCD34D', width=3)))
        fig.add_trace(go.Scatter(x=[funds_eq], y=[r_eq], mode='markers+text', name='Equilibrium',
                                 marker=dict(size=12, color='#34D399'),
                                 text=[f"E* ({funds_eq:.1f}B, {r_eq:.2f}%)"], textposition="top right"))

        fig.update_layout(
            title="Loanable Funds Equilibrium Plane",
            xaxis_title="Quantity of Loanable Funds ($ Billions)",
            yaxis_title="Real Interest Rate (r %)",
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(15, 39, 68, 0.4)',
            margin=dict(l=30, r=30, t=40, b=30),
            height=380,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, use_container_width=True)

# =====================================================================
# MODULE 2: ASSESSMENT DECK
# =====================================================================
elif nav_selection == "📝 Rigorous Macroeconomic Assessment":
    st.markdown("### 📝 Master Examination: Saving-Investment Dynamics & Interest Rates")
    st.markdown("Carefully evaluate the theoretical interactions below. Watch out for classical assumptions versus Keynesian paradoxes and Ricardian conditions.")

    with st.form("macro_advanced_quiz"):
        st.markdown("#### 1. The Paradox of Thrift in Short vs. Long Run")
        q1 = st.radio(
            "In an economy operating with demand-constrained output and fixed investment sensitivity (Keynesian cross), "
            "an exogenous increase in the autonomous propensity to save causes which of the following equilibrium outcomes for total realized national saving?",
            options=[
                "A) Realized saving increases by an amount proportional to the shift in autonomous saving divided by the marginal propensity to consume.",
                "B) Realized saving remains unchanged (or declines if investment depends positively on income via an accelerator), while aggregate equilibrium output contracts.",
                "C) Realized saving rises, driving real interest rates downward and permanently increasing private steady-state capital stock.",
                "D) Realized saving strictly expands because planned saving and realized saving must converge ex-post by accounting identity."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 2. Fiscal Deficits, Ricardian Equivalence & Interest Rates")
        q2 = st.radio(
            "Suppose a government reduces lump-sum taxes today financed entirely by issuing sovereign debt, keeping government expenditures (G) completely constant. "
            "Under strict Barro-Ricardo Equivalence with rational agents possessing infinite horizons (or operational intergenerational bequests):",
            options=[
                "A) The supply curve for loanable funds shifts leftward due to the public deficit, driving the real interest rate upward.",
                "B) National saving is unaffected because private saving increases dollar-for-dollar to offset the public dissaving, leaving the real interest rate unchanged.",
                "C) Investment demand shifts rightward due to expected wealth expansion, raising real interest rates.",
                "D) The real interest rate drops because households deposit the entirety of the tax rebate into commercial banks, expanding reserve velocity."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 3. Fisher Effect and Neutrality Under Inflation Expectations")
        q3 = st.radio(
            "Assume the Mundell-Tobin effect is operative in money markets. When anticipated inflation increases, "
            "how does the nominal interest rate and the real interest rate adjust relative to the strict classical Fisher hypothesis?",
            options=[
                "A) Nominal interest rates rise more than point-for-point with inflation because risk premiums expand.",
                "B) The nominal interest rate rises by less than one-for-one with anticipated inflation, causing the equilibrium real interest rate to fall as wealth shifts from real money balances to real capital assets.",
                "C) The real interest rate increases because lenders demand compensation for capital depreciation caused by nominal bracket creep.",
                "D) The real and nominal rates move identically upward due to compounding term premiums."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 4. Open-Economy Capital Flows and Crowding Out")
        q4 = st.radio(
            "Consider a small open economy with perfect capital mobility and flexible exchange rates. When the national government runs an expansionary fiscal deficit (G increases):",
            options=[
                "A) Domestic real interest rates spike drastically above world rates, causing a severe collapse in domestic investment.",
                "B) The domestic real rate remains tethered to the world rate; upward rate pressure appreciates the domestic currency, completely crowding out net exports rather than domestic investment.",
                "C) Domestic saving surges via compulsory net factor imports, keeping the trade balance in surplus.",
                "D) Domestic investment drops to zero as foreign capital flight drains the domestic loanable funds pool."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 5. Elasticity Extremes and Liquidity Trap")
        q5 = st.radio(
            "In an economy trapped at the effective lower bound (liquidity trap) where the yield on short-term safe assets is zero, "
            "which statement regarding the Saving-Investment clearing mechanism is theoretically correct?",
            options=[
                "A) Real interest rates will automatically adjust downward to negative levels without price deflation to clear the capital market.",
                "B) The classical loanable funds model fails to guarantee equilibrium at full employment because expected deflation raises the ex-ante real interest rate, widening the excess supply of saving.",
                "C) Private investment expands infinitely because the nominal cost of borrowing funds is virtually zero.",
                "D) National saving collapses to zero because negative real returns eliminate any intertemporal incentive to defer consumption."
            ], index=None
        )

        eval_quiz = st.form_submit_button("Submit Advanced Assessment", type="primary")

        if eval_quiz:
            score_acc = 0.0

            if q1 == "B) Realized saving remains unchanged (or declines if investment depends positively on income via an accelerator), while aggregate equilibrium output contracts.":
                score_acc += 20.0
                st.session_state.ans1_ok = True
            else:
                st.session_state.ans1_ok = False

            if q2 == "B) National saving is unaffected because private saving increases dollar-for-dollar to offset the public dissaving, leaving the real interest rate unchanged.":
                score_acc += 20.0
                st.session_state.ans2_ok = True
            else:
                st.session_state.ans2_ok = False

            if q3 == "B) The nominal interest rate rises by less than one-for-one with anticipated inflation, causing the equilibrium real interest rate to fall as wealth shifts from real money balances to real capital assets.":
                score_acc += 20.0
                st.session_state.ans3_ok = True
            else:
                st.session_state.ans3_ok = False

            if q4 == "B) The domestic real rate remains tethered to the world rate; upward rate pressure appreciates the domestic currency, completely crowding out net exports rather than domestic investment.":
                score_acc += 20.0
                st.session_state.ans4_ok = True
            else:
                st.session_state.ans4_ok = False

            if q5 == "B) The classical loanable funds model fails to guarantee equilibrium at full employment because expected deflation raises the ex-ante real interest rate, widening the excess supply of saving.":
                score_acc += 20.0
                st.session_state.ans5_ok = True
            else:
                st.session_state.ans5_ok = False

            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### Assessment Score: **{round(st.session_state.knowledge_rating, 1)} / 100 Points**")

        if not st.session_state.ans1_ok:
            st.error("**Q1 Breakdown (Paradox of Thrift):** In demand-determined models where I is autonomous or fixed, equilibrium requires S = I. An individual desire to save more shifts the saving function upward, but aggregate income drops until actual saving equals the unchanged investment level.")
        if not st.session_state.ans2_ok:
            st.error("**Q2 Breakdown (Ricardian Equivalence):** Under Ricardian assumptions, consumers realize current debt-financed tax cuts imply higher future taxes of identical present value. They save 100% of the tax cut to pay future taxes, leaving national saving and real interest rates completely unchanged.")
        if not st.session_state.ans3_ok:
            st.error("**Q3 Breakdown (Mundell-Tobin Effect):** Expected inflation increases the opportunity cost of holding money, causing agents to rebalance their portfolios into physical capital. This portfolio shift depresses the marginal product of capital and lowers the equilibrium real interest rate.")
        if not st.session_state.ans4_ok:
            st.error("**Q4 Breakdown (Open Economy Crowding Out):** In a small open economy with perfect capital mobility, fiscal deficits attract foreign capital, causing exchange rate appreciation. The appreciation wipes out net exports (NX) until equilibrium returns, sparing domestic investment.")
        if not st.session_state.ans5_ok:
            st.error("**Q5 Breakdown (Liquidity Trap & Fisher Wedge):** At the Zero Lower Bound (i = 0), if prices fall, expected deflation causes the ex-ante real rate to rise, exacerbating the deficiency of investment relative to full-employment saving.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("📈 Capital Theory & Macro Allocations")
with f2:
    st.caption("⚖️ Loanable Funds Engine")
with f3:
    st.caption(f"⏰ Platform Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
