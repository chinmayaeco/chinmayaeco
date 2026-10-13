import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Macro Lab: Exchange Rates & Net Exports",
    page_icon="🌍",
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
    st.markdown("## 🌍 Open Economy Portal")
    module = st.radio(
        "Select Module:",
        [
            "🚢 Module 1: Net Exports & Exchange Rate Simulator (50 Pts)",
            "📝 Module 2: Open Economy Assessment (50 Pts)"
        ]
    )
    st.markdown("---")
    st.markdown("### 🏆 Combined Scoreboard")
    st.markdown(f"**Simulation Lab:** {st.session_state.sim_points} / 50")
    st.markdown(f"**Assessment:** {st.session_state.quiz_score} / 50")
    st.markdown(f"### **Total Mastery:** {total_final_score} / 100")
    if total_final_score == 100:
        st.success("🌟 Perfect Open Economy Mastery!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(f"""
<div class="score-banner">
    <h2 style="color: #FBBF24; margin: 0;">Trade Balance & Exchange Rate Tracker: {total_final_score} / 100</h2>
    <p style="color: #94A3B8; margin: 0.25rem 0 0 0;">
        Simulation Lab: <b>{st.session_state.sim_points}/50 Pts</b> | Conceptual MCQs: <b>{st.session_state.quiz_score}/50 Pts</b>
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# MODULE 1: SIMULATION LAB (50 POINTS)
# =====================================================================
if module == "🚢 Module 1: Net Exports & Exchange Rate Simulator (50 Pts)":
    st.markdown("### 🚢 The Trade Balance: Real Exchange Rates & Income")
    st.markdown("""
    Explore how domestic income ($Y$), foreign income ($Y^*$), and the real exchange rate ($\\epsilon$) dictate **Net Exports** ($NX = X - M$).
    
    The net export function is modeled as:
    $$NX(Y, Y^*, \\epsilon) = [X_0 + x_1 Y^* - x_2 \\epsilon] - [M_0 + m_1 Y + m_2 \\epsilon]$$
    *(Note: A higher $\\epsilon$ represents a real appreciation of the domestic currency, making exports expensive and imports cheap).*
    """)

    col1, col2 = st.columns([1, 1.3], gap="medium")

    with col1:
        st.subheader("🛠️ Economic Levers")

        real_ex_rate = st.slider(
            "1. Real Exchange Rate (ε):",
            min_value=0.5, max_value=2.0, value=1.0, step=0.1,
            help="Relative price of domestic goods in terms of foreign goods. Higher value = appreciated currency."
        )

        dom_income = st.slider(
            "2. Domestic Income (Y):",
            min_value=1000.0, max_value=5000.0, value=3000.0, step=250.0,
            help="Higher domestic income increases the demand for imported goods."
        )

        for_income = st.slider(
            "3. Foreign Income (Y*):",
            min_value=1000.0, max_value=5000.0, value=2500.0, step=250.0,
            help="Higher foreign income increases the foreign demand for domestic exports."
        )

        mpi = st.slider(
            "4. Marginal Propensity to Import (m₁):",
            min_value=0.05, max_value=0.30, value=0.15, step=0.01,
            help="Fraction of an additional dollar of domestic income spent on imports."
        )

        # Baseline parameters
        x0 = 200.0       # Base exports
        x1 = 0.20        # Sensitivity of exports to foreign income
        x2 = 400.0       # Sensitivity of exports to exchange rate
        
        m0 = 100.0       # Base imports
        m2 = 300.0       # Sensitivity of imports to exchange rate

        # Calculations
        exports = x0 + (x1 * for_income) - (x2 * real_ex_rate)
        imports = m0 + (mpi * dom_income) + (m2 * real_ex_rate)
        
        # Prevent negative exports/imports mathematically
        exports = max(0.0, exports)
        imports = max(0.0, imports)
        net_exports = exports - imports

        target_nx_min = 50.0
        target_nx_max = 250.0

        st.markdown("---")
        st.markdown("#### 🎯 Policy Target: Sustainable Trade Surplus")
        st.caption(
            f"Adjust the exchange rate and domestic/foreign dynamics to achieve a moderate trade surplus ($NX$) "
            f"between **{target_nx_min:.0f}** and **{target_nx_max:.0f}**."
        )

        if st.button("Evaluate Trade Balance"):
            if target_nx_min <= net_exports <= target_nx_max:
                st.session_state.sim_points = 50
                st.session_state.sim_completed = True
                st.success("✅ Trade balance achieved within target range! Awarded: 50 / 50 Pts.")
            else:
                st.session_state.sim_points = 25
                st.session_state.sim_completed = True
                st.warning("⚠️ Net Exports are outside the target surplus range (you may be in deficit or extreme surplus). Awarded: 25 / 50 Pts.")
            st.rerun()

    with col2:
        st.subheader("📊 Trade Metrics")

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Exports (X)</div>
                <div class="metric-val" style="color: #10B981;">{exports:.1f}</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Imports (M)</div>
                <div class="metric-val" style="color: #EF4444;">{imports:.1f}</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            nx_color = "#38BDF8" if net_exports > 0 else "#F59E0B"
            st.markdown(f"""
            <div class="metric-panel">
                <div class="metric-title">Net Exports (NX)</div>
                <div class="metric-val" style="color: {nx_color};">{net_exports:.1f}</div>
            </div>
            """, unsafe_allow_html=True)

        # Plotting NX Curve across varying exchange rates
        er_range = np.linspace(0.5, 2.0, 30)
        sim_exports = np.maximum(0, x0 + (x1 * for_income) - (x2 * er_range))
        sim_imports = np.maximum(0, m0 + (mpi * dom_income) + (m2 * er_range))
        nx_curve = sim_exports - sim_imports

        chart_df = pd.DataFrame({
            "Real Exchange Rate (ε)": np.round(er_range, 2),
            "Net Exports (NX)": np.round(nx_curve, 1)
        }).set_index("Real Exchange Rate (ε)")

        st.line_chart(chart_df, color="#38BDF8")
        st.caption(
            f"📍 Current Position: ε = {real_ex_rate:.2f} | NX = {net_exports:.1f}"
        )

# =====================================================================
# MODULE 2: MCQ ASSESSMENT (50 POINTS)
# =====================================================================
elif module == "📝 Module 2: Open Economy Assessment (50 Pts)":
    st.markdown("### 📝 Concepts in Exchange Rates and Net Exports")
    st.markdown("Assess your understanding of open economy macroeconomics (10 points each).")

    with st.form("open_economy_quiz"):
        st.markdown("#### 1. Real vs. Nominal Exchange Rate")
        q1 = st.radio(
            "What does the real exchange rate measure that the nominal exchange rate does not?",
            [
                "A) The absolute volume of currency traded in forex markets.",
                "B) The relative price of domestic goods in terms of foreign goods, adjusting for inflation/price levels.",
                "C) The central bank's benchmark interest rate spread.",
                "D) The total balance of the capital account."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 2. Currency Appreciation")
        q2 = st.radio(
            "Assuming the Marshall-Lerner condition holds, a real appreciation of the domestic currency will generally cause:",
            [
                "A) Exports to rise and imports to fall, increasing NX.",
                "B) Both exports and imports to rise simultaneously.",
                "C) Exports to fall and imports to rise, decreasing NX.",
                "D) No change in the trade balance."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 3. Foreign Income Shocks")
        q3 = st.radio(
            "If a country's major trading partners experience a severe economic recession (a drop in $Y^*$), what is the most likely direct impact on the domestic economy?",
            [
                "A) Domestic imports will surge.",
                "B) Domestic exports will fall, shifting the IS curve to the left.",
                "C) The domestic currency will automatically appreciate.",
                "D) Domestic exports will rise due to the substitution effect."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 4. The Marginal Propensity to Import")
        q4 = st.radio(
            "How does a higher marginal propensity to import (m) affect the Keynesian open-economy multiplier?",
            [
                "A) It increases the multiplier by injecting more money into the domestic economy.",
                "B) It decreases the multiplier because more spending leaks out of the domestic economy to foreign producers.",
                "C) It has no effect on the multiplier.",
                "D) It only affects the multiplier if the government runs a budget deficit."
            ], index=None
        )

        st.markdown("---")
        st.markdown("#### 5. Marshall-Lerner Condition")
        q5 = st.radio(
            "The Marshall-Lerner condition states that a currency depreciation will improve the trade balance ONLY IF:",
            [
                "A) The country has a fixed exchange rate regime.",
                "B) Domestic inflation is lower than foreign inflation.",
                "C) The sum of the price elasticities of demand for exports and imports is greater than 1.",
                "D) The marginal propensity to save equals the marginal propensity to import."
            ], index=None
        )

        submit_quiz = st.form_submit_button("Submit Assessment & Calculate Final Score")

        if submit_quiz:
            correct_keys = {
                "q1": "B) The relative price of domestic goods in terms of foreign goods, adjusting for inflation/price levels.",
                "q2": "C) Exports to fall and imports to rise, decreasing NX.",
                "q3": "B) Domestic exports will fall, shifting the IS curve to the left.",
                "q4": "B) It decreases the multiplier because more spending leaks out of the domestic economy to foreign producers.",
                "q5": "C) The sum of the price elasticities of demand for exports and imports is greater than 1."
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
            st.error("❌ **Q1 Review:** The real exchange rate adjusts nominal rates by the ratio of domestic to foreign price levels ($\\epsilon = E \\cdot P / P^*$).")
        if not rec.get("q2", False):
            st.error("❌ **Q2 Review:** Real appreciation makes domestic goods more expensive abroad (exports fall) and foreign goods cheaper at home (imports rise).")
        if not rec.get("q3", False):
            st.error("❌ **Q3 Review:** Lower foreign income reduces foreign demand for your exports, worsening your trade balance and decreasing aggregate demand.")
        if not rec.get("q4", False):
            st.error("❌ **Q4 Review:** Imports act as a leakage from the circular flow of income. A higher propensity to import reduces the size of the spending multiplier.")
        if not rec.get("q5", False):
            st.error("❌ **Q5 Review:** The Marshall-Lerner condition requires trade volumes to be sufficiently responsive to price changes to overcome the price effect of depreciation.")

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.caption("🌍 Macroeconomic Analysis Portal")
with f2:
    st.caption("⚡ Open Economy: Trade & Exchange Rate Dynamics")
with f3:
    st.caption(f"⏰ System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
