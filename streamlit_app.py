import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Cost Economics & Managerial Analysis Module",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# STYLING & THEME (SLATE & COBALT METROPOLIS)
# =====================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0F172A 0%, #1E293B 40%, #0F172A 100%); }
    
    .section-header {
        color: #FBBF24; font-weight: 700; font-size: 1.4rem; margin-bottom: 1.25rem;
        padding-bottom: 0.75rem; border-bottom: 1px solid rgba(251, 191, 36, 0.2);
    }
    .concept-note { background: rgba(59, 130, 246, 0.08); border-left: 4px solid #3B82F6; padding: 1.25rem; border-radius: 8px; margin: 1.2rem 0; }
    .concept-note h3 { color: #60A5FA; margin-top: 0 !important; font-size: 1.2rem; }
    .case-study { background: rgba(217, 119, 6, 0.08); border-left: 4px solid #D97706; padding: 1.25rem; border-radius: 8px; margin: 1.2rem 0; }
    .case-study h4 { color: #F59E0B; margin-top: 0 !important; font-size: 1.2rem; }
    
    .metric-card {
        background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 1.25rem; border-radius: 8px; text-align: center;
    }
    .metric-card h3 { color: #94A3B8; font-size: 1.05rem; margin: 0 0 0.5rem 0; }
    .metric-value { color: #FBBF24; font-size: 1.8rem; font-weight: 700; margin: 0.25rem 0; }
    .stMarkdown, p, li { color: #E2E8F0 !important; font-size: 0.98rem; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("### 💰 Cost Economics Engine")
    nav_selection = st.radio(
        "Select Cost Module:",
        options=[
            "📐 Cost Curve Dynamic Simulator",
            "📊 Explicit vs. Implicit & Profit Engine",
            "💡 Opportunity Cost & Sunk Cost Framework",
            "📖 Comprehensive Cost Taxonomy Reference"
        ]
    )

# =====================================================================
# MODULE 1: COST CURVE DYNAMIC SIMULATOR
# =====================================================================
if nav_selection == "📐 Cost Curve Dynamic Simulator":
    st.markdown('<div class="section-header">📐 Short-Run & Long-Run Cost Curves Simulator</div>', unsafe_allow_html=True)
    
    col_ctrl, col_plot = st.columns([1, 1.6])
    
    with col_ctrl:
        st.markdown('<div class="concept-note"><h3>⚙️ Cost Function Parameters</h3><p>Model total cost: $TC(Q) = TFC + a \cdot Q + b \cdot Q^2 + c \cdot Q^3$</p></div>', unsafe_allow_html=True)
        
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
        ax1.set_title('Total Cost Curves ($TC = TFC + TVC$)', color='white', fontsize=12)
        ax1.set_ylabel('Total Cost ($)')
        ax1.legend(loc='upper left')

        # Plot Averages & Marginal
        ax2.plot(q_vals, atc_vals, label='Average Total Cost (ATC)', color='#60A5FA', linewidth=2)
        ax2.plot(q_vals, avc_vals, label='Average Variable Cost (AVC)', color='#FBBF24', linewidth=2)
        ax2.plot(q_vals, afc_vals, label='Average Fixed Cost (AFC)', color='#94A3B8', linestyle='--', linewidth=1.5)
        ax2.plot(q_vals, mc_vals, label='Marginal Cost (MC)', color='#10B981', linewidth=2.5)
        ax2.set_title('Per-Unit & Marginal Cost Curves ($MC = \\frac{dTC}{dQ}$)', color='white', fontsize=12)
        ax2.set_xlabel('Output Quantity (Q)')
        ax2.set_ylabel('Cost Per Unit ($)')
        ax2.set_ylim(0, np.percentile(atc_vals, 95) * 2)
        ax2.legend(loc='upper right')

        plt.tight_layout()
        st.pyplot(fig)

# =====================================================================
# MODULE 2: EXPLICIT VS IMPLICIT & PROFIT ENGINE
# =====================================================================
elif nav_selection == "📊 Explicit vs. Implicit & Profit Engine":
    st.markdown('<div class="section-header">📊 Accounting Profit vs. Economic Profit Calculator</div>', unsafe_allow_html=True)
    
    col_in, col_res = st.columns([1, 1])
    
    with col_in:
        st.markdown('<div class="case-study"><h4>📋 Business Financial Inputs</h4></div>', unsafe_allow_html=True)
        total_rev = st.number_input("Total Revenue ($TR$):", min_value=0.0, value=500000.0, step=10000.0)
        
        st.markdown("##### 💵 Explicit Costs (Accounting Outlays)")
        wages = st.number_input("Wages & Salaries:", min_value=0.0, value=180000.0, step=5000.0)
        materials = st.number_input("Raw Materials & Supplies:", min_value=0.0, value=70000.0, step=5000.0)
        rent_overhead = st.number_input("Rent & Utilities:", min_value=0.0, value=50000.0, step=2000.0)
        
        st.markdown("##### 🧠 Implicit Costs (Opportunity Costs)")
        foregone_salary = st.number_input("Owner's Foregone Salary:", min_value=0.0, value=90000.0, step=5000.0)
        foregone_rent = st.number_input("Foregone Rent on Owned Space:", min_value=0.0, value=25000.0, step=2000.0)
        foregone_interest = st.number_input("Foregone Interest on Invested Capital:", min_value=0.0, value=15000.0, step=1000.0)

    # Computations
    total_explicit = wages + materials + rent_overhead
    total_implicit = foregone_salary + foregone_rent + foregone_interest
    economic_cost = total_explicit + total_implicit
    
    acct_profit = total_rev - total_explicit
    econ_profit = total_rev - economic_cost

    with col_res:
        st.markdown('<div class="section-header">📈 Profit Analysis Diagnostics</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="metric-card"><h3>Accounting Profit</h3><div class="metric-value">${acct_profit:,.2f}</div><p style="color: #94A3B8; font-size: 0.85rem;">TR - Explicit Costs</p></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="metric-card"><h3>Economic Profit</h3><div class="metric-value" style="color: {"#10B981" if econ_profit >= 0 else "#EF4444"};">${econ_profit:,.2f}</div><p style="color: #94A3B8; font-size: 0.85rem;">TR - (Explicit + Implicit Costs)</p></div>', unsafe_allow_html=True)
            
        st.markdown(f"""
        <div class="concept-note">
            <h4>💡 Decision Analysis</h4>
            <ul>
                <li><strong>Total Explicit Costs:</strong> ${total_explicit:,.2f}</li>
                <li><strong>Total Implicit Costs:</strong> ${total_implicit:,.2f}</li>
                <li><strong>Total Economic Cost:</strong> ${economic_cost:,.2f}</li>
            </ul>
            <p><strong>Takeaway:</strong> {"The business generates **positive economic profit**, meaning resources are deployed in their absolute best allocation." if econ_profit > 0 else ("The firm earns **zero economic profit (normal profit)**. All explicit costs and forgone opportunities are perfectly covered." if econ_profit == 0 else "The business incurs an **economic loss**. The entrepreneur would be better off redirecting resources to their next best alternatives.")}</p>
        </div>
        """, unsafe_allow_html=True)

# =====================================================================
# MODULE 3: OPPORTUNITY & SUNK COST FRAMEWORK
# =====================================================================
elif nav_selection == "💡 Opportunity Cost & Sunk Cost Framework":
    st.markdown('<div class="section-header">💡 Opportunity Cost & Sunk Cost Decision Engine</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-note">
    <h3>🛑 The Golden Rule of Decision Making</h3>
    <p><strong>Sunk Costs</strong> are past, unrecoverable expenses that must be <em>completely ignored</em> in forward-looking business decisions. Decisions should be evaluated solely on <strong>Incremental (Marginal) Revenue vs. Incremental (Marginal) Cost</strong>, taking into account current <strong>Opportunity Costs</strong>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🛠️ Interactive Sunk Cost Evaluator")
    c1, c2 = st.columns([1, 1])
    
    with c1:
        sunk_expenditure = st.number_input("Past R&D / Capital Spent (Sunk Cost):", min_value=0.0, value=2000000.0, step=100000.0)
        cost_to_complete = st.number_input("Additional Capital Required to Finish:", min_value=0.0, value=500000.0, step=50000.0)
        projected_revenue = st.number_input("Projected Future Revenue Upon Completion:", min_value=0.0, value=750000.0, step=50000.0)
        
    with c2:
        incremental_net = projected_revenue - cost_to_complete
        
        st.markdown('<div class="case-study"><h4>📌 Managerial Recommendation</h4></div>', unsafe_allow_html=True)
        if incremental_net > 0:
            st.success(f"✅ **Proceed with Completion!**\n\nIncremental Revenue (${projected_revenue:,.2f}) exceeds Incremental Cost (${cost_to_complete:,.2f}) by **${incremental_net:,.2f}**. The past spent ${sunk_expenditure:,.2f} is irrelevant.")
        elif incremental_net == 0:
            st.warning(f"⚠️ **Breakeven on Completion.**\n\nIncremental Revenue perfectly equals Incremental Cost (${cost_to_complete:,.2f}). Proceed only if qualitative strategic benefits exist.")
        else:
            st.error(f"❌ **Abandon Project immediately!**\n\nCompleting the project burns an additional **${abs(incremental_net):,.2f}**. Throwing good money after bad (Sunk Cost Fallacy) increases overall loss.")

# =====================================================================
# MODULE 4: COMPREHENSIVE COST TAXONOMY REFERENCE
# =====================================================================
elif nav_selection == "📖 Comprehensive Cost Taxonomy Reference":
    st.markdown('<div class="section-header">📖 Full Managerial & Microeconomic Cost Taxonomy</div>', unsafe_allow_html=True)
    
    st.markdown("""
    | Cost Concept | Definition | Mathematical Expression / Identification | Key Managerial Application |
    | :--- | :--- | :--- | :--- |
    | **Explicit Cost** | Direct, out-of-pocket cash payments for resources. | Recorded in accounting ledgers | Tax reporting, cash flow analysis |
    | **Implicit Cost** | Income forgone by using self-owned resources. | Value of next best alternative | Strategic resource allocation |
    | **Accounting Cost** | Total explicit monetary outlays incurred in the past. | $\\text{Explicit Costs}$ | Financial statements & auditing |
    | **Economic Cost** | Combined explicit and implicit opportunity costs. | $\\text{Explicit Cost} + \\text{Implicit Cost}$ | Firm entry/exit decisions |
    | **Opportunity Cost** | Value of the next best alternative given up. | $OC = \\text{Benefit of Best Alternative}$ | Capital budgeting & investment choice |
    | **Sunk Cost** | Past expense that cannot be recovered by any future decision. | Irrecoverable Outlays | Must be ignored in decision-making |
    | **Fixed Cost (TFC)** | Costs that do not vary with output volume ($Q$). | $TFC = TC - TVC$ | Break-even analysis, operating leverage |
    | **Variable Cost (TVC)**| Costs that change directly with output volume ($Q$). | $TVC = f(Q) = wL + mM$ | Production scaling, shutdown decisions |
    | **Total Cost (TC)** | Sum of all fixed and variable expenses. | $TC = TFC + TVC$ | Baseline budget planning |
    | **Average Total Cost (ATC)**| Total expense per unit of output produced. | $ATC = \\frac{TC}{Q} = AFC + AVC$ | Long-run efficiency & pricing |
    | **Average Fixed Cost (AFC)**| Fixed expense distributed per unit of output. | $AFC = \\frac{TFC}{Q}$ | Overhead spreading analysis |
    | **Average Variable Cost (AVC)**| Variable expense per unit of output. | $AVC = \\frac{TVC}{Q}$ | Short-run shutdown threshold ($P < AVC$) |
    | **Marginal Cost (MC)** | Extra cost incurred by producing 1 additional unit. | $MC = \\frac{\\Delta TC}{\\Delta Q} = \\frac{\\partial TC}{\\partial Q}$ | Profit-maximizing output ($MR = MC$) |
    """)

# =====================================================================
# FOOTER TERMINAL
# =====================================================================
st.markdown("---")
f1, f2 = st.columns(2)
with f1:
    st.caption("🎓 Cost Economics Engine | Corporate Strategy Hub")
with f2:
    st.caption("🚀 Microeconomic Cost Analysis Module Active")
