import streamlit as st
import random
import pandas as pd

# Set page configuration for a premium data-app dashboard feel
st.set_page_config(
    page_title="Behavioral Economics Game",
    page_icon="📈",
    layout="centered"
)

# --- INITIALIZE SESSION STATE ---
if 'game_played' not in st.session_state:
    st.session_state.game_played = False
if 'game_score' not in st.session_state:
    st.session_state.game_score = 0.0
if 'mcq_score' not in st.session_state:
    st.session_state.mcq_score = 0.0
if 'mcq1_answered' not in st.session_state:
    st.session_state.mcq1_answered = False
if 'mcq1_correct' not in st.session_state:
    st.session_state.mcq1_correct = False
if 'mcq2_answered' not in st.session_state:
    st.session_state.mcq2_answered = False
if 'mcq2_correct' not in st.session_state:
    st.session_state.mcq2_correct = False
if 'final_tokens' not in st.session_state:
    st.session_state.final_tokens = 0.0
if 'contributions' not in st.session_state:
    st.session_state.contributions = []

# --- PREMIUM CUSTOM STYLING ---
st.markdown("""
<style>
    /* Global design aesthetics */
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
</style>
""", unsafe_allow_html=True)

# Calculate Total Score out of 100
total_score = min(100, round(st.session_state.game_score + st.session_state.mcq_score))

# =====================================================================
# CONTAINER 1: HEADER & LIVE SCOREBOARD
# =====================================================================
header_container = st.container()
with header_container:
    st.title("📈 Behavioral Economics Simulator")
    st.markdown("Explore strategic decision-making, cooperation dynamics, and cognitive biases in business management.")
    
    # Score scoreboard display
    st.markdown(f"""
    <div class="score-banner">
        <h2>Your Performance Score: {total_score} / 100</h2>
        <p>Game Score: {round(st.session_state.game_score)}/50 | Quiz Score: {round(st.session_state.mcq_score)}/50</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# CONTAINER 2: GAME SIMULATION (INPUTS & DESCRIPTION)
# =====================================================================
game_container = st.container(border=True)
with game_container:
    st.subheader("🎮 Phase 1: The Public Goods Game")
    st.markdown("""
    **The Scenario:** You and 3 other managers are given **100 tokens** of resources. You must decide how much to keep for your own department, and how much to invest in a **shared project (Public Goods Pool)**.
    
    * **The Rule:** Every token contributed to the shared project is multiplied by **2** (due to synergy effects) and then shared **equally** among all 4 managers.
    * **The Dilemma:** You get to keep whatever you don't contribute. Can you trust the other managers to contribute, or will you maximize your private assets?
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
        c1, c2, c3 = st.columns(3)
        c1.metric(label="Your Final Tokens", value=f"{st.session_state.final_tokens:.1f}", delta=f"{st.session_state.final_tokens - 100:.1f} vs start")
        c2.metric(label="Total Shared Pool (2x)", value=f"{sum(st.session_state.contributions) * 2}")
        c3.metric(label="Individual Payout Share", value=f"{(sum(st.session_state.contributions) * 2) / 4:.1f}")
        
        # Data representation & Graph
        st.markdown("### Contribution Comparison Matrix")
        chart_df = pd.DataFrame({
            "Team Members": ["You (Manager A)", "Manager B", "Manager C", "Manager D"],
            "Contribution Amount (Tokens)": st.session_state.contributions,
            "Kept Amount (Tokens)": [100 - x for x in st.session_state.contributions]
        })
        
        # Plotting the visual bar graph representing contributions vs kept assets
        st.bar_chart(chart_df.set_index("Team Members"), y=["Contribution Amount (Tokens)", "Kept Amount (Tokens)"], color=["#4F46E5", "#CBD5E1"])
        
        st.info(f"**Game Score breakdown:** You kept {100 - st.session_state.contributions[0]} tokens, and received {st.session_state.final_tokens - (100 - st.session_state.contributions[0]):.1f} from the synergy pool. Score: **{round(st.session_state.game_score)} / 50**")

# =====================================================================
# CONTAINER 4: MANAGERIAL INSIGHTS & KNOWLEDGE TASKS (MCQs)
# =====================================================================
insights_container = st.container(border=True)
with insights_container:
    st.subheader("💡 Phase 2: Strategic Insights & Application")
    st.markdown("Review the foundational behavioral economics principles demonstrated by this simulation, then answer the questions below.")
    
    # MCQ 1
    st.markdown('<div class="insight-header">🤝 Concept 1: The Free-Rider Dilemma</div>', unsafe_allow_html=True)
    st.info("""
    **Insight:** In groups where rewards are shared equally regardless of input, individuals have an incentive to reduce their own effort/contribution while enjoying group benefits. This leads to team performance decay.
    """)
    
    q1_answer = st.radio(
        "**Managerial Application: How can you structure teams to mitigate the free-rider effect without micromanaging?**",
        options=[
            "A) Pay everyone flat salaries with no transparency or individual metrics.",
            "B) Make contributions and outcomes visible, and combine group incentives with peer accountability.",
            "C) Let the team self-manage entirely without tracking deliverables.",
            "D) Automatically penalize the person with the lowest self-reported contribution."
        ],
        key="q1_ans"
    )
    
    if not st.session_state.mcq1_answered:
        if st.button("Confirm Answer 1"):
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

    st.markdown("---")
    
    # MCQ 2
    st.markdown('<div class="insight-header">📉 Concept 2: Loss Aversion & Endowment Effect</div>', unsafe_allow_html=True)
    st.info("""
    **Insight:** People generally fear losses twice as much as they value equivalent gains. They also overvalue resources they already possess (endowment effect), making them resistant to sharing assets or adopting change.
    """)
    
    q2_answer = st.radio(
        "**Managerial Application: How should a leader pitch a new enterprise tool to employees resistant to changing their workflows?**",
        options=[
            "A) Emphasize only the abstract future efficiency gains of the software.",
            "B) Command everyone to use the tool immediately under threat of termination.",
            "C) Frame the transition around what they are *currently losing* (time, effort, competitiveness) by retaining their old workflows.",
            "D) Offer small cash rewards for every hour spent on the new software."
        ],
        key="q2_ans"
    )
    
    if not st.session_state.mcq2_answered:
        if st.button("Confirm Answer 2"):
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
