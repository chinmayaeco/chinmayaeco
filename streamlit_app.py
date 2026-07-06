import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Price Elasticity Simulator",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# PASSWORD PROTECTION SYSTEM
# =====================================================================
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        if st.session_state["password"] == "PED2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #10B981;'>🔒 Secure Access</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Please enter the password to access the simulator.</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    
    elif not st.session_state["password_correct"]:
        st.markdown("<h1 style='text-align: center; color: #10B981;'>🔒 Secure Access</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Password", type="password", on_change=password_entered, key="password")
            st.error("😕 Password incorrect. Please try again.")
        return False
    
    return True

if not check_password():
    st.stop()

# =====================================================================
# PREMIUM DESIGN SYSTEM (EMERALD & GOLD THEME)
# =====================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    /* Main background */
    .stApp { background: linear-gradient(135deg, #022C22 0%, #064E3B 50%, #022C22 100%); }
    
    /* Header styling */
    .header-gradient {
        background: linear-gradient(135deg, #047857 0%, #10B981 50%, #F59E0B 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.15);
    }
    .header-gradient h1 { color: white !important; font-size: 2.5rem !important; font-weight: 800 !important; margin: 0 !important; text-shadow: 0 2px 8px rgba(0, 0, 0, 0.2); }
    .header-gradient p { color: rgba(255, 255, 255, 0.95) !important; font-size: 1.1rem !important; margin: 0.5rem 0 0 0 !important; }
    
    /* Score banner */
    .score-banner {
        background: linear-gradient(135deg, #064E3B 0%, #065F46 100%);
        border: 2px solid #10B981;
        color: white; padding: 2rem; border-radius: 12px; text-align: center; margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(16, 185, 129, 0.2);
    }
    .score-banner h2 { color: #34D399 !important; margin: 0 !important; font-weight: 700; font-size: 1.8rem; }
    
    /* Container styling */
    .stContainer, .stForm {
        background: rgba(6, 78, 59, 0.8); border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 12px; padding: 2rem; margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2); backdrop-filter: blur(10px);
    }
    
    /* Section headers */
    .section-header {
        color: #FCD34D; font-weight: 700; font-size: 1.5rem; margin-bottom: 1.5rem;
        padding-bottom: 1rem; border-bottom: 2px solid rgba(252, 211, 77, 0.3);
    }
    
    /* Concept note box */
    .concept-note, .case-study { padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; }
    .concept-note { background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(52, 211, 153, 0.1) 100%); border-left: 4px solid #10B981; }
    .concept-note h3 { color: #34D399; margin-top: 0 !important; }
    .case-study { background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(251, 191, 36, 0.05) 100%); border-left: 4px solid #F59E0B; }
    .case-study h4 { color: #FBBF24; margin-top: 0 !important; }
    
    /* Key metrics */
    .metric-card {
        background: rgba(2, 44, 34, 0.6); border: 1px solid rgba(52, 211, 153, 0.3);
        padding: 1.5rem; border-radius: 8px; text-align: center;
    }
    .metric-card h3 { color: #6EE7B7; font-size: 1.2rem; margin: 0 0 0.5rem 0; }
    .metric-value { color: #FCD34D; font-size: 2rem; font-weight: 700; margin: 0.5rem 0; }
    
    /* Buttons */
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #059669 0%, #10B981 100%) !important; color: white !important;
        border: none !important; padding: 0.75rem 2rem !important; border-radius: 8px !important;
        font-weight: 600 !important; transition: all 0.3s ease !important; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3) !important;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover { box-shadow: 0 8px 24px rgba(16, 185, 129, 0.5) !important; transform: translateY(-2px) !important; }
    
    /* Tabs & Text */
    .stTabs [data-baseweb="tab-list"] { background: rgba(6, 78, 59, 0.5); border-bottom: 2px solid rgba(16, 185, 129, 0.2); }
    .stTabs [aria-selected="true"] { border-bottom: 3px solid #10B981 !important; }
    .stMarkdown, p, li { color: rgba(255, 255, 255, 0.9) !important; }
    .stRadio p, .stRadio label, div[role="radiogroup"] p { color: rgba(255, 255, 255, 0.95) !important; font-size: 1.05rem; }
    .stSidebar { background: linear-gradient(180deg, #022C22 0%, #064E3B 100%); }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SESSION STATE INITIALIZATION
# =====================================================================
def initialize_session_state():
    defaults = {
        'game_played': False,
        'sim_score': 0.0,
        'quiz_score': 0.0,
        'sim_history': [],
        'current_round': 0,
        'q1_answered': False, 'q1_correct': False,
        'q2_answered': False, 'q2_correct': False,
        'q3_answered': False, 'q3_correct': False,
        'q4_answered': False, 'q4_correct': False,
        'quiz_submitted': False,
        'best_revenue': 0
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()

# =====================================================================
# SIDEBAR: LEARNING PATH & NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("### 📚 PED Learning Path")
    learning_path = st.radio(
        "Select your focus:",
        options=[
            "🎮 Pricing Simulator",
            "📖 Conceptual Deep Dive",
            "📈 Real-World Indian Cases",
            "📝 Knowledge Check",
            "💼 Executive Summary"
        ]
    )

# =====================================================================
# HEADER SECTION
# =====================================================================
st.markdown("""
<div class="header-gradient">
    <h1>📈 Price Elasticity of Demand (PED)</h1>
    <p>Master the art of pricing. Discover how consumer sensitivity dictates whether a price hike will multiply your profits or destroy your revenue.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# PERFORMANCE DASHBOARD
# =====================================================================
dashboard_col = st.container()
with dashboard_col:
    total_score = min(100, round(st.session_state.sim_score + st.session_state.quiz_score))
    st.markdown(f"""
    <div class="score-banner">
        <h2>Overall Elasticity Mastery: {total_score} / 100</h2>
        <p style='color: #FCD34D;'>🎮 Simulation Score: {round(st.session_state.sim_score)}/50 | 📝 Quiz Score: {round(st.session_state.quiz_score)}/50</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# MAIN CONTENT ROUTING
# =====================================================================

if learning_path == "🎮 Pricing Simulator":
    game_section = st.container()
    with game_section:
        st.markdown('<div class="section-header">🎮 The Total Revenue Test Simulator</div>', unsafe_allow_html=True)
        
        col_concept, col_game = st.columns([1, 1.2])
        
        with col_concept:
            st.markdown("""
            <div class="concept-note">
            <h3>📌 Mission: Maximize Revenue</h3>
            <p><strong>Your Role:</strong> Chief Pricing Officer. You are testing prices for two different products.</p>
            <p><strong>The Challenge:</strong> Determine how consumer demand reacts to price changes based on the product's elasticity. Your goal is to maximize Total Revenue ($TR = P \\times Q$).</p>
            <ul>
                <li><strong>Elastic Product:</strong> Consumers are highly sensitive to price.</li>
                <li><strong>Inelastic Product:</strong> Consumers will buy it regardless of price changes.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col_game:
            st.markdown("""
            <div class="case-study">
            <h4>🎯 Pricing Dashboard</h4>
            <p>Select a product and adjust its price from the baseline of $100.</p>
            </div>
            """, unsafe_allow_html=True)
            
            product_type = st.radio(
                "Select Product Market:",
                ["Essential Insulin Medication (Inelastic)", "Luxury Smartwatch (Elastic)"]
            )
            
            # Setup base metrics
            base_price = 100
            base_quantity = 5000
            base_revenue = base_price * base_quantity
            
            # Determine elasticity coefficient based on selection
            if "Inelastic" in product_type:
                ed = -0.3  # Inelastic (magnitude < 1)
                st.info("💡 Hint: This product has an Elasticity (Ed) of -0.3.")
            else:
                ed = -2.5  # Elastic (magnitude > 1)
                st.info("💡 Hint: This product has an Elasticity (Ed) of -2.5.")
                
            new_price = st.slider("🏷️ Set New Price ($)", min_value=50, max_value=150, value=100, step=5)
            
            submit_sim = st.button("▶️ Calculate Revenue Impact", type="primary", use_container_width=True)
            
            if submit_sim:
                # Calculate % change in price
                pct_change_price = (new_price - base_price) / base_price
                
                # Calculate % change in quantity using elasticity formula: %ΔQ = Ed * %ΔP
                pct_change_quantity = ed * pct_change_price
                
                # Calculate new quantity and revenue
                new_quantity = max(0, int(base_quantity * (1 + pct_change_quantity)))
                new_revenue = new_price * new_quantity
                
                # Determine success state for scoring
                revenue_diff = new_revenue - base_revenue
                if revenue_diff > 0:
                    status = "Revenue Increased! 📈"
                    score_add = min(25, (revenue_diff / base_revenue) * 100) # Max 25 points per good move
                elif revenue_diff < 0:
                    status = "Revenue Decreased! 📉"
                    score_add = 0
                else:
                    status = "Revenue Unchanged ➖"
                    score_add = 5
                
                st.session_state.current_round += 1
                st.session_state.sim_score = min(50, st.session_state.sim_score + score_add)
                
                st.session_state.sim_history.append({
                    'round': st.session_state.current_round,
                    'product': "Inelastic" if "Inelastic" in product_type else "Elastic",
                    'price': new_price,
                    'quantity': new_quantity,
                    'revenue': new_revenue,
                    'status': status
                })
                
                st.session_state.game_played = True
                st.rerun()

    if st.session_state.game_played:
        results_section = st.container()
        with results_section:
            st.markdown('<div class="section-header">📊 Revenue Results</div>', unsafe_allow_html=True)
            
            latest_result = st.session_state.sim_history[-1]
            metric_cols = st.columns(3)
            
            with metric_cols[0]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>New Price ($P$)</h3>
                    <div class="metric-value">${latest_result['price']}</div>
                    <p style="color: #6EE7B7; font-size: 0.9rem;">Base was $100</p>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_cols[1]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Quantity Demanded ($Q_d$)</h3>
                    <div class="metric-value">{latest_result['quantity']:,}</div>
                    <p style="color: #6EE7B7; font-size: 0.9rem;">Base was 5,000</p>
                </div>
                """, unsafe_allow_html=True)
                
            with metric_cols[2]:
                status_color = "#10B981" if "Increased" in latest_result['status'] else "#EF4444"
                if "Unchanged" in latest_result['status']: status_color = "#FCD34D"
                
                st.markdown(f"""
                <div class="metric-card" style="border-color: {status_color};">
                    <h3 style="color: {status_color};">Total Revenue ($TR$)</h3>
                    <div class="metric-value" style="font-size: 1.8rem; color: {status_color};">${latest_result['revenue']:,}</div>
                    <p style="color: {status_color}; font-weight: bold;">{latest_result['status']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            viz_col1, viz_col2 = st.columns(2)
            
            with viz_col1:
                st.markdown("### 📉 Revenue History")
                history_df = pd.DataFrame(st.session_state.sim_history)
                # Plot revenue over rounds
                st.line_chart(history_df.set_index('round')['revenue'], color="#FCD34D")
            
            with viz_col2:
                st.markdown("""
                <div class="case-study">
                <h4>🔍 The Total Revenue Test</h4>
                <p>Did you notice the pattern?</p>
                <ul>
                    <li><strong>Inelastic Products:</strong> When you RAISE the price, total revenue GOES UP. Because the drop in quantity is very small compared to the higher profit margin.</li>
                    <li><strong>Elastic Products:</strong> When you RAISE the price, total revenue PLUMMETS. Consumers flee to substitutes, wiping out your sales volume. To maximize revenue here, you must LOWER the price to capture massive volume.</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)

elif learning_path == "📖 Conceptual Deep Dive":
    st.markdown('<div class="section-header">📚 Understanding Price Elasticity</div>', unsafe_allow_html=True)
    concept_tabs = st.tabs(["What is PED?", "The Formula", "Determinants of Elasticity", "The Total Revenue Test"])
    
    with concept_tabs[0]:
        st.markdown("""
        <div class="concept-note">
        <h3>📏 Elastic vs. Inelastic</h3>
        <p><strong>Price Elasticity of Demand (PED)</strong> measures exactly how sensitive consumers are to a change in price.</p>
        <p><strong>Elastic Demand ($|E_d| > 1$):</strong> Highly sensitive. A 10% price increase might result in a 30% drop in sales. (Think: Brand-name clothing, fast food).</p>
        <p><strong>Inelastic Demand ($|E_d| < 1$):</strong> Barely sensitive. A 10% price increase might only drop sales by 2%. (Think: Insulin, Petrol, Electricity).</p>
        <p><strong>Unitary Elasticity ($|E_d| = 1$):</strong> Perfectly proportional. A 10% price increase leads to exactly a 10% drop in sales.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with concept_tabs[1]:
        st.markdown("""
        <div class="concept-note">
        <h3>🧮 Calculating Elasticity</h3>
        <p>Economists use the midpoint formula to calculate Price Elasticity of Demand ($E_d$). Because price and demand move in opposite directions, the result is always negative, but we usually look at its <strong>absolute value</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"E_d = \left| \frac{\% \Delta \text{Quantity Demanded}}{\% \Delta \text{Price}} \right|")
        
        st.markdown("""
        <p style="margin-top: 1rem;"><strong>Example:</strong> If Netflix raises its subscription price by 20%, and 40% of users cancel their subscriptions:</p>
        """, unsafe_allow_html=True)
        
        st.latex(r"E_d = \left| \frac{-40\%}{+20\%} \right| = |-2.0| = 2.0 \text{ (Highly Elastic)}")

    with concept_tabs[2]:
        st.markdown("""
        <div class="concept-note">
        <h3>🧩 What makes a product Elastic or Inelastic?</h3>
        <ul>
            <li><strong>Availability of Substitutes:</strong> The more substitutes, the more elastic. (If Coke raises prices, you buy Pepsi. Coke is highly elastic).</li>
            <li><strong>Necessity vs. Luxury:</strong> Necessities (water, medicine) are inelastic. Luxuries (yachts, designer bags) are highly elastic.</li>
            <li><strong>Proportion of Income:</strong> A 20% price hike on matchboxes (cheap) won't alter demand. A 20% hike on a car (expensive) drastically alters demand.</li>
            <li><strong>Time Horizon:</strong> In the short term, petrol is inelastic (you need to drive to work today). Over 5 years, it becomes more elastic (people buy EVs, move closer to work).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with concept_tabs[3]:
        st.markdown("""
        <div class="concept-note">
        <h3>💰 The Total Revenue Test</h3>
        <p>This is the most critical application of PED for businesses. Total Revenue is Price $\\times$ Quantity.</p>
        <table style="width: 100%; border-collapse: collapse; color: white;">
            <tr style="border-bottom: 1px solid white;">
                <th style="padding: 10px; text-align: left;">If Demand Is...</th>
                <th style="padding: 10px; text-align: left;">And Price Changes...</th>
                <th style="padding: 10px; text-align: left;">Total Revenue Will...</th>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.2);">
                <td style="padding: 10px;"><strong>Inelastic</strong> (e.g., Salt)</td>
                <td style="padding: 10px;">Increases ⬆️</td>
                <td style="padding: 10px; color: #10B981;">Increase ⬆️</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.2);">
                <td style="padding: 10px;"><strong>Elastic</strong> (e.g., TVs)</td>
                <td style="padding: 10px;">Increases ⬆️</td>
                <td style="padding: 10px; color: #EF4444;">Decrease ⬇️</td>
            </tr>
            <tr>
                <td style="padding: 10px;"><strong>Elastic</strong> (e.g., TVs)</td>
                <td style="padding: 10px;">Decreases ⬇️</td>
                <td style="padding: 10px; color: #10B981;">Increase ⬆️ (via mass volume)</td>
            </tr>
        </table>
        </div>
        """, unsafe_allow_html=True)

elif learning_path == "📈 Real-World Indian Cases":
    st.markdown('<div class="section-header">📈 Indian Corporate Case Studies</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="case-study">
    <h4>📱 Reliance Jio (Leveraging Highly Elastic Demand)</h4>
    <p><strong>The Scenario:</strong> Before 2016, 1GB of mobile data in India cost around ₹250. Internet usage was considered a premium, discretionary spend.</p>
    <p><strong>The Elasticity Reality:</strong> Jio realized that data demand in India was <em>highly elastic</em>. By dropping the price to near zero initially (and later at highly subsidized rates), the quantity demanded didn't just double—it exploded exponentially. Because the demand was elastic, drastically lowering the price expanded the total size of the market, allowing Jio to capture hundreds of millions of users and ultimately drive massive long-term revenue.</p>
    </div>
    
    <div class="case-study">
    <h4>🧂 Tata Salt (Pricing Power via Inelastic Demand)</h4>
    <p><strong>The Scenario:</strong> Salt is a daily necessity in Indian cooking, has no real substitutes, and makes up a tiny fraction of a household's grocery budget.</p>
    <p><strong>The Elasticity Reality:</strong> If Tata Consumer Products raises the price of a 1kg packet of Tata Salt from ₹25 to ₹28 (a 12% increase), demand barely flinches. Consumers will not stop using salt, nor will they spend hours hunting for a ₹2 cheaper substitute. Because $E_d < 1$, raising the price directly increases Tata's total revenue without sacrificing market share.</p>
    </div>
    
    <div class="case-study">
    <h4>🍿 PVR INOX Cinemas (The Danger of Treating Elastic Goods as Inelastic)</h4>
    <p><strong>The Scenario:</strong> Multiplexes offer entertainment, which is a discretionary (non-essential) spend.</p>
    <p><strong>The Elasticity Reality:</strong> Post-pandemic, as multiplexes continually increased ticket and F&B prices, they noticed a severe drop in footfalls. Management treated the product like it was inelastic, but consumers had a cheaper, highly accessible substitute: OTT platforms (Netflix, Prime). Because entertainment is highly elastic, PVR INOX's price hikes led to a disproportionate drop in quantity demanded, hurting total revenue. They recently had to introduce "₹99 Ticket Days" to recover volume.</p>
    </div>
    """, unsafe_allow_html=True)

elif learning_path == "📝 Knowledge Check":
    st.markdown('<div class="section-header">📝 PED Knowledge Check</div>', unsafe_allow_html=True)
    st.markdown("Test your understanding of Price Elasticity. Each correct answer adds **12.5 points** to your total score.")
    
    with st.form("quiz_form"):
        st.markdown("### 1. The Elasticity Formula")
        q1 = st.radio(
            "If a 10% increase in the price of a product causes a 25% decrease in the quantity demanded, what is the product's price elasticity (absolute value), and is it elastic or inelastic?",
            options=[
                "A) 2.5; Elastic",
                "B) 0.4; Inelastic",
                "C) 2.5; Inelastic",
                "D) 0.4; Elastic"
            ],
            index=None
        )
        
        st.markdown("---")
        st.markdown("### 2. The Total Revenue Test")
        q2 = st.radio(
            "You are the manager of a pharmaceutical company selling a patented, life-saving heart medication (Highly Inelastic). To MAXIMIZE total revenue, you should:",
            options=[
                "A) Lower the price to sell more units.",
                "B) Raise the price, because volume won't drop significantly.",
                "C) Keep the price exactly the same.",
                "D) Price elasticity doesn't affect total revenue."
            ],
            index=None
        )
        
        st.markdown("---")
        st.markdown("### 3. Determinants of Elasticity")
        q3 = st.radio(
            "Which of the following would make the demand for a specific good MORE elastic?",
            options=[
                "A) The good is a strict necessity for survival.",
                "B) The good takes up a very small percentage of a consumer's income (like matches).",
                "C) Several new competitors enter the market with nearly identical products.",
                "D) Consumers have less time to adjust to the price change."
            ],
            index=None
        )
        
        st.markdown("---")
        st.markdown("### 4. Real-World Application")
        q4 = st.radio(
            "An airline notices that business travelers will pay almost any price for a last-minute ticket, while vacationers will cancel their trip if the price rises by $50. How should the airline view these two groups?",
            options=[
                "A) Business travelers are elastic; Vacationers are inelastic.",
                "B) Both groups are unitary elastic.",
                "C) Business travelers are inelastic; Vacationers are elastic.",
                "D) Both groups are inelastic."
            ],
            index=None
        )
        
        submit_quiz = st.form_submit_button("Submit Answers", type="primary")
        
        if submit_quiz:
            score = 0.0
            
            if q1 == "A) 2.5; Elastic":
                score += 12.5; st.session_state.q1_correct = True
            else: st.session_state.q1_correct = False
                
            if q2 == "B) Raise the price, because volume won't drop significantly.":
                score += 12.5; st.session_state.q2_correct = True
            else: st.session_state.q2_correct = False
                
            if q3 == "C) Several new competitors enter the market with nearly identical products.":
                score += 12.5; st.session_state.q3_correct = True
            else: st.session_state.q3_correct = False
                
            if q4 == "C) Business travelers are inelastic; Vacationers are elastic.":
                score += 12.5; st.session_state.q4_correct = True
            else: st.session_state.q4_correct = False
                
            st.session_state.quiz_score = score
            st.session_state.quiz_submitted = True
            st.rerun()

    if st.session_state.quiz_submitted:
        st.markdown("---")
        st.markdown(f"### 🎉 Quiz Results: {st.session_state.quiz_score}/50 points")
        
        if not st.session_state.q1_correct:
            st.error("**Q1 Incorrect:** Formula is %ΔQ / %ΔP. 25 / 10 = 2.5. Since 2.5 > 1, it is Elastic.")
        if not st.session_state.q2_correct:
            st.error("**Q2 Incorrect:** For inelastic goods, price and total revenue move in the same direction. Raise price = raise revenue.")
        if not st.session_state.q3_correct:
            st.error("**Q3 Incorrect:** More competitors means more *substitutes*. The availability of substitutes makes consumers highly sensitive to price changes (more elastic).")
        if not st.session_state.q4_correct:
            st.error("**Q4 Incorrect:** Business travelers must fly (necessity = inelastic). Vacationers are price sensitive (luxury/optional = elastic).")
            
        if st.session_state.quiz_score == 50:
            st.success("Perfect score! You are a master of pricing elasticity.")

elif learning_path == "💼 Executive Summary":
    st.markdown('<div class="section-header">💼 Executive Summary: Strategic Pricing</div>', unsafe_allow_html=True)
    exec_col1, exec_col2 = st.columns(2)
    with exec_col1:
        st.markdown("""
        <div class="case-study">
        <h4>🎯 The Golden Rule of Pricing</h4>
        <p>Never change a price without first estimating your Price Elasticity of Demand.</p>
        <p><strong>If you are Inelastic ($E_d < 1$):</strong> You are leaving money on the table. You can likely execute a price hike. Volume will drop slightly, but profit margins and total revenue will expand.</p>
        <p><strong>If you are Elastic ($E_d > 1$):</strong> Be careful with price hikes; they will destroy your volume and revenue. Consider selective discounting, sales, or bundling to drive massive volume instead.</p>
        </div>
        """, unsafe_allow_html=True)
    with exec_col2:
        st.markdown("""
        <div class="concept-note">
        <h4>🛡️ How to Make Your Product INELASTIC</h4>
        <p>The holy grail of business is shifting your product from Elastic to Inelastic, giving you monopolistic pricing power. How? </p>
        <ul>
            <li><strong>Brand Loyalty:</strong> Apple users won't switch to Android over a $100 price hike. (Brand = Inelasticity).</li>
            <li><strong>High Switching Costs:</strong> Make it painful for B2B clients to rip out your software.</li>
            <li><strong>Proprietary Ecosystems:</strong> Create lock-in (e.g., Nespresso pods only fit Nespresso machines).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.caption("🎓 Built for Economic Literacy | Powered by Streamlit")

with footer_col2:
    total_score = min(100, round(st.session_state.sim_score + st.session_state.quiz_score))
    st.caption(f"📈 Total Elasticity Score: {total_score}/100")

with footer_col3:
    st.caption(f"⏰ Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
