import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Macro Lab: Money Velocity, Inflation & AD-AS",
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
        font-size: 1.5rem;
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

total_final_score = st.session_state.sim_points + st.session_state.quiz_score

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("## 🇮🇳 Macroeconomic Portal")
    module = st.radio(
        "Select Module:",
        [
            "📈 Module 1: AD-AS & Money Velocity Simulator (50 Pts)",
            "📝 Module 2: Macro Mastery Assessment (50 Pts)"
        ]
    )
    st.markdown("---")
    st.markdown("### 🏆 Combined Scoreboard")
    st.markdown(f"**Simulation Lab:** {st.session_state.sim_points} / 50")
    st.markdown(f"**Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Total Mastery:** {total_final_score} / 100")
    if total_final_score == 100:
        st.success("🌟 Perfect Macroeconomic Score!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(f"""
<div class="score-banner">
    <h2 style="color: #34D399; margin: 0;">Macro Equilibrium & Monetarist Tracker: {total_final_score} / 100</h2>
    <p style="color: #94A3B8; margin: 0.25rem 0 0 0;">
        Simulation Lab: <b>{st.session_state.sim_points}/50 Pts</b> | Conceptual MCQs: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# MODULE 1: SIMULATION LAB (50 POINTS)
# =====================================================================
if module == "📈 Module 1: AD-AS & Money Velocity Simulator (50 Pts)":
    st.markdown("### 📈 Velocity of Money, Inflation, and AD–AS Equilibrium")
    st.markdown("""
    Model the **Classical Equation of Exchange** ($M \\cdot V = P \\cdot Y$) and short-run macroeconomic clearing. 
    Analyze how shifts in broad money supply ($M_3$), transaction velocity ($V$), and supply-side energy/input shocks 
    affect the **General Price Level ($P$)** and **Real GDP ($Y$)**.
    """)

    col1, col2 = st.columns([1, 1.3], gap="medium")

    with col1:
        st.subheader("🛠️ Macroeconomic Levers")

        money_supply = st.slider(
            "1. Money Stock (M3 Supply Index):",
            min_value=80.0, max_value=220.0, value=120.0, step=5.0,
            help="Total broad money stock circulating in the economy."
        )

        velocity = st.slider(
            "2. Velocity of Circulation (V):",
            min_value=1.0, max_value=2.5, value=1.5, step=0.05,
            help="Number of times an average rupee turns over for final transactions per year."
        )

        supply_shock = st.slider(
            "3. Supply Shock Index (Oil / Agricultural Costs):",
            min_value=-25.0, max_value=25.0, value=0.0, step=1.0,
            help="Adverse (positive value) or favorable (negative value) cost shocks shifting SRAS."
        )

        potential_output = 140.0  # LRAS benchmark (Potential Real GDP)

        # Theoretical Solver:
        # Nominal GDP = M * V
        # AD: P = (M * V) / Y  ==> In linear SR approximation:
        # AD: P = a_ad - b_ad * Y, where a_ad scales with (M * V)
        # SRAS: P = P_base + c_as * (Y - Y_pot) + supply_shock
        # Equilibrium clearance:
        nominal_gdp = money_supply * velocity
        
        # Solving linear clearing for visualization:
        # AD: Y = (M * V) / P
        # SRAS curve: P = 100 + 0.6 * (Y - potential_output) + supply_shock
        # Solving quadratic or linear approximation:
        # Approximate equilibrium around base price 100:
        y_eq = potential_output + ((nominal_gdp - (100.0 + supply_shock) * potential_output) / 
                                   (100.0 + 0.6 * potential_output + 1.2 * nominal_gdp / potential_output))
        y_eq = round(max(90.0, min(180.0, y_eq)), 2)
        p_eq = round(nominal_gdp / y_eq, 2)
        inflation_gap = round(((p_eq - 100.0) / 100.0) * 100, 2)
        output_gap = round(((y_eq - potential_output) / potential_output) * 100, 2)

        st.markdown("---")
        st.markdown("#### 🎯 Policy Target: The 'Goldilocks' Balance")
        st.caption(
            "Calibrate $M$ and manage velocity so that **Price Index ($P$) is between 100 and 110** "
            "and **Real Output ($Y$) is at or above Potential Output (140.0)** without overheating."
        )

        if st.button("Evaluate Stabilization Policy"):
            if 100.0 <= p_eq <= 110.0 and y_eq >= 140.0:
                st.session_state.sim_points = 50
                st.session_state.sim_completed = True
                st.success("✅ Target met! Price stability maintained at full employment potential. Awarded: 50 / 50 Pts.")
            else:
                st.session_state.sim_points = 25
                st.session_state.sim_completed = True
                st.warning("⚠️ Stagflationary or overheating divergence detected. Policy levers need fine-tuning. Awarded: 25 / 50 Pts.")
            st.rerun()

    with col2:
        st.subheader("📊 Output-Inflation Clearance")

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Price Level (P)</div>
                <div class="metric-val">{p_eq:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Real GDP (Y)</div>
                <div class="metric-val" style="color: #10B981;">{y_eq:.1f}</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Nominal GDP (M·V)</div>
                <div class="metric-val" style="color: #F87171;">₹{nominal_gdp:.0f}</div>
            </div>
            """, unsafe_allow_html=True)

        # Plot AD, SRAS, and LRAS curves
        y_range = np.linspace(100.0, 180.0, 40)
        ad_curve = nominal_gdp / y_range
        sras_curve = 100.0 + 0.6 * (y_range - potential_output) + supply_shock

        chart_df = pd.DataFrame({
            "Real Output (Y)": np.round(y_range, 1),
            "Aggregate Demand (AD)": np.round(ad_curve, 2),
            "Short-Run Aggregate Supply (SRAS)": np.round(sras_curve, 2)
        }).set_index("Real Output (Y)")

        st.line_chart(chart_df)
        st.caption(f"📍 Equilibrium: Price Level P* = {p_eq:.2f} | Real Output Y* = {y_eq:.1f} | Output Gap = {output_gap:+.2f}%")

# =====================================================================
# MODULE 2: MCQ ASSESSMENT (50 POINTS)
# =====================================================================
elif module == "📝 Module 2: Macro Mastery Assessment (50 Pts)":
    st.markdown("### 📝 Concepts in Velocity, Price Levels, AD, and AS")
    st.markdown("Test your understanding of the monetary transmission mechanism and aggregate equilibrium (10 points each).")

    with st.form("macro_ad_as_quiz"):
        st.markdown("#### 1. The Quantity Theory of Money")
        q1 = st.radio(
            "According to the Equation of Exchange ($M \\cdot V = P \\cdot Y$), if real output ($Y$) and velocity ($V$) are constant in the long run, a 7% increase in the money supply ($M$) directly leads to:",
            [
                "A) A 7% increase in the price level (P).",
                "B) A 7% decrease in the interest rate with zero inflation.",
                "C) A 14% increase in real production capacity.",
                "D) A permanent decline in velocity."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 2. Determinants of Velocity")
        q2 = st.radio(
            "How does rapid adoption of digital payment infrastructure (like UPI in India) typically influence the transaction velocity of money ($V$)?",
            [
                "A) It drives velocity to zero because physical cash is unused.",
                "B) It tends to increase velocity by lowering transaction friction and clearing balances faster.",
                "C) It has no relationship with money movement.",
                "D) It decreases velocity because households hoard more bank deposits."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 3. Aggregate Demand Downward Slope")
        q3 = st.radio(
            "Why does the Aggregate Demand (AD) curve slope downward with respect to the price level?",
            [
                "A) Higher prices cause firms to supply higher volumes of manufactured goods.",
                "B) The wealth effect, interest rate effect, and net export effect reduce real expenditures as prices rise.",
                "C) Central banks always cut rates when prices increase.",
                "D) Consumer preferences shift exclusively to luxury goods."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 4. Supply Shocks and Stagflation")
        q4 = st.radio(
            "If crude oil prices sharply escalate (a negative/adverse aggregate supply shock), what is the short-run effect on the AD–AS framework?",
            [
                "A) The SRAS curve shifts left/upward, causing higher price levels and lower real output (stagflation).",
                "B) The AD curve shifts right, lowering unemployment without price changes.",
                "C) Both real output and the price level fall simultaneously.",
                "D) Potential output (LRAS) expands immediately."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 5. Long-Run Classical Aggregate Supply")
        q5 = st.radio(
            "Why is the Long-Run Aggregate Supply (LRAS) curve represented as a vertical line at potential GDP ($Y^*$)?",
            [
                "A) In the long run, wages and prices are fully flexible, meaning real output is dictated by technology, capital, and labor, not the price level.",
                "B) Governments set fixed price caps on all final retail products.",
                "C) Central banks prevent nominal wages from adjusting.",
                "D) Money supply cannot grow faster than the population rate."
            ], index=None
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Calculate Final Score")

        if submit_quiz:
            correct_keys = {
                "q1": "A) A 7% increase in the price level (P).",
                "q2": "B) It tends to increase velocity by lowering transaction friction and clearing balances faster.",
                "q3": "B) The wealth effect, interest rate effect, and net export effect reduce real expenditures as prices rise.",
                "q4": "A) The SRAS curve shifts left/upward, causing higher price levels and lower real output (stagflation).",
                "q5": "A) In the long run, wages and prices are fully flexible, meaning real output is dictated by technology, capital, and labor, not the price level."
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
            st.error("❌ **Q1 Review:** Under classical neutrality ($M \\cdot V = P \\cdot Y$), with $V$ and $Y$ fixed, money growth maps 1:1 to price level growth.")
        if not rec.get("q2", False):
            st.error("❌ **Q2 Review:** Financial technologies reduce cash drag and transaction settlement times, boosting the velocity of circulation.")
        if not rec.get("q3", False):
            st.error("❌ **Q3 Review:** The AD curve slopes downward due to the Pigou wealth effect, Keynesian interest rate effect, and Mundell-Fleming exchange rate/net export effect.")
        if not rec.get("q4", False):
            st.error("❌ **Q4 Review:** Adverse cost-push shocks shift the SRAS curve leftward/upward, reducing output and driving up prices (stagflation).")
        if not rec.get("q5", False):
            st.error("❌ **Q5 Review:** LRAS is vertical because nominal price changes do not alter real production capabilities when factor markets clear.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("🇮🇳 Indian Macroeconomic Education Module")
with f2:
    st.caption("⚡ Velocity, Inflation & AD-AS Mechanics")
with f3:
    st.caption(f"⏰ System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
