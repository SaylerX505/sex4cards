# Game Design Overview

## 1. Product vision

THE HOLLOW REALMS is a Discord-native RPG that combines character collection, classic turn-based team combat, equipment progression, repeatable farming and a deliberate roguelite exploration mode.

The tone is dark fantasy with whimsical cartoon energy. The visual language is premium, high-detail pixel art with flexible resolution and pixel density. There is no fixed bit-depth, palette count or sprite-canvas requirement.

The project name is fixed. The design does not include Realm unlocking or Realm progression. Do not add such a system.

## 2. Design pillars

### Discord-native
Core play is operated through slash commands, buttons, select menus, embeds and edited interaction messages. Normal play should not require a separate game client.

### Readable tactical combat
One player controls exactly three characters. The player selects an action for each team member in displayed order; enemies act after the third player action.

### Meaningful team building
Character class, stats, skills, equipment, Runes and accessories define the team's strengths without relying on complicated combo chains or many parallel resources.

### Two distinct repeatable activities
- Auto Hunt is background farming through automated encounters.
- The Hollow Crypt is active exploration with path choices, risk and temporary run effects.

### Recognizable collection and item identity
Every named item should have its own documented dossier and visual identity. Do not treat a category icon or generic silhouette as a named, approved item.

## 3. Core player loop

1. Open the bot's main menu in Discord.
2. Review the character roster, team, inventory and equipment.
3. Select exactly three characters for a battle team.
4. Improve the team through levels, skills, weapons, armor, Runes and accessories.
5. Choose a manual challenge, Auto Hunt session or Hollow Crypt run.
6. Earn rewards and materials.
7. Return to the roster and inventory to prepare the next activity.

## 4. Main systems

| System | Purpose | Status |
|---|---|---|
| Characters | Collectible playable units | Core concept agreed; roster and balance open |
| Classes | Define combat roles | Class-based design agreed; exact list is a proposal |
| Combat | Turn-based team battles | Core flow agreed |
| Mana | Resource for active skills | Mana and slow regeneration agreed |
| Equipment | Character customization | Five slots agreed |
| Runes | Passive stat/effect bonuses | One Rune slot and passive role agreed; effects need balancing |
| Auto Hunt | Background farming | Core behavior agreed; limits and reward rates open |
| Hollow Crypt | Active branching exploration | Concept agreed; room and reward rules open |
| Collection cards | Character/item presentation | UI only; not deck combat |

## 5. What the game is not

- Not a deck-building RPG.
- Does not use Energy alongside Mana.
- Not a three-human battle party.
- Auto Hunt is not a public stream of repeated encounter messages.
- The Crypt is not interchangeable with Auto Hunt.
- Does not currently create original characters or original franchise-like weapons/items.
- Has no Realm unlocking or Realm progression.

## 6. Current content direction: Adventure Time

The current character and item direction is based on existing Adventure Time characters and recognizable franchise objects. No original characters or invented Adventure Time canon items are in scope for now.

Finn, Jake, Marceline, Princess Bubblegum, Ice King and BMO have been mentioned as candidate characters, not a finalized launch roster. Character class, stats, rarity and skill kits are original game mechanics and must not be presented as official franchise canon.

Named weapons already identified for research are Grass Sword, Demon Blood Sword and Ax Bass. Their lore and visual identity are documented separately from their unapproved in-game stats and acquisition routes.

## 7. Inspiration boundaries

- Mortal Kombat Mobile Krypt: inspiration for map-based runs, persistent team health, room choices and reward decisions.
- Slay the Spire: inspiration for branching routes and temporary run-specific passive choices.
- OwO and other Discord RPG bots: inspiration for repeatable hunt loops and compact interactions, not message spam or direct copying.

Use original system design and project-owned presentation. Do not copy protected names, text, art, maps or code from inspiration sources.

## 8. Shared vocabulary

- Character: a collectible playable unit.
- Team: exactly three selected characters.
- Class: a character's game-combat role.
- Skill: an active ability that may consume Mana.
- Rune: permanent passive equipment in the Rune slot.
- Run Relic: a temporary effect for one Hollow Crypt run.
- Item instance: one owned copy of an item definition.
- Auto Hunt session: a background sequence of automated encounters.
- Crypt run: one active exploration attempt through a branching map.

## 9. Scope discipline

When something is not confirmed, label it proposal or open decision. Do not silently turn sample numbers, suggested kits, reward categories or visual shape studies into final game content. See the [item catalogue](items/README.md) for item-by-item status.
