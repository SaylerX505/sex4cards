# The Hollow Realms — Experimental Single-Player Card RPG

> **Status: Experimental design proposal — not canonical and not approved for merge.**
>
> This proposal lives only on the separate feature branch. It does not replace the existing game design on the reference branch named readme.md, and it does not modify main. All combat numbers below are prototype hypotheses until playtested.

## 1. Executive decision

Build a **single-player dark-gothic roguelike deck-building RPG played through a Discord bot using Components V2**.

Each inspiration has a distinct job:

- **Pokétwo / collection bots:** discoverable encounters, a satisfying archive, character/card collection, filters and personal goals.
- **Slay the Spire:** branching runs, card rewards, deck refinement, relics, elites, events and bosses.
- **Persona:** exploit enemy weaknesses, create openings, hand initiative to a different team member, and finish with a coordinated signature action.
- **Balatro:** recognize card patterns, shape a deck around synergies, and use passive items that change rules instead of only adding stats.
- **Discord Components V2:** an interactive message interface made from Containers, Sections, Text Displays, Media Galleries, Selects and Buttons.

These are design references, not content to copy. The game must have original characters, setting, lore, art, card language, terminology and presentation.

### Firm scope decision: single-player only

This is not an online multiplayer RPG.

- No PvP, duels, co-op, parties of human players, guild wars, shared raids, player trading or shared market.
- No battle that requires another Discord member to be present.
- Every player has an isolated save, roster, collection, run, inventory and progression.
- A player controls all three members of their own team.
- A public server may host bot announcements or opt-in personal encounter prompts, but each player's actual encounter and battle are their own private instance.
- Discord and the bot still require an internet connection. Single-player means no player-versus-player or cooperative gameplay; it does not mean an offline desktop game.

This avoids designing around population, time zones, matchmaking, opponent availability or cross-player balance.

## 2. Design pillars

1. **Every turn is a tactical puzzle.** Enemy intention, target, danger and weaknesses are readable before the player commits.
2. **The three characters must matter.** Each has a distinct personal deck and contribution; no member should feel like a replaceable stat stick.
3. **Combos must emerge from play.** Weakness → Opening → Relay → Pattern → payoff is the signature loop.
4. **Builds change rules, not just numbers.** Relics and card transformations should create different decisions and routes.
5. **Runs are temporary; discovery is permanent.** A run deck resets, while the collection, unlocks, mastery and cosmetic archive persist.
6. **Discord interaction should feel native.** A command opens a compact V2 interface; buttons and selects update the existing game screen rather than flooding the channel.
7. **Clarity before spectacle.** Art and effects must never obscure costs, intent, targets, status or the result of a choice.
8. **No required grind and no pay-to-win.** Permanent unlocks expand strategic options; they should not create an uncrossable raw-stat gap.

## 3. Player loop

### Long-term loop

1. Open the bot and view the personal Hub.
2. Inspect the Archive, collection, character mastery and available objectives.
3. Choose exactly three owned characters.
4. Choose a starting loadout and begin an Expedition.
5. Navigate a branching route, fight encounters and adapt the temporary deck.
6. Defeat the region boss or end the run through defeat/retreat.
7. Receive permanent progression, unlocks and a run report.
8. Change the team or build and begin another Expedition.

### Moment-to-moment loop

**Read the enemy → choose cards → exploit a weakness → Relay to another member → complete a Pattern → resolve the enemy phase → adapt.**

The player should make a meaningful choice in most turns. The design must not force the player to perform a long calculation before playing a card.

### Provisional command map

| Command | Purpose |
|---|---|
| /start | Create the player's save and run onboarding |
| /hub | Open the personal V2 home screen |
| /profile | View stats, achievements and personal bests |
| /archive | Browse permanent characters, cards, relics and Bestiary |
| /team | Select and arrange the three-member team |
| /deck | Inspect selected starting decks and card library |
| /expedition | Start or resume a personal run |
| /battle | Reopen the current battleboard |
| /quests | View personal daily, weekly and chapter objectives |
| /settings | Privacy, notifications, accessibility and display options |

Commands are entry points, not the whole UI. Most navigation happens through V2 components.

## 4. Three-member team

The player fields exactly **three characters**. Every character has:

- A personal deck and a clear mechanical identity.
- A passive ability that changes decisions rather than simply increasing a stat.
- Signature cards and unlockable variants.
- One distinctive Crescendo / Ultimate action.
- HP, defensive properties, affinities and status interactions.
- A mastery track that unlocks options, not unlimited raw power.

### Provisional role directions

These are mechanical archetypes, not final names, character identities or rigid classes.

| Role direction | Natural strengths | Intended weaknesses |
|---|---|---|
| Aggressor | Direct pressure, multi-hit attacks, armor and Stability damage, finishers | Needs protection and can struggle when the enemy denies attack windows |
| Occultist | Sigils, status effects, weakness setup, draw/discard manipulation | Lower immediate durability; setup can be punished |
| Warden | Guard, counters, interrupts, protection and retaliation | Lower early burst; needs the other members to convert defense into pressure |

Characters should have multiple card branches so a role does not lock a character into one build. Team composition is strategic, but no one character should be mandatory for all content.

## 5. Card and deck model

### Prototype baseline — test values, not final balance

| Element | Starting hypothesis |
|---|---:|
| Team members | 3 |
| Starting cards per member | 8 |
| Starting cards across team | 24 |
| Cards drawn per member each team turn | 2 |
| Starting hand | 6 cards total |
| Shared Action Points (AP) | 3 per team turn |
| Normal cards committed per turn | Up to 4 |
| Reaction slots | 1 |
| Base active Relic slots | 3 |
| Rank range | 1–9 |
| Starting Sigils | 4 |

Each card belongs to one of the three members. The hand is shared for player decision-making, but a card retains its owner, character identity and personal discard pile.

### Turn and draw flow

- At the start of the team turn, draw two cards from each character's personal deck.
- The resulting six-card hand is visible together, with a clear owner marker on every card.
- AP is shared. Playing a card for one member leaves fewer AP for the other members.
- A normal team turn may commit up to four cards, including zero-cost cards. Reaction setup is separate and still has its own cost.
- Played cards go to their owner's discard pile. When a personal draw pile is empty, shuffle that member's discard pile when the next draw is needed.
- The game must never silently delete a card or reshuffle a deck in a way that changes a result after the player commits.
- The player may end the planning phase early; unspent AP is not automatically converted into damage.
- Card effects, AP cost, Rank, Sigil, owner, target rules and critical tags must be visible before play.

### Card fields

| Field | Meaning |
|---|---|
| Owner | Character whose deck contains the card |
| Rank | Pattern-building value, initially 1–9 |
| Sigil | One of the four magical suits |
| Type | Attack, Guard, Hex, Setup, Control, Reaction or Support |
| AP cost | Shared team action cost |
| Target | Self, ally, one enemy, all enemies or conditional target |
| Effect | Exact gameplay effect and timing |
| Tags | Keywords used by relics, bosses and card synergies |
| Upgrade | Optional improved effect or changed rule |

Avoid a separate Force score in the first prototype. It adds arithmetic without yet proving that it creates better decisions.

### Four initial Sigils

| Sigil | Gameplay identity | Typical effects |
|---|---|---|
| ASH | Pressure and burst | Direct attacks, Burn, explosions, armor pressure |
| THORN | Attrition and exchange | Bleed, drain, sacrifice, damage over time |
| VEIL | Tempo and manipulation | Draw, discard, concealment, disruption, status control |
| GRAVE | Defense and punishment | Guard, counters, weakening, interruption, endurance |

Sigils are original working names. They can influence card patterns and enemy affinities, but a matching Sigil does not automatically mean that an enemy is weak to it.

## 6. Combat engine

### 6.1 Enemy Intentions

At the beginning of the planning phase, each visible enemy displays its next intended action.

Examples:

- Single-target strike: target and estimated damage band.
- Team-wide attack: area marker and estimated danger.
- Charge: a stronger future attack with a visible wind-up.
- Guard: the enemy prepares defense.
- Summon: the enemy intends to add another threat.
- Hex: the enemy attempts to apply a status or disrupt a character.

Intent must communicate enough for a reasoned choice without exposing every hidden boss rule. An enemy changing intent must show the updated intent before the player commits, unless a deliberately telegraphed boss effect says otherwise.

### 6.2 Weakness, Stability and Opening

Every ordinary enemy has affinities, weaknesses and a **Stability** threshold.

- A card that exploits a weakness deals its normal effect and adds Break progress.
- When Stability is depleted, the enemy becomes **Exposed** for a defined window.
- Exposed creates a tactical Opening and enables a Relay to another character.
- Ordinary enemies may be interrupted or exposed; bosses use a separate **Stagger** track and phase rules so they cannot be permanently stun-locked.
- Status and resistance rules must define duration, stacking, refresh and immunity precisely.

Weakness should change what the player can do next, not merely add a small damage percentage.

### 6.3 Relay / Handoff

Relay is the team's signature initiative mechanic.

- A successful Opening creates a Relay opportunity.
- The player can pass the advantage to a different member.
- The next eligible card from that different member receives a limited benefit, such as a one-AP discount (minimum cost zero) and a small Resonance gain.
- A Relay does not refund AP, grant a free extra turn or automatically create another Opening.
- Initial safety limits: no more than two Relays in a team turn; an enemy can generate at most one Relay Opening per turn; a Relay-enhanced card cannot recursively retrigger the same chain.
- The exact discount and Resonance gain are balance variables.

This captures the feeling of tactical handoff without reproducing franchise-specific names, animations or presentation.

### 6.4 Reactions

The player may arm at most one Reaction during the planning phase.

- The Reaction is selected from an eligible card in hand.
- Its AP cost is paid when it is armed; it occupies the Reaction slot and leaves the normal hand.
- It triggers only if its written condition matches the enemy's resolving action.
- A successful Reaction resolves in the enemy phase and goes to its owner's discard pile.
- If the trigger never occurs, the Reaction fizzles at the end of the enemy phase and the card is discarded; AP is not refunded.
- The UI must display the trigger condition and the risk before arming it.

Example reaction types: Parry, Intercept, Dodge, Interrupt, Trap. The first prototype should ship with only a small number.

### 6.5 Patterns — the Balatro-inspired layer

Patterns are detected from the cards committed in the current team turn. They add a specific tactical effect; they are **not** a general damage-multiplier spreadsheet.

Initial patterns:

| Pattern | Prototype recognition | Tactical payoff |
|---|---|---|
| Pair | Two committed cards share a Rank | Echo a limited secondary effect from one of the pair; never repeat full card damage |
| Sequence | Three cards have consecutive Ranks | Gain Momentum: a limited benefit to the next different-member card, not an AP refund loop |
| Flush | Three or more cards share a Sigil | Trigger that Sigil's Ritual effect (ASH pressure, THORN attrition, VEIL tempo, GRAVE defense) |
| Trinity | The committed set includes a card from all three team members | Team-wide Guard and Resonance |

Rules to preserve readability:

- Base card effects resolve normally in the player's selected order.
- A turn can activate **one Pattern payoff** in the first prototype. If more than one is valid, show the eligible choices and their exact previews; the player chooses one.
- No hidden best-pattern scoring.
- Patterns do not stack unrestricted multipliers.
- A Relic may alter how one Pattern works, but must not silently activate unlimited secondary Patterns.
- Later patterns such as Three of a Kind or Full House are added only if the four base Patterns are already fun and readable.

The first prototype should compare two UX options: automatic best-pattern selection with a preview, versus explicit player selection when multiple Patterns are valid.

### 6.6 Resonance and Team Crescendo

Use one shared team Resonance meter, initially 0–100.

Resonance can be generated by successful weakness exploitation and Openings, Relays, Pattern completion and correctly timed Reactions.

At 100, the player can spend the meter to trigger **Team Crescendo** and select one member's unique signature action. One shared meter avoids managing three separate Ultimate currencies. The chosen member and the current enemy phase determine the best payoff.

Resonance must have a cap and clear event log. Overfill, refunds and recursive generation are disabled in the first prototype.

### 6.7 Enemy phase and resolution order

1. Show enemy intentions and draw the team hand.
2. Player commits up to four normal cards and optionally arms one Reaction.
3. Preview and choose one eligible Pattern payoff.
4. Resolve normal card effects in the selected order.
5. Resolve Opening and Relay windows as they occur.
6. Resolve the enemy phase in the displayed priority order.
7. Trigger armed Reactions at the relevant point in that phase.
8. Apply end-of-turn statuses, cooldowns and intent updates.
9. Start the next team turn.

Order is part of the game rules. It must be deterministic and visible in the battle log.

## 7. Relics and build identity

Relics should change rules, incentives or card interactions, rather than provide only flat damage percentages.

- The prototype starts with eight candidate Relics and three active slots.
- Relic effects must state trigger, timing, limit, stacking behavior and interaction with other effects.
- Relics should create a cost or trade-off when they are especially powerful.
- A run may offer more Relics than the player can equip, making replacement a meaningful decision.
- Do not permit an unlimited number of independent multipliers.

Illustrative concepts (names and exact values are not final):

| Relic concept | Rule change | Trade-off / limit |
|---|---|---|
| Bent Metronome | Rank 1 and Rank 9 can be adjacent for Sequence detection | Applies only to one Sequence per turn |
| Choir of Teeth | A Pair can Echo a card's secondary rider | Echo cannot repeat damage, AP refunds or Resonance generation |
| Black Glass | A Reaction card contributes its Sigil to a Pattern | Armed Reaction costs one extra AP |
| Mourning Clock | First zero-cost card each turn gains a stronger rider | Draw one fewer card next turn |
| Fractured Halo | Trinity grants extra Guard and a small character buff | No extra Resonance from the same Trinity |
| Ashen Compass | First ASH Ritual can damage armor before HP | Less effective against unarmored enemies |

Relics must offer choices between different builds, not one best-in-slot build.

## 8. Roguelike Expeditions

Each Expedition is a temporary run with branching routes, encounters and a region boss.

| Node | Purpose |
|---|---|
| Battle | Standard tactical encounter and reward |
| Elite | A stronger test with a higher-value reward |
| Event | Risk/reward decision, strange NPC, curse, bargain or discovery |
| Merchant | Buy, remove, upgrade or transform a card |
| Forge | Upgrade, alter Rank/Sigil, duplicate or remove a card |
| Shrine | Powerful effect with a clear cost |
| Rest | Recover the team or take a limited improvement |
| Treasure | High-value reward with a condition |
| Boss | Multi-phase test of the current build |

The proposed full run has three distinct acts/regions. Each act changes enemy pools, visual identity, event pool and boss rule. The first prototype should use one short route and one boss before committing to full run length.

After encounters, offer a small set of mutually exclusive choices: add a card, upgrade or transform a card, remove a weak card, take resources or skip the reward. Skipping is a real option. Adding more cards is not automatically good; deck consistency matters.

Bosses should change the problem, not simply multiply HP. Example concepts: punishing repeated Ranks, rotating weakness after a visible phase transition, echoing the last Sigil, adding a visible Curse, or rewarding defensive Patterns while punishing burst. Every boss rule must be telegraphed and have counterplay.

## 9. Permanent Archive versus temporary Run Deck

### Permanent Archive

- Unlocked characters and character variants.
- Permanent card library and card mastery.
- Bestiary and discovered enemy affinities.
- Relic archive (knowledge/unlocks, not necessarily ownership of a run Relic).
- Achievements, titles, profile frames and cosmetic effects.
- Chapter/story progress and personal best records.

### Temporary Expedition state

- Selected team.
- Active starting decks.
- Cards added, upgraded, transformed, cursed or removed during the run.
- Run-only Relics.
- Current HP, statuses, route, resources and boss phase.

On a run end, temporary modifications reset under a clearly documented rule. The player keeps permanent unlocks and the expedition report.

Permanent progression should broaden the player's options. Avoid an endless raw-stat ladder that makes a player's first unlocked characters obsolete.

## 10. Collection, encounters and optional idle progression

Take the satisfying discovery rhythm of collection bots, but remove the competitive race to claim a shared rare item.

- Add a personal **Rift Encounter** flow: a server announcement or user command can invite a player to investigate, but clicking opens an isolated personal instance.
- The encounter may offer a creature to record in the Bestiary, a character memory, a card blueprint, an artifact fragment or a battle.
- No first-click winner, public loot race, trading or player market.
- Use /archive with filters, tags, variants, completion progress and a wishlist.
- Quests should ask players to try different mechanics, not repeat one tedious action thousands of times.
- Optional Dispatch missions can resolve over time for low-impact resources, but must not replace active combat or create an energy gate. They are solo background progression, not an online activity.

Collection rewards should have deterministic unlock paths. If random packs are ever introduced, disclose odds, add duplicate protection/pity, provide an earnable path to target unlocks, and never sell combat power.

## 11. Single-player economy and progression

Start with a small economy, not five currencies.

- One common account-bound currency for ordinary shops, repairs and card services.
- One rare account-bound crafting material for high-value permanent unlocks.
- Run-only temporary resources remain inside the Expedition and are discarded at its end.

No player-to-player transfer, market, trade, wagers or gambling. No server-wide wealth pool.

Quest cadence should be gentle: a small personal daily set with optional objectives; weekly/long-form challenges that reward experimenting with different Sigils, Patterns or characters; chapter milestones that unlock new cards, encounters and archive entries; cosmetic and mastery goals for completionists.

Do not punish players for missing days. Avoid streak systems that turn the game into an obligation.

## 12. Components V2 interface — bot-first

The bot is the client. The backend owns game rules and persisted state. The primary screens should use Discord Components V2 from the start.

### Main screens

| Screen | Primary V2 elements |
|---|---|
| Hub | Container, Text Display, Section, thumbnail, action rows |
| Character archive | Section cards, Media Gallery, filters and String Select |
| Team builder | Character sections, role/slot selects, confirm button |
| Deck viewer | Compact card rows/sections, page navigation, filters |
| Battleboard | Boss/arena art, enemy intent, three character status sections, AP/Resonance, card controls and Reaction slot |
| Route map | Text route summary, node buttons, current-path emphasis |
| Reward choice | One section per option with select/confirm controls |
| Profile | Summary, achievements and archive links |

### Battleboard rules

- One primary battleboard message per player battle.
- Update that message after card selection or phase resolution rather than posting a new message for every action.
- Keep the enemy's next intent and target clearly visible above the hand.
- Show three compact character status blocks, then AP and Resonance.
- The player selects a card, then a target when needed; avoid one button per possible card/target combination.
- Use pagination or Select Menus for larger card inventories.
- Use a Modal only for free text or a multi-field setup; do not use a modal for every card play.
- Keep each screen comfortably below Discord's 40-component message maximum. Treat 20–25 components as a soft design ceiling, not a target to fill.
- Provide an accessible text fallback when an image fails.

### Interaction and persistence rules

- Acknowledge interactions within Discord's deadline and defer when game processing cannot finish immediately.
- Do not use an interaction token as long-term session storage. A token's lifetime is limited; the battle state lives in the database.
- Validate that the interacting Discord user owns the save and that the session is in the expected phase.
- Use opaque, compact custom IDs with an action and version/session reference. Never put trusted prices, damage, AP totals or game state only inside the client-supplied custom ID.
- Use optimistic version checks and idempotency keys so double-clicks, stale buttons and concurrent interactions cannot duplicate rewards or play a card twice.
- After a stale interaction, refresh the screen with a clear “this view has changed” response.
- Persist after each committed action; a disconnect or bot restart must not delete an Expedition.
- Do not expose private inventory, collection, save details or battle choices to other server members by default.

Components V2 is a message layout system, not a custom game canvas or a full real-time game engine. It can deliver a polished turn-based RPG interface, but it cannot provide unrestricted drag-and-drop or continuous battlefield animation. The design should embrace clear button/select interactions and card artwork. A Discord Activity is not required for the core game.

## 13. Visual and audio identity

- Premium high-detail pixel art, not low-detail retro placeholders.
- Dark fantasy, emo, gothic, surreal and occasionally strange/whimsical; never childish.
- Palette direction: charcoal, muted violet, bone white, restrained crimson and sickly green.
- Character silhouettes, enemy intent icons and card type/color need strong contrast at small Discord display sizes.
- Cards should look like occult artifacts with worn materials, dark metal, unusual marks and controlled highlights.
- Visual feedback should emphasize Opening, Relay, Pattern, Reaction, Crescendo and boss phase changes.
- Do not use visual effects that hide rules or enemy intent.
- Music direction may be darkwave, industrial ambience, mournful piano and distant choir textures. Use original or properly licensed audio only.

## 14. Prototype plan and acceptance tests

### Prototype scope

- Three original placeholder characters with distinctly different passive and card identities.
- Eight starting cards for each character (24 total).
- Four Sigils and four basic Patterns.
- Three shared AP, six-card starting hand and four-card commit cap.
- One Reaction slot and two-Relay maximum.
- Enemy intents, weaknesses, Stability/Opening, boss Stagger and one Team Crescendo.
- Eight candidate Relics, three active slots.
- Three normal enemy designs, one Elite and one multi-phase Boss.
- One short branching Expedition route.
- Components V2 Hub, Battleboard, Archive, Deck view and Reward screen.
- Durable save/resume and combat event log.

### Playtest questions

1. Does the player understand the hand, AP and enemy intent in under a few seconds?
2. Does every character matter in most fights without forcing all three cards every turn?
3. Does the six-card hand feel like choice or overload?
4. Does the three-AP economy create tension without making most cards unplayable?
5. Are Patterns noticed and deliberately built, or do players ignore them?
6. Does one-pattern-per-turn prevent arithmetic overload while keeping the Balatro-like excitement?
7. Does Relay create a satisfying handoff without infinite action loops?
8. Is the Reaction decision worth its AP and card slot?
9. Do Relics create distinct runs rather than a universal strongest combo?
10. Can the player recover from bad draws through skill and build choices without making randomness meaningless?
11. Does the V2 interface remain readable on desktop and mobile?
12. Can a player resume a long run after the original interaction token has expired or the bot has restarted?

### Metrics

Track average turn duration, cards played per turn, unused AP, hand ownership distribution, Pattern frequency, Pattern choice frequency, Opening and Relay frequency, Reaction trigger/fizzle rate, Resonance generated/spent, damage/mitigation by source, ultimate timing, card skip/remove rates, build win rates, run abandonment points, stale-interaction rate and command-to-action completion.

Balance around decision variety, clarity, consistency, survivability and completion rate—not maximum damage alone.

## 15. Risks and safeguards

| Risk | Safeguard |
|---|---|
| Too many mechanics make each turn slow | Keep only four Patterns, one Reaction and one shared meter in the first test |
| One character becomes mandatory | Test multiple successful team compositions and card branches |
| Pattern math becomes opaque | No universal Force × multiplier formula; show one explicit Pattern payoff |
| Infinite Relay loops | Hard limits, no AP refunds, no recursive triggers |
| Random draw creates dead turns | Character-balanced draw, low-cost options, controlled draw tools and transparent discard rules |
| Boss rules invalidate a build | Telegraph phases and offer counterplay |
| Relics converge on one meta | Trade-offs, limited slots and archetype win-rate tests |
| Collection becomes grind/pay-to-win | Deterministic unlock path, cosmetics and options rather than raw-stat superiority |
| Discord becomes message spam | Edit one battleboard; use private solo screens and short logs |
| Stale or replayed interactions duplicate effects | Server-side validation, version checks and idempotent commits |
| Player privacy is poor | Private-by-default personal screens and explicit opt-in announcements |

## 16. Research and implementation references

- Bot research and comparative takeaways: [DISCORD_GAME_BOT_RESEARCH.md](DISCORD_GAME_BOT_RESEARCH.md)
- Components V2 and backend design: [DISCORD_COMPONENTS_V2_ARCHITECTURE.md](DISCORD_COMPONENTS_V2_ARCHITECTURE.md)

### Official platform references

- [Discord Components Overview](https://discord.com/developers/docs/components/overview)
- [Discord Components Reference](https://discord.com/developers/docs/components/reference)
- [Discord Receiving and Responding to Interactions](https://discord.com/developers/docs/interactions/receiving-and-responding)

## 17. Branch and approval boundary

- This is an experimental alternative design on feature/card-battle-gameplay.
- The canonical reference branch named readme.md remains untouched.
- main remains untouched.
- Existing canonical combat, Auto Hunt, Hollow Crypt, equipment, character and collection specifications are not rewritten by this proposal.
- No merge or replacement of canonical documents is implied.
- Promotion requires a playable prototype, balance review and explicit approval of which canonical systems (if any) should be replaced, adapted or retained.
