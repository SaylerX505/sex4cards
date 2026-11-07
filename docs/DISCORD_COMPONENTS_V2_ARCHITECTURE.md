# Discord Components V2 — Bot and Gameplay Architecture

> **Scope:** technical proposal for the experimental single-player card RPG on feature/card-battle-gameplay. This file is not a code implementation and does not select a final language/library. Verify the target library's current V2 support before implementation.

## 1. Technical direction

Build a **Discord bot with a durable game backend**. Discord is the interactive client; it is not the source of truth for game state.

The intended experience is a turn-based RPG presented through Discord Components V2 messages. The player starts with slash commands, then navigates the Hub, Archive, Team Builder, Deck Builder, Expedition and Battleboard with buttons and select menus.

This is a single-player product:

- A Discord user owns one isolated save.
- The user controls all three characters in their own team.
- The user's Run, battle, random seed, currencies, collection and rewards are private.
- There are no player sessions, shared combat state, PvP, co-op, trading, guilds, shared raids or global markets.
- Server channels may show optional game announcements, but no gameplay reward should be won by another user clicking first.

Discord still requires internet connectivity and the bot process to be online to accept commands and interactions.

## 2. Official Discord Components V2 rules

Primary references:

- [Components Overview](https://discord.com/developers/docs/components/overview)
- [Components Reference](https://discord.com/developers/docs/components/reference)
- [Receiving and Responding to Interactions](https://discord.com/developers/docs/interactions/receiving-and-responding)

### 2.1 V2 message flag and content model

- A message that uses Components V2 must include the IS_COMPONENTS_V2 message flag (bit value 1 << 15, decimal 32768).
- With that flag, the traditional top-level message content and embeds fields no longer work as they do in legacy messages. The layout and text must be built from components such as Text Display and Container.
- Attachments do not automatically appear; they must be exposed through a supported component such as Media Gallery or File.
- Poll and sticker fields are disabled on a Components V2 message.
- Discord documents a maximum of **40 total components per message**.
- Legacy message components remain supported. V2 is the preferred direction for new interactive layouts, but the project should not mix legacy and V2 assumptions in the same screen.

Treat the 40-component maximum as a hard API ceiling, not a design target. Aim for approximately 20–25 components or fewer on normal game screens.

### 2.2 Components that matter to this game

| Component | Discord capability | Game use |
|---|---|---|
| Container | Top-level visual grouping with optional accent color | Main Hub, Archive page, Battleboard |
| Text Display | Markdown-capable text block | HP, AP, enemy intent, descriptions, logs and help |
| Section | One to three Text Display children plus one accessory | Character status blocks and enemy summaries |
| Thumbnail | Accessory for a Section | Character portrait or enemy thumbnail |
| Media Gallery | 1–10 media items | Team portraits, card art, region or event gallery |
| Separator | Visual spacing/divider | Separate enemy, player and action areas |
| Action Row | Up to five buttons, or one select component | Navigation, action choices, confirmation |
| Button | One action per click | Attack, Guard, select, back, confirm, end turn |
| String Select | One selection menu with up to 25 options | Card selection, target selection, route choice, filters |
| Modal | A separate form interaction | Deck name, search text, rename or accessibility preferences |

Useful reference details:

- [V2 flag, message constraints and 40-component limit](https://discord.com/developers/docs/components/reference#what-is-components-v2)
- [Action Row and button/select structure](https://discord.com/developers/docs/components/reference#action-row)
- [Custom ID rules](https://discord.com/developers/docs/components/reference#custom-id)
- [Section structure](https://discord.com/developers/docs/components/reference#section)
- [Media Gallery](https://discord.com/developers/docs/components/reference#media-gallery)
- [Container structure](https://discord.com/developers/docs/components/reference#container)

Interactive component custom IDs must be unique within the message and between 1 and 100 characters. Do not store trusted gameplay values in a custom ID.

A Section supports one to three Text Display children and one accessory. An Action Row can contain up to five buttons or a single select menu. A Media Gallery supports one to ten media items. A String Select supports up to 25 options. Keep these constraints in the component renderer rather than relying on the UI author to remember them.

### 2.3 Important limitations

Components V2 is a more flexible **message layout and interaction system**, not a free-form game canvas.

It does not provide arbitrary HTML/CSS, drag-and-drop card positioning, a continuously animated battlefield, hover-driven game logic or a real-time game surface. Use cards, containers, galleries and buttons intentionally. A later optional Discord Activity could add a more visual battlefield, but the core game must not require one.

## 3. Screen architecture

### 3.1 Hub

Purpose: the player's personal home.

Suggested layout:

1. Container with game logo/name and a short status line.
2. Section with the current chapter / expedition status.
3. Three character portraits or a compact team summary.
4. Small progress summary: Archive completion, active quest, personal best.
5. Two Action Rows of navigation buttons at most.

Primary actions:
- Resume Expedition
- Start Expedition
- Team
- Archive
- Decks
- Quests
- Profile
- Settings

Never make the Hub a wall of 20 commands. The first screen should expose the next useful action.

### 3.2 Archive / Collection

The archive needs to work with hundreds of entries.

Use:
- Text Display for selected entry details.
- Media Gallery for a small number of featured cards/characters.
- String Select for category, rarity, Sigil, owner or sort order.
- Pagination buttons for results.
- A search Modal only when free text is useful.
- An explicit distinction between permanently owned cards and temporary run cards.

Do not render every owned card as its own button. Use a page of 5–10 visual cards and a select menu for the full data set.

### 3.3 Team Builder

The team must always contain exactly three unique characters.

Use:
- Three Sections, each with portrait and concise stats/role.
- One String Select per slot, containing eligible unlocked characters.
- A confirmation button.
- A validation step that prevents duplicate character slots unless a future game rule explicitly permits duplicates.

The player may inspect the passive and example card identity before confirming. Do not make the player open three separate commands to assemble a team.

### 3.4 Deck Builder

Each character keeps a personal starting deck; the run deck is temporary.

Use:
- Character selector.
- Card list with owner, cost, Rank, Sigil and compact effect summary.
- Filters for card type, Sigil, Rank and unlocked status.
- Pagination and detail view.
- Clear indicators for permanent ownership versus current run modification.

Avoid rendering the entire deck as a giant row of card buttons. A select menu should choose the card; the detail area then shows the effect and upgrade.

### 3.5 Battleboard

The Battleboard is the most important screen. The goal is to make the whole turn legible without filling the message to its component limit.

Recommended vertical order:

1. **Enemy header:** artwork or thumbnail, enemy name, HP, Stability/Stagger and state.
2. **Enemy Intent:** next move, target, damage band and any special warning.
3. **Party status:** three compact Sections showing each character's portrait, HP, status and signature readiness.
4. **Shared resources:** AP, Resonance and any current turn modifiers.
5. **Card hand:** six-card starting hand, owner marker, Rank, Sigil, AP cost and short effect.
6. **Selected card detail:** exact effect, valid targets and projected result.
7. **Pattern preview:** detected Pattern, chosen payoff and Resonance change.
8. **Reaction slot:** armed or empty, trigger condition and AP already spent.
9. **Controls:** Play / Confirm, Target selection, Arm Reaction, End Turn, Inspect / Help.

Example player flow:

- Click **Choose Card**.
- Pick one of the current six cards in a String Select.
- The Battleboard updates to show the card's detailed effect and valid target choices.
- Pick a target if needed.
- Confirm the action.
- The server validates the turn, pays AP and updates the board.
- The player repeats until they commit four cards or ends the planning phase.
- If more than one Pattern is valid, the player selects one from the preview before resolution.
- The enemy phase runs and the message updates.

A Select Menu can hold many card options without creating one button per card. Target selection should be shown only when a card needs a target. Keep high-frequency actions to one or two clicks where possible.

### 3.6 Route and reward screens

- A route screen should show a simple path summary and current node, not a huge map made from dozens of buttons.
- The player selects one adjacent node, then confirms.
- Rewards should use clear mutually exclusive options with one confirm step.
- A “Skip” action must always be available when the reward rules allow skipping.
- Boss phase changes should visually distinguish a new intent and new rule.

## 4. Interaction timing and message lifecycle

Discord's official interaction documentation states that an initial response must be sent within **3 seconds**. Interaction tokens are valid for **15 minutes** for follow-up responses.

Implementation rules:

1. Validate the interaction signature and identify the invoking user.
2. Acknowledge or defer promptly. Do not run long combat resolution before the first response.
3. Load the save/session from the database.
4. Validate ownership, state and expected version.
5. Apply the command in a database transaction.
6. Commit state and an event-log record.
7. Render and edit the current V2 message, or return a concise error if the interaction is stale.

Do not save an interaction token as the long-term identity of a battle. A battle may last hours or days and must survive after the original command's token expires. Each later button click creates its own interaction; persistent game state belongs in the backend.

If a message is stale, do not silently execute the old action. Return a clear refresh message and render the current board.

## 5. Backend architecture

### 5.1 Responsibilities

**Discord adapter**
- Receives slash commands, buttons, selects and modal submissions.
- Acknowledges within the platform deadline.
- Converts an interaction into a domain command.
- Renders V2 components from current state.
- Does not calculate final damage or trust client-side state.

**Application / game services**
- Player profile and save service.
- Collection and unlock service.
- Team / deck service.
- Expedition and route service.
- Combat engine.
- Reward and progression service.
- Quest service.
- Notification and optional personal encounter scheduler.

**Combat engine**
- Pure, testable game rules.
- Validates card ownership and costs.
- Applies card effects in a documented order.
- Checks weaknesses, Stability, Openings and Relay caps.
- Detects Patterns and applies one selected Pattern payoff.
- Resolves Reactions, enemy intent, statuses and boss phases.
- Emits a structured combat event log.
- Does not know about Discord buttons, embeds or message IDs.

**Persistence layer**
- Durable user save and run state.
- Transactions and uniqueness constraints.
- Content/ruleset versioning.
- Event log for replay/debugging.
- Backup and migration strategy.

**Renderer**
- Converts domain state into V2 Containers, Text Displays, Sections, galleries, selects and buttons.
- Does not contain game logic.
- Has component-limit tests and fallbacks for missing artwork.

### 5.2 Suggested data model

| Entity | Important fields | Purpose |
|---|---|---|
| PlayerSave | discord_user_id, save_version, chapter, profile_data | One independent save per user |
| CharacterDefinition | id, stats, passive, signatures, unlock_rule | Static character content |
| PlayerCharacter | user_id, character_id, mastery, unlock_state | Characters owned by a player |
| CardDefinition | id, owner_id, rank, sigil, type, cost, effects | Static card catalogue |
| PlayerCardUnlock | user_id, card_id, unlock_source | Permanent card library |
| DeckPreset | user_id, character_id, ordered_card_ids | Starting deck configuration |
| RunSession | run_id, user_id, seed, rng_version, ruleset_version, phase, version | Active personal Expedition |
| RunCharacterState | run_id, character_id, hp, status_state, signature_state | Temporary character state |
| RunCardInstance | run_id, card_id, upgrades, modifiers, pile | Temporary run deck instance |
| RunRelic | run_id, relic_id, slot, modifier_state | Run-only Relics |
| CombatEvent | run_id, turn, sequence, event_type, payload | Append-only combat history |
| CurrencyLedger | user_id, currency_type, delta, reason, reference_id | Auditable balance changes |
| QuestProgress | user_id, quest_id, progress, status, reset_at | Personal objectives |
| InteractionReceipt | interaction_id, user_id, run_id, result | Idempotency and duplicate-action protection |

The exact relational schema can change with the chosen database. The important rule is that Discord message contents are a rendered view, not the canonical save.

## 6. Combat state machine

Use explicit state transitions. Example phases:

- HUB
- TEAM_SELECTION
- DECK_SELECTION
- ROUTE_SELECTION
- COMBAT_DRAW
- COMBAT_PLANNING
- REACTION_ARMED
- PATTERN_SELECTION
- PLAYER_RESOLUTION
- ENEMY_PHASE
- REWARD_SELECTION
- BOSS_PHASE_TRANSITION
- RUN_COMPLETE
- RUN_DEFEAT
- RUN_ABANDONED

Every interaction supplies an action. The server checks whether that action is valid in the current phase. A button shown for an earlier phase must not be able to alter the new phase.

For example, a stale Play Card click received after the turn has ended must be rejected, even if the client still displays the old button.

## 7. Consistency, security and reliability

### 7.1 Ownership and authorization

- The server derives the owner from the Discord interaction's authenticated user ID.
- Never accept a user ID supplied in a select value as proof of ownership.
- Every action checks that the save and run belong to the invoking user.
- Public announcement buttons may open a user's private encounter, but cannot grant an encounter to a different account or claim a shared reward.

### 7.2 Duplicate clicks and concurrency

Buttons can be double-clicked; mobile networks can retry; two interactions can arrive almost together.

Use:
- A unique record for each Discord interaction ID.
- A monotonically increasing session version.
- Atomic transaction for AP payment, card movement, effect resolution and state update.
- Idempotent reward grants.
- A per-run lock or optimistic compare-and-swap for simultaneous clicks.

Only one accepted action can consume a given card or spend the same AP.

### 7.3 Randomness

- Generate a high-entropy run seed on the server when the Expedition begins.
- Use a documented deterministic PRNG version for run simulation.
- Store the seed securely and persist the generator state/counter.
- Record random outcomes in the combat event log.
- Never accept a client-provided seed, damage value, drop roll or reward amount as authoritative.
- A future debug/replay tool should reproduce a run from its seed, content version and action sequence.

This makes bugs reproducible and reduces unexplained combat results. It is not a promise of publicly provable fairness unless a separate cryptographic commitment scheme is designed and audited.

### 7.4 State recovery

- Persist after each committed gameplay action, not only at the end of a fight.
- If the bot restarts, reload the active run and render the current state on the next command/interaction.
- If the user deletes a message, the save still exists; /battle or /expedition can create a fresh view.
- If a component is stale, refresh rather than applying a guessed action.
- Database backups and migration tests are mandatory before a public launch.

### 7.5 Rate limits and rendering

- Acknowledge quickly, then update the existing message.
- Batch multiple cosmetic changes into one render after the game transaction.
- Avoid editing the message for every internal tick; a turn-based game has natural render boundaries.
- Respect Discord API rate limits and retry-after responses.
- Cache immutable artwork and static card definitions; do not cache user HP, inventory or run state as the authority.
- Use a short event log in the message and a full event log in storage.
- Keep custom IDs compact and opaque. The 1–100 character Discord limit is not a reason to encode an entire state object into the ID.

## 8. Privacy and server behavior

- Default to a private game screen (DM or another supported private response pattern).
- If a DM cannot be delivered, explain the issue and offer an owner-only fallback. Do not silently post a private save publicly.
- No Message Content Intent is needed for core gameplay. Prefer slash commands, component interactions and opt-in scheduled prompts over reading normal member chat.
- Server configuration should control only presentation/announcement settings, not ownership of personal progress.
- Personal save, collection and battle choices must remain portable across servers where the bot is installed.
- Announcements should be opt-in and should not create a competition for scarce shared drops.

## 9. Reliability and observability

Record structured events for:

- Command received / acknowledged / completed.
- Session loaded / version mismatch / owner mismatch.
- Card selected / card played / AP spent.
- Pattern recognized / selected / resolved.
- Weakness / Opening / Relay / Reaction / enemy action.
- Reward generated / reward granted.
- Run started / resumed / completed / failed.
- V2 render failed / asset unavailable / rate-limit retry.

Do not log secrets, bot tokens, interaction tokens or unnecessary private text. Keep metrics aggregated where possible.

Monitor:
- Interaction acknowledgement latency.
- Game action transaction time.
- Failed/stale component rate.
- Double-click / duplicate-action rejection rate.
- Run resume success after bot restart.
- Message edit failures and API 429 responses.
- Median battle turn duration and user action count.

## 10. Implementation milestones

### Milestone A — V2 shell

- Register slash commands.
- Build a V2 Hub and a private profile screen.
- Build component renderer and validation for component counts.
- Implement owner-only component handling and stale-view errors.
- No combat yet.

### Milestone B — durable solo state

- Database schema and migrations.
- Create/load player save.
- Store team, deck presets and Archive data.
- Store an active Expedition and resume it after a process restart.
- Add interaction receipts and version checks.

### Milestone C — combat engine without Discord

- Implement card, AP, deck, Pattern, Resonance and turn-order rules as pure domain functions.
- Add enemy intent and target logic.
- Add weakness, Stability, Opening, Relay, Reaction and boss Stagger.
- Write unit tests and simulation tests.
- Test without the Discord adapter first.

### Milestone D — V2 Battleboard

- Render enemy intent, party state, hand, Pattern preview and action controls.
- Connect Select Menus to card and target choice.
- Edit one board message per battle.
- Test desktop and mobile layouts.

### Milestone E — short Expedition

- Route nodes, combat rewards, events, one shop and one boss.
- Run completion/defeat and permanent reward pipeline.
- Add event log and replay/debug tools.

### Milestone F — content and collection

- Archive, Bestiary, card unlocks, personal Rift encounters, quests, cosmetics and optional Dispatch.
- Only expand content after the combat prototype passes its acceptance tests.

## 11. Definition of done for the V2 foundation

The foundation is not done merely because the bot can display buttons.

- V2 messages always use the V2 flag and valid component trees.
- No message exceeds 40 components; common screens remain comfortably under the cap.
- Every interactive custom ID is unique within the message and 1–100 characters.
- Every action is owner-checked, phase-checked and version-checked.
- Double-clicking cannot spend AP twice, play a card twice or grant duplicate rewards.
- A run survives bot restart and the expiration of an earlier interaction token.
- A deleted message can be recreated from persisted state.
- Private screens do not leak player data into a public channel.
- The renderer contains no combat calculations.
- The combat engine can be unit-tested without Discord.
- All visible costs, targets and consequences are confirmed before a committed action.

## 12. Final architecture decision

**Bot-first + Components V2 + durable single-player backend** is the recommended architecture.

Do not start with a Discord Activity. Prove that the whole tactical loop is fun and readable through V2 first. If, later, a 2D animated battlefield becomes important, an Activity can be added as an optional frontend that uses the same backend and rules engine. The core save, combat and progression must remain independent of whichever Discord UI displays them.
