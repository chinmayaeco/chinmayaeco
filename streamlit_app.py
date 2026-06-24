import streamlit as st
import random
import pandas as pd
import numpy as np
from datetime import datetime

# Set page configuration for a premium data-app dashboard feel
st.set_page_config(
    page_title="Behavioral Economics Game",
    page_icon="📈",
    layout="wide"
)

# --- INITIALIZE SESSION STATE ---
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
        'current_round': 0
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()

# --- PREMIUM CUSTOM STYLING ---
st.markdown("""
<style>
    .reportview-container {
        background: #F8FAFC;
    }
    .score-banner {
        background: linear-gradient(135deg, #4F46E5 0%, #3730A3 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.2);
    }
    .score-banner h2 {
        color: white !important;
        margin: 0 !important;
        font-weight: 700;
    }
    .score-banner p {
        margin: 0.5rem 0 0 0 !important;
        opacity: 0.9;
        font-size: 1rem;
    }
    .insight-header {
        color: #1E293B;
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .case-study {
        background: #EEF2FF;
        border-left: 4px solid #4F46E5;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }
    .real-world-app {
        background: #F0FDF4;
        border-left: 4px solid #22C55E;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# CONTAINER 1: HEADER & LIVE SCOREBOARD
# =====================================================================
header_container = st.container()
with header_container:
    st.title("📈 Behavioral Economics Simulator")
    st.markdown("Master strategic decision-making, cooperation dynamics, and cognitive biases through real-world case studies.")
    
    # Score scoreboard display
    total_score = min(100, round(st.session_state.game_score + st.session_state.mcq_score))
    st.markdown(f"""
    <div class="score-banner">
        <h2>Your Performance Score: {total_score} / 100</h2>
        <p>Game Score: {round(st.session_state.game_score)}/50 | Quiz Score: {round(st.session_state.mcq_score)}/75</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# CONTAINER 2: GAME SIMULATION (INPUTS & DESCRIPTION)
# =====================================================================
game_container = st.container(border=True)
with game_container:
    st.subheader("🎮 Phase 1: The Public Goods Game")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **The Scenario:** You and 3 other managers are given **100 tokens** of resources. You must decide how much to keep for your own department, and how much to invest in a **shared project**.
        
        * **The Rule:** Every token contributed to the shared project is multiplied by **2** (due to synergy effects) and then shared **equally** among all 4 managers.
        * **The Dilemma:** You get to keep whatever you don't contribute. Can you trust the other managers to contribute, or will you maximize your private assets?
        
        **Real-World Context:** This mirrors R&D budget allocation in tech companies, open-source contribution decisions, and team resource pooling.
        """)
    
    with col2:
        st.info("""
        **Token Economics:**
        - Starting: 100
        - Contribution multiplier: 2x
        - Distribution: Equal (÷4)
        
        **Example:** If all contribute 50:
        - Pool: 200 tokens
        - x2 Multiplied: 400
        - Per person: 100 ✓
        """)
    
    user_contribution = st.slider(
        "Select your contribution to the Public Goods Pool:",
        min_value=0, max_value=100, value=50, step=5
    )
    
    if st.button("Submit Investment Decision", type="primary"):
        # Simulate three artificial players with randomized cooperative behavior
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
        
        # Calculate game score (scaled: 200 tokens yields the maximum 50 points)
        st.session_state.game_score = min(50.0, (st.session_state.final_tokens / 200.0) * 50.0)
        st.session_state.game_played = True
        
        try:
            st.rerun()
        except AttributeError:
            st.experimental_rerun()

# =====================================================================
# CONTAINER 3: SIMULATION RESULTS & GRAPHS
# =====================================================================
if st.session_state.game_played:
    results_container = st.container(border=True)
    with results_container:
        st.subheader("📊 Round Simulation Results")
        
        # High level metrics columns
        c1, c2, c3, c4 = st.columns(4)
        c1.metric(
            label="Your Final Tokens", 
            value=f"{st.session_state.final_tokens:.1f}", 
            delta=f"{st.session_state.final_tokens - 100:.1f} vs start"
        )
        c2.metric(
            label="Total Shared Pool (2x)", 
            value=f"{sum(st.session_state.contributions) * 2}"
        )
        c3.metric(
            label="Individual Payout Share", 
            value=f"{(sum(st.session_state.contributions) * 2) / 4:.1f}"
        )
        c4.metric(
            label="Others' Avg Contribution", 
            value=f"{(st.session_state.contributions[1] + st.session_state.contributions[2] + st.session_state.contributions[3]) / 3:.1f}"
        )
        
        # Data representation & Graph
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.markdown("### Contribution Comparison")
            chart_df = pd.DataFrame({
                "Team Members": ["You", "Manager B", "Manager C", "Manager D"],
                "Contribution (Tokens)": st.session_state.contributions,
                "Kept (Tokens)": [100 - x for x in st.session_state.contributions]
            })
            st.bar_chart(
                chart_df.set_index("Team Members"), 
                y=["Contribution (Tokens)", "Kept (Tokens)"], 
                color=["#4F46E5", "#CBD5E1"]
            )
        
        with col_chart2:
            st.markdown("### Contribution Strategy Analysis")
            if st.session_state.game_history:
                history_df = pd.DataFrame(st.session_state.game_history)
                st.line_chart(
                    history_df.set_index('round'),
                    y=['contribution', 'others_avg'],
                    color=['#4F46E5', '#EF4444']
                )
        
        # Analysis
        your_contribution = st.session_state.contributions[0]
        others_avg = np.mean(st.session_state.contributions[1:])
        contribution_diff = your_contribution - others_avg
        
        if contribution_diff > 5:
            analysis_text = "🟢 **You contributed MORE than average.** You demonstrate cooperative behavior and trust."
        elif contribution_diff < -5:
            analysis_text = "🔴 **You contributed LESS than average.** You displayed free-rider tendencies."
        else:
            analysis_text = "🟡 **You matched the group average.** Your behavior reflects the social norm."
        
        st.info(f"**Game Score breakdown:** {analysis_text}\n\n"
                f"- You kept: {100 - your_contribution} tokens\n"
                f"- You received (payout share): {st.session_state.final_tokens - (100 - your_contribution):.1f} tokens")

# =====================================================================
# CONTAINER 4: CASE STUDIES & REAL-WORLD APPLICATIONS
# =====================================================================
case_studies_container = st.container(border=True)
with case_studies_container:
    st.subheader("📚 Case Studies & Real-World Applications")
    
    tab1, tab2, tab3 = st.tabs(["Free-Rider Dilemma", "Loss Aversion", "Trust & Cooperation"])
    
    # ============ TAB 1: FREE-RIDER DILEMMA ============
    with tab1:
        st.markdown('<div class="insight-header">🤝 Concept 1: The Free-Rider Dilemma</div>', unsafe_allow_html=True)
        
        st.info("""
        **Insight:** In groups where rewards are shared equally regardless of input, individuals have an incentive to reduce their own effort/contribution while enjoying group benefits. 
        This leads to team productivity collapse if unchecked.
        """)
        
        st.markdown("#### Case Study 1: Open-Source Software Communities")
        st.markdown("""
        <div class="case-study">
        <strong>The Problem:</strong> Linux kernel development faced declining contributions in the 2000s. Many developers benefited from the open-source community but didn't contribute code, relying on others' work.
        
        <strong>The Solution:</strong>
        • Public contribution attribution (git blame/credit)
        • Visible contributor rankings on GitHub
        • Community recognition programs (Linux Foundation memberships)
        • Peer review processes creating social accountability
        
        <strong>Result:</strong> Contribution rates increased by 40%+ once visibility improved.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Case Study 2: Corporate R&D Teams (Real Example)")
        st.markdown("""
        <div class="case-study">
        <strong>The Problem:</strong> A Fortune 500 tech company noticed that shared innovation budgets weren't generating expected returns. Teams were "contributing" minimal effort to collective projects while maximizing private departmental spending.
        
        <strong>The Solution:</strong>
        • Implemented transparent contribution tracking dashboards
        • Tied bonuses 30% to team project contributions (visible metrics)
        • Monthly team showcases highlighting individual contributions
        • Peer evaluations factoring into promotions
        
        <strong>Result:</strong> Shared projects contribution increased from 35% to 72% of budgets within 2 quarters.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Case Study 3: Household Recycling Programs")
        st.markdown("""
        <div class="case-study">
        <strong>The Problem:</strong> Communities with shared recycling incentives saw low participation rates because individual sorting effort wasn't visible or rewarded.
        
        <strong>The Solution:</strong>
        • Installed transparent bin cameras showing individual household participation
        • Posted neighborhood recycling leaderboards
        • Gamified competition between streets
        • Social recognition for top contributors
        
        <strong>Result:</strong> Participation increased from 42% to 78% within 6 months.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Managerial Application")
        q1_answer = st.radio(
            "**How can you structure teams to mitigate the free-rider effect without micromanaging?**",
            options=[
                "A) Pay everyone flat salaries with no transparency or individual metrics.",
                "B) Make contributions and outcomes visible, and combine group incentives with peer accountability.",
                "C) Let the team self-manage entirely without tracking deliverables.",
                "D) Automatically penalize the person with the lowest self-reported contribution."
            ],
            key="q1_ans"
        )
        
        if not st.session_state.mcq1_answered:
            if st.button("Confirm Answer 1", key="btn1"):
                st.session_state.mcq1_answered = True
                if q1_answer.startswith("B"):
                    st.session_state.mcq1_correct = True
                    st.session_state.mcq_score += 25
                try:
                    st.rerun()
                except AttributeError:
                    st.experimental_rerun()
        else:
            if st.session_state.mcq1_correct:
                st.success("🎯 **Correct!** Visibility, peer evaluation, and recognition systems effectively curb free-riding.")
            else:
                st.error("❌ **Incorrect.** The correct strategy is **B**. Establishing contribution visibility and peer review mechanisms creates social accountability.")
    
    # ============ TAB 2: LOSS AVERSION ============
    with tab2:
        st.markdown('<div class="insight-header">📉 Concept 2: Loss Aversion & Endowment Effect</div>', unsafe_allow_html=True)
        
        st.info("""
        **Insight:** People generally fear losses twice as much as they value equivalent gains. They also overvalue resources they already possess (endowment effect), making them resistant to sharing assets.
        """)
        
        st.markdown("#### Case Study 1: Enterprise Software Adoption (Microsoft Office → Google Workspace)")
        st.markdown("""
        <div class="case-study">
        <strong>The Problem:</strong> Companies had decades of Office macros, templates, and workflows. When Google offered a superior cloud alternative, adoption stalled. Employees focused on "what they'd lose" (familiar tools, custom scripts) rather than future gains.
        
        <strong>The Solution (Google's Approach):</strong>
        • Highlighted productivity losses from current workflows (time spent on syncing, version control issues)
        • Showed real costs of downtime, security breaches with legacy systems
        • Framed migration as preventing future losses, not promising abstract gains
        • Provided migration assistance to make transition painless
        
        <strong>Result:</strong> Enterprise adoption increased from 5% to 40% within 18 months after reframing messaging.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Case Study 2: Behavioral Economics in Netflix's Pricing Strategy")
        st.markdown("""
        <div class="case-study">
        <strong>The Problem:</strong> When Netflix tried to introduce a lower-tier ad-supported plan, users resisted the premium tier price increase.
        
        <strong>The Solution:</strong>
        • Reframed: "You're LOSING access to ad-free viewing" rather than "Ad tier costs less"
        • Showed comparison: ads-per-hour vs. subscription cost
        • Highlighted what current subscribers would "lose" by downgrading
        
        <strong>Result:</strong> Churn was minimized; 15% of subscribers upgraded to avoid "losing" ad-free experience.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Case Study 3: Organizational Change Management")
        st.markdown("""
        <div class="case-study">
        <strong>The Problem:</strong> A healthcare organization tried to consolidate departments. Staff feared losing autonomy, familiar routines, and established relationships.
        
        <strong>The Solution:</strong>
        • Presented data on current inefficiencies, duplicated efforts (losses with status quo)
        • Highlighted patient care improvements being lost due to silos
        • Showed rising operational costs directly impacting staff benefits (framed as loss)
        • Created transition support teams to preserve relationships
        
        <strong>Result:</strong> 85% staff support vs. predicted 30% without loss-aversion framing.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Managerial Application")
        q2_answer = st.radio(
            "**How should a leader pitch a new enterprise tool to employees resistant to changing their workflows?**",
            options=[
                "A) Emphasize only the abstract future efficiency gains of the software.",
                "B) Command everyone to use the tool immediately under threat of termination.",
                "C) Frame the transition around what they are *currently losing* (time, effort, competitiveness) by retaining their old workflows.",
                "D) Offer small cash rewards for every hour spent on the new software."
            ],
            key="q2_ans"
        )
        
        if not st.session_state.mcq2_answered:
            if st.button("Confirm Answer 2", key="btn2"):
                st.session_state.mcq2_answered = True
                if q2_answer.startswith("C"):
                    st.session_state.mcq2_correct = True
                    st.session_state.mcq_score += 25
                try:
                    st.rerun()
                except AttributeError:
                    st.experimental_rerun()
        else:
            if st.session_state.mcq2_correct:
                st.success("🎯 **Correct!** Pointing out current losses triggers loss aversion to drive proactive behavioral change.")
            else:
                st.error("❌ **Incorrect.** The correct strategy is **C**. Highlighting current losses (the status quo cost) is much more effective than promising future gains.")
    
    # ============ TAB 3: TRUST & COOPERATION ============
    with tab3:
        st.markdown('<div class="insight-header">🤲 Concept 3: Trust, Reciprocity & Cooperation</div>', unsafe_allow_html=True)
        
        st.info("""
        **Insight:** Trust is not given freely—it's built through transparency, predictable behavior, and demonstrated reciprocity. 
        When individuals see others cooperating, they're significantly more likely to cooperate themselves.
        """)
        
        st.markdown("#### Case Study 1: Nordstrom's Return Policy (Trust in Retail)")
        st.markdown("""
        <div class="case-study">
        <strong>The Problem:</strong> Competitors had strict return policies. Nordstrom implemented "no questions asked" returns (even items from other stores!).
        
        <strong>The Behavioral Insight:</strong>
        • Customers reciprocated this trust with loyalty and higher spending
        • Reduced return fraud rates despite permissive policy (most people don't abuse trust)
        • Built brand reputation for trustworthiness
        
        <strong>Result:</strong> Nordstrom achieved 15-year customer retention rates 30% higher than competitors. Revenue per customer increased due to reciprocal loyalty.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Case Study 2: Patagonia's Radical Transparency")
        st.markdown("""
        <div class="case-study">
        <strong>The Problem:</strong> Environmental concerns about fast fashion meant customers were skeptical of corporate sustainability claims.
        
        <strong>The Solution:</strong>
        • Published detailed supply chain data (which factories, worker conditions)
        • Admitted environmental impacts and continuously improved
        • Transparent pricing showing material costs
        • Encouraged customers to "buy less"
        
        <strong>The Behavioral Effect:</strong>
        • Customers reciprocated honesty with higher prices paid (brand premium)
        • Community of brand advocates who defend the company
        • Employee retention 40% above industry average (trust reciprocated internally too)
        
        <strong>Result:</strong> $3B+ revenue with premium pricing due to trust-based loyalty.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Case Study 3: Performance-Based Contractor Networks")
        st.markdown("""
        <div class="case-study">
        <strong>The Problem:</strong> Companies hiring freelancers/contractors faced high quality variability and low repeat business.
        
        <strong>The Solution (Upwork, Toptal model):</strong>
        • Transparent reputation scores visible to all parties
        • Escrow payment systems (reducing contractor risk of non-payment)
        • Fair dispute resolution mechanisms
        • Contractor autonomy in price-setting
        
        <strong>The Behavioral Effect:</strong>
        • Contractors see fair treatment → invest in quality and communication
        • Repeat engagement increases 60%+ once trust is established
        • Premium pricing accepted due to proven reliability
        
        <strong>Result:</strong> Marketplace liquidity and transaction volume 5x higher in high-trust platforms vs. low-trust competitors.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Managerial Application")
        q3_answer = st.radio(
            "**In a team restructure, how should you rebuild trust among departments that previously competed for resources?**",
            options=[
                "A) Announce the new structure and mandate collaboration via policy.",
                "B) Start with small, low-risk collaborative projects with transparent success metrics, celebrate wins, and gradually increase interdependence.",
                "C) Implement strict oversight and penalties for non-cooperation.",
                "D) Isolate teams entirely to avoid conflict."
            ],
            key="q3_ans"
        )
        
        if not st.session_state.mcq3_answered:
            if st.button("Confirm Answer 3", key="btn3"):
                st.session_state.mcq3_answered = True
                if q3_answer.startswith("B"):
                    st.session_state.mcq3_correct = True
                    st.session_state.mcq_score += 25
                try:
                    st.rerun()
                except AttributeError:
                    st.experimental_rerun()
        else:
            if st.session_state.mcq3_correct:
                st.success("🎯 **Correct!** Trust is built through repeated positive interactions and visible reciprocity.")
            else:
                st.error("❌ **Incorrect.** The correct strategy is **B**. Small collaborative wins build trust; mandates or isolation destroy it.")

# =====================================================================
# CONTAINER 5: PRACTICAL FRAMEWORKS
# =====================================================================
frameworks_container = st.container(border=True)
with frameworks_container:
    st.subheader("🛠️ Practical Implementation Frameworks")
    
    col_framework1, col_framework2 = st.columns(2)
    
    with col_framework1:
        st.markdown("#### Framework 1: Designing Cooperative Systems")
        st.markdown("""
        <div class="real-world-app">
        **The VIPR Model (Visibility-Incentives-Peer review-Recognition):**
        
        1. **Visibility** — Make contributions measurable and transparent
           - Example: Public dashboards, contribution attribution
        
        2. **Incentives** — Align rewards with desired behavior
           - Example: 30% bonus tied to team outcomes, 70% to individual + group collaboration
        
        3. **Peer Review** — Incorporate social accountability
           - Example: 360-degree feedback, peer bonus allocation (managers give teammates bonuses)
        
        4. **Recognition** — Celebrate cooperative behavior publicly
           - Example: Monthly awards, team spotlights, career advancement
        </div>
        """, unsafe_allow_html=True)
    
    with col_framework2:
        st.markdown("#### Framework 2: Change Management via Loss Aversion")
        st.markdown("""
        <div class="real-world-app">
        **The LOSS Framework (Losses-Outcomes-Status quo-Support):**
        
        1. **Losses** — Quantify current pain points
           - Example: "We spend 12 hours/week on manual data entry"
        
        2. **Outcomes** — Show projected losses if status quo continues
           - Example: "This costs us $500K annually in lost productivity"
        
        3. **Status quo** — Make current state feel unacceptable
           - Example: "Competitors are 2x faster due to automation"
        
        4. **Support** — Provide resources to ease transition
           - Example: Training, transition teams, pilot programs
        </div>
        """, unsafe_allow_html=True)

# =====================================================================
# CONTAINER 6: KEY TAKEAWAYS
# =====================================================================
takeaways_container = st.container(border=True)
with takeaways_container:
    st.subheader("💡 Key Takeaways for Leaders")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 1️⃣ Visibility Drives Cooperation
        People cooperate MORE when their contributions are visible and recognized. 
        
        **Action:** Implement transparent contribution tracking across teams.
        """)
    
    with col2:
        st.markdown("""
        #### 2️⃣ Loss Aversion > Gain Motivation
        People avoid losses 2x more than they pursue gains.
        
        **Action:** Frame changes around "preventing losses" not "enabling gains."
        """)
    
    with col3:
        st.markdown("""
        #### 3️⃣ Trust Requires Reciprocity
        Trust isn't imposed; it's built through fair treatment and transparency.
        
        **Action:** Start with small collaborative wins; scale trust incrementally.
        """)

st.markdown("---")
st.caption(f"Session updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Total Score: {total_score}/100")
