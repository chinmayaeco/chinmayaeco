import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Saving, Investment & Interest Rate Lab",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Slate & Emerald Theme)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .stApp {
        background: radial-gradient(circle at 15% 15%, #0B192C 0%, #06101E 60%, #020617 100%);
        color: #E2E8F0;
    }
    
    .score-banner {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(14, 165, 233, 0.15) 100%);
        border: 1px solid rgba(52, 211, 153, 0.3);
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .metric-panel {
        background: rgba(15, 23, 42, 0.7);
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
    }
    .metric-val {
        color: #38BDF8;
        font-size: 1.6rem;
        font-weight: 800;
        margin-top: 0.25rem;
    }
    
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.6rem !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

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

# Calculate Unified Score
total_final_score = st.session_state.sim_points + st.session_state.quiz_score

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("## 🇮🇳 Macroeconomic Portal")
    module = st.radio(
        "Navigation:",
        ["📈 Step 1: Policy Simulator (50 Pts)", "📝 Step 2: Knowledge Assessment (50 Pts)"]
    )
    st.markdown("---")
    st.markdown("### 🏆 Combined Scoreboard")
    st.markdown(f"**Simulation Lab:** {st.session_state.sim_points} / 50")
    st.markdown(f"**MCQ Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Total Mastery:** {total_final_score} / 100")
    if total_final_score == 100:
        st.success("🌟 Perfect Macroeconomic Score!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(f"""
<div class="score-banner">
    <h2 style="color: #34D399; margin: 0;">Aggregate Macro Performance: {total_final_score} / 100</h2>
    <p style="color: #94A3B8; margin: 0.25rem 0 0 0;">
        Simulation Lab: <b>{st.session_state.sim_points}/50 Pts</b> | Conceptual MCQs: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# MODULE 1: SIMULATION LAB (50 POINTS)
# =====================================================================
if module == "📈 Step 1: Policy Simulator (50 Pts)":
    st.markdown("### 📈 Simple Loanable Funds & Policy Rate Simulator")
    st.markdown("""
    Explore how household savings, corporate investment appetite, government borrowing, and the RBI policy benchmark 
    determine the real interest rate and total capital cleared in India's financial system.
    """)

    col1, col2 = st.columns([1, 1.3], gap="medium")

    with col1:
        st.subheader("🛠️ Macro Levers")
        
        household_savings = st.slider(
            "1. Household Savings Base (₹ Crore):",
            min_value=20000, max_value=80000, value=45000, step=2500,
            help="Higher savings expand the pool of loanable funds."
        )
        
        corp_investment = st.slider(
            "2. Corporate Investment Demand (₹ Crore):",
            min_value=20000, max_value=80000, value=50000, step=2500,
            help="Businesses borrowing funds to build factories, infrastructure, and machinery."
        )
        
        govt_borrowing = st.slider(
            "3. Govt. Fiscal Deficit Borrowing (₹ Crore):",
            min_value=0, max_value=30000, value=10000, step=1000,
            help="Government competing for private savings to fund the deficit."
        )
        
        rbi_repo_bias = st.slider(
            "4. RBI Benchmark Repo Anchor (%):",
            min_value=3.5, max_value=8.5, value=6.5, step=0.25,
            help="Base cost of money influenced by central bank policy."
        )

        # Theoretical Equilibrium Solver
        # Net funds available = Household Savings - Govt Borrowing + sensitivity * r
        # Investment demand = Corporate Investment - sensitivity * r
        # Clearing: rate adjusts to balance funds
        excess_demand = corp_investment - (household_savings - govt_borrowing)
        r_eq = rbi_repo_bias + (excess_demand / 12000.0)
        r_eq = round(max(3.0, min(14.0, r_eq)), 2)
        cleared_funds = int(max(10000, corp_investment - (r_eq - rbi_repo_bias) * 1800))

        st.markdown("---")
        st.markdown("#### 🎯 Policy Mission: Stabilize the Economy")
        st.caption("Adjust sliders so that the **Market Interest Rate settles between 6.50% and 7.50%** and **Cleared Capital is at least ₹45,000 Crore**.")
        
        if st.button("Evaluate Simulation Policy"):
            if 6.50 <= r_eq <= 7.50 and cleared_funds >= 45000:
                st.session_state.sim_points = 50
                st.session_state.sim_completed = True
                st.success("✅ Excellent policy coordination! Equilibrium achieved. Awarded: 50 / 50 Pts.")
            else:
                st.session_state.sim_points = 25
                st.session_state.sim_completed = True
                st.warning("⚠️ Partial target achieved. Rate or capital volume out of the ideal stabilization band. Awarded: 25 / 50 Pts.")
            st.rerun()

    with col2:
        st.subheader("📊 Indian Financial Market Clearance")
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Equilibrium Interest Rate</div>
                <div class="metric-val">{r_eq:.2f}%</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Cleared Investment (S = I)</div>
                <div class="metric-val" style="color: #10B981;">₹{cleared_funds:,} Cr</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Govt. Absorption</div>
                <div class="metric-val" style="color: #F87171;">₹{govt_borrowing:,} Cr</div>
            </div>
            """, unsafe_allow_html=True)

        # Plot Supply and Demand for Funds
        rates = np.linspace(3.0, 14.0, 30)
        net_savings_curve = (household_savings - govt_borrowing) + (rates - rbi_repo_bias) * 3500
        investment_curve = corp_investment - (rates - rbi_repo_bias) * 3500

        chart_df = pd.DataFrame({
            "Interest Rate (%)": np.round(rates, 2),
            "Available Funds / Savings (₹ Cr)": net_savings_curve,
            "Investment Demand (₹ Cr)": investment_curve
        }).set_index("Interest Rate (%)")

        st.line_chart(chart_df)
        st.caption(f"📍 Market Equilibrium: r* = {r_eq:.2f}% | Cleared Capital = ₹{cleared_funds:,} Crore")

# =====================================================================
# MODULE 2: MCQ ASSESSMENT (50 POINTS)
# =====================================================================
elif module == "📝 Step 2: Knowledge Assessment (50 Pts)":
    st.markdown("### 📝 Concepts in Saving, Investment & Interest Rates")
    st.markdown("Answer these 5 core questions (10 points each). Your score will directly add to your final total.")

    with st.form("simple_macro_quiz"):
        st.markdown("#### 1. Real vs. Nominal Interest Rate")
        q1 = st.radio(
            "If an Indian commercial bank offers an interest rate of 8% on fixed deposits, and expected inflation is 5%, what is the real interest rate?",
            [
                "A) 13%",
                "B) 3%",
                "C) 1.6%",
                "D) 8%"
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 2. Determinants of Business Investment")
        q2 = st.radio(
            "When interest rates rise across commercial banks, what typically happens to planned business investment?",
            [
                "A) It decreases because borrowing costs for machinery and expansions increase.",
                "B) It increases because higher interest rates mean businesses make more revenue.",
                "C) It remains constant because investment depends solely on export demand.",
                "D) It increases because banks give discounts to corporate borrowers."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 3. Government Borrowing and Crowding-Out")
        q3 = st.radio(
            "What does 'crowding out' refer to in the loanable funds market?",
            [
                "A) When too many commercial banks open branches in the same city.",
                "B) When heavy government borrowing drives up interest rates, leaving fewer funds for private investment.",
                "C) When foreign investors take over all government bonds.",
                "D) When consumers spend all their savings on imported retail goods."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 4. The Incentive to Save")
        q4 = st.radio(
            "From a classical economic perspective, an increase in the real interest rate provides households with:",
            [
                "A) A greater reward for delaying current consumption and saving for the future.",
                "B) A strong incentive to borrow more money for personal travel.",
                "C) A reason to stop placing funds in bank accounts.",
                "D) An automatic reduction in total income taxes."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 5. Saving and Investment Identity")
        q5 = st.radio(
            "In a closed domestic economy without foreign trade, what equality must hold true in macroeconomic equilibrium?",
            [
                "A) National Saving = Total Domestic Investment",
                "B) Government Spending = Household Savings",
                "C) Bank Deposits = Total Tax Revenue",
                "D) Corporate Profit = Currency in Circulation"
            ], index=None
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Calculate Final Score")

        if submit_quiz:
            correct_keys = {
                "q1": "B) 3%",
                "q2": "A) It decreases because borrowing costs for machinery and expansions increase.",
                "q3": "B) When heavy government borrowing drives up interest rates, leaving fewer funds for private investment.",
                "q4": "A) A greater reward for delaying current consumption and saving for the future.",
                "q5": "A) National Saving = Total Domestic Investment"
            }

            records = {
                "q1": (q1 == correct_keys["q1"]),
                "q2": (q2 == correct_keys["q2"]),
                "q3": (q3 == correct_keys["q3"]),
                "q4": (q4 == correct_keys["q4"]),
                "q5": (q5 == correct_keys["q5"])
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
            st.error("❌ **Q1 Review:** Fisher Equation: Real Interest Rate = Nominal Rate (8%) - Inflation (5%) = 3%.")
        if not rec.get("q2", False):
            st.error("❌ **Q2 Review:** Higher interest rates make capital loans more expensive, lowering planned capital expenditures.")
        if not rec.get("q3", False):
            st.error("❌ **Q3 Review:** Crowding out occurs when state deficits absorb loanable funds and raise interest rates, displacing private firms.")
        if not rec.get("q4", False):
            st.error("❌ **Q4 Review:** Higher real interest rates reward saving by providing a greater intertemporal return.")
        if not rec.get("q5", False):
            st.error("❌ **Q5 Review:** In a closed economy, aggregate equilibrium requires National Saving (S) = Investment (I).")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("🇮🇳 Indian Macroeconomic Education Module")
with f2:
    st.caption("💰 Saving, Investment & Interest Rates")
with f3:
    st.caption(f"⏰ System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
