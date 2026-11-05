# Characters & Classes

## 1. Character concept

Characters are collectible units used to form the player's combat team. Each battle team contains **exactly three characters**, all controlled by one player.

The current creative direction is:
- Adventure Time characters for the roster.
- No original player characters or invented franchise characters for now.
- 16-bit pixel-art presentation.
- RPG classes and statistics are game mechanics layered onto the selected characters; they are not claims about official franchise canon.

The roster is not finalized. Finn, Jake, Marceline, Princess Bubblegum, Ice King and BMO have been mentioned as possible entries, but none of their final stats, rarity, skills or launch availability have been locked.

## 2. Character data model

A character definition should eventually contain:

| Field | Meaning |
|---|---|
| character_id | Stable internal identifier |
| display_name | Character's display name |
| source_franchise | Franchise/source attribution |
| class_id | Assigned RPG class |
| rarity | Collection rarity tier, if approved |
| base_stats | Starting attributes |
| growth_curve | How stats change with level |
| passive_skill_id | Always-on passive, if used |
| active_skill_ids | Active skill definitions |
| ultimate_skill_id | Ultimate definition, if used |
| portrait_asset | Pixel-art portrait reference |
| battle_sprite_asset | Battle sprite reference |
| signature_weapon_id | Optional associated weapon, if approved |
| acquisition_sources | Approved ways to obtain the character |
| is_available | Whether the character can currently be obtained |

Character ownership belongs to a player-character record, not to the global character definition.

## 3. Classes

The design uses classes rather than making every character a completely unique, unclassifiable role. The following six classes are a **proposed starting set**, not a finalized list:

| Class | Intended role | Typical strengths |
|---|---|---|
| Warrior | Reliable physical damage | ATK and balanced durability |
| Tank | Protect the team | HP, DEF and mitigation |
| Mage | Magical damage | Skill damage and Mana synergy |
| Assassin | Burst damage | Critical chance and single-target pressure |
| Healer | Restore health and sustain | Healing effectiveness |
| Ranger | Ranged/offensive utility | Consistent damage and accuracy |

A character should have one primary class in the initial version unless a multi-class rule is explicitly approved later.

## 4. Suggested character kit structure

A simple kit is preferred:
- One passive ability.
- Two active skills.
- One ultimate ability.

This is a proposed template. It is not yet a confirmed rule for every character. Avoid large skill trees, long combo chains or many overlapping resource meters.

### Passive
An always-on effect. It should be easy to understand and should not require a button press every turn.

### Active skills
Player-selected actions that usually consume Mana. A skill should have a clear purpose such as damage, healing, defense or applying a status effect.

### Ultimate
A signature high-impact ability. The ultimate's charge rules, Mana cost and availability are still open decisions.

## 5. Character statistics

Candidate stats discussed so far:

| Stat | Meaning |
|---|---|
| HP | Current and maximum health |
| ATK | Physical attack strength |
| DEF | Damage mitigation/defense |
| SPD | Speed-related stat; its effect on turn order is not decided |
| CRIT Rate | Chance to critically hit |
| CRIT DMG | Critical damage multiplier/bonus |
| Accuracy | Chance for attacks/effects to connect |
| Resistance | Defensive resistance to selected effects or damage types |
| Max Mana | Maximum Mana capacity |

Do not assume every stat must be shown to the player at all times. The UI should prioritize the stats that matter for the selected character and action.

### Turn order note
The initial combat flow uses the order in which the three characters are placed in the team. Speed may become relevant later, but it has **not** been approved as the mechanic that determines player turn order.

## 6. Levels and growth

Character levels are expected to increase base stats. Exact level cap, XP curve, ascension, duplicate handling and skill-upgrade costs are open decisions.

A future progression model may separate:
1. Character level and base-stat growth.
2. Skill upgrades.
3. Equipment upgrades.
4. Rune and accessory customization.

Do not implement Character Ascension as a required system until its rules are designed.

## 7. Rarity

Common, Rare, Epic and Legendary were discussed as possible rarity tiers. They are **proposed**, not finalized. Rarity should communicate collection value and acquisition difficulty without making lower-rarity characters useless.

Balance principle: a well-built lower-rarity character should retain a meaningful niche through class utility, skills or team synergy.

## 8. Acquisition rules

One important rule has been stated: **ordinary Auto Hunt does not directly award playable characters or weapons**.

Possible character acquisition activities still need to be selected. Quests, challenges, bosses, exploration rewards or special events are ideas, not final reward guarantees.

Do not add a gacha, card-pack or random character banner without an explicit design decision.

## 9. Franchise and asset caution

Adventure Time characters and their visual designs are protected franchise material. A public or commercial release may require licensing/permission. Do not create replacement characters that imitate protected characters as a workaround. Keep source attribution and asset provenance in the content database, and obtain legal guidance before release.
