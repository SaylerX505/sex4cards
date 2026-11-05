# Combat System

## 1. Combat format

Combat is **classic turn-based RPG**. One player controls a team of exactly three characters. The team is not three separate human players.

The basic round structure:

1. The player selects an action for Team Slot 1.
2. The player selects an action for Team Slot 2.
3. The player selects an action for Team Slot 3.
4. Enemies perform their actions.
5. End-of-round effects resolve and the next round begins.

The initial order follows the team's displayed slot order. Speed may be used for other mechanics later, but it is not currently confirmed as the player-turn ordering rule.

## 2. Player action menu

Each active character can choose from:

| Action | Purpose | Mana |
|---|---|---|
| Attack | Basic attack | Free |
| Skill | Use one of the character's active skills | Usually costs Mana |
| Defend | Reduce incoming damage or apply a defensive state | Cost not finalized; expected to be free |
| Item | Use an eligible battle consumable | Item is consumed according to its rules |

Basic Attack must remain usable even when the character has no Mana.

If Mana is insufficient for a selected skill, the bot should clearly explain that the skill cannot be used and present valid alternatives. A character with no Mana can still Attack or Defend.

## 3. Mana rules

Mana is the only skill resource currently selected. There is no separate Energy bar.

Confirmed direction:
- Skills use Mana.
- Basic Attack does not use Mana.
- Mana regeneration is slow.
- Mana does not refill after every individual character action.
- A small amount may regenerate after a complete round.
- Mana-restoring potions may exist.
- Some equipment/runes may affect Max Mana or regeneration.

The exact maximum Mana, skill costs, regeneration amount, potion strength and exceptions are not finalized. Avoid hard-coding example values as final balance.

## 4. Skill design principles

Skills should be short, readable and tactically distinct. Prefer:
- Single-target damage.
- Multi-target damage.
- Healing.
- Damage reduction or protection.
- Status effects such as Poison, Bleed, Freeze or Mana Drain, if approved for the relevant content.

Avoid complex multi-step combos and excessive cooldown/resource systems. Mana is the current resource model; do not reintroduce Energy.

A proposed character kit structure is Passive + two Active Skills + Ultimate. The structure still needs final approval.

## 5. Statistics used in combat

Candidate combat attributes include HP, ATK, DEF, SPD, CRIT Rate, CRIT DMG, Accuracy, Resistance and Max Mana. Their formulas and rounding behavior must be specified in a balance document before implementation.

Recommended formula requirements:
- Define whether damage is physical, magical or true damage.
- Define critical hit order and rounding.
- Define minimum damage and damage caps.
- Define how DEF and resistance interact.
- Define status-effect duration and stacking.
- Define healing caps and revive behavior.
- Keep the formulas deterministic and testable once the random roll is supplied.

## 6. Enemy turns and encounter state

Enemies act after the player's three actions. Each enemy definition should specify:
- Stats and level/scaling rules.
- Available actions and target selection.
- Status effects.
- Reward table.
- Encounter-specific behavior.

Enemy AI should be deterministic where possible, with controlled randomness for target selection or special moves. All random outcomes must be generated server-side.

## 7. Status effects

Potential status effects mentioned during design include Poison, Bleed, Freeze, protection effects and Mana Drain. These are candidate mechanics; exact names, durations, stacking and cleansing rules remain open.

Every status effect must define:
- Trigger timing (on action, end of turn, start/end of round).
- Duration.
- Whether it stacks, refreshes or replaces.
- Whether it can be cleansed or resisted.
- Whether it affects bosses.
- Its UI icon and concise tooltip.

## 8. Battle lifecycle

A battle state should track:
- Battle ID and owner.
- Encounter and difficulty.
- Team member IDs and their current HP/Mana.
- Enemy IDs and their current HP/statuses.
- Current round and active action slot.
- Actions already submitted this round.
- Turn phase.
- Outcome and reward-claim status.

Persist battle state after each accepted action. A Discord interaction retry must not execute the same action twice.

## 9. Victory, defeat and rewards

Victory/defeat behavior depends on the activity:
- A normal encounter can grant its defined rewards on victory.
- Auto Hunt continues or stops according to its session rules.
- The Crypt carries selected run state between rooms and resolves the run separately.

Reward tables, XP, Gold, drop rates, boss guarantees and defeat compensation are still open. Do not assume a single universal reward formula.

## 10. Discord battle UI

A battle message should show:
- Encounter name and current round.
- Three team members with HP/Mana.
- Enemy health and visible status effects.
- The currently acting character.
- Buttons or a select menu for Attack, Skill, Defend and Item.
- Skill descriptions and Mana costs before confirmation.

Edit the existing battle message whenever possible rather than posting a new message for every action. Disable or reject stale controls after the state changes.
