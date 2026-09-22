import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="National Income & Macroeconomic Accounting Engine",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# SECURE ACCESS SYSTEM
# =====================================================================
def check_password():
    """Validates authorization token before deploying the application."""
    def password_entered():
        if st.session_state["password"] == "MACRO2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #38BDF8;'>🔒 Operations Engine Security</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #94A3B8;'>Enter credential key to deploy the National Accounting Architecture.</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.4, 1])
        with col2:
            st.text_input("Security Access Key (Default: 'MACRO2026')", type="password", on_change=password_entered, key="password")
        return False

    elif not st.session_state["password_correct"]:
        st.markdown("<h1 style='text-align: center; color: #38BDF8;'>🔒 Operations Engine Security</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.4, 1])
        with col2:
            st.text_input("Security Access Key (Default: 'MACRO2026')", type="password", on_change=password_entered, key="password")
            st.error("Access denied. Invalid authentication key.")
        return False

    return True

if not check_password():
    st.stop()

# =====================================================================
# CORE DESIGN SYSTEM (MIDNIGHT SAPPHIRE, CYAN & WARM GOLD)
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

    .stContainer, .stForm {
        background: rgba(15, 39, 68, 0.55) !important;
        border: 1px solid rgba(56, 189, 248, 0.15) !important;
        border-radius: 14px; 
        padding: 1.75rem; 
        margin-bottom: 1.5rem;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3); 
        backdrop-filter: blur(14px);
    }

    .section-header {
        color: #FCD34D; 
        font-weight: 700; 
        font-size: 1.45rem; 
        margin-bottom: 1.25rem;
        padding-bottom: 0.75rem; 
        border-bottom: 1px solid rgba(252, 211, 77, 0.25);
    }

    .concept-note, .case-study { 
        padding: 1.25rem; 
        border-radius: 10px; 
        margin: 1.2rem 0; 
    }
    .concept-note { 
        background: rgba(14, 165, 233, 0.08); 
        border-left: 4px solid #0EA5E9; 
    }
    .concept-note h3 { 
        color: #38BDF8; 
        margin-top: 0 !important; 
        font-size: 1.2rem; 
    }
    .case-study { 
        background: rgba(245, 158, 11, 0.08); 
        border-left: 4px solid #F59E0B; 
    }
    .case-study h4 { 
        color: #FCD34D; 
        margin-top: 0 !important; 
        font-size: 1.2rem; 
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
        font-size: 1rem; 
        margin: 0 0 0.5rem 0; 
        font-weight: 500;
    }
    .metric-value { 
        color: #38BDF8; 
        font-size: 1.85rem; 
        font-weight: 700; 
        margin: 0.25rem 0; 
    }

    .formula-badge {
        background: rgba(245, 158, 11, 0.12);
        border: 1px solid rgba(245, 158, 11, 0.35);
        color: #FCD34D;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
        margin: 0.4rem 0;
    }

    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%) !important; 
        color: white !important;
        border: none !important; 
        padding: 0.65rem 1.8rem !important; 
        border-radius: 8px !important;
        font-weight: 600 !important; 
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover { 
        transform: translateY(-1px) !important; 
        box-shadow: 0 6px 20px rgba(14, 165, 233, 0.4) !important; 
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
# SIDEBAR CONTROL NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("### 🌐 Aggregates & Output Portal")
    nav_selection = st.radio(
        "Navigation Module:",
        options=[
            "⚖️ Core Macroeconomic Aggregates (NDP, GNP, NNP)",
            "🔀 Aggregate Bridge & Identities Matrix",
            "🧮 Aggregate Derivation Engine & Visualizer",
            "📝 Aggregate Mastery Assessment"
        ]
    )

# =====================================================================
# PERFORMANCE SCOREBOARD
# =====================================================================
score_container = st.container()
with score_container:
    st.markdown(f"""
    <div class="score-banner">
        <h2>National Aggregates Accounting Mastery: {round(st.session_state.knowledge_rating, 1)} / 100</h2>
        <p style='color: #FCD34D; margin: 0.25rem 0 0 0;'>
            🌐 Gross vs Net (Depreciation) | Domestic vs National (NFIA) | Market Price vs Factor Cost (NIT)
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE MODULES
# =====================================================================

# --- MODULE 1: CORE AGGREGATES BREAKDOWN ---
if nav_selection == "⚖️ Core Macroeconomic Aggregates (NDP, GNP, NNP)":
    st.markdown('<div class="section-header">⚖️ Core National Aggregates: NDP, GNP, NNP & National Income</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-note">
        <h3>🌐 Deconstructing the Macroeconomic Ladder</h3>
        <p>National income accounting derives primary economic indicators using three fundamental dualities:</p>
        <ul>
            <li><strong>Gross vs. Net:</strong> Mediated by <code>Depreciation</code> (Consumption of Fixed Capital).</li>
            <li><strong>Domestic vs. National:</strong> Mediated by <code>NFIA</code> (Net Factor Income from Abroad).</li>
            <li><strong>Market Price vs. Factor Cost:</strong> Mediated by <code>NIT</code> (Net Indirect Taxes = Indirect Taxes - Subsidies).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # 1. NET DOMESTIC PRODUCT (NDP)
    st.markdown("### 1. Net Domestic Product (NDP)")
    ndp_col1, ndp_col2 = st.columns(2)

    with ndp_col1:
        st.markdown("""
        <div class="case-study">
            <h4>📦 NDP at Market Price (NDP_MP)</h4>
            <p>The net economic output produced strictly within national geographical borders after deducting capital consumption.</p>
            <div class="formula-badge">NDP_MP = GDP_MP - Depreciation</div>
            <ul>
                <li><strong>Significance:</strong> Represents sustainable domestic production. Producing output while depleting physical assets without replacement erodes the capital base.</li>
                <li><strong>Measurement:</strong> Depreciation is an accounting estimate, making NDP subject to differing national calculation standards.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with ndp_col2:
        st.markdown("""
        <div class="concept-note" style="border-left-color: #10B981;">
            <h4 style="color: #34D399;">💼 NDP at Factor Cost (NDP_FC)</h4>
            <p>Commonly referred to as <strong>Domestic Factor Income</strong>. It measures the net return to domestic production factors within territorial borders.</p>
            <div class="formula-badge">NDP_FC = NDP_MP - Net Indirect Taxes (NIT)</div>
            <p><strong>Factor Component Equation:</strong></p>
            <div class="formula-badge">NDP_FC = Compensation of Employees + Operating Surplus + Mixed Income</div>
        </div>
        """, unsafe_allow_html=True)

    # 2. GROSS NATIONAL PRODUCT (GNP)
    st.markdown("### 2. Gross National Product (GNP)")
    gnp_col1, gnp_col2 = st.columns(2)

    with gnp_col1:
        st.markdown("""
        <div class="case-study">
            <h4>🌍 GNP at Market Price (GNP_MP)</h4>
            <p>The total market value of all final production owned and generated by legal residents of an economy, irrespective of geography.</p>
            <div class="formula-badge">GNP_MP = GDP_MP + NFIA</div>
            <ul>
                <li><strong>Factor Inflow (+):</strong> Compensation, investment returns, and profits earned by national residents and firms abroad.</li>
                <li><strong>Factor Outflow (-):</strong> Income repatriated out of the economy by foreign workers and foreign capital.</li>
                <li><strong>Comparative Rule:</strong> If foreign factor income outflows exceed domestic resident inflows abroad, <code>GDP &gt; GNP</code>.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with gnp_col2:
        st.markdown("""
        <div class="concept-note" style="border-left-color: #38BDF8;">
            <h4 style="color: #38BDF8;">🏭 GNP at Factor Cost (GNP_FC)</h4>
            <p>The total gross earnings received by normal residents before accounting for capital wear and tear, calculated at factor costs.</p>
            <div class="formula-badge">GNP_FC = GNP_MP - Net Indirect Taxes (NIT)</div>
            <div class="formula-badge">GNP_FC = GDP_FC + NFIA</div>
            <p style="margin-top: 0.5rem; font-size: 0.9rem; color: #94A3B8;">
                Provides an assessment of the gross purchasing power and production claim generated by citizens before product tax distortion.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 3. NET NATIONAL PRODUCT (NNP) & NATIONAL INCOME
    st.markdown("### 3. Net National Product (NNP) & Pure National Income")
    nnp_col1, nnp_col2 = st.columns(2)

    with nnp_col1:
        st.markdown("""
        <div class="case-study">
            <h4>🏷️ NNP at Market Price (NNP_MP)</h4>
            <p>The net market value of final commodities produced by normal residents of an economy.</p>
            <div class="formula-badge">NNP_MP = GNP_MP - Depreciation</div>
            <div class="formula-badge">NNP_MP = NDP_MP + NFIA</div>
            <p style="margin-top: 0.5rem; font-size: 0.9rem; color: #94A3B8;">
                Indicates the net quantity of goods and services available for consumption and net capital addition at current retail price levels.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with nnp_col2:
        st.markdown("""
        <div class="concept-note" style="border-left-color: #F59E0B;">
            <h4 style="color: #FCD34D;">👑 NNP at Factor Cost (NNP_FC) — "National Income"</h4>
            <p>The exact theoretical and technical definition of <strong>National Income (NI)</strong>.</p>
            <div class="formula-badge">National Income (NI) = NNP_MP - Net Indirect Taxes</div>
            <div class="formula-badge">National Income (NI) = NDP_FC + NFIA</div>
            <ul>
                <li>Excludes capital consumption allowance (depreciation).</li>
                <li>Excludes production income earned by non-residents within domestic boundaries.</li>
                <li>Excludes indirect sales/service taxes and adds back production subsidies.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- MODULE 2: AGGREGATE BRIDGE & IDENTITIES MATRIX ---
elif nav_selection == "🔀 Aggregate Bridge & Identities Matrix":
    st.markdown('<div class="section-header">🔀 Structural Conversion Nexus & Identities Matrix</div>', unsafe_allow_html=True)

    b1, b2, b3 = st.columns(3)
    with b1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #38BDF8;">Gross ⟷ Net</h3>
            <p style="color: #FCD34D; font-weight: 700; font-size: 1.1rem; margin: 0.6rem 0;">Depreciation Pivot</p>
            <p style="font-size: 0.88rem; color: #94A3B8;">Accounts for the loss of value of capital goods through physical wear, tear, or obsolescence.</p>
            <div class="formula-badge" style="font-size: 0.85rem;">Net = Gross - Depreciation</div>
        </div>
        """, unsafe_allow_html=True)

    with b2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #38BDF8;">Domestic ⟷ National</h3>
            <p style="color: #FCD34D; font-weight: 700; font-size: 1.1rem; margin: 0.6rem 0;">NFIA Pivot</p>
            <p style="font-size: 0.88rem; color: #94A3B8;">Factor income earned by residents abroad minus factor income paid to foreign owners domestically.</p>
            <div class="formula-badge" style="font-size: 0.85rem;">National = Domestic + NFIA</div>
        </div>
        """, unsafe_allow_html=True)

    with b3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #38BDF8;">Market Price ⟷ Factor Cost</h3>
            <p style="color: #FCD34D; font-weight: 700; font-size: 1.1rem; margin: 0.6rem 0;">Fiscal Wedge (NIT)</p>
            <p style="font-size: 0.88rem; color: #94A3B8;">Indirect taxes inflate market prices above factor payments; government subsidies lower market prices.</p>
            <div class="formula-badge" style="font-size: 0.85rem;">Market Price = Factor Cost + NIT</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 📋 Complete Macroeconomic Aggregates Matrix")
    summary_matrix = pd.DataFrame([
        {
            "Aggregate Symbol": "GDP_MP",
            "Nomenclature": "Gross Domestic Product at Market Price",
            "Formula Definition": "C + I + G + (X - M)",
            "Deduction / Addition": "Gross territory output"
        },
        {
            "Aggregate Symbol": "NDP_MP",
            "Nomenclature": "Net Domestic Product at Market Price",
            "Formula Definition": "GDP_MP - Depreciation",
            "Deduction / Addition": "Subtracts capital wear and tear"
        },
        {
            "Aggregate Symbol": "GNP_MP",
            "Nomenclature": "Gross National Product at Market Price",
            "Formula Definition": "GDP_MP + NFIA",
            "Deduction / Addition": "Swaps geographic border for resident ownership"
        },
        {
            "Aggregate Symbol": "NNP_MP",
            "Nomenclature": "Net National Product at Market Price",
            "Formula Definition": "GNP_MP - Depreciation  |  NDP_MP + NFIA",
            "Deduction / Addition": "Net resident production at market transaction price"
        },
        {
            "Aggregate Symbol": "GDP_FC",
            "Nomenclature": "Gross Domestic Product at Factor Cost",
            "Formula Definition": "GDP_MP - NIT",
            "Deduction / Addition": "Strips out indirect taxes and re-adds subsidies"
        },
        {
            "Aggregate Symbol": "NDP_FC",
            "Nomenclature": "Net Domestic Product at Factor Cost (Domestic Income)",
            "Formula Definition": "NDP_MP - NIT  |  GDP_FC - Depreciation",
            "Deduction / Addition": "Wages + Rent + Interest + Profit + Mixed Income"
        },
        {
            "Aggregate Symbol": "GNP_FC",
            "Nomenclature": "Gross National Product at Factor Cost",
            "Formula Definition": "GNP_MP - NIT  |  GDP_FC + NFIA",
            "Deduction / Addition": "Gross citizen earnings at factor production cost"
        },
        {
            "Aggregate Symbol": "NNP_FC",
            "Nomenclature": "Net National Product at Factor Cost (National Income)",
            "Formula Definition": "NNP_MP - NIT  |  NDP_FC + NFIA",
            "Deduction / Addition": "Official technical National Income (NI)"
        }
    ])

    st.dataframe(summary_matrix, use_container_width=True, hide_index=True)

# --- MODULE 3: DERIVATION ENGINE & SIMULATOR ---
elif nav_selection == "🧮 Aggregate Derivation Engine & Visualizer":
    st.markdown('<div class="section-header">🧮 National Accounting Derivation Engine</div>', unsafe_allow_html=True)
    st.markdown("Adjust primary macroeconomic parameters to observe real-time derivations across all 8 aggregates.")

    sim_c1, sim_c2 = st.columns([1, 1.25])

    with sim_c1:
        st.markdown("#### Baseline Output (in Billions)")
        gdp_val = st.slider("Nominal GDP at Market Price (GDP_MP):", min_value=500.0, max_value=5000.0, value=2500.0, step=50.0)
        dep_val = st.slider("Capital Consumption Allowance (Depreciation):", min_value=20.0, max_value=600.0, value=250.0, step=10.0)

        st.markdown("#### Factor Income Flows Across Borders")
        fi_in = st.slider("Factor Income Earned by Domestic Residents Abroad:", min_value=0.0, max_value=300.0, value=140.0, step=5.0)
        fi_out = st.slider("Factor Income Paid to Foreign Entities Domestically:", min_value=0.0, max_value=300.0, value=90.0, step=5.0)

        st.markdown("#### Government Fiscal Intervention")
        ind_tax = st.slider("Indirect Taxes (GST, Sales, Customs):", min_value=10.0, max_value=500.0, value=260.0, step=10.0)
        subs = st.slider("Production Subsidies:", min_value=0.0, max_value=200.0, value=70.0, step=5.0)

        # Computations
        nfia = fi_in - fi_out
        nit = ind_tax - subs
        ndp_mp = gdp_val - dep_val
        gnp_mp = gdp_val + nfia
        nnp_mp = gnp_mp - dep_val
        gdp_fc = gdp_val - nit
        ndp_fc = ndp_mp - nit
        gnp_fc = gnp_mp - nit
        nnp_fc = nnp_mp - nit

    with sim_c2:
        st.markdown("#### 📊 Derived National Accounting Aggregates")

        r1, r2 = st.columns(2)
        with r1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Domestic Income (NDP_FC)</h3>
                <div class="metric-value">{ndp_fc:,.2f}</div>
                <p style="color: #94A3B8; font-size: 0.85rem;">Factor earnings within borders</p>
            </div>
            """, unsafe_allow_html=True)
        with r2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>National Income (NNP_FC)</h3>
                <div class="metric-value" style="color: #FCD34D;">{nnp_fc:,.2f}</div>
                <p style="color: #94A3B8; font-size: 0.85rem;">Net earnings of normal residents</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        derivation_table = pd.DataFrame([
            {"Aggregate": "GDP_MP", "Operation": "Reported Gross Output", "Result (Billion $)": f"{gdp_val:,.2f}"},
            {"Aggregate": "NDP_MP", "Operation": "GDP_MP - Depreciation", "Result (Billion $)": f"{ndp_mp:,.2f}"},
            {"Aggregate": "GNP_MP", "Operation": "GDP_MP + NFIA", "Result (Billion $)": f"{gnp_mp:,.2f}"},
            {"Aggregate": "NNP_MP", "Operation": "GNP_MP - Depreciation", "Result (Billion $)": f"{nnp_mp:,.2f}"},
            {"Aggregate": "GDP_FC", "Operation": "GDP_MP - NIT", "Result (Billion $)": f"{gdp_fc:,.2f}"},
            {"Aggregate": "NDP_FC", "Operation": "NDP_MP - NIT", "Result (Billion $)": f"{ndp_fc:,.2f}"},
            {"Aggregate": "GNP_FC", "Operation": "GNP_MP - NIT", "Result (Billion $)": f"{gnp_fc:,.2f}"},
            {"Aggregate": "NNP_FC (NI)", "Operation": "NNP_MP - NIT", "Result (Billion $)": f"{nnp_fc:,.2f}"}
        ])
        st.dataframe(derivation_table, use_container_width=True, hide_index=True)

        chart_df = pd.DataFrame({
            "Aggregate": ["GDP (MP)", "NDP (MP)", "GNP (MP)", "NNP (MP)", "NDP (FC)", "NNP (FC)"],
            "Magnitude": [gdp_val, ndp_mp, gnp_mp, nnp_mp, ndp_fc, nnp_fc]
        }).set_index("Aggregate")
        st.bar_chart(chart_df)

# --- MODULE 4: KNOWLEDGE DECK ---
elif nav_selection == "📝 Aggregate Mastery Assessment":
    st.markdown('<div class="section-header">📝 Macroeconomic Aggregates Assessment</div>', unsafe_allow_html=True)
    st.markdown("Test your understanding of conversions between Gross, Net, Domestic, National, Factor Cost, and Market Price.")

    with st.form("aggregates_quiz"):
        st.markdown("### 1. The Domestic-to-National Pivot")
        q1 = st.radio(
            "Which factor explains the numerical difference between Gross Domestic Product (GDP) and Gross National Product (GNP)?",
            options=[
                "A) Consumption of fixed capital (Depreciation).",
                "B) Net Factor Income from Abroad (NFIA).",
                "C) Net Indirect Taxes (Indirect Taxes minus Subsidies).",
                "D) The GDP Deflator."
            ], index=None
        )

        st.markdown("---")
        st.markdown("### 2. Market Price vs. Factor Cost Conversion")
        q2 = st.radio(
            "To derive an aggregate at Factor Cost (FC) starting from Market Price (MP), which adjustment is made?",
            options=[
                "A) Add Indirect Taxes and deduct Subsidies.",
                "B) Deduct Indirect Taxes and add Subsidies (Subtract Net Indirect Taxes).",
                "C) Add Depreciation and add NFIA.",
                "D) Deduct NFIA and divide by the price index."
            ], index=None
        )

        st.markdown("---")
        st.markdown("### 3. Depreciation and Capital Conservation")
        q3 = st.radio(
            "What distinguishes Net Domestic Product (NDP) from Gross Domestic Product (GDP)?",
            options=[
                "A) NDP excludes output produced by state-owned enterprises.",
                "B) NDP deducts the monetary value of capital wear, tear, and obsolescence (Depreciation).",
                "C) NDP includes intermediate consumption directly in final output.",
                "D) NDP adjusts for imported consumption items."
            ], index=None
        )

        st.markdown("---")
        st.markdown("### 4. Technical Definition of National Income")
        q4 = st.radio(
            "In national income accounting, which aggregate is officially termed 'National Income'?",
            options=[
                "A) Gross National Product at Market Price (GNP_MP).",
                "B) Net Domestic Product at Factor Cost (NDP_FC).",
                "C) Net National Product at Factor Cost (NNP_FC).",
                "D) Gross Domestic Product at Factor Cost (GDP_FC)."
            ], index=None
        )

        st.markdown("---")
        st.markdown("### 5. Multi-Step Aggregate Derivation")
        q5 = st.radio(
            "Given: GDP_MP = 1,000 | Depreciation = 100 | Indirect Taxes = 80 | Subsidies = 20 | NFIA = -40. What is National Income (NNP_FC)?",
            options=[
                "A) 800",
                "B) 860",
                "C) 920",
                "D) 780"
            ], index=None
        )

        eval_quiz = st.form_submit_button("Submit Assessment", type="primary")

        if eval_quiz:
            score_acc = 0.0

            if q1 == "B) Net Factor Income from Abroad (NFIA).":
                score_acc += 20.0; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False

            if q2 == "B) Deduct Indirect Taxes and add Subsidies (Subtract Net Indirect Taxes).":
                score_acc += 20.0; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False

            if q3 == "B) NDP deducts the monetary value of capital wear, tear, and obsolescence (Depreciation).":
                score_acc += 20.0; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False

            if q4 == "C) Net National Product at Factor Cost (NNP_FC).":
                score_acc += 20.0; st.session_state.ans4_ok = True
            else: st.session_state.ans4_ok = False

            # Calculation for Q5:
            # NDP_MP = 1000 - 100 = 900
            # NNP_MP = NDP_MP + NFIA = 900 + (-40) = 860
            # NIT = 80 - 20 = 60
            # NNP_FC = NNP_MP - NIT = 860 - 60 = 800
            if q5 == "A) 800":
                score_acc += 20.0; st.session_state.ans5_ok = True
            else: st.session_state.ans5_ok = False

            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### Assessment Score: {round(st.session_state.knowledge_rating, 1)} / 100 Points")

        if not st.session_state.ans1_ok:
            st.error("Q1 Analysis: The difference between Domestic and National output is Net Factor Income from Abroad (NFIA).")
        if not st.session_state.ans2_ok:
            st.error("Q2 Analysis: Transitioning to Factor Cost requires deducting indirect taxes and adding subsidies (subtracting NIT).")
        if not st.session_state.ans3_ok:
            st.error("Q3 Analysis: Gross minus Net equals Depreciation (Consumption of Fixed Capital).")
        if not st.session_state.ans4_ok:
            st.error("Q4 Analysis: National Income is technically defined as Net National Product at Factor Cost (NNP_FC).")
        if not st.session_state.ans5_ok:
            st.error("Q5 Analysis: NNP_FC = GDP_MP - Depreciation + NFIA - NIT = 1000 - 100 + (-40) - (80 - 20) = 900 - 40 - 60 = 800.")

# =====================================================================
# SYSTEM FOOTER
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("🌐 Macroeconomic Aggregates & Identities Architecture")

with foot_c2:
    st.caption("📈 NDP, GNP, NNP & Factor Cost Translation")

with foot_c3:
    st.caption(f"⏰ Platform Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
