from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Macro Lab: Money Market Equilibrium & The LM Curve",
    page_icon="🪙",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling (Dark Slate & Amber / Emerald Theme)
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .stApp {
        background: radial-gradient(circle at 15% 15%, #0B192C 0%, #06101E 60%, #020617 100%);
        color: #E2E8F0;
    }
    
    .score-banner {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(16, 185, 129, 0.15) 100%);
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
""",
    unsafe_allow_html=True,
)

# =====================================================================
# SESSION STATE ENGINE
# =====================================================================
if "lm_sim_points" not in st.session_state:
  st.session_state.lm_sim_points = 0
if "lm_sim_completed" not in st.session_state:
  st.session_state.lm_sim_completed = False
if "lm_quiz_score" not in st.session_state:
  st.session_state.lm_quiz_score = 0
if "lm_quiz_submitted" not in st.session_state:
  st.session_state.lm_quiz_submitted = False
if "lm_eval_records" not in st.session_state:
  st.session_state.lm_eval_records = {}

total_final_score = (
    st.session_state.lm_sim_points + st.session_state.lm_quiz_score
)

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
  st.markdown("## 🪙 Money Market Portal")
  module = st.radio(
      "Select Module:",
      [
          "📈 Module 1: Money Demand, Supply & LM Simulator (50 Pts)",
          "📝 Module 2: LM Curve Mastery Assessment (50 Pts)",
      ],
  )
  st.markdown("---")
  st.markdown("### 🏆 Combined Scoreboard")
  st.markdown(f"**Simulation Lab:** {st.session_state.lm_sim_points} / 50")
  st.markdown(f"**Assessment:** {st.session_state.lm_quiz_score} / 50")
  st.markdown(f"### **Total Mastery:** {total_final_score} / 100")
  if total_final_score == 100:
    st.success("🌟 Perfect Money Market Mastery!")

# =====================================================================
# GLOBAL SCORE BANNER
# =====================================================================
st.markdown(
    f"""
<div class="score-banner">
    <h2 style="color: #FBBF24; margin: 0;">Money Market & LM Equilibrium Tracker: {total_final_score} / 100</h2>
    <p style="color: #94A3B8; margin: 0.25rem 0 0 0;">
        Simulation Lab: <b>{st.session_state.lm_sim_points}/50 Pts</b> | Conceptual MCQs: <b>{st.session_state.lm_quiz_score}/50 Pts</b>
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================================================
# MODULE 1: SIMULATION LAB (50 POINTS)
# =====================================================================
if module == "📈 Module 1: Money Demand, Supply & LM Simulator (50 Pts)":
  st.markdown("### 📈 Money Market Clearing: Liquidity Preference & The LM Curve")
  st.markdown(r"""
    The money market clears when real money supply equals real money demand:
    $$\frac{M}{P} = L(Y, r) = k \cdot Y - h \cdot r$$
    
    Solving for the nominal/real interest rate gives the **LM Curve**:
    $$r = \frac{k}{h} \cdot Y - \frac{1}{h} \left(\frac{M}{P}\right)$$
    """)

  col1, col2 = st.columns([1, 1.3], gap="medium")

  with col1:
    st.subheader("🛠️ Monetary & Liquidity Levers")

    m_nominal = st.slider(
        "1. Nominal Money Supply (M):",
        min_value=400.0,
        max_value=1600.0,
        value=900.0,
        step=50.0,
        help="Monetary base controlled by the central bank via open market operations.",
    )

    p_level = st.slider(
        "2. Aggregate Price Level (P):",
        min_value=1.0,
        max_value=3.0,
        value=1.5,
        step=0.1,
        help="Price level determining the purchasing power of money balances.",
    )

    y_income = st.slider(
        "3. Real Output / Aggregate Income (Y):",
        min_value=1000.0,
        max_value=2500.0,
        value=1600.0,
        step=50.0,
        help="National income driving transactions and precautionary money demand.",
    )

    h_sensitivity = st.slider(
        "4. Speculative Interest Sensitivity (h):",
        min_value=20.0,
        max_value=100.0,
        value=50.0,
        step=5.0,
        help="Responsiveness of money demand to interest rates (speculative/portfolio demand).",
    )

    # Fixed structural parameters
    k_sensitivity = 0.50  # Transaction money demand sensitivity to income

    # Calculations
    real_money_supply = m_nominal / p_level
    transaction_demand = k_sensitivity * y_income

    # Equilibrium interest rate on the LM curve: r* = (k*Y - M/P) / h
    r_eq = (transaction_demand - real_money_supply) / h_sensitivity

    # LM Curve Slope: dr/dY = k/h
    lm_slope = k_sensitivity / h_sensitivity

    target_r_min = 3.0
    target_r_max = 6.0

    st.markdown("---")
    st.markdown("#### 🎯 Central Bank Target Rate Window")
    st.caption(
        f"Calibrate monetary policy ($M$) relative to price level ($P$) and output ($Y$) "
        f"to achieve an equilibrium clearing rate ($r^*$) between **{target_r_min:.1f}%** and **{target_r_max:.1f}%**."
    )

    if st.button("Evaluate Money Market Equilibrium"):
      if target_r_min <= r_eq <= target_r_max:
        st.session_state.lm_sim_points = 50
        st.session_state.lm_sim_completed = True
        st.success(
            f"✅ Target interest rate band met at r = {r_eq:.2f}%! Awarded: 50"
            " / 50 Pts."
        )
      else:
        st.session_state.lm_sim_points = 25
        st.session_state.lm_sim_completed = True
        st.warning(
            f"⚠️ Rate {r_eq:.2f}% is outside the {target_r_min:.1f}% - {target_r_max:.1f}% stability band. Awarded: 25 / 50 Pts."
        )
      st.rerun()

  with col2:
    st.subheader("📊 Liquidity Market Metrics & LM Trajectory")

    m1, m2, m3 = st.columns(3)
    with m1:
      st.markdown(
          f"""
            <div class="metric-panel">
                <div class="metric-title">Real Money Stock (M/P)</div>
                <div class="metric-val">{real_money_supply:.1f}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )
    with m2:
      st.markdown(
          f"""
            <div class="metric-panel">
                <div class="metric-title">Equilibrium Rate (r*)</div>
                <div class="metric-val" style="color: {'#10B981' if target_r_min <= r_eq <= target_r_max else '#F87171'};">{r_eq:.2f}%</div>
            </div>
            """,
          unsafe_allow_html=True,
      )
    with m3:
      st.markdown(
          f"""
            <div class="metric-panel">
                <div class="metric-title">LM Slope (k / h)</div>
                <div class="metric-val" style="color: #F59E0B;">{lm_slope:.3f}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

    # Plotting the LM Curve: r as a function of Y across income levels
    y_range = np.linspace(800.0, 2600.0, 30)
    r_lm_curve = (k_sensitivity * y_range - real_money_supply) / h_sensitivity

    chart_df = pd.DataFrame({
        "Output / Income (Y)": np.round(y_range, 0),
        "LM Curve: Market Clearing Interest Rate (r %)": np.round(
            r_lm_curve, 2
        ),
    }).set_index("Output / Income (Y)")

    st.line_chart(chart_df)
    st.caption(
        f"📍 Current Equilibrium Point on LM: Y = {y_income:.0f} | r* = {r_eq:.2f}% | "
        f"Transaction Demand = {transaction_demand:.1f} | Speculative Demand = {(h_sensitivity * r_eq):.1f}"
    )

# =====================================================================
# MODULE 2: MCQ ASSESSMENT (50 POINTS)
# =====================================================================
elif module == "📝 Module 2: LM Curve Mastery Assessment (50 Pts)":
  st.markdown("### 📝 Concepts in Money Demand, Money Supply & The LM Schedule")
  st.markdown(
      "Assess your understanding of liquidity preference, central banking, and"
      " LM slopes (10 points each)."
  )

  with st.form("money_market_quiz"):
    st.markdown("#### 1. Components of Keynesian Money Demand")
    q1 = st.radio(
        "According to Keynes' Liquidity Preference Theory, real money demand"
        " depends directly on:",
        [
            (
                "A) Income (positively for transactions/precaution) and interest"
                " rates (negatively for speculative demand)."
            ),
            (
                "B) The real interest rate positively and government spending"
                " negatively."
            ),
            "C) Solely on the gold reserves maintained by the central bank.",
            "D) Income negatively and the marginal propensity to save positively.",
        ],
        index=None,
    )

    st.markdown("---")
    st.markdown("#### 2. The Upward Slope of the LM Curve")
    q2 = st.radio(
        "Why does the LM schedule exhibit an upward (positive) slope in (Y, r)"
        " space?",
        [
            (
                "A) Lower output increases consumer borrowing, causing interest"
                " rates to climb."
            ),
            (
                "B) Higher output increases transaction demand for money; with a"
                " fixed real money supply, interest rates must rise to choke off"
                " speculative demand and restore equilibrium."
            ),
            (
                "C) Higher interest rates force commercial banks to reduce"
                " credit creation."
            ),
            (
                "D) Higher output lowers the price level, reducing nominal"
                " balances."
            ),
        ],
        index=None,
    )

    st.markdown("---")
    st.markdown("#### 3. Shifting the LM Schedule")
    q3 = st.radio(
        "Which event shifts the LM curve downward and to the right?",
        [
            (
                "A) An increase in the price level (P) while nominal money"
                " remains fixed."
            ),
            (
                "B) An open market purchase of bonds by the central bank"
                " (expansionary monetary policy)."
            ),
            "C) An increase in autonomous government expenditure (G).",
            "D) An increase in transaction demand sensitivity (k).",
        ],
        index=None,
    )

    st.markdown("---")
    st.markdown("#### 4. The Liquidity Trap")
    q4 = st.radio(
        "In a liquidity trap, what happens to the money demand interest"
        " sensitivity (h) and the LM curve?",
        [
            (
                "A) Sensitivity h becomes zero (d = 0), rendering the LM curve"
                " completely vertical (Classical case)."
            ),
            (
                "B) Sensitivity h approaches infinity, making the LM curve"
                " horizontal; monetary expansion cannot lower interest rates"
                " further."
            ),
            (
                "C) The LM curve shifts continuously to the left without bound."
            ),
            "D) Money velocity expands toward infinity.",
        ],
        index=None,
    )

    st.markdown("---")
    st.markdown("#### 5. Slope Determinants of the LM Curve")
    q5 = st.radio(
        "Holding all else constant, the LM curve becomes steeper when:",
        [
            (
                "A) Money demand is highly sensitive to the interest rate (large"
                " h)."
            ),
            (
                "B) The income responsiveness of money demand (k) is high and"
                " interest sensitivity (h) is low."
            ),
            "C) The money multiplier drops to zero.",
            "D) Government taxes increase sharply.",
        ],
        index=None,
    )

    submit_quiz = st.form_submit_button(
        "Submit Assessment & Calculate Final Score"
    )

    if submit_quiz:
      correct_keys = {
          "q1": (
              "A) Income (positively for transactions/precaution) and interest"
              " rates (negatively for speculative demand)."
          ),
          "q2": (
              "B) Higher output increases transaction demand for money; with a"
              " fixed real money supply, interest rates must rise to choke off"
              " speculative demand and restore equilibrium."
          ),
          "q3": (
              "B) An open market purchase of bonds by the central bank"
              " (expansionary monetary policy)."
          ),
          "q4": (
              "B) Sensitivity h approaches infinity, making the LM curve"
              " horizontal; monetary expansion cannot lower interest rates"
              " further."
          ),
          "q5": (
              "B) The income responsiveness of money demand (k) is high and"
              " interest sensitivity (h) is low."
          ),
      }

      records = {
          "q1": (q1 == correct_keys["q1"]),
          "q2": (q2 == correct_keys["q2"]),
          "q3": (q3 == correct_keys["q3"]),
          "q4": (q4 == correct_keys["q4"]),
          "q5": (q5 == correct_keys["q5"]),
      }

      st.session_state.lm_quiz_score = sum(records.values()) * 10
      st.session_state.lm_quiz_submitted = True
      st.session_state.lm_eval_records = records
      st.rerun()

  if st.session_state.lm_quiz_submitted:
    st.markdown("---")
    st.markdown(
        f"### Assessment Score: **{st.session_state.lm_quiz_score} / 50"
        " Points**"
    )

    rec = st.session_state.lm_eval_records
    if not rec.get("q1", False):
      st.error(
          "❌ **Q1 Review:** Money demand $M^d/P = kY - hr$. Transactions and"
          " precautionary needs grow with $Y$, while speculative demand drops as"
          " $r$ rises (higher opportunity cost of holding cash)."
      )
    if not rec.get("q2", False):
      st.error(
          "❌ **Q2 Review:** When $Y$ expands, households demand more cash for"
          " transactions. With $M/P$ constant, bond sales push bond prices down"
          " and interest rates up until money demand re-equilibrates with"
          " supply."
      )
    if not rec.get("q3", False):
      st.error(
          "❌ **Q3 Review:** Open market purchases increase nominal balances"
          " $M$, raising real supply $M/P$. This shifts the LM curve downward"
          " and rightward, reducing $r$ for any given $Y$."
      )
    if not rec.get("q4", False):
      st.error(
          "❌ **Q4 Review:** In a Keynesian Liquidity Trap, interest rates are"
          " so low that money and bonds become near-perfect substitutes ($h"
          r" \to \infty$), making the LM curve completely horizontal."
      )
    if not rec.get("q5", False):
      st.error(
          "❌ **Q5 Review:** The slope of the LM curve is $\\frac{\\Delta"
          r" r}{\\Delta Y} = \frac{k}{h}$. A larger income sensitivity ($k$)"
          " or a lower interest sensitivity ($h$) makes the curve steeper."
      )

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
  st.caption("🪙 Macroeconomic Analysis Portal")
with f2:
  st.caption("⚡ Money Market Clearing & LM Schedule Dynamics")
with f3:
  st.caption(f"⏰ System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
