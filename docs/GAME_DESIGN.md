# Game Design Overview

## 1. Product vision

**THE HOLLOW REALMS** is a Discord-native RPG that combines familiar turn-based party combat, character collection, equipment progression, repeatable farming and a more deliberate roguelite exploration mode.

The intended tone is **dark fantasy with whimsical cartoon energy**. The world should feel mysterious and slightly eerie without becoming relentlessly grim. The art direction is 16-bit pixel art, with readable silhouettes, expressive faces, compact sprites and richly themed environments.

The project name is fixed as **THE HOLLOW REALMS**. The current design does **not** include a Realm Unlocking or Realm Progression system. Do not introduce one as a core progression layer.

## 2. Design pillars

### Discord-native
The game is operated through slash commands, buttons, select menus, embeds and edited interaction messages. A player should be able to manage their party, inspect equipment and play encounters without leaving Discord.

### Readable tactical combat
Combat is classic turn-based RPG. The player controls exactly three characters and selects an action for each. The enemies act after the player's team has completed its actions.

### Meaningful team building
Character class, base stats, skills, equipment, runes and accessories combine to define a team's strengths. The player should have meaningful choices without needing complicated combos or a large number of subsystems.

### Two different repeatable activities
- **Auto Hunt:** efficient background farming and repeated encounters.
- **The Hollow Crypt:** active exploration, branching choices, risk management and temporary run effects.

These modes share the battle rules where applicable, but they should not feel interchangeable.

### Collection and visual identity
Characters and items should be easy to browse, recognize and compare. Pixel-art portraits, sprites, item icons, rarity treatments and clear stat summaries support the collection fantasy.

## 3. Core player loop

1. Open the bot's main menu in Discord.
2. Review character roster, team, inventory and equipment.
3. Select three characters for a battle team.
4. Improve the team through levels, weapons, armor, runes, accessories and skills.
5. Choose an activity: manual challenge, dungeon/Auto Hunt or The Hollow Crypt.
6. Earn rewards and materials.
7. Return to roster and inventory management, then prepare for the next activity.

## 4. Main systems

| System | Purpose | Design status |
|---|---|---|
| Characters | Collectible party members with classes and skills | Core concept agreed; roster and balance open |
| Classes | Define a character's combat role | Class-based characters agreed; exact class list is a proposal |
| Combat | Tactical turn-based battles | Core flow agreed |
| Mana | Resource used by active skills | Mana confirmed; slow regeneration confirmed |
| Equipment | Character power customization | Five equipment slots agreed |
| Runes | Passive stat/effect bonuses | Rune slot and passive-buff role agreed |
| Auto Hunt | Background farming | Core behavior agreed; limits and formulas open |
| Hollow Crypt | Active branching exploration | Concept agreed; room rules and rewards open |
| Collection cards | Visual presentation of owned characters/items | UI direction only; not deck combat |
| Trading/PvP | Social/economy features | Not in initial scope; not approved |

## 5. What the game is not

- It is not a deck-building RPG.
- It does not use Energy alongside Mana.
- It is not a three-player battle party; one player controls three characters.
- Auto Hunt is not a stream of repeated public Discord messages.
- The Crypt is not the same thing as Auto Hunt.
- The game does not currently create original characters or original franchise-like weapons.
- The game does not have Realm unlocking/progression.

## 6. Current content direction: Adventure Time

The current character concept is a mix of Adventure Time characters, with **no original characters added for now**. Character names, depictions, recognizable weapons and items should be sourced from the franchise rather than invented for this project.

The game mechanics (classes, stats, battle rules, item slots and reward systems) are original game-design structures. They should not be confused with official Adventure Time canon.

Examples of characters discussed as possible roster entries include Finn, Jake, Marceline, Princess Bubblegum, Ice King and BMO. This is a candidate list, not a finalized launch roster. Class assignments and skill kits must be researched and approved rather than treated as canon.

## 7. Inspirations and reference boundaries

- **Mortal Kombat Mobile Krypt:** reference for a map-based run, persistent team health, room choices, consumables and a special reward shop.
- **Slay the Spire:** reference for branching route selection and run-specific passive relic choices.
- **OwO and other Discord RPG bots:** reference for repeatable hunt loops and compact Discord interactions, not for message spam or copying their complete mechanics.

References are inspiration, not instructions to copy protected assets, names, code or exact content.

## 8. Product language

Use these terms consistently:
- **Character:** a collectible playable unit.
- **Team:** exactly three selected characters for combat.
- **Class:** the character's combat role.
- **Skill:** an active ability that may consume Mana.
- **Ultimate:** a character's strongest active ability; exact charge/availability rules remain open.
- **Rune:** a passive piece of equipment in one dedicated slot.
- **Run Relic:** a temporary effect that exists only during a Hollow Crypt run.
- **Auto Hunt session:** a background sequence of automated dungeon encounters.
- **Crypt run:** one active exploration attempt through a branching map.

## 9. Scope discipline

When a mechanic has not been confirmed, label it as a proposal or open decision. Do not quietly turn sample numbers, suggested character kits, drop tables or room schedules into final requirements.
