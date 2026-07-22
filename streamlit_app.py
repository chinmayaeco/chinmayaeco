import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Microeconomic Cost Engine",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# SECURE ACCESS SYSTEM
# =====================================================================
def check_password():
    """Returns `True` if the user enters the correct security key."""
    def password_entered():
        if st.session_state["password"] == "PED2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Cost Engine Security</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Enter credential key to deploy the Cost Optimization Engine.</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.text_input("Security Password", type="password", on_change=password_entered, key="password")
        return False
    
    elif not st.session_state["password_correct"]:
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Cost Engine Security</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.text_input("Security Password", type="password", on_change=password_entered, key="password")
            st.error("😕 Access denied. Invalid token key.")
        return False
    
    return True

if not check_password():
    st.stop()

# =====================================================================
# CORE DESIGN SYSTEM (SLATE, COBALT & AMBER METROPOLIS THEME)
# =====================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Main Background & Core Canvas Layout */
    .stApp { background: linear-gradient(135deg, #0F172A 0%, #1E293B 40%, #0F172A 100%); }
    
    /* Dynamic Performance Score Indicator */
    .score-banner {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid rgba(59, 130, 246, 0.3);
        color: #FFFFFF; padding: 1.5rem; border-radius: 12px; text-align: center; margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    }
    .score-banner h2 { color: #60A5FA !important; margin: 0 !important; font-weight: 700; font-size: 1.6rem; }
    
    /* System Division Headers */
    .section-header {
        color: #FBBF24; font-weight: 700; font-size: 1.4rem; margin-bottom: 1.25rem;
        padding-bottom: 0.75rem; border-bottom: 1px solid rgba(251, 191, 36, 0.2);
    }
    
    /* Concept Info Cards & Box Systems */
    .concept-note, .case-study { padding: 1.25rem; border-radius: 8px; margin: 1.2rem 0; }
    .concept-note { background: rgba(59, 130, 246, 0.08); border-left: 4px solid #3B82F6; }
    .concept-note h3 { color: #60A5FA; margin-top: 0 !important; font-size: 1.2rem; }
    .case-study { background: rgba(217, 119, 6, 0.08); border-left: 4px solid #D97706; }
    .case-study h4 { color: #F59E0B; margin-top: 0 !important; font-size: 1.2rem; }
    
    /* Dynamic Metric Highlight Blocks */
    .metric-card {
        background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 1.25rem; border-radius: 8px; text-align: center;
    }
    .metric-card h3 { color: #94A3B8; font-size: 1.05rem; margin: 0 0 0.5rem 0; }
    .metric-value { color: #FBBF24; font-size: 1.8rem; font-weight: 700; margin: 0.25rem 0; }
    
    /* Interface Control Elements / Buttons */
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important; color: white !important;
        border: none !important; padding: 0.65rem 1.75rem !important; border-radius: 6px !important;
        font-weight: 600 !important; transition: all 0.2s ease !important;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover { 
        transform: translateY(-1px) !important; 
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4) !important; 
    }
    
    /* Framework Global Text Elements Adjustments */
    .stMarkdown, p, li { color: #E2E8F0 !important; font-size: 0.98rem; line-height: 1.6; }
    .stSidebar { background: #0F172A !important; border-right: 1px solid rgba(255, 255, 255, 0.05); }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SESSION STATE SYSTEM MANAGEMENT
# =====================================================================
def init_system_state():
    defaults = {
        'knowledge_rating': 0.0,
        'quiz_done': False,
        'ans1_ok': False, 'ans2_ok': False, 'ans3_ok': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_system_state()

# =====================================================================
# SIDEBAR CONTROL DECK
# =====================================================================
with st.sidebar:
    st.markdown("### 💰 Cost Economics Hub")
    nav_selection = st.radio(
        "Navigation Deck:",
        options=[
            "📐 Cost Curves Simulator",
            "📊 Explicit vs. Implicit Costs & Profit",
            "💡 Opportunity & Sunk Costs Evaluator",
            "📖 Comprehensive Cost Taxonomy",
            "📝 Cost Architecture Knowledge Check"
        ]
    )

# =====================================================================
# LIVE SCORE TRACKING ENGINE
# =====================================================================
score_container = st.container()
with score_container:
    final_score = round(st.session_state.knowledge_rating, 1)
    
    st.markdown(f"""
    <div class="score-banner">
        <h2>Cost Economics Mastery Score: {final_score} / 100</h2>
        <p style='color: #FBBF24; margin: 0.25rem 0 0 0;'>
            📝 Quiz Accuracy Rating: {final_score}/100
        </p>
        <small style='color: #94A3B8;'>Evaluate cost dynamics, avoid sunk cost fallacies, and optimize profit margins.</small>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE ROUTING ARCHITECTURE
# =====================================================================

# --- SECTION 1: COST CURVES SIMULATOR ---
if nav_selection == "📐 Cost Curves Simulator":
    st.markdown('<div class="section-header">📐 Short-Run & Long-Run Cost Curves Simulator</div>', unsafe_allow_html=True)
    
    col_ctrl, col_plot = st.columns([1, 1.6])
    
    with col_ctrl:
        st.markdown(r'<div class="concept-note"><h3>⚙️ Cost Function Controls</h3><p>Model total short-run cost:<br>$$TC(Q) = TFC + a \cdot Q + b \cdot Q^2 + c \cdot Q^3$$</p></div>', unsafe_allow_html=True)
        
        tfc = st.number_input("Total Fixed Cost ($TFC$):", min_value=10.0, max_value=500.0, value=100.0, step=10.0)
        param_a = st.slider("Linear Cost Coeff ($a$):", 1.0, 50.0, 20.0, step=1.0)
        param_b = st.slider("Quadratic Coeff ($b$ - Diminishing Returns):", -5.0, 5.0, -1.5, step=0.1)
        param_c = st.slider("Cubic Coeff ($c$ - Capacity Constraints):", 0.01, 0.5, 0.05, step=0.01)
        q_max = st.slider("Maximum Output Volume ($Q$):", 10, 100, 40, step=5)

    # Compute Curves
    q_vals = np.linspace(1, q_max, 200)
    tvc_vals = param_a * q_vals + param_b * (q_vals**2) + param_c * (q_vals**3)
    tc_vals = tfc + tvc_vals
    
    afc_vals = tfc / q_vals
    avc_vals = tvc_vals / q_vals
    atc_vals = tc_vals / q_vals
    mc_vals = param_a + 2 * param_b * q_vals + 3 * param_c * (q_vals**2)

    with col_plot:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
        fig.patch.set_facecolor('#0F172A')
        for ax in [ax1, ax2]:
            ax.set_facecolor('#1E293B')
            ax.tick_params(colors='white')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            ax.grid(True, linestyle='--', alpha=0.3)

        # Plot Totals
        ax1.plot(q_vals, tc_vals, label='Total Cost (TC)', color='#3B82F6', linewidth=2.5)
        ax1.plot(q_vals, tvc_vals, label='Total Variable Cost (TVC)', color='#F59E0B', linewidth=2)
        ax1.axhline(y=tfc, label='Total Fixed Cost (TFC)', color='#EF4444', linestyle=':', linewidth=2)
        ax1.set_title(r'Total Cost Curves ($TC = TFC + TVC$)', color='white', fontsize=12)
        ax1.set_ylabel('Total Cost ($)')
        ax1.legend(loc='upper left')

        # Plot Averages & Marginal
        ax2.plot(q_vals, atc_vals, label='Average Total Cost (ATC)', color='#60A5FA', linewidth=2)
        ax2.plot(q_vals, avc_vals, label='Average Variable Cost (AVC)', color='#FBBF24', linewidth=2)
        ax2.plot(q_vals, afc_vals, label='Average Fixed Cost (AFC)', color='#94A3B8', linestyle='--', linewidth=1.5)
        ax2.plot(q_vals, mc_vals, label='Marginal Cost (MC)', color='#10B981', linewidth=2.5)
        ax2.set_title(r'Per-Unit & Marginal Cost Curves ($MC = \frac{dTC}{dQ}$)', color='white', fontsize=12)
        ax2.set_xlabel('Output Quantity (Q)')
        ax2.set_ylabel('Cost Per Unit ($)')
        ax2.set_ylim(0, float(np.percentile(atc_vals, 95)) * 2)
        ax2.legend(loc='upper right')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

# --- SECTION 2: EXPLICIT VS IMPLICIT COSTS ---
elif nav_selection == "📊 Explicit vs. Implicit Costs & Profit":
    st.markdown('<div class="section-header">📊 Accounting Profit vs. Economic Profit Engine</div>', unsafe_allow_html=True)
    
    col_in, col_res = st.columns([1, 1])
    
    with col_in:
        st.markdown('<div class="case-study"><h4>📋 Business Financial Outlays</h4></div>', unsafe_allow_html=True)
        total_rev = st.number_input("Total Revenue ($TR$):", min_value=0.0, value=500000.0, step=10000.0)
        
        st.markdown("##### 💵 Explicit Costs (Out-of-Pocket Ledger Expenses)")
        wages = st.number_input("Wages & Payroll:", min_value=0.0, value=180000.0, step=5000.0)
        materials = st.number_input("Raw Materials & Operating Outlays:", min_value=0.0, value=70000.0, step=5000.0)
        rent_overhead = st.number_input("Rent & Facilities Overhead:", min_value=0.0, value=50000.0, step=2000.0)
        
        st.markdown("##### 🧠 Implicit Costs (Opportunity Costs)")
        foregone_salary = st.number_input("Owner's Foregone Salary:", min_value=0.0, value=90000.0, step=5000.0)
        foregone_rent = st.number_input("Foregone Rent on Self-Owned Real Estate:", min_value=0.0, value=25000.0, step=2000.0)
        foregone_interest = st.number_input("Foregone Interest on Equity Capital:", min_value=0.0, value=15000.0, step=1000.0)

    # Computations
    total_explicit = wages + materials + rent_overhead
    total_implicit = foregone_salary + foregone_rent + foregone_interest
    economic_cost = total_explicit + total_implicit
    
    acct_profit = total_rev - total_explicit
    econ_profit = total_rev - economic_cost

    with col_res:
        st.markdown('<div class="section-header">📈 Profit Diagnostics & Analysis</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="metric-card"><h3>Accounting Profit</h3><div class="metric-value">${acct_profit:,.2f}</div><p style="color: #94A3B8; font-size: 0.85rem;">TR - Explicit Costs</p></div>', unsafe_allow_html=True)
        with c2:
            color_code = "#10B981" if econ_profit >= 0 else "#EF4444"
            st.markdown(f'<div class="metric-card"><h3>Economic Profit</h3><div class="metric-value" style="color: {color_code};">${econ_profit:,.2f}</div><p style="color: #94A3B8; font-size: 0.85rem;">TR - (Explicit + Implicit Costs)</p></div>', unsafe_allow_html=True)
            
        status_msg = (
            "The business generates **positive economic profit**, indicating resources earn more than their best alternative."
            if econ_profit > 0 else (
                "The firm earns **zero economic profit (normal profit)**. All explicit expenses and opportunity costs are fully covered."
                if econ_profit == 0 else
                "The business incurs an **economic loss**. Reallocating resources to their next best alternative would yield a higher return."
            )
        )
        
        st.markdown(f"""
        <div class="concept-note">
            <h4>💡 Summary Diagnostic</h4>
            <ul>
                <li><strong>Total Explicit Costs:</strong> ${total_explicit:,.2f}</li>
                <li><strong>Total Implicit Costs:</strong> ${total_implicit:,.2f}</li>
                <li><strong>Total Economic Cost:</strong> ${economic_cost:,.2f}</li>
            </ul>
            <p><strong>Takeaway:</strong> {status_msg}</p>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 3: OPPORTUNITY & SUNK COSTS ---
elif nav_selection == "💡 Opportunity & Sunk Costs Evaluator":
    st.markdown('<div class="section-header">💡 Opportunity Cost & Sunk Cost Framework</div>', unsafe_allow_html=True)
    
    col_opp, col_sunk = st.columns(2)
    
    with col_opp:
        st.markdown("""
        <div class="concept-note">
        <h3>💡 Opportunity Cost</h3>
        <p>The value of the <strong>next best alternative forgone</strong> when choosing a decision path.</p>
        <p>Every allocation of capital or time carries an opportunity cost. Economic cost always accounts for both cash expenses and opportunity costs.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_sunk:
        st.markdown("""
        <div class="case-study">
        <h3>🛑 Sunk Cost</h3>
        <p>An expense that has <strong>already been paid and cannot be recovered</strong> by any future choice.</p>
        <p><strong>The Golden Rule:</strong> Sunk costs are <em>irrelevant</em> for forward-looking economic choices. Rational managers compare <strong>incremental revenue to incremental cost</strong> only.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🛠️ Interactive Sunk Cost Evaluator")
    c1, c2 = st.columns([1, 1])
    
    with c1:
        sunk_expenditure = st.number_input("Past Expenditure / Unrecoverable R&D (Sunk Cost):", min_value=0.0, value=2000000.0, step=100000.0)
        cost_to_complete = st.number_input("Additional Cost Required to Finish:", min_value=0.0, value=500000.0, step=50000.0)
        projected_revenue = st.number_input("Projected Future Revenue Upon Completion:", min_value=0.0, value=750000.0, step=50000.0)
        
    with c2:
        incremental_net = projected_revenue - cost_to_complete
        
        st.markdown('<div class="case-study"><h4>📌 Decision Analysis</h4></div>', unsafe_allow_html=True)
        if incremental_net > 0:
            st.success(f"✅ **Proceed with Project!**\n\nIncremental Revenue (${projected_revenue:,.2f}) exceeds Incremental Cost (${cost_to_complete:,.2f}) by **${incremental_net:,.2f}**. The past spent ${sunk_expenditure:,.2f} is sunk and irrelevant.")
        elif incremental_net == 0:
            st.warning(f"⚠️ **Breakeven on Completion.**\n\nIncremental Revenue equals Incremental Cost (${cost_to_complete:,.2f}). Proceed only if qualitative strategic benefits exist.")
        else:
            st.error(f"❌ **Abandon Project!**\n\nCompleting the project burns an additional **${abs(incremental_net):,.2f}**. Continuing to spend money just to justify a past expense is the Sunk Cost Fallacy.")

# --- SECTION 4: TAXONOMY REFERENCE ---
elif nav_selection == "📖 Comprehensive Cost Taxonomy":
    st.markdown('<div class="section-header">📖 Comprehensive Microeconomic Cost Taxonomy</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
| Cost Concept | Definition | Mathematical Expression | Managerial Application |
| :--- | :--- | :--- | :--- |
| **Explicit Cost** | Direct out-of-pocket cash payments for resources. | Recorded in accounting ledgers | Cash flow tracking, tax reporting |
| **Implicit Cost** | Non-monetary opportunity costs of using owned resources. | Value of next best alternative | Strategic resource allocation |
| **Accounting Cost** | Total explicit cash outlays incurred. | $\text{Explicit Costs}$ | Financial statements & auditing |
| **Economic Cost** | Combined explicit and implicit opportunity costs. | $\text{Explicit Cost} + \text{Implicit Cost}$ | Firm entry/exit decisions |
| **Opportunity Cost** | Value of the next best alternative forgone. | $OC = \text{Benefit of Best Alternative}$ | Capital budgeting & investment choices |
| **Sunk Cost** | Past expense that cannot be recovered. | Irrecoverable Outlays | Must be ignored in future decisions |
| **Fixed Cost (TFC)** | Costs that do not vary with output volume ($Q$). | $TFC = TC - TVC$ | Operating leverage & break-even |
| **Variable Cost (TVC)**| Costs that change directly with output volume ($Q$). | $TVC = f(Q)$ | Production scaling & shutdown choices |
| **Total Cost (TC)** | Sum of fixed and variable expenses. | $TC = TFC + TVC$ | Total budget planning |
| **Average Total Cost (ATC)**| Total expense per unit of output. | $ATC = \frac{TC}{Q} = AFC + AVC$ | Long-run pricing & unit efficiency |
| **Average Fixed Cost (AFC)**| Fixed expense distributed per unit of output. | $AFC = \frac{TFC}{Q}$ | Overhead spreading analysis |
| **Average Variable Cost (AVC)**| Variable expense per unit of output. | $AVC = \frac{TVC}{Q}$ | Short-run shutdown threshold ($P < AVC$) |
| **Marginal Cost (MC)** | Extra cost incurred by producing 1 additional unit. | $MC = \frac{\Delta TC}{\Delta Q} = \frac{\partial TC}{\partial Q}$ | Profit-maximizing output ($MR = MC$) |
""")

# --- SECTION 5: KNOWLEDGE CHECK ---
elif nav_selection == "📝 Cost Architecture Knowledge Check":
    st.markdown('<div class="section-header">📝 Master Cost Economics Knowledge Evaluation</div>', unsafe_allow_html=True)
    
    with st.form("cost_quiz"):
        st.markdown("### 1. Economic Profit Calculation")
        q1 = st.radio(
            "An entrepreneur leaves a $100,000/year job to start a firm. Revenues are $300,000 and explicit costs are $180,000. What is the Economic Profit?",
            options=[
                "A) $120,000",
                "B) $20,000",
                "C) $300,000",
                "D) -$80,000"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. Sunk Cost & Decision Theory")
        q2 = st.radio(
            "A company spent $5M developing a prototype that turns out to be non-viable. To complete it will cost $1M more, but projected revenue is only $500,000. Should they proceed?",
            options=[
                "A) Yes, to recover part of the initial $5M investment.",
                "B) No, because incremental revenue ($500k) is less than incremental cost ($1M); the $5M is a sunk cost.",
                "C) Yes, because total revenue exceeds the remaining variable cost.",
                "D) No, because fixed costs must always be amortized fully."
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Marginal Cost Intersections")
        q3 = st.radio(
            "At what point does the Marginal Cost (MC) curve intersect the Average Total Cost (ATC) curve?",
            options=[
                "A) At the maximum point of ATC.",
                "B) At the absolute minimum point of ATC.",
                "C) At the point where fixed costs equal variable costs.",
                "D) At zero output volume."
            ], index=None
        )
        
        eval_quiz = st.form_submit_button("Submit Performance Metrics", type="primary")
        
        if eval_quiz:
            score_acc = 0.0
            
            if q1 == "B) $20,000":
                score_acc += 33.33; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False

            if q2 == "B) No, because incremental revenue ($500k) is less than incremental cost ($1M); the $5M is a sunk cost.":
                score_acc += 33.33; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False
                
            if q3 == "B) At the absolute minimum point of ATC.":
                score_acc += 33.34; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False
                
            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Performance Score: {round(st.session_state.knowledge_rating, 1)} / 100 Points")
        
        if not st.session_state.ans1_ok:
            st.error("**Q1 Analysis:** Accounting Profit = $300k - $180k = $120k. Subtract the $100k foregone salary (implicit cost) to get Economic Profit = $20,000.")
        if not st.session_state.ans2_ok:
            st.error("**Q2 Analysis:** The $5M spent is a sunk cost and unrecoverable. Marginal cost to finish ($1M) exceeds marginal revenue ($500k), so continuing loses another $500k.")
        if not st.session_state.ans3_ok:
            st.error("**Q3 Analysis:** $MC$ always intersects $ATC$ (and $AVC$) at its minimum point. When $MC < ATC$, $ATC$ falls; when $MC > ATC$, $ATC$ rises.")

# =====================================================================
# SYSTEM FOOTER DATA TERMINAL
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("🎓 Microeconomic Cost Engine | Corporate Strategy Hub")

with foot_c2:
    st.caption("🚀 Cost & Profitability Optimization Active")

with foot_c3:
    st.caption(f"⏰ System Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
