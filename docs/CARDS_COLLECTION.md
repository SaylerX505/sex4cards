# Cards, Character Collection & Item Presentation

## 1. Important terminology

The project has a collection-oriented RPG identity, and Discord interfaces may use **cards** as compact visual panels. However, the user has explicitly ruled out deck-based combat.

For this specification:
- A **Character Card** is a UI/presentation view of one owned character.
- An **Item Card** is a UI/presentation view of one weapon, armor piece, Rune, accessory or consumable.
- A **Collection Card** is a compact tile in a roster or inventory gallery.
- A **Deck** is not part of the current combat design.

Do not implement card draws, deck construction, card hands, card energy or deck-based battles unless the game direction is explicitly changed.

## 2. Character collection

The character collection should let a player:
- Browse all characters they own.
- See locked/unowned entries if a discovery index is approved.
- Filter by class or rarity.
- Sort by level, name or recently acquired.
- Open a character detail view.
- Inspect current stats, skills and equipment.
- Select characters for the three-person team.

The collection should be usable on mobile Discord. Use pagination and compact controls rather than trying to show the entire roster in one embed.

## 3. Character card content

A character card can show:
- Pixel-art portrait or sprite.
- Display name.
- Class icon/name.
- Rarity, if the rarity system is approved.
- Character level.
- HP, ATK and other relevant stats.
- Owned/equipped status.
- A button to open full details.

Do not invent final stats or rarity labels in static art. Bind displayed values to the character's saved data.

## 4. Item cards

An item card should show:
- Pixel-art icon.
- Item name and category.
- Rarity (if approved).
- Main stats and secondary effects.
- Compatible class/slot, if restrictions exist.
- Upgrade level.
- Equipped-by indicator.
- Equip/unequip/compare controls.

For a Rune, make its passive nature clear. For a Crypt Run Relic, show that it expires at the end of the run.

## 5. Visual card layout

Recommended information hierarchy:
1. Image/silhouette and name.
2. Role or item category.
3. One or two key stats.
4. Short effect description.
5. Action controls.

Keep descriptions short enough for Discord. A full details view can contain the longer tooltip and full stat list.

## 6. Rarity presentation

Common/Rare/Epic/Legendary were discussed as possible tiers. If approved, rarity should be communicated with a consistent border, label or icon—not color alone. Ensure the interface remains readable for color-blind players and in Discord dark/light themes.

## 7. Collection completion

Achievements, collection completion rewards, favorites, wishlists and trading were discussed as possible future features in broader bot research. They are not currently approved core systems. Keep the initial data model extensible, but do not add these features to the MVP without a design decision.

## 8. No deck combat

This is a hard boundary in the current design:
- No card-based turn selection.
- No deck-building.
- No card draw mechanic.
- No card energy.
- Combat remains character-based, turn-based RPG with Attack, Skill, Defend and Item choices.

## 9. Asset provenance

Store asset source, license/permission status, attribution and file path alongside each character/item image. Adventure Time artwork is protected franchise material; the existence of a wiki image or a public URL does not mean the project has permission to redistribute it.

## 10. Visual example

![Character collection cards](assets/cards-collection-mockup.svg)

See [Visual Examples](VISUAL_EXAMPLES.md) for the full collection and Character Card mockups. Cards remain collection/presentation UI only; they do not become a deck or combat mechanic.

