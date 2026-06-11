import streamlit as st
import random

# Set page configuration for a wider, more app-like layout
st.set_page_config(page_title="BE Games: Public Goods", page_icon="📈", layout="centered")

# --- CUSTOM CSS FOR STYLING ---
# We can inject some custom CSS to make it look a bit more polished
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
</style>
""", unsafe_allow_html=True)

# --- MAIN APP HEADER ---
st.title("📈 Behavioral Economics: The Public Goods Game")
st.markdown("---")

# --- GAME SECTION ---
st.header("🎮 Game Simulation")
st.markdown("""
You and 3 other team members are given **100 tokens** each. You can choose to keep them or contribute any amount to a "public pool". 
The total amount in the pool will be **multiplied by 2** and then **divided equally** among all 4 members, regardless of their individual contributions.
""")

# Input for the game
user_contribution = st.number_input(
    "How much will you contribute to the public pool?", 
    min_value=0, max_value=100, value=0, step=1
)

# Button to trigger the game logic
if st.button("Invest in Public Pool", type="primary"):
    # Simulate 3 other players who contribute randomly between 20 and 80
    p2 = random.randint(20, 80)
    p3 = random.randint(20, 80)
    p4 = random.randint(20, 80)
    
    total_pool = user_contribution + p2 + p3 + p4
    multiplied_pool = total_pool * 2
    individual_payout = multiplied_pool / 4
    
    final_tokens = (100 - user_contribution) + individual_payout
    
    # Display the results
    st.success("Results Calculated!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Your Contribution", value=f"{user_contribution} tokens")
        st.metric(label="Other Players' Contributions", value=f"{p2 + p3 + p4} tokens")
    with col2:
        st.metric(label="Total Pool (after 2x multiplier)", value=f"{multiplied_pool} tokens")
        st.metric(label="Your Share from the Pool", value=f"{individual_payout:.1f} tokens")
        
    st.info(f"**Your Total Earnings:** {(100 - user_contribution)} (kept) + {individual_payout:.1f} (from pool) = **{final_tokens:.1f} tokens!**")


st.markdown("---")

# --- MANAGERIAL INSIGHTS SECTION ---
st.header("💡 Practical Examples & Managerial Insights")

st.markdown("""
<div class="insight-box">
    <div class="insight-title">1. The "Free-Rider" Problem in Cross-Functional Teams</div>
    <p><strong>Practical Example:</strong> A team is tasked with cleaning up a shared codebase or organizing a company event. If everyone helps, the burden is light. But an individual might realize they can do nothing (keep their tokens) and still benefit from the organized code/event (the public pool).</p>
    <p><strong>Managerial Insight:</strong> Relying purely on goodwill leads to under-provision. Managers must align individual incentives with team goals. This can be done by making individual contributions visible (transparency), rewarding team-level outcomes, or establishing strong social norms and peer accountability.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="insight-box">
    <div class="insight-title">2. Loss Aversion in Change Management</div>
    <p><strong>Practical Example:</strong> Rolling out a new, more efficient software system. Employees resist because they overvalue the comfort of the old system (endowment effect) and fear the pain of learning the new one more than they value the eventual time saved.</p>
    <p><strong>Managerial Insight:</strong> Frame the change not just as a "gain" but highlight what the team is currently "losing" by staying with the old system (e.g., "We are losing 5 hours a week"). Provide a safety net during the transition so the perceived risk of loss is mitigated.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="insight-box">
    <div class="insight-title">3. The Decoy Effect in Pricing & Feature Tiers</div>
    <p><strong>Practical Example:</strong> A SaaS company offers a "Basic" tier for $50 and a "Pro" tier for $150. Many users choose Basic. The company introduces a "Pro without Analytics" tier for $140.</p>
    <p><strong>Managerial Insight:</strong> The $140 option isn't meant to be bought; it's a decoy. It makes the $150 "Pro" tier look like an incredible deal, shifting the majority of users away from "Basic" and up to "Pro". Managers can use pricing architecture to guide customer choices without restricting their freedom.</p>
</div>
""", unsafe_allow_html=True)
