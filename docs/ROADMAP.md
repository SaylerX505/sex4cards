# Roadmap & Open Decisions

## 1. Suggested implementation order

The order below is a recommendation for building a playable foundation. It is not a statement that these tasks are complete.

### Phase 0 — Product specification
- [x] Establish THE HOLLOW REALMS as the project name.
- [x] Choose dark-fantasy + whimsical-cartoon direction.
- [x] Choose 16-bit pixel-art direction.
- [x] Set character direction to Adventure Time mix for now; no original characters currently.
- [x] Confirm three-character player-controlled team.
- [x] Confirm classic turn-based combat flow.
- [x] Choose Mana and slow Mana regeneration; no Energy resource.
- [x] Confirm equipment slots: Weapon, Armor, Rune, Accessory 1, Accessory 2.
- [x] Define Auto Hunt and Hollow Crypt as distinct modes.
- [ ] Finalize detailed balance, roster and reward tables.

### Phase 1 — Bot foundation
- [ ] Create Discord application and bot.
- [ ] Implement command registration and interaction routing.
- [ ] Add configuration/secrets handling.
- [ ] Add database connection and migrations.
- [ ] Add a basic main menu and profile.

### Phase 2 — Character collection
- [ ] Create character definitions and player ownership.
- [ ] Implement roster, detail view and pagination.
- [ ] Implement team selection with exactly three slots.
- [ ] Add class/stat display.
- [ ] Add asset provenance tracking.

### Phase 3 — Equipment and inventory
- [ ] Implement item definitions and owned item instances.
- [ ] Add five equipment slots.
- [ ] Implement equip/unequip and replacement behavior.
- [ ] Implement Rune passive effects.
- [ ] Add inventory filters and pagination.

### Phase 4 — Battle engine
- [ ] Implement three-character turn-based battle.
- [ ] Add Attack, Skill, Defend and Item actions.
- [ ] Implement Mana spending and slow round-based regeneration.
- [ ] Add enemy turns and encounter resolution.
- [ ] Add battle persistence and restart recovery.
- [ ] Add battle UI and stale-interaction protection.

### Phase 5 — Dungeons and Auto Hunt
- [ ] Define initial dungeon and enemy content.
- [ ] Define difficulty modifiers.
- [ ] Implement background session worker.
- [ ] Implement run summaries and reward settlement.
- [ ] Verify that ordinary Auto Hunt cannot award characters or weapons.

### Phase 6 — The Hollow Crypt
- [ ] Implement branching map generation.
- [ ] Add room types and room transitions.
- [ ] Add persistent run HP and recovery rules.
- [ ] Add temporary Run Relics.
- [ ] Add run currency/merchant only after rules are finalized.
- [ ] Add victory, defeat and escape settlement.

### Phase 7 — Polish
- [ ] Complete pixel-art asset set.
- [ ] Add responsive embeds and mobile testing.
- [ ] Add logs, metrics, backups and admin tools.
- [ ] Run economy and combat simulations.
- [ ] Review IP/licensing before public release.

## 2. Open design decisions

The following require explicit decisions before they should be treated as final implementation requirements.

### Characters
- Final launch roster.
- Class assignment for each Adventure Time character.
- Character rarity and whether rarity is needed.
- Character acquisition routes.
- Level cap and XP curve.
- Skill upgrade rules.
- Whether every character follows the same skill-kit structure.

### Combat
- Exact stat formulas.
- Max Mana and per-skill costs.
- Mana regeneration amount and timing.
- Ultimate charge/availability rules.
- Speed's role, if any.
- Status effect definitions and stacking.
- Defend formula.
- Enemy targeting and AI rules.
- KO/revive rules outside the Crypt.

### Equipment
- Weapon and armor compatibility.
- Exact item catalogue.
- Rarity tiers.
- Upgrade system and materials.
- Rune effect list and values.
- Accessory stacking rules.
- Whether any equipment has character-specific restrictions.

### Auto Hunt
- Dungeon list and encounter length.
- Difficulty names and scaling.
- Session limits and costs.
- HP/Mana persistence between runs.
- Automation policy and stop conditions.
- Reward tables and drop rates.
- Whether and how Auto Hunt progression unlocks.

### Hollow Crypt
- Map size and branching rules.
- Room distribution.
- Run length and boss placement.
- HP/Mana persistence.
- KO and revive rules.
- Run Relic offer frequency and stacking.
- Temporary currency and merchant inventory.
- Escape/defeat reward rules.

### Cards and social features
- Whether "cards" remain purely collection UI.
- Favorites/wishlist.
- Collection achievements.
- Trading.
- PvP or co-op features.

These should not be assumed merely because they are common in other Discord RPGs.

## 3. MVP recommendation

A practical first playable milestone:
1. Discord bot foundation.
2. Character ownership and three-person team.
3. Inventory and five equipment slots.
4. Battle engine with Mana.
5. One dungeon and a manual battle loop.
6. Auto Hunt background processing.
7. Hollow Crypt after the shared battle and persistence systems are stable.

This sequence reduces duplicated combat logic and allows the team to validate the core loop before building the more complex exploration mode.

## 4. Definition of done for a feature

A feature is not done just because a command responds. It should:
- Have documented rules.
- Validate ownership and legal state.
- Persist changes.
- Handle retries and restarts.
- Have tests for normal and edge cases.
- Work on mobile Discord.
- Avoid unnecessary message spam.
- Have clear player-facing help text.

## 5. Project status

The repository documentation is being established first. No bot implementation, database schema, deployed Discord application or completed gameplay feature is claimed by this roadmap.
