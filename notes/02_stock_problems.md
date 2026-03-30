# Stock Problems

## Related Leetcode questions
- [**0121 Best Time to Buy and Sell Stock**](https://github.com/gab-lee/Leetcode/tree/main/problems/0121_best_time_to_buy_and_sell_stock):
Find max profit from one buy + one sell (buy before sell).
- **0122 Best Time to Buy and Sell Stock II**:
Unlimited transactions, but must sell before buying again.
- **0123 Best Time to Buy and Sell Stock III**:
Max profit with at most 2 transactions.
- **0188 Best Time to Buy and Sell Stock IV**:
Max profit with at most k transactions.
- **0309 Best Time to Buy and Sell Stock with Cooldown**: Unlimited transactions, but 1-day cooldown after each sell.
- **0714 Best Time to Buy and Sell Stock with Transaction Fee**: Unlimited transactions, but pay a fee on each transaction.

## Problem Concept
Core concept: Dynamic Programming with state machines.

You're tracking multiple states at each day (holding stock, not holding, in cooldown, transactions remaining) and the optimal profit in each state. The recurrence relations define how you transition between states.
What makes them hard:

## What this tests
1. **State machine modeling** - Can you map a real-world constraint system (transaction rules) onto discrete states and transitions?

2. **DP pattern recognition** - Realizing "optimal substructure" exists: best profit at day i depends on best profit at day i-1 plus today's decision.

3. **Constraint handling** - Each variant adds a constraint (transaction limit, cooldown, fee). Can you modify your model without rebuilding from scratch?

4. **Space optimization** - Going from O(n×states) to O(states) by recognizing you only need the previous row.

## Core techniques

1. **State definition** - "What do I need to know at day i to make optimal decisions?" Usually: holding/not holding, transactions used, cooldown status.

2. **Recurrence relations** - For each state, "How do I get here optimally?" Example: `hold[i] = max(hold[i-1], notHold[i-1] - prices[i])` means "either I was already holding, or I buy today."

3. **Base cases** - Day 0 initialization. Holding requires buying, so profit is negative.

4. **Rolling variables** - Replace 2D array with variables that update in-place: `prevHold`, `currHold`.

5. **Greedy insight** (122 only) - When transactions are unlimited, just sum all positive deltas. No DP needed.

## Why these are difficult

1. **State explosion** - As constraints layer (transaction limits, cooldowns, fees), you need more states. 123 needs 4 states. 188 needs 2k+1 states. Easy to lose track.

2. **Initialization traps** - Getting day 0 wrong breaks everything. "Holding stock on day 0" means you bought it, so profit is -prices[0], not 0. Miss that, wrong answer.

3. **Recurrence logic isn't obvious** - "Should I sell today?" depends on "was I holding yesterday?" But 309 adds: "and was I NOT in cooldown?" The logic branches multiply.

4. **Off-by-one bugs** - Cooldown affects day i+1, not day i. Transaction count increments on buy or sell? Easy to misplace.

5. **Optimization pressure** - Naive DP is O(nk) space. Interviewers expect you to compress to O(k) or O(1) by realizing you only need the previous day's states.

## Bottom line

This is really a test of **systematic thinking under constraints**. Can you build a mental model, encode it correctly, and adapt it when rules change?

The 121→122→123→188→309→714 progression is pedagogical—each adds one constraint. But you can't just "see" the pattern; you have to derive the state machine each time.