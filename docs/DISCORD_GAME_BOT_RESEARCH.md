# Discord Game Bot Research — 40 References

> Research snapshot: **7 November 2026**. This is a curated design study, not a claim that every bot was exhaustively tested in a live server. The strongest candidates were checked against official sites, official guides or current listings; smaller listings are clearly marked as low-confidence examples. Bot features, invite links, ownership and availability can change.

## 1. Executive summary

The most useful conclusion is not “copy the most popular bot.” Successful Discord game loops solve different jobs:

1. **Discovery and collection** make players curious enough to return.
2. **Private progression screens** let a player make progress without requiring other people to be online.
3. **Readable, button-driven battles** keep gameplay inside Discord rather than sending users to a separate app.
4. **Deck-building and run choices** create strategic replayability.
5. **Quests, archive goals and cosmetics** create long-term goals without making the player grind every day.

For this project, the strongest bot references are:

- **Collection / archive:** Pokétwo, PokéMeow, Karuta, SOFI, Gachord and Lumina.
- **Solo Discord RPG presentation:** Levlix, EnderBot and Legends of Discord.
- **Deck / team / PvE loop:** WildCards and Beastly Dungeons (both are smaller, less-proven references than the established collection bots).
- **Combat readability and rules:** Avrae, EPIC RPG and Dice Maiden.
- **Progression and side activities:** Dank Memer, TacoShack, Virtual Fisher and AestherBot.

The design still takes its central combat inspiration from Slay the Spire, Persona and Balatro. Discord bots are useful mainly for the way the game is delivered, collected, navigated and persisted.

## 2. Deep case studies

### 2.1 Pokétwo — discovery, collection and a recognizable battle screen

Links: [Official site](https://poketwo.net/) · [Official docs](https://docs.poketwo.net/) · [Spawning and catching guide](https://docs.poketwo.net/basics/spawning-and-catching) · [Top.gg listing](https://top.gg/bot/716390085896962058)

**What it does:** creatures appear based on server activity; users catch and collect them, complete a Pokédex, trade, and use teams in 3v3 battles. The official site also highlights filters, time/weather, shiny hunting and form changes.

**What we should learn:**
- Make discoveries feel like moments, not just inventory rows.
- Build an archive with completion tracking, rarity, variants and filters.
- Present a three-member team clearly.
- A battle screen should communicate sides, HP, active unit and action state at a glance.
- An encounter should be quick to understand and have a satisfying reveal.

**What we should change:** Pokétwo's natural activity spawns and first-claim race depend on a live social server. Our game is single-player, so each Rift encounter must create a personal instance for its owner. No race to claim, no player trading, no Pokémon, Poké Balls, copied move names, creature designs or franchise assets.

### 2.2 PokéMeow — a structured collection routine

Links: [Official site](https://pokemeow.com/) · [Official wiki](https://pokemeow.com/wiki/) · [Starting guide](https://pokemeow.com/wiki/starting-guide/)

**What it does:** collection, catching, team and trainer battles, quests, checklists, daily rewards and rotating events.

**What we should learn:**
- Use an optional daily checklist to remind players of varied activities.
- Give collection goals a clear next step.
- Make a three-slot team simple to inspect and manage.
- Use events to rotate objectives and reward different play styles.

**What we should change:** daily goals should be optional, should not require server activity or another player, and should not punish missed days. No copied Pokémon content or PvP.

### 2.3 Karuta — card ownership as a collectible object

Links: [Official site](https://karuta.com/) · [Studio / card information](https://karuta.com/studio/)

**What it does:** collectible character cards, editions/conditions, card customization, collection and trading.

**What we should learn:**
- A character/card should have a compelling presentation beyond its combat stats.
- Variants, frames, art treatments and collection completion can provide long-term goals.
- A collection viewer needs sorting, filtering and detailed card inspection.

**What we should change:** cosmetics and variants must use original art and must not create a paid combat advantage. Do not copy anime characters or Karuta's art.

### 2.4 SOFI — inventory, tagging and collection management

Links: [Official guide](https://guide.sofi.gg/) · [General commands](https://guide.sofi.gg/general-commands) · [Tasks and quests](https://guide.sofi.gg/tasks-quests)

**What it does:** card collection, detailed filtering/sorting, wishlists, inventory, card cosmetics, tags, albums, achievements, tasks, events and raids.

**What we should learn:**
- The Archive needs search, tags, sort, filters, favorites and missing-item views.
- Let players save a wishlist of cards or unlocks they want.
- Use cosmetics as personalization, not power.
- Daily, weekly and chapter objectives should ask for different kinds of play.

**What we should change:** SOFI's guilds, server-wide raids and trading are explicitly out of scope. We should not make collection completion dependent on other people.

### 2.5 Gachord — a configurable card catalog and protection against bad luck

Links: [Official site and live demo](https://gachord.com/) · [Commands](https://gachord.com/commands) · [Admin guide](https://gachord.com/admin) · [FAQ](https://gachord.com/faq)

**What it does:** custom card catalogs, packs, sets, card variants, drop spawners, pity counters and several table/card games. Its site describes configurable drop rates and pity rules.

**What we should learn:**
- Build internal card-authoring tools so content can be created without hand-editing code.
- Support card variants and set/collection completion.
- If random acquisition is ever added, publish probabilities and use duplicate protection / pity.
- A small visual puzzle can make an encounter more memorable than a pure “claim” button.
- Separate catalog data, card artwork, variant rules and drop tables.

**What we should change:** our core character and card unlocks should have deterministic paths. Any randomized pack is optional and earnable; no wagering, player-to-player trade or multiplayer TCG table is part of this game.

### 2.6 Levlix — one of the closest references for solo RPG screens in Discord

Links: [RPG overview](https://levlix.io/features/rpg) · [RPG documentation](https://levlix.io/docs/features/rpg/overview) · [Module guide](https://levlix.io/docs/guides/modules/rpg)

**What it does:** a text-channel RPG with character classes, skills, equipment, hunts, generated dungeons, pets and other progression. Its documentation says ordinary fights can resolve automatically while elites and bosses are fought manually. Its solo screens are private by default; some party, guild, market, arena and raid features also exist. The RPG module is currently labelled beta in its documentation.

**What we should learn:**
- Treat the private solo screen as the player's personal game window.
- Use one navigation surface with clear Back/Home paths.
- Distinguish low-friction encounters from deliberate boss fights.
- Make each character archetype play differently, not just display different class names.
- Save state independently of the Discord message.

**What we should change:** the project's multiplayer systems, market, parties, raids and arena are not adopted. We are not copying its classes, UI or content. The beta status is a reminder to test implementation maturity rather than assume every feature is production-ready.

### 2.7 EnderBot — a useful in-Discord dungeon walkthrough

Links: [Official site and interactive preview](https://ender.gg/) · [Getting started guide](https://ender.gg/wiki/guides/getting-started)

**What it does:** an RPG with cards, a dungeon, pets, a farm and a resource loop. Its site shows a compact three-floor dungeon, a boss at the end, a small set of clear actions, and a boon choice after each floor.

**What we should learn:**
- A short run with a few clearly differentiated decisions is a good Discord format.
- Show the available action choices instead of hiding the rules in long text.
- Offer a small selection of mutually exclusive floor boons.
- Make the pet / companion layer optional and easy to manage.
- Give the player a readable summary after defeat or victory.

**What we should change:** do not copy its resource loop or punitive loot-loss rules. Our combat is card-driven and turn-based, and the player should not be forced to grind resources before engaging with it.

### 2.8 Legends of Discord — button-first dungeon navigation

Link: [Top.gg listing](https://top.gg/bot/876046855614627882) · [Creator's itch.io page](https://hamzalopode.itch.io/legendsofdiscord)

**What it does:** the listing describes a dungeon crawler navigated with buttons and a same-message interface, random dungeons and gear, quests and bosses every few floors. The listing also states it is still in development and has a small review sample.

**What we should learn:**
- One command should enter the game; buttons should handle most navigation.
- Editing the same message is much cleaner than sending a new message for every room.
- Random routes and generated loot can make repeated journeys feel different.

**Evidence caution:** the listing is a design example, not proof of large-scale success or a benchmark for quality.

### 2.9 WildCards — a direct card-RPG comparison

Links: [Top.gg listing](https://top.gg/bot/1235064105098936372) · [Official site linked from listing](https://top.gg/bot/1235064105098936372)

**What it does:** its current listing describes a card RPG with collection, team building, PvE floors, bosses, roguelike progression and other social modes. It advertises over 1,500 cards and 300+ PvE floors, alongside PvP, raids and trading.

**What we should learn:**
- The collection can become the source material for a PvE campaign.
- The player should build a team from owned cards, then take it through floors and bosses.
- Content volume and run progression are connected rather than separate menus.

**What we should change:** adopt only the solo PvE progression idea. No PvP, raids, trading or multiplayer economy. The numbers are the bot's own listing claims, not an independent verification of content depth.

### 2.10 Avrae — combat state and rules presentation

Links: [Official site](https://avrae.io/) · [Documentation](https://avrae.readthedocs.io/en/latest/) · [GitHub](https://github.com/avrae/avrae)

**What it does:** D&D character-sheet integration, dice expressions, initiative tracking, combatants, HP, AC, resistances and status tracking.

**What we should learn:**
- Treat combat as explicit state, not just a sequence of chat messages.
- Maintain a structured combat log with action, target, modifier and result.
- Keep status effects and durations visible.
- Separate game rules from the command / message interface.

**What we should change:** our combat should be easier to understand than a full tabletop rules engine. The player should not need to memorize a large tabletop ruleset.

### 2.11 Dank Memer — varied side activities and content cadence

Links: [Official site](https://dankmemer.lol/)

**What it does:** a large economy/social game with items, fishing, NPCs, challenges, pets, farming and other activities.

**What we should learn:**
- Side systems can give players alternative ways to make progress.
- NPCs and quests can connect otherwise separate activities.
- A living item catalogue gives the game more than one source of rewards.

**What we should change:** do not reproduce robbing, gambling, spam-oriented grind or a bloated economy. Side activities should support the RPG, not replace combat.

### 2.12 TacoShack — idle management without another combat system

Links: [Official site](https://tacoshack.dev/) · [Official Discord server](https://discord.com/servers/tacoshack-official-server-495827872292929538)

**What it does:** an incremental management game built around upgrades, employees, ads, customers, locations, tasks and events.

**What we should learn:**
- A modest idle/dispatch layer can make progress continue between active runs.
- Upgrades should unlock new decisions or regions.
- Use short objectives and events to vary the routine.

**What we should change:** do not introduce a second full management game. Dispatch should be a small optional support feature, not a mandatory energy timer or grind gate.

## 3. Curated scan of 40 bots and what we take from each

The first 15 entries below are the strongest reference set for this project. Later entries are useful for particular subsystems, but should not be read as endorsements or proof that the bot's entire design is successful.

| # | Bot / reference | Link | Useful idea to adapt | What we do not adopt / evidence note |
|---:|---|---|---|---|
| 1 | **Pokétwo** | [Site](https://poketwo.net/) · [Docs](https://docs.poketwo.net/) | Encounter reveal, archive/Dex, filters, three-member team and battle readability | No franchise IP, claim race, trading or PvP |
| 2 | **PokéMeow** | [Site](https://pokemeow.com/) · [Wiki](https://pokemeow.com/wiki/) | Collection checklist, quests, events, team and progress goals | No Pokémon content, server competition or required daily grind |
| 3 | **Mudae** | [Help](https://mudae.net/bot/help) | Wishlists, search/filter tools, profile arrangement, collection milestones and badges | No anime IP, claim sniping, claim race or competitive server collection |
| 4 | **Karuta** | [Site](https://karuta.com/) | Card presentation, editions/conditions, cosmetic customization and collection display | No external copyrighted roster, trading or value speculation |
| 5 | **SOFI** | [Guide](https://guide.sofi.gg/) | Deep inventory filters, tags, wishlists, cosmetics, tasks and achievements | No guilds, global raids, trading or server-wide competition |
| 6 | **Lumina** | [Site](https://luminabot.net/) | Frames, fonts, stickers, animated effects and player-personalized cards | No anime roster or trading; keep animation optional and lightweight |
| 7 | **Gachord** | [Site](https://gachord.com/) | Custom card catalog, variants, sets, pity safeguards and puzzle-based claim ideas | No paid power, wagers or PvP table games; small-card content tooling only |
| 8 | **Kyuu** | [Top.gg](https://top.gg/bot/777894474079666227) | Cross-category card catalog, personal collection and duplicate-management ideas | Listing has modest evidence; do not build a social card market |
| 9 | **TBOT** | [Top.gg](https://top.gg/bot/884898667486654514) | Card fusion, custom profile presentation, chest and collection UI ideas | Avoid loot-box dependence, IP roster and unbounded power creep |
| 10 | **GPKdex** | [Top.gg](https://top.gg/bot/1441613547829334166) | Set completion, duplicate-to-craft variants, puzzle pieces and collection XP | Tiny/newer listing and external card IP; treat as feature inspiration only |
| 11 | **PokéCards** | [Top.gg](https://top.gg/bot/1521832704411439224) | Three-card expedition idea, region quests, card grading and fragments | Only a handful of listed servers/reviews at research time; low-confidence concept reference, no Pokémon IP |
| 12 | **PokéTCB** | [Top.gg](https://top.gg/bot/697251439684223056) | Card grading, collection filters, daily quests, sets and seasonal goals | Pokémon IP; no need for a season pass in our first release |
| 13 | **Munch (retired)** | [Top.gg](https://top.gg/bot/717368969102622770) | Historical example of chat-activity card drops and catalog collecting | Listing states it is retired; lesson: hosting, maintenance and migration matter as much as mechanics |
| 14 | **Levlix** | [RPG page](https://levlix.io/features/rpg) · [Docs](https://levlix.io/docs/features/rpg/overview) | Private solo screens, class identity, hunts, dungeons, manual boss fights and persistent state | RPG module is labelled beta; exclude parties, guilds, raids, arena and player market |
| 15 | **EnderBot** | [Site](https://ender.gg/) · [Guide](https://ender.gg/wiki/guides/getting-started) | Compact dungeon preview, three-floor pacing, boss end point, boon choices, pet progression | Do not copy its economy, punitive loot-loss or social organization mechanics |
| 16 | **Legends of Discord** | [Top.gg](https://top.gg/bot/876046855614627882) · [itch.io](https://hamzalopode.itch.io/legendsofdiscord) | Button-first single-message dungeon navigation and random gear | Listing says development is ongoing and review sample is small |
| 17 | **EPIC RPG** | [Top.gg](https://top.gg/bot/555955826880413696) · [Commands wiki](https://epic-rpg.fandom.com/wiki/Commands) | Long-form area unlocks, dungeons, equipment, bosses and quest progression | Its listing calls combat simple and includes PvP/co-op/gambling; those are not our combat model |
| 18 | **OwO** | [Top.gg](https://top.gg/bot/owo) | Hunt / zoo / pet collection, equipment and a companion-oriented collection loop | No user-versus-user animal battles, gambling or social leaderboard dependence |
| 19 | **Epic Quest** | [Top.gg](https://top.gg/bot/1220826504905363526) | Enemy elemental affinities, weapon/skill builds, exploration and boss-gated areas | Listing describes party/world-boss/guild features; keep only solo enemy/build ideas; small sample |
| 20 | **Beastly Dungeons** | [Top.gg](https://top.gg/bot/1401528604101185536) | Three-slot deck, dungeon floors, bosses and build-changing artifacts | Very small review sample; treat as a design sketch, not a proven quality benchmark |
| 21 | **WildCards** | [Top.gg](https://top.gg/bot/1235064105098936372) | Collection feeding a card-team PvE floor progression loop | No PvP, raids, market or trading; listing figures are promotional claims |
| 22 | **DeltaCord** | [Top.gg](https://top.gg/bot/1492087180070359111) | Story-driven turns, scouting, item choice, routes and consequences | One-server / no-review listing at research time; inspired by an existing franchise, so no copied content |
| 23 | **AestherBot** | [Site](https://spartanbots.github.io/AestherBot/) | Companion collection, pet training, biome unlocks, skilling and pity protection | Avoid 99-level grind, paid boosts and gambling; pet battle is not our main loop |
| 24 | **Avrae** | [Site](https://avrae.io/) · [Docs](https://avrae.readthedocs.io/en/latest/) | Initiative, health/status bookkeeping, structured combat actions and event log | Do not inherit tabletop complexity or require DM/player co-operation |
| 25 | **Dice Maiden** | [GitHub](https://github.com/Humblemonk/DiceMaiden) | Transparent dice expressions, visible roll breakdown and command ergonomics | No hidden rolls in core combat; our random outcomes need a deterministic server-side log |
| 26 | **Dank Memer** | [Site](https://dankmemer.lol/) | Side activity variety, NPCs, quests, pets and a broad item catalogue | Exclude crime/rob, gambling and repetitive activity spam |
| 27 | **TacoShack** | [Site](https://tacoshack.dev/) · [Discord](https://discord.com/servers/tacoshack-official-server-495827872292929538) | Incremental upgrades, optional idle tasks, new location unlocks and recurring objectives | Do not let idle timers replace active RPG play |
| 28 | **UnbelievaBoat** | [Site](https://unbelievaboat.com/) · [Guides](https://faq.unbelievaboat.com/guides/overview/) | Categorized shop items, money sinks, balance limits and audit logs | Casino games, crime, player transfers and server economy are out of scope |
| 29 | **Tatsu** | [Economy page](https://tatsu.gg/economy) | Profile presentation, badges/accolades, reward shop and clear item catalogue | No global currency or message-volume pay-to-progress loop |
| 30 | **Mimu** | [Docs](https://docs.mimu.bot/) · [Currency guide](https://docs.mimu.bot/currency-system/getting-started) | Simple commands, configurable features and clear user-facing help | Its per-server shared currency and gambling commands are not adopted |
| 31 | **NadekoBot** | [Docs](https://docs.nadeko.bot/) | Open-source deployment patterns, modular commands and permission/configuration design | It is a general-purpose bot, not a combat benchmark; no need to copy its broad scope |
| 32 | **Virtual Fisher** | [Guide](https://virtualfisher.com/guide.php) · [Features](https://virtualfisher.com/index/data.php) | Biome unlocks, gear upgrades, permanent boosts and prestige decisions | Fishing cooldown loops and clan bonuses are not central to our game |
| 33 | **FishingRPG** | [Top.gg](https://top.gg/bot/1209026334970482698) | Bestiary, seasons/weather, pet care, aquarium collections and quests | Listing has very few reviews; side-system inspiration only |
| 34 | **MooLoot** | [Top.gg](https://top.gg/bot/1146766407271469126) | Pets, quests, crafting, economy categories and localization | Do not reproduce a general server toolkit or player economy |
| 35 | **Idle Slayer** | [Top.gg](https://top.gg/bot/805946990176894976) | Rebirth/prestige as an optional long-term reset with permanent choices | Listing identifies early development; not a production benchmark; no gambling |
| 36 | **Just Fish** | [Top.gg](https://top.gg/bot/947700634373742653) | Button-based navigation through profile, inventory, shop and biomes | Very small review sample; borrow only interaction simplicity |
| 37 | **GamesROB** | [Top.gg](https://top.gg/bot/383995098754711555) | Small standalone games can support short breaks and varied objectives | Most games are social/competitive; only independent solo puzzles are relevant |
| 38 | **TriviaBot** | [Official help](https://triviabot.co.uk/help/) · [GitHub](https://github.com/brainboxdotcc/triviabot) | Short quizzes, categories, quickfire rounds, statistics and achievements | Use original lore/Bestiary questions; no dependence on a live external trivia API |
| 39 | **MiniGames** | [Top.gg](https://top.gg/bot/1285070559087951974) | Small solo word, riddle, flag and reflex games with a simple currency reward | Exclude betting, slots and member-versus-member modes |
| 40 | **GarticBOT** | [Official Gartic Discord](https://discord.com/servers/469229972641284097) | Visual drawing/puzzle events can add variety outside combat | Group drawing is not a fit for the core solo campaign; at most use occasional personal picture puzzles |

## 4. What to build from this research

### Adopt now

| System | Best reference | Our adaptation |
|---|---|---|
| Encounter discovery | Pokétwo, PokéMeow | Personal Rift prompts and private investigation instances |
| Archive / collection | Pokétwo, Karuta, SOFI, Gachord | Filterable personal Archive with variants, tags, wishlist and Bestiary |
| Button-based solo navigation | Levlix, Legends of Discord, EnderBot | One V2 Hub and one battleboard per player's active run |
| PvE floor / run progression | Slay the Spire, EnderBot, WildCards | Branching solo Expedition with fights, elite, events, shop, shrine and boss |
| Tactical enemy state | Avrae, EPIC RPG, Levlix | Enemy intent, target, status, weakness, Stability and boss phases |
| Character identity | Persona, Levlix | Three distinct personal decks, passives and signature actions |
| Run synergy | Balatro, Slay the Spire | Rank/Sigil Patterns and rule-changing Relics |
| Optional long-term goals | SOFI, PokéMeow, Dank Memer | Personal quests, chapter objectives, mastery and collection completion |
| Optional side progression | TacoShack, Virtual Fisher, AestherBot | Small solo dispatch / biome unlock track, never an energy gate |
| Card content tooling | Gachord | Data-driven card catalogue, variants, reward pools and preview tools |

### Explicitly do not build

- PvP, Co-op, guilds, global raids, party dungeons, trading, player markets or shared currencies.
- A first-click claim race for rare spawns.
- A mandatory daily streak or high-frequency message-spam reward loop.
- Gambling, wagers, casino loops or paid random combat power.
- A permanent stat ladder that overwhelms tactical decisions.
- A separate card game unrelated to the combat system.
- A full second management/fishing/farming game that distracts from the main RPG.
- Copied Pokémon, anime, Persona, Balatro or Slay the Spire characters, names, artwork, logos, dialogue, music or franchise-specific UI.

## 5. Reference images and interface examples

These are external inspiration images only. They are not project assets and must not be shipped as game art.

### Pokétwo-style encounter and battle readability

![Pokétwo battle interface example](https://i.imgur.lol/705BKir.png)

Source: [Discord bot listing image](https://discordbotlist.com/bots/poketwo). We take the clear sides/HP/active battle presentation, not the Pokémon art or player-versus-player format.

### Card collecting and drop presentation

![Karuta card drop example](https://cdn.techgyd.com/karuta-bot-discord.jpg)

Source: [TechGyd Karuta overview](https://www.techgyd.com/karuta-bot/50185/). We take the visual reveal and card identity, not the copyrighted characters.

### Slay the Spire combat hand and enemy intent

![Slay the Spire combat screen](https://cdn-ilagipn.nitrocdn.com/splvaRIRHyNATOPdyhWgNgSXoDwgWUOO/assets/images/optimized/rev-f41352c/cdn.vox-cdn.com/thumbor/vcjKa0jC3Cz-b-AP9jGJLpiFysM%3D/0x0%3A1920x1080/1200x0/filters:focal(0x0:1920x1080):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/13669198/Slay_The_Spire_Screenshot_2019.01.04___14.27.18.28.png)

Source: [The Mechanics of Magic analysis](https://mechanicsofmagic.com/2021/05/25/critical-play-is-this-game-balanced-slay-the-spire/). We take card-cost readability and enemy-intent planning.

### Balatro pattern / joker synergy

![Balatro interface example](https://images.pushsquare.com/screenshots/145246/large.jpg)

Source: [Push Square screenshot](https://www.pushsquare.com/reviews/ps5/balatro). We take visible patterns and build-defining passive synergies, not its poker presentation.

### Gachord collection UI example

![Gachord collection interface](https://gachord.com/static/img/landing/screens/collection.png?v=1782433058)

Source: [Gachord official site](https://gachord.com/). We take collection filtering and variant sorting as UX references.

### Persona turn handoff visual example

![Persona 5 Royal baton pass example](https://images.gamebanana.com/img/ss/mods/64f680630d760.jpg)

Source: [GameBanana image page](https://gamebanana.com/mods/466968). This is a third-party mod screenshot and is included only to communicate the feeling of a team handoff. The implementation must use original terminology and presentation.

## 6. Research method and limitations

- The set includes **40 bots**: collection/card bots, RPG/dungeon bots, economy/idle bots and short-game bots.
- The deeper case studies focus on the references closest to our core design: Pokétwo, PokéMeow, Karuta, SOFI, Gachord, Levlix, EnderBot, Legends of Discord, WildCards, Avrae, Dank Memer and TacoShack.
- Other entries are targeted subsystem scans: a feature or mechanic is recorded when a current official page, guide or directory listing describes it.
- An official feature page proves that the maker describes a feature; it does not prove the feature is balanced, popular or enjoyable.
- Directory review counts and server counts are snapshots and can change. Very small listings (for example PokeCards, Beastly Dungeons or DeltaCord) are marked as experimental references rather than popularity benchmarks.
- Retired projects are marked as retired. Beta/development projects are not treated as production benchmarks.
- No bot's entire economy, monetization, private backend or current live combat balance was reverse-engineered. This document is a design research map, not a claim of hands-on QA against all 40 bots.

## 7. Sources to revisit during production

- [Discord Developer Documentation — Components V2](https://discord.com/developers/docs/components/overview)
- [Discord Developer Documentation — Component Reference](https://discord.com/developers/docs/components/reference)
- [Discord Developer Documentation — Interactions](https://discord.com/developers/docs/interactions/receiving-and-responding)
- [Pokétwo Docs](https://docs.poketwo.net/)
- [PokéMeow Wiki](https://pokemeow.com/wiki/)
- [SOFI Guide](https://guide.sofi.gg/)
- [Mudae Help](https://mudae.net/bot/help)
- [Gachord Docs](https://gachord.com/commands)
- [Levlix RPG Docs](https://levlix.io/docs/features/rpg/overview)
- [EnderBot Guide](https://ender.gg/wiki/guides/getting-started)
- [Avrae Docs](https://avrae.readthedocs.io/en/latest/)

---
**Design conclusion:** use the Discord bots to learn collection, presentation, navigation, progression and persistence. Use Slay the Spire, Persona and Balatro to build the combat itself. Keep all of it inside a private single-player save and a Components V2 interface.
