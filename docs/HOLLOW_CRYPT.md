# The Hollow Crypt

## 1. Mode identity

**The Hollow Crypt** is an active, choice-driven exploration mode. It is separate from Auto Hunt.

- Auto Hunt: background farming and repeated automated dungeon encounters.
- Hollow Crypt: the player actively chooses paths, rooms, risk and temporary run upgrades.

The concept draws inspiration from the map exploration and persistent-team-health ideas of Mortal Kombat Mobile's Krypt, and the branching route and run-specific passive choices found in Slay the Spire. It should use its own content and balance.

## 2. Run setup

A proposed setup flow:
1. Choose a Crypt difficulty.
2. Choose a team of exactly three characters.
3. Start a new run.
4. Reveal the first available map choices.

Normal, Hard, Nightmare and Abyss were discussed as possible difficulty names, but they are not final.

## 3. Branching map

The Crypt is envisioned as a randomized branching map. Some of the map may be hidden until the player explores it. The player chooses which connected room to enter.

Potential room types:
- **Battle:** standard enemy encounter.
- **Elite:** harder encounter with a more valuable reward.
- **Treasure:** item or resource reward.
- **Event:** a choice with a benefit, cost or risk.
- **Merchant:** spend run currency on supplies or temporary effects.
- **Shrine/Rest:** recovery or a special choice.
- **Boss:** major encounter or run milestone.

Room frequency, map length, reveal rules and route generation are all open decisions.

## 4. Persistent team health

The central risk-management idea is that team HP carries between battles within the same Crypt run. The player must decide when to spend healing resources and which route to take.

The exact treatment of Mana between rooms, KO, revives, recovery rooms and consumable limits needs final rules. Do not assume that a character knocked out in the Crypt is unavailable to the player in every other game mode.

A Crypt run should not impose an excessive lockout on the player's characters outside the run.

## 5. Temporary Run Relics

The Crypt may offer temporary passive effects called **Run Relics**. They are not the same as permanent equipment Runes.

- Permanent Rune: equipped to one character in the Rune slot and retained in inventory.
- Run Relic: temporary effect for the current Crypt run; removed when the run ends.

A proposed reward choice is to present three Run Relics after selected milestones (for example, an Elite or Boss), letting the player choose one. The number of choices, rarity and stacking rules remain open.

Possible effect themes include attack, defense, healing, sustain or special encounter utility. Names and numerical effects are not finalized.

## 6. Run currency and merchant

A special temporary currency and a run-only merchant were proposed. The merchant could offer healing items, consumables, temporary effects or selected run supplies.

The currency name, acquisition, prices, shop inventory and whether any permanent rewards are available are not decided.

## 7. Outcomes

Possible outcomes:
- Victory: clear the final objective and receive the run's rewards.
- Defeat: the team can no longer continue under the run's defeat rules.
- Escape: the player chooses to leave early, with rewards resolved under an explicit escape rule.

Partial rewards after defeat or escape were discussed as possibilities, not confirmed guarantees.

## 8. Difficulty and encounter variety

Difficulty should change enemy composition, mechanics and risk—not just inflate HP. Elite enemies and bosses should have recognizable patterns and readable status effects.

## 9. Discord interaction design

The Crypt should feel like a compact adventure interface:
- One main map/status message.
- Buttons or a select menu for connected paths.
- Room detail and encounter messages.
- A clear team HP display.
- A concise inventory/temporary relic view.
- Edited messages rather than repeated channel spam.

Private or ephemeral responses may be used for player-specific choices when appropriate.

## 10. Persistence and safety

Persist the current run after each meaningful choice, room transition, battle action and reward. A run must survive a bot restart. Use a unique run ID and ensure a room reward can only be claimed once.

## 11. Reference links

- [Mortal Kombat official site](https://www.mortalkombat.com/)
- [Slay the Spire official site](https://www.megacrit.com/)

The references explain inspiration only; do not reproduce their maps, text, artwork, names or exact reward content.

## 12. Crypt map visual example

![Hollow Crypt branching map](assets/hollow-crypt-map.svg)

The sample map demonstrates connected room choices only. Actual map size, room distribution, run length, reward values and transition rules remain open until approved.


## Raster map preview

![Hollow Crypt branching map concept](assets/hollow-crypt-map.png)

This PNG is the visual route example. The path layout is illustrative; generation rules, map size, room frequencies and reward tables remain open decisions.
