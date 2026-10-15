import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Macro Lab: Goods Market Equilibrium & The IS Curve",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Slate & Amber Theme)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .stApp {
        background: radial-gradient(circle at 15% 15%, #0B192C 0%, #06101E 60%, #020617 100%);
        color: #E2E8F0;
    }
    
    .score-banner {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(14, 165, 233, 0.15) 100%);
        border: 1px solid rgba(251, 191, 36, 0.3);
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
        font-size: 1.5rem;
        font-weight: 800;
        margin-top: 0.25rem;
    }
    
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
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

total_final_score = st.session_state.sim_points + st.session_state.quiz_score

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("## 🏛️ Goods Market Portal")
    module = st.radio(
        "Select Module:",
        [
            "📈 Module 1: Saving, Investment & IS Simulator (50 Pts)",
            "📝 Module 2: IS Curve Mastery Assessment (50 Pts)"
        ]
    )
    st.markdown("---")
    st.markdown("### 🏆 Combined Scoreboard")
    st.markdown(f"**Simulation Lab:** {st.session_state.sim_points} / 50")
    st.markdown(f"**Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Total Mastery:** {total_final_score} / 100")
    if total_final_score == 100:
        st.success("🌟 Perfect Goods Market Mastery!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(f"""
<div class="score-banner">
    <h2 style="color: #FBBF24; margin: 0;">Goods Market & IS Equilibrium Tracker: {total_final_score} / 100</h2>
    <p style="color: #94A3B8; margin: 0.25rem 0 0 0;">
        Simulation Lab: <b>{st.session_state.sim_points}/50 Pts</b> | Conceptual MCQs: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# MODULE 1: SIMULATION LAB (50 POINTS)
# =====================================================================
if module == "📈 Module 1: Saving, Investment & IS Simulator (50 Pts)":
    st.markdown("### 📈 Goods Market Clearing: Saving = Investment & The IS Curve")
    st.markdown("""
    Explore the equilibrium where **Total Leakages equal Total Injections** ($S + T = I + G$).
    
    The goods market clears along the **IS curve**, given by:
    $$Y = \\frac{1}{1 - c(1 - t)} \\cdot \\left[ c_0 - c \\cdot T_0 + I_0 - d \\cdot r + G \\right]$$
    """)

    col1, col2 = st.columns([1, 1.3], gap="medium")

    with col1:
        st.subheader("🛠️ Behavioral & Policy Levers")

        mpc = st.slider(
            "1. Marginal Propensity to Consume (c):",
            min_value=0.50, max_value=0.90, value=0.75, step=0.05,
            help="Fraction of disposable income consumed. Determines the multiplier k = 1 / [1 - c(1 - t)]."
        )

        interest_rate = st.slider(
            "2. Real Interest Rate (r %):",
            min_value=1.0, max_value=12.0, value=5.0, step=0.5,
            help="Cost of borrowing. Higher rates decrease interest-sensitive investment spending."
        )

        gov_spending = st.slider(
            "3. Government Purchases (G):",
            min_value=100.0, max_value=500.0, value=250.0, step=25.0,
            help="Autonomous fiscal injection that shifts the IS curve rightward."
        )

        inv_sensitivity = st.slider(
            "4. Investment Sensitivity to Interest Rate (d):",
            min_value=10.0, max_value=60.0, value=30.0, step=5.0,
            help="Responsiveness of capital expenditure to changes in borrowing rates."
        )

        # Behavioral & policy parameters
        c0 = 120.0       # Autonomous consumption
        tax_rate = 0.20  # Flat income tax (t = 20%)
        t0 = 20.0        # Lump-sum tax
        i0 = 300.0       # Autonomous investment confidence

        # Multiplier & IS Engine
        multiplier = 1.0 / (1.0 - mpc * (1.0 - tax_rate))
        
        # Investment at current rate r
        planned_investment = i0 - (inv_sensitivity * interest_rate)
        
        # Autonomous spending excluding rate-sensitive investment
        autonomous_base = c0 - (mpc * t0) + i0 + gov_spending
        
        # Equilibrium Output Y*
        y_eq = multiplier * (autonomous_base - (inv_sensitivity * interest_rate))
        y_eq = round(max(400.0, min(2400.0, y_eq)), 2)

        # Disposable Income, Consumption, and Saving
        taxes = t0 + (tax_rate * y_eq)
        yd = y_eq - taxes
        consumption = c0 + (mpc * yd)
        private_saving = yd - consumption
        public_saving = taxes - gov_spending
        national_saving = private_saving + public_saving

        target_y_min = 1200.0
        target_y_max = 1450.0

        st.markdown("---")
        st.markdown("#### 🎯 Policy Target: Sustainable Potential GDP")
        st.caption(
            f"Tune fiscal policy ($G$) and borrowing rates ($r$) to reach equilibrium output "
            f"between **{target_y_min:.0f}** and **{target_y_max:.0f}** with positive investment."
        )

        if st.button("Evaluate Goods Market Equilibrium"):
            if target_y_min <= y_eq <= target_y_max and planned_investment > 0:
                st.session_state.sim_points = 50
                st.session_state.sim_completed = True
                st.success("✅ Equilibrium achieved within target output range! Awarded: 50 / 50 Pts.")
            else:
                st.session_state.sim_points = 25
                st.session_state.sim_completed = True
                st.warning("⚠️ Market equilibrium is outside target output range or investment is depressed. Awarded: 25 / 50 Pts.")
            st.rerun()

    with col2:
        st.subheader("📊 Goods Market Clearance")

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Equilibrium Output (Y*)</div>
                <div class="metric-val">{y_eq:.1f}</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Planned Investment (I)</div>
                <div class="metric-val" style="color: #10B981;">{planned_investment:.1f}</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Keynesian Multiplier (k)</div>
                <div class="metric-val" style="color: #F59E0B;">{multiplier:.2f}</div>
            </div>
            """, unsafe_allow_html=True)

        # Plotting the IS Curve across varying interest rates
        r_range = np.linspace(1.0, 14.0, 30)
        y_is_curve = multiplier * (autonomous_base - (inv_sensitivity * r_range))

        chart_df = pd.DataFrame({
            "Real Interest Rate (r %)": np.round(r_range, 1),
            "IS Curve (Goods Market Equilibrium Output Y)": np.round(y_is_curve, 1)
        }).set_index("Real Interest Rate (r %)")

        st.line_chart(chart_df)
        st.caption(
            f"📍 Current Equilibrium: r = {interest_rate:.1f}% | Y* = {y_eq:.1f} | "
            f"National Saving (S) = Planned Investment (I) = {planned_investment:.1f}"
        )

# =====================================================================
# MODULE 2: MCQ ASSESSMENT (50 POINTS)
# =====================================================================
elif module == "📝 Module 2: IS Curve Mastery Assessment (50 Pts)":
    st.markdown("### 📝 Concepts in Saving, Investment, and the IS Schedule")
    st.markdown("Assess your understanding of goods market equilibrium and multiplier dynamics (10 points each).")

    with st.form("goods_market_quiz"):
        st.markdown("#### 1. Goods Market Clearance Identity")
        q1 = st.radio(
            "In an open economy with government, what is the fundamental accounting condition for goods market equilibrium (the IS relation)?",
            [
                "A) S + T + M = I + G + X (Total Leakages = Total Injections)",
                "B) Money Supply = Money Demand",
                "C) Government Spending = Tax Receipts (Balanced Budget)",
                "D) Private Saving = Autonomous Consumption"
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 2. The Negative Slope of the IS Curve")
        q2 = st.radio(
            "Why does the IS curve slope downward in (Y, r) space?",
            [
                "A) A higher price level reduces the real purchasing power of cash balances.",
                "B) A higher interest rate increases the cost of borrowing, lowering planned investment and aggregate demand.",
                "C) Higher output raises liquidity preference, pushing up loan rates.",
                "D) Higher savings automatically reduce long-term capital productivity."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 3. Shifts in the IS Curve")
        q3 = st.radio(
            "Which of the following actions causes the IS curve to shift to the right?",
            [
                "A) A reduction in government purchases (G).",
                "B) An increase in autonomous taxes (T0).",
                "C) An increase in business investor confidence that raises autonomous investment (I0).",
                "D) A contractionary monetary policy implemented by the central bank."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 4. The Paradox of Thrift")
        q4 = st.radio(
            "According to Keynesian theory, if all households attempt to increase autonomous saving without an increase in investment demand:",
            [
                "A) National output expands due to an abundance of loanable funds.",
                "B) Aggregate expenditure drops, reducing equilibrium income so total realized savings remains unchanged or declines.",
                "C) The IS curve shifts outward to the right.",
                "D) Capital investment surges unconditionally."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 5. Steepness and Slope Sensitivity")
        q5 = st.radio(
            "What condition makes the IS curve relatively flatter (more interest-elastic)?",
            [
                "A) Investment demand is highly sensitive to the real interest rate (large d) and the multiplier is large.",
                "B) Investment is completely insensitive to interest rates (d = 0).",
                "C) The marginal propensity to consume is close to zero.",
                "D) The tax rate is 100%."
            ], index=None
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Calculate Final Score")

        if submit_quiz:
            correct_keys = {
                "q1": "A) S + T + M = I + G + X (Total Leakages = Total Injections)",
                "q2": "B) A higher interest rate increases the cost of borrowing, lowering planned investment and aggregate demand.",
                "q3": "C) An increase in business investor confidence that raises autonomous investment (I0).",
                "q4": "B) Aggregate expenditure drops, reducing equilibrium income so total realized savings remains unchanged or declines.",
                "q5": "A) Investment demand is highly sensitive to the real interest rate (large d) and the multiplier is large."
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
            st.error("❌ **Q1 Review:** Goods market equilibrium requires leakages ($S + T + M$) to equal injections ($I + G + X$).")
        if not rec.get("q2", False):
            st.error("❌ **Q2 Review:** Higher interest rates raise the cost of financing capital projects, curtailing investment and aggregate income.")
        if not rec.get("q3", False):
            st.error("❌ **Q3 Review:** Positive shifts in autonomous spending ($C_0, I_0, G$) shift the IS curve rightward by $\\Delta A \\times \\text{multiplier}$.")
        if not rec.get("q4", False):
            st.error("❌ **Q4 Review:** The Paradox of Thrift shows an autonomous push to save lowers consumption demand, reducing output until saving balances lower investment.")
        if not rec.get("q5", False):
            st.error("❌ **Q5 Review:** The slope of the IS curve is $-\\frac{1 - c(1-t)}{d}$. High sensitivity $d$ and high multiplier make the curve flatter.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("🏛️ Macroeconomic Analysis Portal")
with f2:
    st.caption("⚡ Goods Market Clearing & IS Schedule Dynamics")
with f3:
    st.caption(f"⏰ System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
