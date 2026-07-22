import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Long-Run Production & Cost Optimization Engine",
    page_icon="🚀",
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
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Production Engine Security</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Enter credential key to deploy the Long-Run Optimization Simulator.</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.text_input("Security Password", type="password", on_change=password_entered, key="password")
        return False
    
    elif not st.session_state["password_correct"]:
        st.markdown("<h1 style='text-align: center; color: #3B82F6;'>🔒 Production Engine Security</h1>", unsafe_allow_html=True)
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
    
    /* Premium Header Area Custom Styling */
    .header-gradient {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 50%, #D97706 100%);
        padding: 2.5rem 2rem;
        border-radius: 14px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.15);
    }
    .header-gradient h1 { color: #FFFFFF !important; font-size: 2.4rem !important; font-weight: 800 !important; margin: 0 !important; }
    .header-gradient p { color: rgba(255, 255, 255, 0.9) !important; font-size: 1.05rem !important; margin: 0.5rem 0 0 0 !important; }
    
    /* Dynamic Performance Score Indicator */
    .score-banner {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid rgba(59, 130, 246, 0.3);
        color: #FFFFFF; padding: 1.5rem; border-radius: 12px; text-align: center; margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    }
    .score-banner h2 { color: #60A5FA !important; margin: 0 !important; font-weight: 700; font-size: 1.6rem; }
    
    /* Elegant Content Blocks (Containers/Forms) */
    .stContainer, .stForm {
        background: rgba(30, 41, 59, 0.7) !important; 
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px; padding: 1.75rem; margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25); backdrop-filter: blur(12px);
    }
    
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
        'lr_calculated': False,
        'lr_efficiency': 0.0,
        'knowledge_rating': 0.0,
        'lr_history': [],
        'lr_round_counter': 0,
        'quiz_done': False,
        'ans1_ok': False, 'ans2_ok': False, 'ans3_ok': False, 'ans4_ok': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_system_state()

# =====================================================================
# SIDEBAR CONTROL DECK
# =====================================================================
with st.sidebar:
    st.markdown("### 🚀 Long-Run Operations")
    nav_selection = st.radio(
        "Navigation Hub:",
        options=[
            "🚀 Long-Run Simulator Sandbox",
            "📖 Core Production Theory",
            "📊 Cost Economics & Financial Taxonomy",
            "📈 Geometric Expansion Paths",
            "📝 Operational Knowledge Check"
        ]
    )

# =====================================================================
# LIVE SCORE TRACKING ENGINE
# =====================================================================
score_container = st.container()
with score_container:
    combined_raw = st.session_state.lr_efficiency + st.session_state.knowledge_rating
    final_score = max(0.0, min(100.0, round(combined_raw, 1)))
    
    st.markdown(f"""
    <div class="score-banner">
        <h2>Long-Run Operational Efficiency Index: {final_score} / 100</h2>
        <p style='color: #FBBF24; margin: 0.25rem 0 0 0;'>
            🚀 Optimization Yield: {round(st.session_state.lr_efficiency, 1)}/50 | 
            📝 Quiz Accuracy: {round(st.session_state.knowledge_rating, 1)}/50
        </p>
        <small style='color: #94A3B8;'>System Constraint Note: Maximizing long-run index parameters requires configuring an exact least-cost asset footprint combinations layout.</small>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE ROUTING ARCHITECTURE
# =====================================================================

# --- SECTION 1: LONG RUN SIMULATOR ---
if nav_selection == "🚀 Long-Run Simulator Sandbox":
    st.markdown('<div class="section-header">🚀 Long-Run Isoquant & Cost Minimization Sandbox</div>', unsafe_allow_html=True)
    panel_left, panel_right = st.columns([1, 1.2])
    
    with panel_left:
        st.markdown("""
        <div class="concept-note">
        <h3>📌 Long-Run Scale Optimization</h3>
        <p><strong>All Inputs Are Variable:</strong> In the long run, your facility can scale both <strong>Workforce (Labor - $L$)</strong> and <strong>Infrastructure (Capital - $K$)</strong> without capacity limits.</p>
        <p><strong>Production Function:</strong> Modeled via a non-linear Cobb-Douglas framework:
        $$Q = A \cdot L^\alpha \cdot K^\beta$$</p>
        <p><strong>The Cost-Minimization Target:</strong> To achieve optimal output efficiency for a given budget, the firm must align inputs such that the Marginal Rate of Technical Substitution ($MRTS$) equals the input factor price ratio:
        $$MRTS_{L,K} = \frac{MP_L}{MP_K} = \frac{w}{r} \implies \frac{\alpha K}{\beta L} = \frac{w}{r}$$</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### ⚙️ Factor Input Prices & Elasticity Matrix")
        w_price = st.number_input("Wage Rate ($w$ / Unit of Labor):", min_value=1.0, max_value=200.0, value=20.0, step=5.0)
        r_price = st.number_input("Capital Rental Rate ($r$ / Unit of Capital):", min_value=1.0, max_value=200.0, value=40.0, step=5.0)
        
        st.markdown("##### Cobb-Douglas Output Scaling Parameters")
        alpha_val = st.slider("Labor Output Elasticity ($\\alpha$):", min_value=0.1, max_value=1.5, value=0.6, step=0.1)
        beta_val = st.slider("Capital Output Elasticity ($\\beta$):", min_value=0.1, max_value=1.5, value=0.4, step=0.1)

    with panel_right:
        st.markdown('<div class="case-study"><h4>🛠️ Operational Capacity Scaling Controls</h4></div>', unsafe_allow_html=True)
        st.write("Adjust both parameters simultaneously to configure your factory blueprint size.")
        
        input_l = st.slider("Select Long-Run Labor Force ($L$):", min_value=1, max_value=100, value=30, step=1)
        input_k = st.slider("Select Long-Run Capital Footprint ($K$):", min_value=1, max_value=100, value=20, step=1)
        
        compute_lr = st.button("🚀 Calculate Long-Run System Dynamics", type="primary", use_container_width=True)
        
        if compute_lr:
            tech_coeff = 10.0
            q_output = float(round(tech_coeff * (input_l ** alpha_val) * (input_k ** beta_val), 1))
            total_cost = float(round((w_price * input_l) + (r_price * input_k), 2))
            unit_cost = float(round(total_cost / q_output, 2)) if q_output > 0 else 0.0
            
            optimal_k_l_ratio = (beta_val * w_price) / (alpha_val * r_price)
            current_k_l_ratio = input_k / input_l
            ratio_deviation = abs(current_k_l_ratio - optimal_k_l_ratio) / optimal_k_l_ratio
            
            rts_sum = alpha_val + beta_val
            if abs(rts_sum - 1.0) < 0.01:
                rts_status = "Constant Returns to Scale (CRS) ⚖️"
            elif rts_sum > 1.0:
                rts_status = "Increasing Returns to Scale (IRS) 🚀"
            else:
                rts_status = "Decreasing Returns to Scale (DRS) 📉"
                
            if ratio_deviation <= 0.05:
                efficiency_status = "Optimal Input Mix: Perfect Alignment Chosen 🌟"
                points = 50.0
            elif ratio_deviation <= 0.25:
                efficiency_status = "Suboptimal Mix: Minor Resource Friction Detected ⚠️"
                points = 35.0
            else:
                efficiency_status = "Inefficient Mix: Major Resource Imbalance 🚨"
                points = 15.0
                
            st.session_state.lr_round_counter += 1
            st.session_state.lr_efficiency = min(50.0, points)
            
            st.session_state.lr_history.append({
                'run': st.session_state.lr_round_counter, 'L': input_l, 'K': input_k, 'Q': q_output,
                'cost': total_cost, 'unit_cost': unit_cost, 'rts': rts_status, 'efficiency': efficiency_status,
                'opt_ratio': optimal_k_l_ratio, 'curr_ratio': current_k_l_ratio
            })
            st.session_state.lr_calculated = True
            st.rerun()

    if st.session_state.lr_calculated:
        lr_metrics_block = st.container()
        with lr_metrics_block:
            st.markdown('<div class="section-header">📊 Dynamic Macro-Factory Performance Tracking</div>', unsafe_allow_html=True)
            latest_lr = st.session_state.lr_history[-1]
            c1, c2, c3, c4 = st.columns(4)
            
            with c1:
                st.markdown(f'<div class="metric-card"><h3>Total Output ($Q$)</h3><div class="metric-value">{latest_lr["Q"]} Units</div><p style="color: #64748B; font-size: 0.85rem;">Cobb-Douglas Production</p></div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div class="metric-card"><h3>Total Cost ($TC$)</h3><div class="metric-value">${latest_lr["cost"]}</div><p style="color: #64748B; font-size: 0.85rem;">$wL + rK$ Outlay</p></div>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div class="metric-card"><h3>Average Unit Cost</h3><div class="metric-value">${latest_lr["unit_cost"]}</div><p style="color: #64748B; font-size: 0.85rem;">Economic Cost Per Unit</p></div>', unsafe_allow_html=True)
            with c4:
                st.markdown(f'<div class="metric-card"><h3>Returns Matrix</h3><div class="metric-value" style="font-size: 1.15rem; padding-top: 0.4rem;">{latest_lr["rts"]}</div></div>', unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="concept-note" style="border-left-color: #FBBF24;">
                <h4>Allocation Diagnosis: {latest_lr['efficiency']}</h4>
                <p>Target Cost-Minimizing Ratio ($K/L$): <strong>{round(latest_lr['opt_ratio'], 3)}</strong> | Current Deployed Ratio ($K/L$): <strong>{round(latest_lr['curr_ratio'], 3)}</strong></p>
                <small>To lower unit costs to the absolute structural floor, alter inputs until your engineered ratio perfectly hits the target allocation threshold.</small>
            </div>
            """, unsafe_allow_html=True)

# --- SECTION 2: CORE THEORY DEEP DIVE ---
elif nav_selection == "📖 Core Production Theory":
    st.markdown('<div class="section-header">📚 Structural Mechanics of Long-Run Microeconomic Production</div>', unsafe_allow_html=True)
    theory_tabs = st.tabs(["Long-Run Variably Scaled Foundations", "Returns to Scale (RTS) Dynamics"])
    
    with theory_tabs[0]:
        st.markdown("""
        <div class="concept-note">
        <h3>🚀 Long-Run Production Functions & Isoquants</h3>
        <p>In analytical economics, the <strong>Long Run</strong> is defined as an optimization horizon where <strong>all factors of production are fully variable</strong>. Firms can switch asset sizes, construct new plants, or reshape total operational layouts simultaneously.</p>
        <p><strong>The Isoquant Map:</strong> An isoquant is a contour curve representing all distinct combinations of labor ($L$) and capital ($K$) that yield the <strong>exact same level of absolute total output</strong> ($Q$). Higher curves symbolize larger output capacity volumes.</p>
        <p><strong>Marginal Rate of Technical Substitution ($MRTS$):</strong> Measures the exact rate at which a firm can substitute capital for labor while maintaining a static output volume. It reflects the negative slope of the isoquant curve:</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"MRTS_{L,K} = -\frac{\Delta K}{\Delta L} = \frac{MP_L}{MP_K}")

    with theory_tabs[1]:
        st.markdown("""
        <div class="concept-note">
        <h3>⚖️ Returns to Scale Parameter Tracking</h3>
        <p>Returns to Scale evaluates how total output behaves when <strong>all production inputs are increased by the exact same proportional factor</strong> ($\lambda$).</p>
        <p>Using a homogeneous Cobb-Douglas function ($Q = A L^\alpha K^\beta$), scaling inputs by $\lambda$ results in: $Q(\lambda L, \lambda K) = \lambda^{\alpha + \beta} Q$.</p>
        <ul>
            <li><strong>Constant Returns to Scale (CRS):</strong> $\alpha + \beta = 1$. Doubling inputs perfectly doubles output yield.</li>
            <li><strong>Increasing Returns to Scale (IRS):</strong> $\alpha + \beta > 1$. Doubling inputs more than doubles total output (driven by structural specialization or specialization advantages).</li>
            <li><strong>Decreasing Returns to Scale (DRS):</strong> $\alpha + \beta < 1$. Doubling inputs leads to a less-than-proportional increase in total output (often caused by administrative complexity or management fragmentation).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 3: COST ECONOMICS & FINANCIAL TAXONOMY ---
elif nav_selection == "📊 Cost Economics & Financial Taxonomy":
    st.markdown('<div class="section-header">📊 Integrated Microeconomic Cost Analysis & Taxonomy</div>', unsafe_allow_html=True)
    
    cost_tab1, cost_tab2, cost_tab3, cost_tab4 = st.tabs([
        "💰 Accounting vs. Economic Cost",
        "🛑 Opportunity & Sunk Costs",
        "📉 Short-Run Cost Structure (FC, VC, TC)",
        "📐 Unit & Marginal Costs (AC, AFC, AVC, MC)"
    ])

    with cost_tab1:
        st.markdown("""
        <div class="concept-note">
        <h3>Accounting Cost vs. Economic Cost</h3>
        <p>Strategic decision-making requires distinguishing between conventional accounting expenditures and true economic cost.</p>
        <ul>
            <li><strong>Explicit Cost (Accounting Cost):</strong> Direct, out-of-pocket monetary expenses recorded in financial ledgers (e.g., wages, raw materials, rent, utilities).</li>
            <li><strong>Implicit Cost:</strong> The non-monetary opportunity costs of using self-owned resources (e.g., foregone salary of the owner, foregone rent on owned land, foregone interest on invested equity capital).</li>
            <li><strong>Economic Cost Equation:</strong></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"\text{Economic Cost} = \text{Explicit Costs} + \text{Implicit Costs}")
        
        st.markdown("""
        <div class="case-study">
        <h4>💡 Profitability Metrics Comparison</h4>
        <p><strong>Accounting Profit</strong> = Total Revenue - Explicit Costs</p>
        <p><strong>Economic Profit</strong> = Total Revenue - (Explicit Costs + Implicit Costs) = Total Revenue - Economic Cost</p>
        <p><em>Note: If Economic Profit = 0, the firm earns a <strong>Normal Profit</strong>, covering all explicit and implicit opportunity costs.</em></p>
        </div>
        """, unsafe_allow_html=True)

    with cost_tab2:
        col_opp, col_sunk = st.columns(2)
        
        with col_opp:
            st.markdown("""
            <div class="concept-note">
            <h3>💡 Opportunity Cost</h3>
            <p>The value of the <strong>next best alternative forgone</strong> when making a decision.</p>
            <p>Every resource deployment choice carries an opportunity cost. In cost minimization, if capital is deployed into machinery, its opportunity cost is the return it would have generated in its next best alternative investment.</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col_sunk:
            st.markdown("""
            <div class="case-study">
            <h3>🛑 Sunk Cost</h3>
            <p>An expense that has <strong>already been incurred and cannot be recovered</strong> by any future decision.</p>
            <p><strong>The Golden Rule of Sunk Costs:</strong> Sunk costs are <em>irrelevant</em> for forward-looking economic decisions. Rational firms ignore sunk costs when evaluating marginal production steps.</p>
            </div>
            """, unsafe_allow_html=True)

    with cost_tab3:
        st.markdown("""
        <div class="concept-note">
        <h3>Short-Run Production Cost Components</h3>
        <p>In the short run, at least one factor of production (usually Capital $K$) is fixed.</p>
        <ul>
            <li><strong>Total Fixed Cost (TFC):</strong> Expenses that do not vary with output volume ($Q$). They must be paid even if output is zero (e.g., factory lease, administrative salaries).</li>
            <li><strong>Total Variable Cost (TVC):</strong> Expenses that vary directly with output volume ($Q$) (e.g., raw materials, direct hourly labor).</li>
            <li><strong>Total Cost (TC) Identity:</strong></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r"TC(Q) = TFC + TVC(Q)")

    with cost_tab4:
        st.markdown("""
        <div class="concept-note">
        <h3>Per-Unit and Marginal Cost Dynamics</h3>
        <p>Dividing total metrics by volume ($Q$) yields per-unit cost curves, which govern competitive pricing and profit-maximization behavior.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"ATC = \frac{TC}{Q} = \frac{TFC + TVC}{Q} = AFC + AVC")
        st.latex(r"MC = \frac{\Delta TC}{\Delta Q} = \frac{\partial TC}{\partial Q}")
        
        st.markdown("""
        <div class="case-study">
        <h4>📌 Critical Curve Relationships</h4>
        <ul>
            <li><strong>Average Fixed Cost ($AFC$):</strong> Continuously declines as output scales (known as <em>"spreading the overhead"</em>).</li>
            <li><strong>Marginal Cost ($MC$) and Average Cost ($ATC$/$AVC$):</strong>
                <ul>
                    <li>When $MC < ATC$, Average Total Cost is falling.</li>
                    <li>When $MC > ATC$, Average Total Cost is rising.</li>
                    <li>$MC$ intersects $ATC$ and $AVC$ at their absolute <strong>minimum points</strong>.</li>
                </ul>
            </li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 4: GEOMETRIC EXPANSION PATHS ---
elif nav_selection == "📈 Geometric Expansion Paths":
    st.markdown('<div class="section-header">📈 Core Mathematical Intersections & Long-Run Expansion Paths</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="case-study">
    <h4>🗺️ Long-Run Optimization & The Expansion Path Frontier</h4>
    <p>In long-run optimization geometry, structural efficiency is modeled by overlaying <strong>Isoquants</strong> with <strong>Isocost Lines</strong>:</p>
    <ul>
        <li><strong>Isocost Line Equation:</strong> Represents all asset combinations costing an identical total financial capital outlay ($TC = wL + rK$). The slope equals the relative economic price ratio: $-w/r$.</li>
        <li><strong>Tangency Optimization Equilibrium:</strong> The least-cost combination to achieve a target output level occurs at the precise graphic location where an isoquant curve is perfectly tangent to the lowest achievable isocost line. At this point:</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.latex(r"MRTS_{L,K} = \frac{MP_L}{MP_K} = \frac{w}{r}")
    st.markdown("""
    <div class="case-study">
    <p><strong>The Expansion Path:</strong> Connecting all consecutive tangency equilibrium points as production scales creates the firm's <strong>Long-Run Expansion Path</strong>. This line traces the most financially rational path for structural asset configuration as a company scales.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION 5: KNOWLEDGE CHECK ---
elif nav_selection == "📝 Operational Knowledge Check":
    st.markdown('<div class="section-header">📝 Master Long-Run Production & Cost Knowledge Evaluation Deck</div>', unsafe_allow_html=True)
    st.markdown("Test your integrated understanding of production scaling and economic cost architecture.")
    
    with st.form("integrated_production_quiz"):
        st.markdown("### 1. Long-Run Cost Minimization Parameter Alignment")
        q1 = st.radio(
            "What condition mathematically characterizes the optimal, least-cost combinations of inputs along a firm's long-run expansion path?",
            options=[
                "A) Marginal product of all variable assets drops to absolute zero.",
                "B) The MRTS is perfectly equal to the ratio of the factor input prices (w/r).",
                "C) Labor and capital inputs are utilized in an identical 1:1 hardware footprint ratio.",
                "D) Total fixed outlays perfectly equal total variable outlays."
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. Decoding Returns to Scale Functionality")
        q2 = st.radio(
            "If a company doubles both its labor force and its capital assets, and total output increases by exactly 150%, how is this function categorized?",
            options=[
                "A) Decreasing Returns to Scale (DRS)",
                "B) Constant Returns to Scale (CRS)",
                "C) Increasing Returns to Scale (IRS)",
                "D) Conflicted Diminishing Returns Architecture"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Economic Profit vs. Accounting Profit")
        q3 = st.radio(
            "An entrepreneur leaves a $100,000/year job to start a firm. Revenues are $300,000 and explicit costs are $180,000. What is the Economic Profit?",
            options=[
                "A) $120,000",
                "B) $20,000",
                "C) $300,000",
                "D) -$80,000"
            ], index=None
        )
        
        st.markdown("---")
        st.markdown("### 4. Sunk Cost & Decision Theory")
        q4 = st.radio(
            "A company spent $5M developing a prototype that turns out to be non-viable. To complete it will cost $1M more, but projected revenue is only $500,000. Should they proceed?",
            options=[
                "A) Yes, to recover part of the initial $5M investment.",
                "B) No, because incremental revenue ($500k) is less than incremental cost ($1M); the $5M is a sunk cost.",
                "C) Yes, because total revenue exceeds the remaining variable cost.",
                "D) No, because fixed costs must always be amortized fully."
            ], index=None
        )
        
        eval_quiz = st.form_submit_button("Submit Performance Metrics", type="primary")
        
        if eval_quiz:
            score_acc = 0.0
            
            if q1 == "B) The MRTS is perfectly equal to the ratio of the factor input prices (w/r).":
                score_acc += 12.5; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False
                
            if q2 == "C) Increasing Returns to Scale (IRS)":
                score_acc += 12.5; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False
                
            if q3 == "B) $20,000":
                score_acc += 12.5; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False

            if q4 == "B) No, because incremental revenue ($500k) is less than incremental cost ($1M); the $5M is a sunk cost.":
                score_acc += 12.5; st.session_state.ans4_ok = True
            else: st.session_state.ans4_ok = False
                
            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Performance Score: {round(st.session_state.knowledge_rating, 1)} / 50 Points")
        
        if not st.session_state.ans1_ok:
            st.error("**Q1 Analysis:** Cost minimization dictates that the rate at which you can technically trade inputs ($MRTS$) must align with the market rate for buying them ($w/r$).")
        if not st.session_state.ans2_ok:
            st.error("**Q2 Analysis:** Scaling inputs by 2x (100% increase) yielding a 2.5x (150% increase) output shift indicates Increasing Returns to Scale ($\alpha + \beta > 1$).")
        if not st.session_state.ans3_ok:
            st.error("**Q3 Analysis:** Accounting Profit = $300k - $180k = $120k. Subtract the $100k foregone salary (implicit cost) to get Economic Profit = $20,000.")
        if not st.session_state.ans4_ok:
            st.error("**Q4 Analysis:** The $5M spent is a sunk cost and unrecoverable. Marginal cost to finish ($1M) exceeds marginal revenue ($500k), so continuing loses another $500k.")

# =====================================================================
# SYSTEM FOOTER DATA TERMINAL
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("🎓 Production & Cost Optimization Engine | Corporate Strategy Hub")

with foot_c2:
    st.caption("🚀 Fully Variable Asset Scale Optimization Active")

with foot_c3:
    st.caption(f"⏰ Engine System Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
