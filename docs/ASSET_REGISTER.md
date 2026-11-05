# Asset Register & Provenance

This register separates current owner-supplied references, historical concept sheets, interface mockups and future production assets.

## 1. Current owner-supplied references

| Asset | Repository path | Use | Status |
|---|---|---|---|
| Character quality reference | assets/references/character-quality-reference.jpg | Pixel-art finish, silhouette and rendering reference | Current internal reference; creator/rights status not supplied |
| Rune overview | assets/references/rune-reference-overview.jpg | Rune names, visual categories and first example effects | Current internal reference; values are proposals |
| Rune details | assets/references/rune-reference-details.jpg | Wisdom, Restoration and Protection reference details | Current internal reference; values are proposals |

These images were supplied in the project owner's visual-reference commit dated 2026-11-05. They are retained as internal design references. They are not automatically approved for shipped artwork; creator, permission, license and redistribution rights must be confirmed before public release.

## 2. Historical generated concepts

The following PNGs remain in the repository for comparison and history. They are not the current art target.

| Asset | Repository path | Status |
|---|---|---|
| Character sprite roster | assets/character-pixel-roster.png | Superseded placeholder; old 64×72 base sprites |
| Weapon/Rune/accessory sheet | assets/weapons-runes-equipment.png | Superseded concept sheet |
| Accessory shape study | assets/accessory-shape-studies.png | Generic non-canon silhouettes; not approved items |
| Character collection cards | assets/character-collection-cards.png | Layout/content placeholder |
| Battle/equipment UI | assets/battle-equipment-ui.png | Layout/content placeholder |
| Crypt raster map | assets/hollow-crypt-map.png | Route illustration placeholder |

The generic Pendant, Ring, Bracelet, Brooch, Charm, Buckle, Medallion and Watch shapes are explicitly excluded from the canonical item catalogue until source-backed Adventure Time objects are selected.

## 3. Interface mockups

SVG files under assets are UI/layout concepts, such as character cards, collection, equipment inventory, battle UI, Discord main menu, Auto Hunt, Hollow Crypt map and visual overview. They are not screenshots of a deployed bot.

## 4. Production asset record template

Every production asset should have a record containing:

| Field | Required information |
|---|---|
| asset_id | Stable internal identifier |
| display_name | Human-readable name |
| linked_content_id | Character/item/system record using the asset |
| file_path | Repository path |
| source_url | Original source or approved brief |
| creator | Artist/creator |
| license_or_permission | Exact licence, permission or written approval |
| attribution | Required attribution text |
| derivative_rights | Whether edits, crops and redistribution are allowed |
| created_at | Creation date |
| revision | Version/revision identifier |
| status | Reference, draft, review, approved or retired |
| reviewer | Person who approved the asset |

Do not mark an asset approved while creator, rights or source identity remain unknown.

## 5. Production export checklist

- Master artwork retained separately from exports.
- Portrait, embed, thumbnail and inventory crops are intentional.
- Transparent-background exports are used where appropriate.
- Dimensions are chosen per composition, not by a universal sprite limit.
- Pixel clusters, lighting and materials meet [Art Direction](ART_DIRECTION.md).
- The matching character/item dossier exists.
- Rights, attribution and asset path are recorded.
