import streamlit as st
import random
import pandas as pd

# Set page configuration
st.set_page_config(page_title="BE Games: Public Goods", page_icon="📈", layout="centered")

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
    st.session_state.final_tokens = 0
if 'contributions' not in st.session_state:
    st.session_state.contributions = []

st.markdown("""
<style>
    .insight-box {
        background-color: #F8FAFC;
        border-left: 4px solid #10B981;
        padding: 1.5rem;
        border-radius: 0 8px 8px 0;
        margin-bottom: 1rem;
    }
    .insight-title {
        color: #111827;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    .score-box {
        background-color: #EEF2FF;
        border: 2px dashed #4F46E5;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- TOTAL SCORE DISPLAY ---
total_score = min(100, round(st.session_state.game_score + st.session_state.mcq_score))

st.title("📈 Behavioral Economics: The Public Goods Game")
st.markdown(f"""
<div class="score-box">
    <h2 style="margin:0; color:#4F46E5;">Total Score: {total_score} / 100</h2>
    <p style="margin:0; color:#6B7280;">Game Score: {round(st.session_state.game_score)}/50 &nbsp;|&nbsp; MCQ Score: {round(st.session_state.mcq_score)}/50</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- GAME SECTION ---
st.header("🎮 Game Simulation (Max 50 points)")
st.markdown("""
You and 3 other team members are given **100 tokens** each. You can choose to keep them or contribute any amount to a "public pool". 
The total amount in the pool will be **multiplied by 2** and then **divided equally** among all 4 members, regardless of their individual contributions.
*(Your Game Score is based on the final tokens you accumulate).*
""")

user_contribution = st.number_input(
    "How much will you contribute to the public pool?", 
    min_value=0, max_value=100, value=0, step=1
)

if st.button("Invest in Public Pool", type="primary"):
    p2 = random.randint(20, 80)
    p3 = random.randint(20, 80)
    p4 = random.randint(20, 80)
    
    total_pool = user_contribution + p2 + p3 + p4
    multiplied_pool = total_pool * 2
    individual_payout = multiplied_pool / 4
    
    st.session_state.final_tokens = (100 - user_contribution) + individual_payout
    st.session_state.contributions = [user_contribution, p2, p3, p4]
    
    # Calculate score. 200 tokens roughly maps to a perfect 50 points. 
    calculated_game_score = min(50.0, (st.session_state.final_tokens / 200) * 50)
    st.session_state.game_score = calculated_game_score
    st.session_state.game_played = True
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()

if st.session_state.game_played:
    st.success("Results Calculated!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Your Contribution", value=f"{st.session_state.contributions[0]} tokens")
        st.metric(label="Other Players' Contributions", value=f"{sum(st.session_state.contributions[1:])} tokens")
    with col2:
        st.metric(label="Total Pool (after 2x multiplier)", value=f"{sum(st.session_state.contributions)*2} tokens")
        st.metric(label="Your Share from the Pool", value=f"{(sum(st.session_state.contributions)*2)/4:.1f} tokens")
        
    st.info(f"**Your Total Earnings:** {st.session_state.final_tokens:.1f} tokens! This gives you a Game Score of **{round(st.session_state.game_score)} / 50**.")
    
    # --- GRAPHS SECTION ---
    st.subheader("📊 Contribution Graph")
    chart_data = pd.DataFrame({
        "Players": ["You", "Player 2", "Player 3", "Player 4"],
        "Tokens Contributed": st.session_state.contributions
    })
    # Streamlit native bar chart
    st.bar_chart(chart_data.set_index("Players"), use_container_width=True)

st.markdown("---")

# --- MANAGERIAL INSIGHTS & MCQs SECTION ---
st.header("💡 Knowledge Check & Insights (Max 50 points)")

# --- MCQ 1 ---
st.markdown("""
<div class="insight-box">
    <div class="insight-title">1. The "Free-Rider" Problem</div>
    <p>Relying purely on goodwill leads to under-provision. Managers must align individual incentives with team goals.</p>
</div>
""", unsafe_allow_html=True)

st.write("**Question 1: What is the most effective way for a manager to reduce the 'free-rider' problem in a cross-functional team? (25 points)**")
q1_answer = st.radio("Select an option for Question 1:", [
    "A) Reduce the team's budget so everyone has to work harder.",
    "B) Make individual contributions visible to the team and reward team-level outcomes.",
    "C) Ignore the problem, as team dynamics will naturally resolve it over time.",
    "D) Give the team easier tasks."
], key="q1_radio")

if not st.session_state.mcq1_answered:
    if st.button("Submit Answer 1"):
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
        st.success("✅ **Correct!** Transparency and aligned incentives mitigate free-riding. (+25 points)")
    else:
        st.error("❌ **Incorrect.** The best approach is to make individual contributions visible and reward team outcomes (Option B).")

st.write("")

# --- MCQ 2 ---
st.markdown("""
<div class="insight-box">
    <div class="insight-title">2. Loss Aversion in Change Management</div>
    <p>Employees often overvalue the comfort of the old system and fear the pain of learning a new one.</p>
</div>
""", unsafe_allow_html=True)

st.write("**Question 2: According to 'Loss Aversion', how should a manager frame the rollout of a new software system? (25 points)**")
q2_answer = st.radio("Select an option for Question 2:", [
    "A) Only highlight the amazing new features the software has.",
    "B) Force employees to use it without explanation.",
    "C) Highlight what the team is currently 'losing' (e.g. time, efficiency) by staying with the old system.",
    "D) Pay employees extra to use the new software."
], key="q2_radio")

if not st.session_state.mcq2_answered:
    if st.button("Submit Answer 2"):
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
        st.success("✅ **Correct!** Framing change as a way to avoid a loss is often more motivating than framing it as a gain. (+25 points)")
    else:
        st.error("❌ **Incorrect.** Highlighting current losses like inefficiency is the key insight of loss aversion (Option C).")

