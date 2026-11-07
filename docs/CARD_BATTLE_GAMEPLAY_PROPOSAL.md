# Experimental Card-Battle Gameplay Proposal

> **Status: Experimental proposal — not approved as the canonical game design.**
>
> This document describes an alternative gameplay direction for a separate feature branch. It does not replace the current turn-based combat, Auto Hunt, Hollow Crypt, equipment, character, or collection specifications on the reference `readme.md` branch. Do not merge this proposal into the canonical design without explicit approval.

## 1. High concept

Build a **dark-gothic, surreal roguelike deck-building RPG** that combines three complementary gameplay strengths:

- **Persona-style tactical combat:** enemy weaknesses, readable intentions, knockdowns/openings, turn handoffs, team attacks, and charged signature abilities.
- **Slay the Spire-style run structure:** branching routes, encounter choices, card rewards, deck refinement, relics, elites, events, shops, and bosses.
- **Balatro-style card synergy:** ranks, magical suits/sigils, pattern recognition, scoring, multipliers, rule-changing passive items, and surprising build combinations.

The game must not feel like three systems bolted together. Each influence has a clear job, while the game's own identity comes from one central interaction:

**Exploit an enemy opening → hand the advantage to another team member → assemble a card pattern → amplify its effect through synergies → finish with a coordinated action.**

The result should reward planning and experimentation without turning every turn into a long arithmetic exercise.

### Design pillars

1. **Tactical clarity:** players can understand enemy intent, weaknesses, costs, and likely consequences before committing.
2. **Expressive deck-building:** a run can develop into meaningfully different play styles rather than a small numerical upgrade to the same strategy.
3. **Three-member cooperation:** each team member has a distinct card identity, but the most exciting patterns reward mixing their cards.
4. **Readable spectacle:** successful patterns and team chains should feel powerful and visually satisfying.
5. **Run-to-run discovery:** route choices, rewards, relic combinations, and boss rules should create new problems to solve.
6. **Dark, strange atmosphere:** gothic, emo, surreal, eerie and occasionally whimsical; never childish or generic high-fantasy.

## 2. Inspiration boundaries

Use mechanics as design inspiration, not protected expression.

| Inspiration | Gameplay principles to adapt |
|---|---|
| Persona series | Weakness exploitation, knockdowns/openings, turn handoffs, coordinated attacks, charged signature abilities, tactical enemy intent |
| Slay the Spire | Deck-building, branching run map, card rewards, deck thinning, upgrades, relics, elite encounters, events, bosses |
| Balatro | Rank/suit patterns, hand recognition, score and multiplier interactions, passive rule-changing items, build-defining synergies |

Do **not** copy characters, storylines, dialogue, settings, names, logos, card frames, artwork, symbols, music, UI layouts, or other franchise-specific expression from these games. The roster, world, terminology, visual assets, lore, and presentation must be original or separately rights-cleared.

The scope of this document is gameplay systems. It does not decide the cast, story, character identities, or narrative canon.

## 3. Three-member team and character decks

The player fields exactly **three team members**. Each member owns a distinct deck and mechanical identity.

### Initial prototype structure

| Element | Prototype target |
|---|---:|
| Team size | 3 members |
| Starting cards per member | 8 |
| Cards drawn per member each team turn | 2 |
| Starting hand size | 6 total |
| Shared Action Points (AP) | 3 per team turn |
| Maximum cards committed in one turn | 5 |
| Reaction slots | 1 reserved card |
| Maximum Handoffs | 2 per team turn |
| Ultimate / Awakening | 1 personal gauge per member |

These are **test values, not final balance commitments**. Playtesting may change them.

### Deck and hand flow

- Each member begins with a personal deck of eight cards in the first prototype.
- At the start of the team turn, draw two cards from each member's deck to create a six-card shared hand.
- Cards remain visibly associated with their owner; the hand is shared for decision-making, not ownership.
- The player may play cards from any member in any order, provided the card's cost and conditions are met.
- AP is shared across the whole team. Spending AP on one member means less AP is available to the other two.
- Played cards go to their owner's discard pile. When a personal draw pile is empty, shuffle that member's discard pile to form a new draw pile.
- A card cannot be played more than once in the same turn unless a card or relic explicitly permits it.
- The five-card commitment limit prevents long chains from overwhelming the turn structure. Free or zero-cost cards still count toward this card limit.
- The exact draw timing, reshuffle rules, hand limit, and discard behavior should be validated in the prototype.

### Character identity

The three members should have different mechanical roles, but roles must not become rigid classes. A member can support more than one build through card choices.

Illustrative role directions:

- **Aggressor:** direct attacks, armor breaks, multi-hit sequences, finishers.
- **Manipulator:** elemental or occult effects, weakness exploitation, status application, draw and discard control.
- **Controller:** defense, counters, interrupts, protection, enemy manipulation.

These are role examples only. They do not define characters or story.

## 4. Card model: Rank, Sigil, Force, Type and Effect

Each card should expose a compact set of properties that support both tactical readability and pattern building.

| Property | Purpose |
|---|---|
| Rank | A value used to form patterns; prototype range 1–9 |
| Sigil | A magical suit used for matching and enemy affinity; four initial sigils |
| Force | The card's base contribution to Resonance scoring |
| Type | Attack, Defense, Magic, Control, Reaction, or another approved category |
| AP cost | Shared team resource required to play the card |
| Owner | Which team member's deck contains the card |
| Effect | The card's tactical behavior, conditions, target rules, and status effects |
| Tags | Optional keywords used by relics, enemies, and card synergies |

A card must be understandable before play. Put its main effect, AP cost, Rank, Sigil, and owner in the primary card view; move advanced tags or explanatory details into secondary UI.

### Four starting Sigils

The following are working names and identities for the prototype. They are original working terminology, not final lore.

| Sigil | Primary gameplay identity | Example effects |
|---|---|---|
| **ASH** | Aggression and burst | Direct damage, burn, explosions, pressure |
| **THORN** | Attrition and exchange | Bleed, life drain, sacrifice, damage over time |
| **VEIL** | Manipulation and tempo | Draw, concealment, discard control, enemy disruption |
| **GRAVE** | Defense and punishment | Guard, counter, mitigation, weakening, endurance |

Sigils also provide a readable affinity language for enemy weaknesses and resistances. However, a Sigil match should not automatically guarantee a weakness: enemy intent, armor, phase, or a special rule may change the best answer.

## 5. Resonance: the central card-pattern system

Resonance is the primary bridge between Balatro-style card patterns and tactical RPG effects.

When the player commits a sequence of cards, the game checks the selected cards for valid Rank and Sigil patterns. A detected pattern generates a **Resonance result** that amplifies the sequence's payoff.

### Prototype scoring model

`Resonance Score = Total Force × Pattern Multiplier`

- **Total Force** is the sum of the Force values on the committed cards.
- **Pattern Multiplier** comes from the strongest valid pattern, with possible bonuses from relics, card effects, weaknesses, and team synergies.
- The score is then converted into a tactical payoff based on the finisher card or the selected resolution mode.

The score should not become an unexplained extra damage number. The interface must show which cards formed the pattern, which multiplier applied, and what the resulting payoff will be before the player commits whenever practical.

### Initial pattern set

| Pattern | Recognition rule | Example payoff direction |
|---|---|---|
| Pair | Two cards with the same Rank | Repeat or strengthen part of one effect |
| Two Pair | Two separate matching-Rank pairs | Small offensive and defensive bonus |
| Three of a Kind | Three cards with the same Rank | Strong Multiplier |
| Sequence | Three or more consecutive Ranks | Tempo bonus, card draw, or Handoff support |
| Flush | Three or more cards with the same Sigil | Sigil-specific Ritual effect |
| Full House | Three of one Rank plus a Pair | Coordinated team attack or compound effect |
| Four of a Kind | Four cards with the same Rank | High-impact burst effect |

The thresholds above deliberately adapt poker-like patterns for a six-card tactical hand and a maximum five-card commitment. They are prototype rules, not a promise to reproduce standard poker scoring.

### How a pattern resolves

The prototype should use a clear resolution rule:

1. The player chooses up to five cards and pays their combined AP cost.
2. The game identifies the strongest valid pattern among the committed cards.
3. Individual card effects resolve in the selected order, subject to their own conditions.
4. The pattern generates a Resonance payoff.
5. The final committed card, called the **Finisher**, determines the payoff channel:
   - Attack finisher: convert Resonance into additional damage or a strike effect.
   - Defense finisher: convert Resonance into Guard, mitigation, or a protective effect.
   - Control finisher: convert Resonance into control potency, status duration, draw, or disruption.
6. Relics and other modifiers are applied in a documented order.

This makes the pattern matter without making every card do the same thing. A player can deliberately end with an Attack, Defense, or Control card to direct the pattern's reward.

### Anti-complexity rules

- Show the best detected pattern and projected payoff before confirmation.
- Avoid hidden scoring rules.
- Keep the first prototype to a small number of pattern types and modifiers.
- Avoid stacking several independent multipliers without clear ordering.
- Add advanced patterns only when the basic patterns are already fun and readable.
- Balance pattern value against card cost, card count, and the opportunity cost of delaying an action.

## 6. Tactical combat: Openings, Weaknesses and Handoffs

Combat combines card selection with enemy-state reading. Enemies should communicate what they are about to do and how the player can disrupt them.

### Enemy intent

Before the enemy phase, show a readable intent for each relevant enemy, such as:

- Heavy single-target attack.
- Team-wide attack.
- Spell or special ability.
- Guard or reinforcement.
- Charge-up for a future high-impact action.
- Status effect or attempt to disrupt a team member.

Intent descriptions should communicate target, approximate severity, and any unusual condition. They should not reveal hidden boss mechanics that are intended to be discovered.

### Weakness and Opening

- Enemies have affinities: weaknesses, resistances, and sometimes neutral Sigils.
- Hitting a weakness can apply **Exposed** or **Downed**, depending on enemy type.
- A successful weakness exploit opens a limited opportunity called an **Opening**.
- An Opening gives the team a chance to transfer initiative to another member.
- Bosses may resist ordinary knockdowns and use a Stagger meter or phase-specific openings instead.

A weakness should matter tactically, not only add a small damage bonus. It should change what the player can do next.

### Handoff

Handoff transfers the current advantage to a different team member.

Prototype rules:

- A Handoff is unlocked by a successful Opening or by a specific card/relic effect.
- The next eligible card played by a different member receives a temporary discount and/or a Resonance bonus.
- A Handoff can help complete a cross-member pattern.
- Limit Handoffs to two per team turn in the initial prototype.
- Handoffs do not refund all AP or create an unlimited action loop.

The purpose is to make the team feel coordinated while preserving meaningful resource decisions.

### Team attack: Rupture

When all eligible ordinary enemies are Downed or Exposed at the same time, the player may trigger **Rupture**, a coordinated team attack.

Rupture should:

- Provide a satisfying payoff for setting up multiple weaknesses.
- Consume or close the active Openings.
- Resolve through a clear animation and combat log.
- Scale through team synergy and selected cards, not only a fixed percentage.
- Be unavailable or modified against bosses that use Stagger phases instead of ordinary knockdowns.

### Reactions

At the end of the team's planning phase, the player may reserve one eligible Reaction card in a dedicated slot.

- A Reaction triggers only when its stated condition occurs.
- Examples include Counter, Dodge, Guard, Interrupt, or redirecting an attack.
- The player sees the trigger condition before reserving it.
- A Reaction may have a cost or consume a limited resource, as defined by that card.
- Unused Reactions should not automatically become free value; their opportunity cost must be clear.

This gives the player a meaningful way to plan around enemy intent outside the normal card-play sequence.

### Ultimate / Awakening abilities

Each team member has a personal Awakening gauge, charged by behavior aligned with that member's identity.

Examples:

- Aggressor gains charge from exploiting weaknesses or landing multi-hit attacks.
- Manipulator gains charge from status effects, Sigil interactions, or pattern setup.
- Controller gains charge from protecting allies, interrupting, or countering.

When full, the member's Ultimate becomes available in a dedicated ability slot rather than relying on a random draw. This keeps the moment exciting and makes charge progression legible.

## 7. Run structure and route choices

A run is a branching journey with escalating danger and a boss at the end of each major stage.

### Suggested route nodes

| Node | Purpose |
|---|---|
| Normal Battle | Standard encounter and card/reward choice |
| Elite | High-risk encounter with a stronger relic reward |
| Event | A decision with a cost, risk, or uncertain outcome |
| Shop | Buy cards, relics, upgrades, or services |
| Forge | Upgrade, transform, duplicate, or remove a card |
| Rest | Recover health or choose a limited improvement |
| Vault | High-value reward with a price or condition |
| Boss | Test of deck construction, team synergy, and tactical understanding |

### Three-stage run structure

Three major stages are a good initial target, each with a distinct theme, encounter pool, and boss rule. This is a pacing proposal, not a fixed campaign length.

A run should alternate between combat, planning, and meaningful route decisions. Avoid long sequences of identical normal fights.

### Reward decisions

After a standard encounter, the player should usually choose one of a few offered rewards:

- Add one card to the run deck.
- Take a resource or currency reward.
- Take a card upgrade or transformation.
- Decline a card and preserve deck consistency.

The option to skip a new card is essential. More cards do not automatically make a deck stronger; removing weak cards can make a build more reliable.

### Boss rules

Bosses should change the problem the player must solve, rather than simply having more HP.

Examples:

- A boss punishes repeated use of the same Rank.
- A boss weakens Flush patterns but is vulnerable to Sequences.
- A boss echoes the last card played.
- A boss adds Cursed cards to the player's deck during combat.
- A boss changes its weakness after a telegraphed phase transition.

Boss modifiers must be learnable and counterable. Avoid arbitrary rules that invalidate a player's build without offering a response.

## 8. Relics and build-defining synergies

Relics are passive run items that alter card values, pattern rewards, turn rules, or tactical conditions. They are the main tool for making a run's build feel distinct.

The starting prototype may use **five Relic slots**, subject to playtesting. A new Relic should create a real choice: the player may need to replace an existing item rather than collect everything.

### Illustrative Relics

| Relic | Example effect |
|---|---|
| **Broken Bell** | Each completed Sequence gains an additional Multiplier. |
| **Crown of Worms** | THORN Flush patterns apply extra Bleed, but exacting a cost from the team. |
| **Cracked Mirror** | The first Pair in each battle repeats a limited portion of one card effect. |
| **Mourning Clock** | Zero-cost cards gain Force, but the team draws fewer cards at the next turn. |
| **Black Halo** | Playing at least one card from each team member in the same sequence grants a Resonance bonus. |

These are design examples, not final item names or balance values. Effects must define timing, stacking, limits, and edge cases precisely.

### Deck manipulation tools

Run rewards and services may allow players to:

- Change a card's Rank.
- Change a card's Sigil.
- Upgrade its Force or effect.
- Duplicate a card.
- Remove a weak or unwanted card.
- Remove or transform a Curse.
- Transform a card into a different card within an approved reward pool.

These tools should be scarce enough to make choices matter, but available often enough that players can pursue a build deliberately.

## 9. Build archetypes

The game should support several viable strategies. No single pattern, Sigil, or character role should dominate every encounter.

| Build direction | Core plan | Strength | Trade-off |
|---|---|---|---|
| **Ash Overload** | Build ASH patterns and burst payoffs | High immediate damage | Can be vulnerable when setup fails |
| **Thorn Drain** | Stack Bleed and recover through attrition | Strong long-fight sustain | Slower against enemies with short damage windows |
| **Veil Engine** | Draw, cycle, and assemble Sequences | Consistent setup and control | Requires careful resource management |
| **Grave Fortress** | Guard, Counter, and convert defense into payoff | Strong survival and punish windows | Lower early burst |
| **Trinity Build** | Mix cards from all three members for team bonuses | Strong cross-member coordination | Requires a balanced hand and careful timing |

These are targets for build diversity, not locked classes or exhaustive strategies. Hybrid builds should be possible.

## 10. Permanent Collection and temporary Run Deck

The progression model separates long-term collection from the temporary deck assembled during a run.

### Permanent Collection

- Players unlock and collect cards over time.
- Collection milestones introduce new strategic options and variants.
- Pre-run choices determine the starting card pool or allowed loadout.
- Permanent progression should expand options rather than provide unlimited raw-stat power.

### Temporary Run Deck

- The run begins with a selected starting setup.
- Cards, upgrades, transformations, Curses, and removals acquired during the run affect the temporary deck.
- Relic combinations and route decisions shape the build.
- At the end of the run, temporary modifications reset according to the final progression rules.

The distinction must be explicit in the UI so players understand which cards are permanently owned and which only belong to the current run.

### Long-term replayability

Potential replay systems include:

- Challenges with special run rules.
- Difficulty modifiers that change enemy behavior and reward quality.
- Rotating encounter pools.
- Optional routes with higher risk and stronger rewards.
- Collection completion goals and alternative card variants.

Avoid making permanent progression so powerful that older content becomes trivial or a failed run feels like lost time.

## 11. Visual and audio direction

The gameplay presentation should support the intended **dark, emo, gothic, surreal and slightly whimsical** atmosphere.

### Visual treatment

- Premium, high-detail pixel art rather than crude 8-bit or 16-bit styling.
- Deep charcoal and near-black foundations, muted violet, blood red, bone white, and restrained sickly green.
- Cards should feel like occult artifacts: worn materials, dark metal, strange markings, layered shadows, and controlled highlights.
- Use strong silhouettes and clear iconography so cards remain readable at small sizes.
- Pattern recognition should produce satisfying visual feedback: linked card edges, sigil resonance, rank highlights, and a distinct resolution effect.
- Enemy intent and weakness indicators must remain legible and not disappear beneath decorative effects.
- Use restrained animation to emphasize Opening, Handoff, Resonance, Rupture, Reactions, and Ultimates.

### Audio treatment

The intended direction is darkwave, industrial, gothic ambience, mournful piano, distant choir textures, and carefully designed combat impacts. Music should reinforce tension and discovery without overwhelming card and enemy-intent feedback.

This section defines tone only. It does not authorize copying existing compositions, sound recordings, visual designs, or franchise assets.

## 12. Prototype specification

Build one compact playable combat prototype before expanding the run map, collection, story, or content catalogue.

### First prototype contents

- Three mechanically distinct but unnamed team members.
- Eight starting cards in each member's personal deck.
- Four Sigils: ASH, THORN, VEIL, GRAVE.
- A small set of Rank and Sigil patterns.
- Three shared AP per team turn.
- Six drawn cards per starting hand.
- A five-card maximum commitment per turn.
- One Reaction slot.
- Weaknesses, enemy intent, Openings, and up to two Handoffs per team turn.
- One coordinated Rupture condition.
- One charged Ultimate per team member.
- A small enemy group and one boss with a telegraphed special rule.
- A handful of relics that create clearly different builds.

### Questions the prototype must answer

1. Are card patterns exciting to discover, or do they make players calculate more than they play?
2. Does a six-card shared hand offer enough choice without overwhelming the player?
3. Do three shared AP create tension without making most cards feel unusable?
4. Do Weakness and Handoff mechanics create meaningful team cooperation?
5. Can players understand how a Resonance score was produced?
6. Do Relics create genuinely different builds, or do players converge on one optimal combination?
7. Does the Reaction slot improve planning without slowing the turn too much?
8. Does the combat loop remain enjoyable against ordinary enemies after the novelty of the first encounters?

### Initial balance tests

Track at least:

- Average team-turn duration.
- Number of cards played per turn.
- AP left unused.
- Frequency of detected patterns.
- Frequency of successful Openings and Handoffs.
- Average damage and defensive value from Resonance.
- Reaction trigger rate and value.
- Ultimate charge rate.
- Win rate by build archetype.
- Number of cards added, upgraded, skipped, and removed per run.

Do not balance only around maximum damage. Consistency, survivability, decision variety, clarity, and run completion are equally important.

## 13. Risks and safeguards

| Risk | Safeguard |
|---|---|
| Too many systems compete for attention | Introduce systems in layers; keep the first prototype small |
| Pattern scoring becomes slow arithmetic | Preview patterns and payoff; make modifiers visible; limit multiplier stacking |
| One combination dominates | Test build win rates and revise patterns/relics rather than only increasing enemy HP |
| Handoffs create infinite loops | Hard limit Handoffs per turn; define once-per-turn effects and trigger order |
| Shared AP makes some members feel irrelevant | Check card cost distribution and ensure each member has useful low-cost options |
| Draw randomness creates unwinnable turns | Provide controlled draw, discard, or card-selection tools without removing uncertainty |
| Boss rules invalidate a deck | Telegraph rules and preserve at least one counterplay route |
| Collection progression becomes pay-to-win or grind-heavy | Prefer unlocks that broaden choices over permanent raw-stat inflation |
| Visual effects obscure tactics | Prioritize card text, enemy intent, targets, and state indicators over decoration |

## 14. Decisions still open

The following must remain open until a working prototype provides evidence:

- Final number of cards in each personal deck.
- Whether draw is always two cards per member or can be modified by card effects.
- Exact AP costs and whether AP resets fully each turn.
- Whether the five-card commitment limit is always active.
- Exact Rank range and whether all Ranks are equally available.
- Final pattern thresholds and pattern priority.
- Whether Resonance amplifies only the Finisher or can be divided among multiple effects.
- Whether a card can have more than one Sigil.
- Exact Weakness, Resistance, Exposed, Downed, and Stagger rules.
- Handoff discounts, limits, and trigger order.
- Reaction timing and whether reserved Reactions consume AP.
- Awakening charge rates and Ultimate cooldown behavior.
- Relic slot count, rarity, stacking, and replacement rules.
- Run length, route-node frequency, and reward economy.
- Which progression rewards persist after a run.
- Whether the game is ultimately delivered through Discord or another client; this document does not decide implementation architecture.

## 15. Status and relationship to the canonical design

This is an **experimental alternative gameplay direction**.

- It is stored on the separate `feature/card-battle-gameplay` branch.
- The canonical `readme.md` branch remains unchanged.
- The `main` branch remains unchanged.
- Existing canonical combat, Auto Hunt, Hollow Crypt, equipment, character, and collection documents are not rewritten by this proposal.
- The existing meaning of collection/detail cards remains intact in the canonical design.
- No merge, replacement of canonical docs, or implementation approval is implied.

Promotion into the main project requires explicit review of the prototype, approval of the core loop, and a deliberate decision about which existing systems would be replaced, adapted, or retained.
