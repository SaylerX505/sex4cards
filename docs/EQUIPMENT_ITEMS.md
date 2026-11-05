# Weapons, Equipment & Inventory

## 1. Equipment slots

Each character has exactly five currently agreed equipment slots:

| Slot | Purpose |
|---|---|
| Weapon | Main offensive weapon and weapon effects |
| Armor | Defensive stats and possible defensive effects |
| Rune | Passive stat/effect bonuses |
| Accessory 1 | Additional stats or passive effect |
| Accessory 2 | Additional stats or passive effect |

There is **no Headgear slot** in the current design.

## 2. Weapons

Weapons are equipment items. Their exact weapon catalogue must be based on the approved Adventure Time content direction for now; do not invent original weapons while the user has asked to avoid original content.

A weapon definition may include:
- Stable item ID.
- Display name and franchise/source attribution.
- Compatible class(es), if class restrictions are used.
- Base ATK or other relevant stats.
- Secondary stat bonuses.
- Passive effect, if any.
- Rarity and upgrade level.
- Pixel-art inventory icon.
- Acquisition sources.

Whether every character can equip every weapon or whether some weapons are character/class-restricted is still an open decision.

### Weapon acquisition
A confirmed design constraint: ordinary Auto Hunt does not directly award weapons. Candidate acquisition routes include manual challenges, bosses, quests, exploration or crafting, but the exact routes are not finalized.

## 3. Armor

Armor is the defensive equipment slot. It may improve HP, DEF, resistance or other defensive attributes. Armor types, class restrictions, rarity and upgrade costs remain open.

## 4. Runes

Runes have one dedicated slot per character. They are passive: once equipped, their effects apply automatically. They are not activated as battle skills.

The user-defined purpose of Runes is to grant buffs such as damage, HP/Health, healing and similar bonuses.

Possible Rune effect families discussed:
- Attack/Damage increase.
- Maximum HP increase.
- Maximum Mana increase.
- Healing effectiveness increase.
- Damage reduction.
- Critical damage increase.
- Other carefully balanced passive effects.

The names and exact numerical values are not finalized. Example percentages previously discussed are placeholders only.

### Rune behavior
- One Rune can be equipped per character.
- Replacing a Rune returns the old Rune to the player's inventory; equipping a new one does not consume the old Rune.
- Rune effects are passive and should be reflected in the character's effective stats.
- Rune upgrades and sets are possible future systems, not MVP commitments.

### Runes vs. Crypt Relics
Do not confuse permanent equipment Runes with temporary **Run Relics** found during The Hollow Crypt. Runes belong to a character and remain in the inventory when unequipped. Run Relics are temporary effects for one Crypt run and expire when that run ends.

## 5. Accessories

Each character has two accessory slots. Accessories may provide:
- Direct stat bonuses.
- Passive effects.
- Defensive or offensive utility.
- Utility effects for specific activities, if balanced.

Accessory stacking, duplicate restrictions, rarity and upgrade rules remain open.

## 6. Rarity and upgrades

Rarity tiers such as Common, Rare, Epic and Legendary have been discussed for equipment but are not finalized. Upgrade systems and material costs also need balancing.

Avoid making rarity alone the only determinant of item value. Different effects should support different team builds.

## 7. Inventory requirements

Inventory should support:
- Category filters (weapons, armor, runes, accessories, consumables, materials).
- Sorting by rarity, level, name or recently obtained.
- Pagination suitable for Discord component limits.
- Item detail view with stats and effect description.
- Equip, unequip and compare actions.
- Safe handling of duplicate items.
- A clear indication when an item is currently equipped and by whom.

## 8. Item ownership and transaction safety

The database should distinguish item definitions from owned item instances. An owned item instance should have a unique ID, owner, upgrade level and optional equipped-character reference.

Equip operations must validate ownership and slot compatibility in one transaction. Replacing equipment must not delete the previous item. Prevent double-selling, double-consuming or double-equipping due to repeated Discord interactions.

## 9. Consumables and materials

Battle consumables may restore HP or Mana and may support the Crypt's recovery decisions. Upgrade materials, crafting materials, monster drops, Essence and Gold are possible reward categories. Exact names, sources and economy values remain open.

## 10. Equipment visual example

![Equipment and inventory mockup](assets/equipment-inventory-mockup.svg)

The image shows the five agreed slots only: Weapon, Armor, Rune, Accessory 1 and Accessory 2. Generic symbols are category placeholders, not invented weapon designs.

