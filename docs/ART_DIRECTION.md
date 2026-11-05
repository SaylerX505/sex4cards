# Art Direction & Visual Style

## 1. Core style

The approved visual direction is **16-bit pixel art** throughout the game.

The tone combines:
- Dark fantasy atmosphere.
- Whimsical cartoon energy.
- Expressive, readable character silhouettes.
- Cute/chibi proportions where they suit the source character.
- Strange, mysterious environments and monsters.
- Clear item silhouettes and strong visual hierarchy.

The palette direction discussed includes deep purple, black, crimson and gold accents. These are art-direction cues, not mandatory exact hex values.

## 2. Pixel-art constraints

- Use deliberate pixel clusters; avoid blurry scaling.
- Keep character silhouettes readable at small Discord attachment sizes.
- Use consistent sprite scale and perspective within a scene.
- Keep outlines and shading coherent across characters, monsters and items.
- Prefer a limited palette per asset.
- Export crisp PNGs; preserve transparency for sprites/icons where needed.
- Scale sprites using nearest-neighbor interpolation.
- Avoid mixing smooth vector art or painterly illustrations into the core asset set.

## 3. Asset categories

| Asset | Use |
|---|---|
| Character portrait | Collection and character detail |
| Battle sprite | Team/enemy battle display |
| Character expression/emote | Optional reaction or status presentation |
| Weapon icon | Inventory/equipment |
| Armor icon | Inventory/equipment |
| Rune icon | Inventory/equipment |
| Accessory icon | Inventory/equipment |
| Consumable icon | Battle and inventory |
| Enemy sprite | Battle |
| Dungeon background | Activity/encounter atmosphere |
| Crypt room/map tile | Exploration interface |
| UI icons | Class, status, currency, buttons |

## 4. UI style

The interface should feel like a compact pixel-art RPG menu adapted to Discord:
- Dark panels with high-contrast text.
- Gold or warm highlights for important selections.
- Purple/crimson accent colors for magical or dangerous states.
- Consistent icons for HP, Mana, class, rarity and status effects.
- Clear disabled states.
- Minimal decorative clutter.

Discord embeds and buttons have layout limits. Artwork should support the information, not make the UI too tall or difficult to read on mobile.

## 5. Character art direction

The current content direction is Adventure Time characters only for now; the user explicitly asked not to add original characters at this stage.

Pixel-art adaptations must preserve recognizable character identity while fitting the same sprite scale and rendering style. The art should not invent new franchise characters, alternate canon outfits or signature items without an explicit decision.

## 6. Item art direction

Weapon and item icons should be readable at small sizes. Each icon should have:
- Distinct silhouette.
- Consistent light direction.
- Consistent outline treatment.
- Transparent background where appropriate.
- A source/provenance record.

Do not invent original weapons while the current content constraint is in effect. Use only existing franchise weapons/items that have been researched and approved.

## 7. Motion and effects

Optional sprite animation may include idle, attack, hit, defend, skill and victory states. Animation frame counts and exact sprite-sheet sizes are not decided. If animation is too expensive for the MVP, prioritize static sprites and clear battle feedback.

## 8. Image and licensing policy

A visual reference link is not an asset license. Do not scrape or redistribute Adventure Time images from fan wikis or search results without checking rights. Maintain an asset register containing source URL, creator, license/permission, attribution requirements and local filename.

For any original UI/background assets created for the project, record the creator and usage rights. Obtain the necessary franchise license before publicly distributing protected Adventure Time character art or branding.

## 9. Useful references

- [Adventure Time — Cartoon Network](https://www.cartoonnetwork.com/)
- [OpenGameArt](https://opengameart.org/) — check each asset's individual license.
- [Lospec Pixel Art Tutorials](https://lospec.com/pixel-art-tutorials)
- [Lospec Palette List](https://lospec.com/palette-list)
- [Aseprite](https://www.aseprite.org/) — pixel-art editor.

## 10. Visual mockups

The project includes interface and style-board examples in [Visual Examples](VISUAL_EXAMPLES.md):
- [Overall visual overview](assets/visual-overview.svg)
- [Pixel-art palette and rules](assets/pixel-art-style-board.svg)
- [Discord main menu](assets/discord-main-menu.svg)

These are SVG design mockups. They use neutral art placeholders and do not introduce new characters or named franchise items. Final Adventure Time pixel-art assets must be approved/licensed and tracked in the asset register.


## Raster pixel-art examples

![Character roster pixel-art studies](assets/character-pixel-roster.png)

![Weapon and Rune icon pixel-art studies](assets/weapons-runes-equipment.png)

The PNGs show the current pixel-art direction directly. They are early concept studies, not final licensed franchise assets. Keep the crisp 16-bit treatment, clear silhouettes and controlled palette when replacing these studies with final art.
