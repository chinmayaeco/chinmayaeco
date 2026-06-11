<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Behavioral Economics: The Public Goods Game</title>
    <style>
        :root {
            --primary: #4F46E5;
            --primary-hover: #4338CA;
            --background: #F3F4F6;
            --surface: #FFFFFF;
            --text-main: #111827;
            --text-muted: #6B7280;
            --success: #10B981;
        }
        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            background-color: var(--background);
            color: var(--text-main);
            margin: 0;
            padding: 2rem;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        .card {
            background: var(--surface);
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            margin-bottom: 2rem;
        }
        h1, h2, h3 {
            color: var(--text-main);
            margin-top: 0;
        }
        h1 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: var(--primary);
        }
        .game-area {
            text-align: center;
            padding: 2rem;
            background: #EEF2FF;
            border-radius: 8px;
            border: 2px dashed var(--primary);
        }
        .input-group {
            margin: 1.5rem 0;
        }
        input[type="number"] {
            padding: 0.75rem;
            border: 1px solid #D1D5DB;
            border-radius: 6px;
            font-size: 1rem;
            width: 150px;
            text-align: center;
        }
        button {
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 6px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        button:hover {
            background-color: var(--primary-hover);
        }
        .insights-section {
            background: #F8FAFC;
            border-left: 4px solid var(--success);
            padding: 1.5rem;
            border-radius: 0 8px 8px 0;
        }
        .insight-card {
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid #E2E8F0;
        }
        .insight-card:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>The Public Goods Game</h1>
    
    <div class="card">
        <h2>Game Simulation</h2>
        <p>You and 3 other team members are given <strong>100 tokens</strong> each. You can choose to keep them or contribute any amount to a "public pool". The pool will be multiplied by 2 and then divided equally among all 4 members, regardless of their individual contributions.</p>
        
        <div class="game-area">
            <h3>How much will you contribute?</h3>
            <div class="input-group">
                <input type="number" id="contribution" min="0" max="100" placeholder="0 - 100">
            </div>
            <button onclick="playGame()">Invest in Public Pool</button>
            
            <div id="result" style="margin-top: 1.5rem; font-weight: bold; display: none;"></div>
        </div>
    </div>
    <div class="card insights-section">
        <h2>Practical Examples & Managerial Insights</h2>
        
        <div class="insight-card">
            <h3>1. The "Free-Rider" Problem in Cross-Functional Teams</h3>
            <p><strong>Practical Example:</strong> A team is tasked with cleaning up a shared codebase or organizing a company event. If everyone helps, the burden is light. But an individual might realize they can do nothing (keep their tokens) and still benefit from the organized code/event (the public pool).</p>
            <p><strong>Managerial Insight:</strong> Relying purely on goodwill leads to under-provision. Managers must align individual incentives with team goals. This can be done by making individual contributions visible (transparency), rewarding team-level outcomes, or establishing strong social norms and peer accountability.</p>
        </div>
        <div class="insight-card">
            <h3>2. Loss Aversion in Change Management</h3>
            <p><strong>Practical Example:</strong> Rolling out a new, more efficient software system. Employees resist because they overvalue the comfort of the old system (endowment effect) and fear the pain of learning the new one more than they value the eventual time saved.</p>
            <p><strong>Managerial Insight:</strong> Frame the change not just as a "gain" but highlight what the team is currently "losing" by staying with the old system (e.g., "We are losing 5 hours a week"). Provide a safety net during the transition so the perceived risk of loss is mitigated.</p>
        </div>
        <div class="insight-card">
            <h3>3. The Decoy Effect in Pricing & Feature Tiers</h3>
            <p><strong>Practical Example:</strong> A SaaS company offers a "Basic" tier for $50 and a "Pro" tier for $150. Many users choose Basic. The company introduces a "Pro without Analytics" tier for $140.</p>
            <p><strong>Managerial Insight:</strong> The $140 option isn't meant to be bought; it's a decoy. It makes the $150 "Pro" tier look like an incredible deal, shifting the majority of users away from "Basic" and up to "Pro". Managers can use pricing architecture to guide customer choices without restricting their freedom.</p>
        </div>
    </div>
</div>
<script>
    function playGame() {
        const contributionInput = document.getElementById('contribution').value;
        const resultDiv = document.getElementById('result');
        
        if (contributionInput === '' || contributionInput < 0 || contributionInput > 100) {
            alert("Please enter a valid contribution between 0 and 100.");
            return;
        }
        const userContribution = parseInt(contributionInput);
        
        // Simulate 3 other players who contribute randomly between 20 and 80
        const p2 = Math.floor(Math.random() * 60) + 20;
        const p3 = Math.floor(Math.random() * 60) + 20;
        const p4 = Math.floor(Math.random() * 60) + 20;
        const totalPool = userContribution + p2 + p3 + p4;
        const multipliedPool = totalPool * 2;
        const individualPayout = multipliedPool / 4;
        
        const finalTokens = (100 - userContribution) + individualPayout;
        resultDiv.style.display = "block";
        resultDiv.innerHTML = `
            <p>You contributed: <strong>${userContribution}</strong> tokens.</p>
            <p>Total pool after multiplier: <strong>${multipliedPool}</strong> tokens.</p>
            <p>Your share from the pool: <strong>${individualPayout.toFixed(1)}</strong> tokens.</p>
            <p style="color: var(--success); font-size: 1.2rem;">Your Total Earnings: <strong>${finalTokens.toFixed(1)}</strong> tokens!</p>
        `;
    }
</script>
</body>
</html>

