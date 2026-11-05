# Auto Hunt

## 1. Purpose

Auto Hunt is the game's background farming activity. The player selects a dungeon, difficulty and a team of three characters, starts a session, and the bot resolves repeated encounters automatically.

Its purpose is efficient progression farming—not active map exploration.

## 2. Session setup

A session setup flow should let the player:
1. Select an available dungeon.
2. Select a difficulty.
3. Select a saved team or choose three characters.
4. Review expected risk and session rules.
5. Start the session.

The team is controlled by one player and contains exactly three characters.

## 3. Automatic run behavior

The same underlying battle rules should be used as manual combat wherever possible:
- HP and Mana.
- Character stats.
- Classes and skills.
- Equipment and Runes.
- Enemy abilities and status effects.

The difference is that the Auto Hunt engine chooses actions according to the automated battle policy and advances encounters without asking the player to click every turn.

The team's power and composition determine how far it can progress. A session should continue while its configured continuation rules are satisfied, and stop on defeat or another defined stop condition.

## 4. Rewards

Potential Auto Hunt reward categories:
- Runes.
- Accessories.
- Gold.
- Upgrade materials.
- Monster drops.
- Crafting materials.
- Essence and other progression resources.

**Characters and Weapons are not direct rewards from ordinary Auto Hunt.** This is an explicit design constraint. Do not add either to standard Auto Hunt drop tables.

## 5. Difficulty and dungeon design

Dungeons are expected to support difficulty options. Normal, Hard, Nightmare and Abyss were discussed as candidate tiers, but the final names, scaling and availability are not locked.

Difficulty should not be only a multiplier to enemy HP. Higher difficulties can introduce:
- More dangerous enemy formations.
- Enemy skills and status effects.
- Protection or support relationships between enemies.
- More punishing encounter modifiers.
- Different elite or boss patterns.

Potential effects discussed include Poison, Bleed and Mana Drain. Their exact behavior remains open.

## 6. Progression over time

Potential long-term Auto Hunt progression includes:
- Auto Hunt level.
- Run efficiency.
- Loot bonuses.
- Longer or more efficient sessions.

These are ideas, not finalized mechanics. Avoid creating too many currencies or upgrade tracks just to support Auto Hunt.

## 7. Session limits and balance

Possible controls:
- Maximum session duration.
- Maximum number of runs.
- Energy-free entry costs or another clearly explained cost model.
- Per-dungeon access requirements.
- Cooldown or daily limit, if necessary.

No specific cost, cap or timer has been approved. The implementation must not silently assume one.

## 8. Background processing

Auto Hunt must run in a worker/background process rather than sending a Discord message for every encounter.

Recommended behavior:
- Save session state and each completed run.
- Send a concise start acknowledgement.
- Update a single progress/status message at a sensible interval.
- Send a final summary when the session ends.
- Allow the player to inspect the session result later.
- Resume safely after a bot restart using persisted state.

## 9. Session state

Track at minimum:
- Session ID and owner.
- Selected dungeon, difficulty and team.
- Start/end timestamps.
- Current run number and progress.
- Current team HP/Mana and relevant persistent state.
- Reward totals and run summaries.
- Stop reason.
- Claim/settlement status.

The exact persistence rules for HP/Mana between Auto Hunt encounters must be specified in the dungeon/session rules. Do not assume Crypt persistence rules automatically apply to Auto Hunt.

## 10. Failure and fairness

Automated action selection must use the same valid action rules as a human player. It must not cast skills without sufficient Mana or use items the player does not own. Random outcomes must be server-side and auditable through logs.

If a worker crashes, a run must not be paid twice or lost silently. Use idempotent run settlement and transaction-safe reward grants.
