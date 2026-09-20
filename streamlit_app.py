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
    st.markdown("### 🌐 Macroeconomic Portal")
    nav_selection = st.radio(
        "Navigation Module:",
        options=[
            "📌 National Output Foundations (GDP & Methods)",
            "⚖️ The Conversion Nexus: Gross/Net, Dom/Nat, FC/MP",
            "📉 GDP Deflator & Inflation Mechanics",
            "📅 Base Year Selection Architecture",
            "🧮 Macroeconomic Aggregates Simulator",
            "📝 Macroeconomic Accounting Knowledge Deck"
        ]
    )

# =====================================================================
# PERFORMANCE SCOREBOARD
# =====================================================================
score_container = st.container()
with score_container:
    st.markdown(f"""
    <div class="score-banner">
        <h2>National Income Accounting Mastery: {round(st.session_state.knowledge_rating, 1)} / 100</h2>
        <p style='color: #FCD34D; margin: 0.25rem 0 0 0;'>
            🌐 Gross Domestic Product, Deflator Dynamics, Factor Cost Conversions & Base-Year Architecture
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# INTERACTIVE MODULES
# =====================================================================

# --- MODULE 1: GDP FOUNDATIONS ---
if nav_selection == "📌 National Output Foundations (GDP & Methods)":
    st.markdown('<div class="section-header">📌 Gross Domestic Product & Measurement Approaches</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-note">
    <h3>🌐 Defining Gross Domestic Product (GDP)</h3>
    <p>Gross Domestic Product represents the total monetary value of all final goods and services produced within the territorial borders of a country over a defined duration (typically one fiscal year or quarter), before deductions for capital depreciation.</p>
    <ul>
        <li><strong>Final vs. Intermediate Output:</strong> Only goods at the endpoint of the production pipeline are incorporated to avoid catastrophic double-counting.</li>
        <li><strong>Geographic Boundary:</strong> Includes all domestic production regardless of whether produced by domestic citizens or foreign multinational entities.</li>
        <li><strong>Current Flow:</strong> Measures current production flows exclusively; pre-owned second-hand asset transfers and purely financial portfolio transactions are strictly excluded.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="case-study">
        <h4>📦 The Expenditure Method</h4>
        <p>Measures aggregate end-user expenditure across economic agents:</p>
        <div class="formula-badge">GDP = C + I + G + (X - M)</div>
        <ul>
            <li><strong>C (Private Consumption):</strong> Household spending on durable goods, nondurables, and services.</li>
            <li><strong>I (Gross Investment):</strong> Capital assets, infrastructure, and inventory accumulations.</li>
            <li><strong>G (Government Spending):</strong> Public consumption and capital infrastructure spending.</li>
            <li><strong>X - M (Net Exports):</strong> Domestic goods demanded abroad minus domestic demand for foreign imports.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="concept-note" style="border-left-color: #10B981;">
        <h4 style="color: #34D399;">💼 The Income & Value Added Methods</h4>
        <p><strong>1. Income Method:</strong> Evaluates earnings distributed to primary production factors:</p>
        <div class="formula-badge">GDP = Wages + Rent + Interest + Corporate Profits + Depreciation + Net Indirect Taxes</div>
        <p><strong>2. Production (Value Added) Method:</strong> Sums value generated across industry links to negate cascading intermediate costs:</p>
        <div class="formula-badge">Gross Value Added (GVA) = Gross Value of Output - Value of Intermediate Inputs</div>
        </div>
        """, unsafe_allow_html=True)

# --- MODULE 2: AGGREGATE BRIDGE ---
elif nav_selection == "⚖️ The Conversion Nexus: Gross/Net, Dom/Nat, FC/MP":
    st.markdown('<div class="section-header">⚖️ The Three Fundamental Conceptual Bridges</div>', unsafe_allow_html=True)

    st.markdown("""
    National income accounting evaluates identical production totals through three structural translation axes:
    """)

    b1, b2, b3 = st.columns(3)
    with b1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #38BDF8;">1. Gross vs. Net</h3>
            <p style="color: #FCD34D; font-weight: 700; font-size: 1.1rem; margin: 0.6rem 0;">Depreciation Pivot</p>
            <p style="font-size: 0.88rem; color: #94A3B8;">Deducts capital consumption from wear, tear, and technological obsolescence.</p>
            <div class="formula-badge" style="font-size: 0.85rem;">Net = Gross - Depreciation</div>
        </div>
        """, unsafe_allow_html=True)

    with b2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #38BDF8;">2. Domestic vs. National</h3>
            <p style="color: #FCD34D; font-weight: 700; font-size: 1.1rem; margin: 0.6rem 0;">NFIA Pivot</p>
            <p style="font-size: 0.88rem; color: #94A3B8;">Adjusts for earnings of national citizens abroad minus foreigners inside domestic borders.</p>
            <div class="formula-badge" style="font-size: 0.85rem;">National = Domestic + NFIA</div>
        </div>
        """, unsafe_allow_html=True)

    with b3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #38BDF8;">3. Factor Cost vs. Market Price</h3>
            <p style="color: #FCD34D; font-weight: 700; font-size: 1.1rem; margin: 0.6rem 0;">Fiscal Wedge (NIT)</p>
            <p style="font-size: 0.88rem; color: #94A3B8;">Factors in government intervention via product taxes and subsidies.</p>
            <div class="formula-badge" style="font-size: 0.85rem;">Market Price = Factor Cost + NIT</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    trans_table = pd.DataFrame([
        {"Base Metric": "GDP at Market Price (GDP_MP)", "Conversion Operation": "Starting Gross Domestic Output", "Resulting Metric": "GDP_MP"},
        {"Base Metric": "GDP at Market Price (GDP_MP)", "Conversion Operation": "Deduct Depreciation", "Resulting Metric": "NDP at Market Price (NDP_MP)"},
        {"Base Metric": "NDP at Market Price (NDP_MP)", "Conversion Operation": "Deduct Net Indirect Taxes (Taxes - Subsidies)", "Resulting Metric": "NDP at Factor Cost (NDP_FC)"},
        {"Base Metric": "NDP at Factor Cost (NDP_FC)", "Conversion Operation": "Add Net Factor Income from Abroad (NFIA)", "Resulting Metric": "NNP at Factor Cost (National Income)"},
        {"Base Metric": "GDP at Market Price (GDP_MP)", "Conversion Operation": "Add Net Factor Income from Abroad (NFIA)", "Resulting Metric": "GNP at Market Price (GNP_MP)"}
    ])
    st.dataframe(trans_table, use_container_width=True)

# --- MODULE 3: GDP DEFLATOR ---
elif nav_selection == "📉 GDP Deflator & Inflation Mechanics":
    st.markdown('<div class="section-header">📉 GDP Deflator, Real Output & Price Adjustments</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="concept-note">
    <h3>🔍 The Comprehensive Domestic Price Level Measure</h3>
    <p>The GDP Deflator is an implicit price index that standardizes nominal economic expansion into pure physical output growth by stripping out inflationary distortions.</p>
    <div class="formula-badge" style="font-size: 1.05rem;">GDP Deflator = (Nominal GDP / Real GDP) * 100</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="case-study">
        <h4>⚡ Core Analytical Utilities</h4>
        <ul>
            <li><strong>Purifying Economic Expansion:</strong> Converts aggregate nominal metrics into Real GDP to identify if an economy is physically expanding or simply experiencing price inflation:
                <br><strong style="color: #FCD34D;">Real GDP = (Nominal GDP / GDP Deflator) * 100</strong>
            </li>
            <li><strong>Universal Coverage:</strong> Unlike consumer price indices that monitor only household consumer bundles, the deflator encompasses capital goods, government purchases, and exported items.</li>
            <li><strong>Dynamic Indexing:</strong> Acts as an automatically adjusting Paasche index where component weights shift naturally according to current production realities.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="concept-note" style="border-left-color: #38BDF8;">
        <h4>📊 Structural Comparison: GDP Deflator vs. CPI</h4>
        <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.9rem;">
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.1); color: #FCD34D;">
                <th style="text-align: left; padding: 6px;">Feature</th>
                <th style="text-align: left; padding: 6px;">GDP Deflator</th>
                <th style="text-align: left; padding: 6px;">Consumer Price Index (CPI)</th>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 6px; font-weight: 600;">Coverage</td>
                <td style="padding: 6px;">All domestic final goods</td>
                <td style="padding: 6px;">Fixed consumer basket</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 6px; font-weight: 600;">Imported Goods</td>
                <td style="padding: 6px;">Strictly excluded</td>
                <td style="padding: 6px;">Included (consumer items)</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 6px; font-weight: 600;">Capital Goods</td>
                <td style="padding: 6px;">Included</td>
                <td style="padding: 6px;">Strictly excluded</td>
            </tr>
            <tr>
                <td style="padding: 6px; font-weight: 600;">Weight Structure</td>
                <td style="padding: 6px;">Flexible (Current year)</td>
                <td style="padding: 6px;">Fixed (Base year basket)</td>
            </tr>
        </table>
        </div>
        """, unsafe_allow_html=True)

# --- MODULE 4: BASE YEAR SELECTION ---
elif nav_selection == "📅 Base Year Selection Architecture":
    st.markdown('<div class="section-header">📅 Base Year Selection Architecture & Rebasing Dynamics</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="concept-note">
    <h3>🎯 Criteria for Selecting a National Accounting Base Year</h3>
    <p>A base year provides the benchmark constant price structure used to evaluate Real GDP. Statistical bodies select benchmark years according to rigorous criteria to ensure realistic comparisons.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="case-study">
        <h4>1. Economic Normalcy & Stability</h4>
        <p>The chosen year must represent an uncorrupted macroeconomic equilibrium:</p>
        <ul>
            <li><strong>Absence of Shocks:</strong> Avoids periods influenced by wars, pandemic disruptions, financial panics, or trade embargoes.</li>
            <li><strong>Price Stability:</strong> Years experiencing extreme hyperinflation or sharp deflationary spirals are disqualified.</li>
            <li><strong>Normal Weather & Harvests:</strong> Critical for economies where agricultural yields impact total production volumes.</li>
        </ul>
        <h4>2. Data Depth & Survey Concurrence</h4>
        <p>Requires comprehensive national censuses:</p>
        <ul>
            <li>Aligned with extensive household consumer expenditure surveys and business establishment censuses.</li>
            <li>Provides statistical coverage for informal, unorganized, and service sector firms.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="concept-note" style="border-left-color: #EF4444;">
        <h4 style="color: #F87171;">3. Modernization & The Substitution Bias</h4>
        <p>Why national accounting authorities periodically revise and update the base year every five to ten years:</p>
        <ul>
            <li><strong>Incorporation of New Sectors:</strong> Captures structural shifts such as green energy, cloud infrastructure, and fintech services that did not exist in older base eras.</li>
            <li><strong>Removing Obsolete Output:</strong> Prunes obsolete manufactured items whose transaction volumes have dropped toward zero.</li>
            <li><strong>Preventing the Gerschenkron Effect:</strong> When an old base year is maintained too long, items experiencing rapid technological cost deflation (e.g., computers) look artificially valuable at ancient base prices, creating an upward distortion in calculated Real GDP.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# --- MODULE 5: MACRO SIMULATOR ---
elif nav_selection == "🧮 Macroeconomic Aggregates Simulator":
    st.markdown('<div class="section-header">🧮 Comprehensive National Accounting Engine</div>', unsafe_allow_html=True)
    st.markdown("Adjust national production parameters to observe the instantaneous recalculation of aggregate metrics, market prices, and deflator values.")

    sim_c1, sim_c2 = st.columns([1, 1.25])

    with sim_c1:
        st.markdown("#### Primary Economic Parameters (in Billions)")
        gdp_val = st.slider("Nominal GDP at Market Price:", min_value=500.0, max_value=5000.0, value=2500.0, step=50.0)
        dep_val = st.slider("Capital Depreciation:", min_value=20.0, max_value=600.0, value=280.0, step=10.0)
        
        st.markdown("#### Cross-Border Income Flows")
        fi_in = st.slider("Factor Income Earned by Residents Abroad:", min_value=0.0, max_value=300.0, value=120.0, step=5.0)
        fi_out = st.slider("Factor Income Paid to Non-Residents:", min_value=0.0, max_value=300.0, value=90.0, step=5.0)

        st.markdown("#### Government Fiscal Wedge")
        ind_tax = st.slider("Indirect Taxes (GST, Excise, Customs):", min_value=10.0, max_value=500.0, value=260.0, step=10.0)
        subs = st.slider("Production Subsidies:", min_value=0.0, max_value=200.0, value=80.0, step=5.0)

        st.markdown("#### Price Level Reference")
        real_gdp_val = st.slider("Real GDP (Constant Base-Year Prices):", min_value=400.0, max_value=4000.0, value=2000.0, step=50.0)

        # Derived calculations
        nfia = fi_in - fi_out
        nit = ind_tax - subs
        ndp_mp = gdp_val - dep_val
        gnp_mp = gdp_val + nfia
        nnp_mp = gnp_mp - dep_val
        gdp_fc = gdp_val - nit
        ndp_fc = ndp_mp - nit
        nnp_fc = nnp_mp - nit  # National Income
        deflator = (gdp_val / real_gdp_val) * 100.0
        implicit_inf = deflator - 100.0

    with sim_c2:
        st.markdown("#### 📊 Derived National Accounting Aggregates")

        row1_a, row1_b = st.columns(2)
        with row1_a:
            st.markdown(f"""
            <div class="metric-card">
                <h3>National Income (NNP at Factor Cost)</h3>
                <div class="metric-value">{nnp_fc:,.2f}</div>
                <p style="color: #94A3B8; font-size: 0.85rem;">Net resident earnings from production</p>
            </div>
            """, unsafe_allow_html=True)
        with row1_b:
            st.markdown(f"""
            <div class="metric-card">
                <h3>GDP Deflator (Price Index)</h3>
                <div class="metric-value">{deflator:,.2f}</div>
                <p style="color: #94A3B8; font-size: 0.85rem;">Implicit inflation: {implicit_inf:,.2f}%</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        overview_df = pd.DataFrame([
            {"Aggregate Term": "Gross Domestic Product at Market Price (GDP_MP)", "Formula Applied": "Base Reported Input", "Resulting Magnitude": f"{gdp_val:,.2f}"},
            {"Aggregate Term": "Net Domestic Product at Market Price (NDP_MP)", "Formula Applied": "GDP_MP - Depreciation", "Resulting Magnitude": f"{ndp_mp:,.2f}"},
            {"Aggregate Term": "Gross National Product at Market Price (GNP_MP)", "Formula Applied": "GDP_MP + NFIA", "Resulting Magnitude": f"{gnp_mp:,.2f}"},
            {"Aggregate Term": "Net National Product at Market Price (NNP_MP)", "Formula Applied": "GNP_MP - Depreciation", "Resulting Magnitude": f"{nnp_mp:,.2f}"},
            {"Aggregate Term": "Gross Domestic Product at Factor Cost (GDP_FC)", "Formula Applied": "GDP_MP - Net Indirect Taxes", "Resulting Magnitude": f"{gdp_fc:,.2f}"},
            {"Aggregate Term": "Net Domestic Product at Factor Cost (NDP_FC)", "Formula Applied": "NDP_MP - Net Indirect Taxes", "Resulting Magnitude": f"{ndp_fc:,.2f}"},
            {"Aggregate Term": "Net National Product at Factor Cost (NNP_FC / National Income)", "Formula Applied": "NNP_MP - Net Indirect Taxes", "Resulting Magnitude": f"{nnp_fc:,.2f}"},
            {"Aggregate Term": "Net Factor Income from Abroad (NFIA)", "Formula Applied": "Factor Income In - Factor Income Out", "Resulting Magnitude": f"{nfia:,.2f}"},
            {"Aggregate Term": "Net Indirect Taxes (NIT)", "Formula Applied": "Indirect Taxes - Subsidies", "Resulting Magnitude": f"{nit:,.2f}"}
        ])
        st.dataframe(overview_df, use_container_width=True)

        # Comparative Visualization
        chart_data = pd.DataFrame({
            "Aggregate": ["GDP (MP)", "NDP (MP)", "GNP (MP)", "NNP (MP)", "National Income (NNP_FC)"],
            "Magnitude": [gdp_val, ndp_mp, gnp_mp, nnp_mp, nnp_fc]
        }).set_index("Aggregate")
        st.bar_chart(chart_data)

# --- MODULE 6: KNOWLEDGE DECK ---
elif nav_selection == "📝 Macroeconomic Accounting Knowledge Deck":
    st.markdown('<div class="section-header">📝 National Accounting Mastery Assessment</div>', unsafe_allow_html=True)
    st.markdown("Evaluate your understanding of macroeconomic aggregates, deflator mechanics, and factor cost adjustments.")

    with st.form("macro_quiz"):
        st.markdown("### 1. Conceptual Distinction Between Domestic and National")
        q1 = st.radio(
            "Which factor differentiates Gross Domestic Product (GDP) from Gross National Product (GNP)?",
            options=[
                "A) Deductions made for capital depreciation over the fiscal year.",
                "B) Net Factor Income from Abroad (NFIA).",
                "C) Government subsidies minus indirect sales taxes.",
                "D) Total consumer spending on domestic services."
            ], index=None
        )

        st.markdown("---")
        st.markdown("### 2. Factor Cost vs Market Price Wedge")
        q2 = st.radio(
            "To convert an aggregate from Market Price to Factor Cost, which of the following operations is required?",
            options=[
                "A) Add Depreciation and subtract foreign factor earnings.",
                "B) Add Indirect Taxes and subtract Production Subsidies.",
                "C) Deduct Indirect Taxes and add Production Subsidies (Subtract Net Indirect Taxes).",
                "D) Divide by the GDP Deflator and multiply by 100."
            ], index=None
        )

        st.markdown("---")
        st.markdown("### 3. The Definitional Scope of the GDP Deflator")
        q3 = st.radio(
            "What distinguishes the GDP Deflator from the Consumer Price Index (CPI)?",
            options=[
                "A) The GDP deflator includes imported consumer goods while the CPI excludes them.",
                "B) The GDP deflator tracks all domestically produced final goods and updates weights dynamically, whereas the CPI monitors a fixed consumption basket.",
                "C) The GDP deflator is strictly an unweighted arithmetic mean of commodity prices.",
                "D) The GDP deflator measures only intermediate wholesale materials."
            ], index=None
        )

        st.markdown("---")
        st.markdown("### 4. Base Year Selection Criteria")
        q4 = st.radio(
            "Why do national statistical organizations deliberately avoid selecting a pandemic or economic crisis year as a base year?",
            options=[
                "A) A crisis year carries unusual relative price structures and abnormal production volumes that distort Real GDP growth estimates.",
                "B) Base years can only be chosen in years ending in zero or five under international law.",
                "C) Depreciation rates drop to zero during economic depressions.",
                "D) Factor costs become identical to market prices during economic slowdowns."
            ], index=None
        )

        st.markdown("---")
        st.markdown("### 5. Identification of National Income")
        q5 = st.radio(
            "In macroeconomic national accounting, which metric represents the standard technical definition of National Income?",
            options=[
                "A) Gross Domestic Product at Market Price (GDP_MP).",
                "B) Net Domestic Product at Market Price (NDP_MP).",
                "C) Net National Product at Factor Cost (NNP_FC).",
                "D) Gross National Product at Factor Cost (GNP_FC)."
            ], index=None
        )

        eval_quiz = st.form_submit_button("Submit Accounting Mastery Assessment", type="primary")

        if eval_quiz:
            score_acc = 0.0

            if q1 == "B) Net Factor Income from Abroad (NFIA).":
                score_acc += 20.0; st.session_state.ans1_ok = True
            else: st.session_state.ans1_ok = False

            if q2 == "C) Deduct Indirect Taxes and add Production Subsidies (Subtract Net Indirect Taxes).":
                score_acc += 20.0; st.session_state.ans2_ok = True
            else: st.session_state.ans2_ok = False

            if q3 == "B) The GDP deflator tracks all domestically produced final goods and updates weights dynamically, whereas the CPI monitors a fixed consumption basket.":
                score_acc += 20.0; st.session_state.ans3_ok = True
            else: st.session_state.ans3_ok = False

            if q4 == "A) A crisis year carries unusual relative price structures and abnormal production volumes that distort Real GDP growth estimates.":
                score_acc += 20.0; st.session_state.ans4_ok = True
            else: st.session_state.ans4_ok = False

            if q5 == "C) Net National Product at Factor Cost (NNP_FC).":
                score_acc += 20.0; st.session_state.ans5_ok = True
            else: st.session_state.ans5_ok = False

            st.session_state.knowledge_rating = score_acc
            st.session_state.quiz_done = True
            st.rerun()

    if st.session_state.quiz_done:
        st.markdown("---")
        st.markdown(f"### Assessment Score: {round(st.session_state.knowledge_rating, 1)} / 100 Points")

        if not st.session_state.ans1_ok:
            st.error("Q1 Analysis: Domestic refers to geographical production boundaries, while National reflects resident ownership. The bridge between them is Net Factor Income from Abroad (NFIA).")
        if not st.session_state.ans2_ok:
            st.error("Q2 Analysis: Market Price includes the net fiscal wedge. Transitioning to Factor Cost requires deducting Indirect Taxes and adding Subsidies (deducting NIT).")
        if not st.session_state.ans3_ok:
            st.error("Q3 Analysis: The GDP Deflator encompasses all domestic production (including capital and government goods) with flexible weights, whereas the CPI focuses exclusively on a consumer basket that includes imports.")
        if not st.session_state.ans4_ok:
            st.error("Q4 Analysis: A base year must reflect macroeconomic stability to avoid skewing long-term real growth rates through distorted relative prices.")
        if not st.session_state.ans5_ok:
            st.error("Q5 Analysis: By definition in economic theory, National Income is Net National Product at Factor Cost (NNP_FC).")

# =====================================================================
# SYSTEM FOOTER
# =====================================================================
st.markdown("---")
foot_c1, foot_c2, foot_c3 = st.columns(3)

with foot_c1:
    st.caption("🌐 National Accounting & Aggregates Architecture")

with foot_c2:
    st.caption("📈 GDP Deflator & Price Adjustment Mechanics")

with foot_c3:
    st.caption(f"⏰ Platform Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
