# Art Direction & Visual Style

## 1. Core vision

The target is **premium, high-detail pixel-art illustration**, not a retro hardware simulation. Do not lock the art to 8-bit, 12-bit, 16-bit, a fixed palette size, or a tiny sprite canvas. Pixel art is the visual language; quality, expressive design and readability are the priorities.

The desired finish should feel like a professionally art-directed indie RPG: richly rendered character illustrations, intentional pixel clusters, layered shading, controlled highlights, strong silhouettes and carefully designed materials. The characters should feel like polished game artwork—not tiny placeholder sprites enlarged with nearest-neighbor scaling.

The world combines:
- Dark-fantasy atmosphere with whimsical cartoon character energy.
- Expressive character acting and recognizable silhouettes.
- Richly detailed hair, faces, clothing, accessories and weapons.
- Dramatic but readable lighting.
- Deep purple, near-black, crimson and antique-gold accents, balanced with each character's recognizable colors.
- Cohesive UI and item art that feels part of the same game.

## 2. Character quality bar

Character art is the highest-priority visual category. Every character needs a deliberate design pass, not a generic sprite template.

**Required qualities**
- Strong, instantly recognizable silhouette and proportions.
- Face with expressive eyes, brows, mouth and readable emotion.
- Layered hair/fur/skin shading with intentional highlights and shadow shapes.
- Clothing with folds, seams, trims, material variation and small identifying details.
- Weapons and accessories drawn as designed objects with clear construction, perspective and highlights.
- A coherent light source and consistent rendering finish.
- Enough resolution and pixel density to preserve detail in both a large character view and a smaller Discord UI crop.

**Do not**
- Force all characters into 32×32, 64×64 or any other fixed canvas.
- Enlarge crude sprites and call the result finished art.
- Use large flat rectangles as substitutes for anatomy, clothing or facial features.
- Make every character share the same body proportions or face.
- simplify signature shapes until the character is no longer recognizable.

## 3. Pixel technique and flexibility

Use high-resolution pixel-art techniques where they improve the result:
- Variable canvas dimensions per asset.
- Dense, intentional pixel clusters and selective single-pixel accents.
- Multi-step ramps for skin, fabric, metal, hair and magical effects.
- Clean anti-cluster control: avoid noisy dithering and random pixel texture.
- Pixel-shaped highlights and shadows; no automatic blur.
- Nearest-neighbor scaling for actual sprite exports, while allowing larger native-resolution illustrations for portraits and cards.
- Separate source artwork from UI-sized exports so the game can create multiple crops without degrading the master.

There is no mandatory bit depth, palette limit, tile size, sprite frame size or universal pixel scale. Define technical dimensions per asset after its composition and use are known.

## 4. Character asset set

Each approved character should eventually have:
1. **Hero artwork / portrait:** polished, detailed presentation art for collection and profile views.
2. **Battle sprite:** readable combat pose with the same design language and carefully chosen pixel density.
3. **Portrait crop:** face-focused view for compact Discord embeds.
4. **Expression set:** a small number of clear emotions/status expressions if useful.
5. **Animation frames:** idle, attack, hit, defend, skill and victory only when the MVP needs them.

All versions must come from one approved design sheet. Do not redesign facial features, costume details or weapon proportions independently between views.

## 5. Weapons, Runes and Accessories

Items must receive the same level of care as characters:
- Weapons: readable construction, blade/handle details, material highlights and recognizable silhouette.
- Runes: distinct magical symbols with layered stone/crystal/metal treatment, but clear enough to read as small UI icons.
- Accessories: more variety in shape and material—metal, gems, leather, cloth and magical details—while remaining grounded in approved Adventure Time items.
- Keep transparent-background master assets where appropriate.
- The two Accessory equipment slots remain unchanged; this is an art-quality update, not a slot-system change.

Do not invent new Adventure Time canon objects or original franchise characters. The current content scope remains existing Adventure Time characters and source-backed items only.

## 6. Palette and lighting

The world palette uses deep purple, black, crimson and gold as environmental/UI anchors. Character-specific colors remain important; do not recolor Finn, Jake, Marceline or others into a single monochrome palette. Use warm/cool contrast to separate characters from dark backgrounds. Gold should signal rarity, rewards or important UI focus—not cover every object.

## 7. Discord presentation

Prepare art for three display contexts:
- **Large view:** full detail and character personality.
- **Embed view:** clear face, silhouette and main equipment.
- **Thumbnail/icon:** simplified focal point that remains recognizable.

Do not shrink a detailed portrait until its important features disappear. Use intentional crops and dedicated icon exports. The artwork must remain legible on mobile Discord clients.

## 8. Current mockup status

The existing PNG character roster is an early placeholder study and does **not** meet this updated quality bar. Keep the other UI, map, Rune and equipment concepts as provisional references where useful, but replace the character art with a new professional pass before treating it as final. Do not present the old 64×72 studies as the desired style.

## 9. Licensing and provenance

Adventure Time characters, recognizable designs, branding and signature items are protected franchise material. Any public or commercial release needs appropriate rights. A reference image, fan wiki page or search result is not a license.

Track source URL, creator, rights/permission, attribution requirements and repository path for each asset. Do not scrape or redistribute reference artwork without checking its terms.

## 10. References

- [Adventure Time — Cartoon Network](https://www.cartoonnetwork.com/)
- [Lospec Pixel Art Tutorials](https://lospec.com/pixel-art-tutorials)
- [Lospec Palette List](https://lospec.com/palette-list)
- [Aseprite](https://www.aseprite.org/)
- [Visual Examples](VISUAL_EXAMPLES.md)
