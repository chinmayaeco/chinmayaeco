import streamlit as st
import random
import pandas as pd
import numpy as np
from datetime import datetime
import json

# =====================================================================
# PAGE CONFIGURATION & THEME
# =====================================================================
st.set_page_config(
    page_title="Behavioral Economics Simulator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# PREMIUM DESIGN SYSTEM
# =====================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F172A 100%);
    }
    
    /* Header styling */
    .header-gradient {
        background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 50%, #EC4899 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(99, 102, 241, 0.15);
    }
    
    .header-gradient h1 {
        color: white !important;
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .header-gradient p {
        color: rgba(255, 255, 255, 0.95) !important;
        font-size: 1.1rem !important;
        margin: 0.5rem 0 0 0 !important;
    }
    
    /* Score banner */
    .score-banner {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 2px solid #4F46E5;
        color: white;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(79, 70, 229, 0.2);
    }
    
    .score-banner h2 {
        color: #60A5FA !important;
        margin: 0 !important;
        font-weight: 700;
        font-size: 1.8rem;
    }
    
    .score-banner p {
        color: rgba(255, 255, 255, 0.8);
        margin: 0.5rem 0 0 0 !important;
        font-size: 1rem;
    }
    
    /* Container styling */
    .stContainer {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }
    
    /* Section headers */
    .section-header {
        color: #60A5FA;
        font-weight: 700;
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid rgba(96, 165, 250, 0.3);
    }
    
    /* Concept note box */
    .concept-note {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
        border-left: 4px solid #3B82F6;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .concept-note h3 {
        color: #3B82F6;
        margin-top: 0 !important;
    }
    
    .concept-note p {
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.6;
    }
    
    /* Case study */
    .case-study {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(34, 197, 94, 0.05) 100%);
        border-left: 4px solid #22C55E;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .case-study h4 {
        color: #22C55E;
        margin-top: 0 !important;
    }
    
    .case-study p {
        color: rgba(255, 255, 255, 0.85);
        line-height: 1.6;
    }
    
    .case-study strong {
        color: #86EFAC;
    }
    
    /* Managerial lesson */
    .managerial-lesson {
        background: linear-gradient(135deg, rgba(249, 115, 22, 0.1) 0%, rgba(249, 115, 22, 0.05) 100%);
        border-left: 4px solid #F97316;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .managerial-lesson h4 {
        color: #FB923C;
        margin-top: 0 !important;
    }
    
    .managerial-lesson p {
        color: rgba(255, 255, 255, 0.85);
        line-height: 1.6;
    }
    
    /* Real-world application */
    .real-world-app {
        background: linear-gradient(135deg, rgba(236, 72, 153, 0.1) 0%, rgba(236, 72, 153, 0.05) 100%);
        border-left: 4px solid #EC4899;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .real-world-app h4 {
        color: #EC4899;
        margin-top: 0 !important;
    }
    
    .real-world-app p {
        color: rgba(255, 255, 255, 0.85);
        line-height: 1.6;
    }
    
    /* Key metrics */
    .metric-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(96, 165, 250, 0.3);
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
    }
    
    .metric-card h3 {
        color: #60A5FA;
        font-size: 1.2rem;
        margin: 0 0 0.5rem 0;
    }
    
    .metric-value {
        color: #10B981;
        font-size: 2rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3) !important;
    }
    
    .stButton > button:hover {
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.5) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(30, 41, 59, 0.5);
        border-bottom: 2px solid rgba(96, 165, 250, 0.2);
    }
    
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #6366F1 !important;
    }
    
    /* Text colors */
    .stMarkdown {
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Sidebar */
    .stSidebar {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
    }
    
    /* Info boxes */
    .stInfo {
        background: rgba(59, 130, 246, 0.1) !important;
        border-left: 4px solid #3B82F6 !important;
    }
    
    .stSuccess {
        background: rgba(34, 197, 94, 0.1) !important;
        border-left: 4px solid #22C55E !important;
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.1) !important;
        border-left: 4px solid #EF4444 !important;
    }
    
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SESSION STATE INITIALIZATION
# =====================================================================
def initialize_session_state():
    """Initialize all session state variables"""
    defaults = {
        'game_played': False,
        'game_score': 0.0,
        'mcq_score': 0.0,
        'mcq1_answered': False,
        'mcq1_correct': False,
        'mcq2_answered': False,
        'mcq2_correct': False,
        'mcq3_answered': False,
        'mcq3_correct': False,
        'final_tokens': 0.0,
        'contributions': [],
        'game_history': [],
        'current_round': 0,
        'show_concept_details': False,
        'show_implementation_guide': False
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()

# =====================================================================
# SIDEBAR: LEARNING PATH & NAVIGATION
# =====================================================================
with st.sidebar:
    st.markdown("### 📚 Learning Path")
    learning_path = st.radio(
        "Select your focus:",
        options=[
            "🎮 Play & Learn",
            "📖 Conceptual Deep Dive",
            "💼 Executive Summary",
            "🛠️ Implementation Guide"
        ]
    )

# =====================================================================
# HEADER SECTION
# =====================================================================
st.markdown("""
<div class="header-gradient">
    <h1>🧠 Behavioral Economics Simulator</h1>
    <p>Master strategic decision-making through interactive games, real-world case studies, and actionable frameworks for organizational leadership.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# PERFORMANCE DASHBOARD
# =====================================================================
dashboard_col = st.container()
with dashboard_col:
    total_score = min(100, round(st.session_state.game_score + st.session_state.mcq_score))
    
    st.markdown(f"""
    <div class="score-banner">
        <h2>Your Performance Score: {total_score} / 100</h2>
        <p>🎮 Game Score: {round(st.session_state.game_score)}/50 | 📝 Quiz Score: {round(st.session_state.mcq_score)}/75</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# MAIN CONTENT ROUTING
# =====================================================================

if learning_path == "🎮 Play & Learn":
    # =========================================================
    # SECTION 1: PUBLIC GOODS GAME
    # =========================================================
    game_section = st.container()
    with game_section:
        st.markdown('<div class="section-header">🎮 Phase 1: The Public Goods Game</div>', unsafe_allow_html=True)
        
        col_concept, col_game = st.columns([1, 1.2])
        
        with col_concept:
            st.markdown("""
            <div class="concept-note">
            <h3>📌 Core Concept</h3>
            <p><strong>The Social Dilemma:</strong> Individual rationality leads to collective irrationality. When personal benefit conflicts with group benefit, most people choose personal gain—even though cooperation would benefit everyone.</p>
            <p><strong>Key Variables:</strong></p>
            <ul>
                <li><strong>N=4 players</strong> (you + 3 others)</li>
                <li><strong>Endowment:</strong> 100 tokens each</li>
                <li><strong>Multiplier:</strong> 2x on pooled contributions</li>
                <li><strong>Distribution:</strong> Equal split among all 4</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="managerial-lesson">
            <h4>💼 Why This Matters</h4>
            <p>This game mirrors real organizational challenges:</p>
            <ul>
                <li>R&D budget allocation (share findings or hide for competitive advantage)</li>
                <li>Knowledge management (contribute to wikis or hoard expertise)</li>
                <li>Team projects (invest effort or let others carry the load)</li>
                <li>Infrastructure investments (fund shared systems or keep separate resources)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col_game:
            st.markdown("""
            <div class="concept-note">
            <h3>🎯 The Game Mechanics</h3>
            <p><strong>Example Scenario:</strong></p>
            <p style="background: rgba(0,0,0,0.2); padding: 1rem; border-radius: 6px; font-family: monospace;">
            You contribute: 50 tokens<br>
            Others contribute: 40, 60, 55 (avg: 51.7)<br>
            <br>
            Total pool: 205 tokens<br>
            Multiplied: 205 × 2 = 410<br>
            Per player: 410 ÷ 4 = 102.5<br>
            <br>
            Your outcome:<br>
            • Kept: 50 tokens<br>
            • Received: 102.5 tokens<br>
            • Total: 152.5 ✓
            </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Game input
        st.markdown("---")
        col_slider, col_info = st.columns([2, 1])
        
        with col_slider:
            user_contribution = st.slider(
                "💰 How much will you contribute to the shared project?",
                min_value=0, max_value=100, value=50, step=5,
                help="0 = All for yourself (free-rider) | 100 = All for group (cooperator)"
            )
            
            st.caption(f"📊 You'll keep: {100 - user_contribution} | Pool receives: {user_contribution}")
        
        with col_info:
            st.info(f"""
            **Token Balance**
            - Starting: 100
            - Contributing: {user_contribution}
            - Keeping: {100 - user_contribution}
            """)
        
        # Submit button with explanation
        col_btn1, col_btn2 = st.columns([1, 2])
        with col_btn1:
            submit_game = st.button("▶️ Submit Decision", type="primary", use_container_width=True)
        
        if submit_game:
            # Simulate three other players with varied cooperation levels
            p2 = random.randint(20, 80)
            p3 = random.randint(20, 80)
            p4 = random.randint(20, 80)
            
            total_pool = user_contribution + p2 + p3 + p4
            multiplied_pool = total_pool * 2
            payout = multiplied_pool / 4
            
            st.session_state.final_tokens = (100 - user_contribution) + payout
            st.session_state.contributions = [user_contribution, p2, p3, p4]
            st.session_state.current_round += 1
            
            # Store game history
            st.session_state.game_history.append({
                'round': st.session_state.current_round,
                'contribution': user_contribution,
                'final_tokens': st.session_state.final_tokens,
                'others_avg': (p2 + p3 + p4) / 3
            })
            
            # Calculate game score
            st.session_state.game_score = min(50.0, (st.session_state.final_tokens / 200.0) * 50.0)
            st.session_state.game_played = True
            
            try:
                st.rerun()
            except AttributeError:
                st.experimental_rerun()
    
    # =========================================================
    # SECTION 2: GAME RESULTS & ANALYSIS
    # =========================================================
    if st.session_state.game_played:
        results_section = st.container()
        with results_section:
            st.markdown('<div class="section-header">📊 Round Results & Analysis</div>', unsafe_allow_html=True)
            
            # High-level metrics
            metric_cols = st.columns(4)
            
            with metric_cols[0]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Your Tokens</h3>
                    <div class="metric-value">{st.session_state.final_tokens:.1f}</div>
                    <p style="color: #60A5FA; font-size: 0.9rem;">+{st.session_state.final_tokens - 100:.1f} vs start</p>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_cols[1]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Total Pool</h3>
                    <div class="metric-value">{sum(st.session_state.contributions) * 2:.0f}</div>
                    <p style="color: #60A5FA; font-size: 0.9rem;">After 2x multiplier</p>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_cols[2]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Your Share</h3>
                    <div class="metric-value">{(sum(st.session_state.contributions) * 2) / 4:.1f}</div>
                    <p style="color: #60A5FA; font-size: 0.9rem;">1/4 of pool</p>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_cols[3]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Others' Avg</h3>
                    <div class="metric-value">{(st.session_state.contributions[1] + st.session_state.contributions[2] + st.session_state.contributions[3]) / 3:.1f}</div>
                    <p style="color: #60A5FA; font-size: 0.9rem;">Their contribution</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Visualizations
            st.markdown("---")
            viz_col1, viz_col2 = st.columns(2)
            
            with viz_col1:
                st.markdown("### 📈 Contribution Breakdown")
                chart_df = pd.DataFrame({
                    "Team Members": ["You", "Manager B", "Manager C", "Manager D"],
                    "Contributed": st.session_state.contributions,
                    "Kept": [100 - x for x in st.session_state.contributions]
                })
                st.bar_chart(
                    chart_df.set_index("Team Members"),
                    y=["Contributed", "Kept"],
                    color=["#6366F1", "#94A3B8"]
                )
            
            with viz_col2:
                if len(st.session_state.game_history) > 0:
                    st.markdown("### 📉 Strategy Evolution Over Rounds")
                    history_df = pd.DataFrame(st.session_state.game_history)
                    st.line_chart(
                        history_df.set_index('round'),
                        y=['contribution', 'others_avg'],
                        color=['#6366F1', '#EF4444']
                    )
                else:
                    st.info("Play multiple rounds to see strategy evolution")
            
            # Detailed analysis
            st.markdown("---")
            your_contribution = st.session_state.contributions[0]
            others_avg = np.mean(st.session_state.contributions[1:])
            contribution_diff = your_contribution - others_avg
            
            analysis_col1, analysis_col2 = st.columns([1, 1])
            
            with analysis_col1:
                if contribution_diff > 5:
                    analysis_emoji = "🟢"
                    analysis_type = "Cooperator"
                    analysis_text = "You contributed MORE than others. You demonstrate trust and cooperation instincts."
                elif contribution_diff < -5:
                    analysis_emoji = "🔴"
                    analysis_type = "Free-Rider"
                    analysis_text = "You contributed LESS than others. You optimized for personal gain over group benefit."
                else:
                    analysis_emoji = "🟡"
                    analysis_type = "Reciprocator"
                    analysis_text = "You matched the group average. Your behavior reflects the social norm."
                
                st.markdown(f"""
                <div class="real-world-app">
                <h4>{analysis_emoji} Your Behavioral Type: {analysis_type}</h4>
                <p>{analysis_text}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with analysis_col2:
                st.markdown(f"""
                <div class="managerial-lesson">
                <h4>💡 Key Insight</h4>
                <p><strong>Payoff Breakdown:</strong></p>
                <ul>
                    <li>Tokens kept: {100 - your_contribution}</li>
                    <li>Share from pool: {st.session_state.final_tokens - (100 - your_contribution):.1f}</li>
                    <li><strong>Total: {st.session_state.final_tokens:.1f}</strong></li>
                </ul>
                <p style="margin-top: 1rem; font-size: 0.9rem; color: rgba(255,255,255,0.7);">
                Optimal outcome occurs when <strong>all players cooperate fully</strong> = 200 tokens each (vs your {st.session_state.final_tokens:.1f})
                </p>
                </div>
                """, unsafe_allow_html=True)

elif learning_path == "📖 Conceptual Deep Dive":
    st.markdown('<div class="section-header">📚 Behavioral Economics Concepts</div>', unsafe_allow_html=True)
    
    concept_tabs = st.tabs(["Free-Rider Dilemma", "Loss Aversion", "Trust & Cooperation", "Cognitive Biases"])
    
    with concept_tabs[0]:
        st.markdown("""
        <div class="concept-note">
        <h3>🤝 The Free-Rider Problem: A Deep Dive</h3>
        <p><strong>Definition:</strong> A free-rider is someone who benefits from a shared resource or public good without contributing proportionally to its creation or maintenance.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Root Causes:**
        1. **Individual Rationality vs. Collective Irrationality** — Each person reasons: "My small contribution won't matter, but I'll enjoy the benefits"
        2. **Information Asymmetry** — Others may not know my true contribution level
        3. **Diffusion of Responsibility** — "Someone else will handle it"
        4. **Low Cost of Defection** — Punishing free-riders is often expensive
        """)
        
        st.markdown("""
        <div class="case-study">
        <h4>📱 Case Study 1: Wikipedia & Volunteer Knowledge Commons</h4>
        <p><strong>The Problem:</strong> 99% of Wikipedia users never edit. These "free-riders" enjoy thousands of articles without contributing a single sentence.</p>
        <p><strong>Why It Still Works:</strong></p>
        <ul>
            <li><strong>Low barrier to contribution</strong> — Anyone can edit; no special permission needed</li>
            <li><strong>Intrinsic motivation matters</strong> — 1% of highly motivated users generate value for 99%</li>
            <li><strong>Social recognition</strong> — Edit history is public; contributors gain reputation</li>
            <li><strong>Community norms</strong> — Strong enforcement of quality standards</li>
        </ul>
        <p><strong>Lesson:</strong> Systems designed around low contribution friction and visible attribution can thrive even with high free-rider ratios.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="managerial-lesson">
        <h4>💼 Application Framework: VIPR Model</h4>
        <p>To combat free-riding in organizations:</p>
        <ul>
            <li><strong>V</strong> — Make contributions <strong>Visible</strong> (dashboards, attribution)</li>
            <li><strong>I</strong> — Align <strong>Incentives</strong> with desired behavior</li>
            <li><strong>P</strong> — Implement <strong>Peer review</strong> & accountability</li>
            <li><strong>R</strong> — Provide public <strong>Recognition</strong></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with concept_tabs[1]:
        st.markdown("""
        <div class="concept-note">
        <h3>📉 Loss Aversion: Why Losses Feel Worse Than Gains</h3>
        <p><strong>The Principle:</strong> Losing $100 causes ~2x more pain than gaining $100 brings pleasure. This asymmetry drives decision-making.</p>
        <p><strong>Discovered by:</strong> Kahneman & Tversky (1979), foundational to Prospect Theory</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Neuroscience Explanation:**
        - Loss-related brain activity (amygdala, insula) is ~2.5x stronger than gain-related activity
        - Evolutionary advantage: Early humans survived by avoiding losses more than pursuing gains
        """)
        
        st.markdown("""
        <div class="case-study">
        <h4>💰 Case Study 2: Mortgage Refinancing Paradox</h4>
        <p><strong>The Situation:</strong> Interest rates dropped 1.5%, meaning homeowners could refinance and save $200/month ($2,400/year).</p>
        <p><strong>Observed Behavior:</strong> Only 35% refinanced despite obvious financial benefit.</p>
        <p><strong>Why:</strong> Loss aversion prevented action:
        <ul>
            <li>"I'll lose my existing stable arrangement"</li>
            <li>"The hassle/effort/risk feels like a loss"</li>
            <li>"What if rates drop further?"</li>
        </ul>
        </p>
        <p><strong>Solution (Used by Lenders):</strong> Reframe as "Lock in your savings before rates rise" (loss framing) rather than "Save money by refinancing" (gain framing). Adoption jumped to 72%.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="real-world-app">
        <h4>🏢 Organizational Example: Software Migration</h4>
        <p>Company wants teams to migrate from Excel to a modern data platform.</p>
        <p><strong>❌ What Fails (Gain Framing):</strong> "New system will save 10 hours/week!"</p>
        <p><strong>✅ What Works (Loss Framing):</strong> "Current system costs us 20 security incidents/year and $500K in audit failures. Platform prevents 95% of these losses."</p>
        </div>
        """, unsafe_allow_html=True)
    
    with concept_tabs[2]:
        st.markdown("""
        <div class="concept-note">
        <h3>🤲 Trust: The Foundation of Cooperation</h3>
        <p><strong>Core Principle:</strong> Trust is not given; it's built through repeated positive interactions, transparency, and demonstrated reciprocity.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Components of Trust:**
        1. **Competence** — Do they have the skill? (Technical trust)
        2. **Integrity** — Will they follow through? (Reliability trust)
        3. **Benevolence** — Do they have my interests in mind? (Social trust)
        """)
        
        st.markdown("""
        <div class="case-study">
        <h4>🌲 Case Study 3: Patagonia & Radical Transparency</h4>
        <p><strong>The Challenge:</strong> Customers are skeptical of "green" companies (greenwashing is common).</p>
        <p><strong>Patagonia's Approach:</strong>
        <ul>
            <li>Published detailed supply chain (factory locations, worker conditions, wages)</li>
            <li>Admitted environmental impacts openly (not hidden)</li>
            <li>Continuous improvement reported publicly</li>
            <li>Encouraged customers to "buy less" (cannibalizing their own revenue)</li>
        </ul>
        </p>
        <p><strong>Result:</strong>
        <ul>
            <li>Customers reciprocated honesty with premium prices (brand commands 40% markup)</li>
            <li>Loyal advocates defend the brand online</li>
            <li>Employee retention 2x industry average (trust works internally too)</li>
            <li>$3B+ revenue despite higher costs</li>
        </ul>
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="managerial-lesson">
        <h4>💼 Building Trust in Teams</h4>
        <p><strong>The TRUST Framework:</strong></p>
        <ul>
            <li><strong>T</strong> — Transparency in decisions & communication</li>
            <li><strong>R</strong> — Reciprocity (give before asking)</li>
            <li><strong>U</strong> — Undo misunderstandings quickly</li>
            <li><strong>S</strong> — Show consistent behavior</li>
            <li><strong>T</strong> — Test with small commitments first</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with concept_tabs[3]:
        st.markdown("""
        <div class="concept-note">
        <h3>🧩 Common Cognitive Biases in Organizations</h3>
        </div>
        """, unsafe_allow_html=True)
        
        biases_data = {
            "Bias": [
                "Confirmation Bias",
                "Sunk Cost Fallacy",
                "Anchoring",
                "Status Quo Bias",
                "Dunning-Kruger Effect"
            ],
            "Definition": [
                "Seeking info that confirms existing beliefs",
                "Continuing bad projects due to past investment",
                "Over-weighting first information received",
                "Preferring things to stay the same",
                "Overestimating own competence"
            ],
            "Organizational Impact": [
                "Homogeneous teams make poor decisions",
                "Companies throw good money after bad",
                "First job offer anchors negotiation",
                "Resistance to change despite better alternatives",
                "Mediocre managers don't seek improvement"
            ],
            "Mitigation": [
                "Diverse hiring & devil's advocate roles",
                "Sunken cost audits; focus on future value",
                "Multiple reference points & market research",
                "Pilot programs with clear metrics",
                "360-degree feedback; skill assessments"
            ]
        }
        
        bias_df = pd.DataFrame(biases_data)
        st.dataframe(bias_df, use_container_width=True)

elif learning_path == "💼 Executive Summary":
    st.markdown('<div class="section-header">💼 Executive Summary: Behavioral Economics for Leaders</div>', unsafe_allow_html=True)
    
    exec_col1, exec_col2 = st.columns(2)
    
    with exec_col1:
        st.markdown("""
        <div class="managerial-lesson">
        <h4>🎯 The Three Laws of Organizational Behavior</h4>
        <p><strong>Law 1: Visibility Drives Cooperation</strong></p>
        <p>When contributions are invisible, free-riding increases. Transparent attribution can boost contribution rates by 40-60%.</p>
        <p><strong>Law 2: Loss Aversion > Gain Motivation</strong></p>
        <p>Framing decisions around preventing losses is 2-3x more effective than highlighting gains.</p>
        <p><strong>Law 3: Trust Requires Reciprocity</strong></p>
        <p>Trust isn't mandated; it's earned through predictable, fair treatment. Small acts of trust beget larger reciprocal commitments.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with exec_col2:
        st.markdown("""
        <div class="real-world-app">
        <h4>📊 ROI Impact</h4>
        <ul>
            <li><strong>Visibility + Incentives:</strong> +35% team productivity</li>
            <li><strong>Loss Framing:</strong> +60% adoption rates for new systems</li>
            <li><strong>Trust Building:</strong> +40% employee retention</li>
            <li><strong>Combined Effect:</strong> +120% team output potential</li>
        </ul>
        <p style="font-size: 0.85rem; color: rgba(255,255,255,0.6); margin-top: 1rem;">
        Based on meta-analysis of 200+ organizational studies
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick decision matrix
    st.markdown("### 🛠️ Quick Decision Matrix")
    
    decision_matrix = {
        "Challenge": [
            "Teams not collaborating on shared projects",
            "Low adoption of new systems/processes",
            "High turnover despite good compensation",
            "Knowledge hoarding across departments"
        ],
        "Root Cause": [
            "Lack of visibility & accountability",
            "Change perceived as loss (not gain)",
            "Low psychological safety & trust",
            "Free-rider incentives (no recognition)"
        ],
        "Intervention": [
            "Implement transparent dashboards + peer recognition",
            "Quantify current pain points; frame as loss prevention",
            "Leader transparency; pilot programs; listen to concerns",
            "Public attribution; LinkedIn profiles; career advancement"
        ],
        "Expected Impact": [
            "+30-50% contribution",
            "+50-70% adoption",
            "-30% turnover",
            "+40-60% knowledge sharing"
        ]
    }
    
    decision_df = pd.DataFrame(decision_matrix)
    st.dataframe(decision_df, use_container_width=True)

elif learning_path == "🛠️ Implementation Guide":
    st.markdown('<div class="section-header">🛠️ Implementation Guide: From Theory to Practice</div>', unsafe_allow_html=True)
    
    impl_tabs = st.tabs(["30-Day Plan", "Metrics & KPIs", "Common Pitfalls", "Tools & Templates"])
    
    with impl_tabs[0]:
        st.markdown("""
        <div class="managerial-lesson">
        <h4>📅 30-Day Behavioral Economics Implementation Plan</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Week 1: Foundation (Awareness)**
        - [ ] Share behavioral economics concepts with leadership team
        - [ ] Identify one high-impact organizational challenge (free-riding, low adoption, etc.)
        - [ ] Establish baseline metrics
        - [ ] Run this simulation with your team
        
        **Week 2: Visibility Initiative**
        - [ ] Design contribution tracking system (dashboards, metrics)
        - [ ] Brief team on new transparency measures
        - [ ] Communicate "Why": connection to behavioral economics
        - [ ] Soft launch with pilot team
        
        **Week 3: Incentive Alignment**
        - [ ] Map current incentives to desired behaviors
        - [ ] Design peer recognition program
        - [ ] Create visible leaderboards or achievement systems
        - [ ] Train managers on behavioral motivation techniques
        
        **Week 4: Build & Monitor**
        - [ ] Full rollout of visibility + incentives
        - [ ] Weekly pulse surveys on adoption
        - [ ] Celebrate early wins publicly
        - [ ] Gather feedback; iterate
        """)
    
    with impl_tabs[1]:
        st.markdown("""
        <div class="real-world-app">
        <h4>📊 Metrics to Track</h4>
        </div>
        """, unsafe_allow_html=True)
        
        metrics_data = {
            "Behavioral Metric": [
                "Contribution Rate (%)",
                "System Adoption (%)",
                "Voluntary Collaboration",
                "Employee Retention (%)",
                "Knowledge Sharing (docs/week)",
                "Team Satisfaction (NPS)"
            ],
            "Baseline": [
                "40%",
                "35%",
                "Low",
                "85%",
                "12",
                "52"
            ],
            "Target (90 days)": [
                "70%",
                "80%",
                "Medium-High",
                "88%",
                "35",
                "68"
            ],
            "Measurement Method": [
                "Dashboard tracking",
                "Feature usage logs",
                "Project participation surveys",
                "HR data",
                "Wiki/CMS analytics",
                "Monthly pulse survey"
            ]
        }
        
        metrics_df = pd.DataFrame(metrics_data)
        st.dataframe(metrics_df, use_container_width=True)
    
    with impl_tabs[2]:
        st.markdown("""
        <div class="case-study">
        <h4>⚠️ Common Implementation Pitfalls</h4>
        <p><strong>Pitfall 1: Transparency Without Trust</strong></p>
        <ul>
            <li>❌ Showing contribution dashboards before establishing psychological safety</li>
            <li>✅ Build trust first; then add visibility</li>
        </ul>
        <p><strong>Pitfall 2: Incentives Misaligned with Behavior</strong></p>
        <ul>
            <li>❌ Rewarding individual performance while expecting team collaboration</li>
            <li>✅ Make team outcomes 40-60% of compensation</li>
        </ul>
        <p><strong>Pitfall 3: Loss Framing Without Solutions</strong></p>
        <ul>
            <li>❌ Highlighting current pain points without showing how new system solves it</li>
            <li>✅ Pair loss messaging with clear solutions & transition support</li>
        </ul>
        <p><strong>Pitfall 4: Change Fatigue</strong></p>
        <ul>
            <li>❌ Implementing 5 behavioral initiatives simultaneously</li>
            <li>✅ Start with one high-impact initiative; expand after 60 days</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with impl_tabs[3]:
        st.markdown("""
        <div class="real-world-app">
        <h4>🛠️ Ready-to-Use Templates</h4>
        </div>
        """, unsafe_allow_html=True)
        
        template_col1, template_col2 = st.columns(2)
        
        with template_col1:
            st.markdown("""
            **Communication Email Template**
            
            ```
            Subject: How Behavioral Economics Will Transform Our Team
            
            Hi team,
            
            We're launching a new initiative based on behavioral 
            economics research. The goal: increase collaboration, 
            reduce silos, and boost our shared project success.
            
            Starting [DATE]:
            • New contribution visibility dashboard
            • Peer recognition program
            • Team collaboration bonuses (30% of bonus pool)
            
            Why this matters: Research shows that 70% of failed 
            collaborations stem from invisibility and misaligned 
            incentives. This fixes both.
            
            Questions? Let's discuss.
            
            [Your Name]
            ```
            """)
        
        with template_col2:
            st.markdown("""
            **One-Pager: Loss Aversion Change Narrative**
            
            ```
            THE CURRENT STATE (2024)
            ❌ 200 manual data entry hours/week
            ❌ $500K annual productivity loss
            ❌ 15 security incidents/year
            
            THE NEW STATE (2025)
            ✓ 20 automated data hours/week
            ✓ $480K annual savings
            ✓ 1-2 security incidents/year
            
            WHAT WE'RE PREVENTING BY ACTING NOW:
            → Losing competitive edge
            → Risk of audit failures
            → Talent drain (team frustration)
            ```
            """)

# =====================================================================
# FOOTER
# =====================================================================
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.caption("🎓 Built with behavioral economics research | Powered by Streamlit")

with footer_col2:
    total_score = min(100, round(st.session_state.game_score + st.session_state.mcq_score))
    st.caption(f"📈 Your Performance: {total_score}/100")

with footer_col3:
    st.caption(f"⏰ Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
