# Roadmap & Open Decisions

## 1. Suggested implementation order

This is a recommendation for development, not a statement that tasks are complete.

### Phase 0 — Product and visual specification
- [x] Establish THE HOLLOW REALMS as the project name.
- [x] Choose dark-fantasy atmosphere with whimsical cartoon character energy.
- [x] Set premium, high-detail pixel-art direction with flexible resolution and pixel density.
- [x] Set character scope to existing Adventure Time characters; no original characters for now.
- [x] Confirm exactly three player-controlled characters per team.
- [x] Confirm classic turn-based combat flow.
- [x] Choose Mana and slow Mana regeneration; no Energy resource.
- [x] Confirm equipment slots: Weapon, Armor, Rune, Accessory 1 and Accessory 2.
- [x] Define Auto Hunt and Hollow Crypt as distinct modes.
- [x] Add owner-supplied character and Rune visual references to the asset archive.
- [ ] Finalize detailed balance, roster, source-backed item catalogue and reward tables.

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
- [ ] Add the five equipment slots.
- [ ] Implement equip/unequip and replacement behavior.
- [ ] Implement passive Rune effects.
- [ ] Add inventory filters and pagination.
- [ ] Research and approve source-backed accessory and armor items.

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
- [ ] Verify ordinary Auto Hunt cannot award characters or weapons.

### Phase 6 — The Hollow Crypt
- [ ] Implement branching map generation.
- [ ] Add room types and room transitions.
- [ ] Add persistent run HP and recovery rules.
- [ ] Add temporary Run Relics.
- [ ] Add run currency/merchant only after the rules are finalized.
- [ ] Add victory, defeat and escape settlement.

### Phase 7 — Art and release polish
- [ ] Produce final character designs that meet the new quality bar.
- [ ] Produce isolated Rune icons based on the five current references.
- [ ] Produce approved weapon, armor, accessory, consumable and material icons.
- [ ] Add responsive embeds and mobile testing.
- [ ] Add logs, metrics, backups and admin tools.
- [ ] Run economy and combat simulations.
- [ ] Review IP/licensing before public release.

## 2. Open design decisions

### Characters
- Final launch roster.
- Class assignment for each Adventure Time character.
- Character rarity, level cap and XP curve.
- Character acquisition routes.
- Skill upgrade and duplicate handling rules.

### Combat
- Damage formulas and rounding.
- Max Mana and per-skill costs.
- Mana regeneration amount and timing.
- Ultimate charge/availability rules.
- Speed's role, if any.
- Status effect definitions and stacking.
- Defend formula, enemy targeting and KO/revive rules.

### Equipment and items
- Weapon/armor compatibility and exact in-game stats.
- Final Rune effects, values and formulas.
- Rarity tiers and upgrade system.
- Accessory catalogue from actual source-backed Adventure Time items.
- HP/Mana consumable names, values and limits.
- Gold sinks, material names, crafting recipes and drop tables.
- Item acquisition outside ordinary Auto Hunt.

### Auto Hunt
- Dungeon list, encounter length and difficulty scaling.
- Session limits/costs and persistence rules.
- Automation policy and stop conditions.
- Reward tables and drop rates.

### Hollow Crypt
- Map size, branching and room distribution.
- Run length and boss placement.
- HP/Mana persistence, KO and revive rules.
- Run Relic list, offer frequency and stacking.
- Temporary currency, merchant inventory and defeat/escape rewards.

### Collection and social features
- Favorites, achievements, trading, PvP or co-op.
- Whether collection cards remain purely presentation UI.

## 3. MVP recommendation

1. Discord bot foundation.
2. Character ownership and three-person team.
3. Inventory and five equipment slots.
4. Battle engine with Mana.
5. One dungeon and a manual battle loop.
6. Auto Hunt background processing.
7. Hollow Crypt after battle persistence is stable.

## 4. Definition of done

A feature is not done just because a command responds. It should have documented rules, validated state transitions, persisted data, retry/restart behavior, tests for normal and edge cases, a mobile-friendly UI and clear player-facing help.

## 5. Project status

The repository currently contains design documentation and concept assets. No deployed bot, database schema or completed gameplay feature is claimed.
