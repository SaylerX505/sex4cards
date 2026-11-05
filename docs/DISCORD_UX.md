# Discord User Experience

## 1. Discord is the game interface

The game is designed to be played inside Discord using:
- Slash commands.
- Buttons.
- Select menus.
- Embeds and message attachments.
- Edited interaction messages.
- Ephemeral/private responses where suitable.

A separate web game client is not required for the core game loop.

## 2. UX principles

- **Mobile first:** short labels, readable embeds and compact navigation.
- **Low spam:** edit existing status/battle messages instead of sending a new message for every action.
- **Clear state:** always show whose action is expected and what choices are valid.
- **Fast navigation:** provide Back, Cancel and page controls consistently.
- **Safe actions:** confirm irreversible or expensive actions.
- **Private where useful:** keep personal inventory and session controls private when public channel visibility adds no value.

## 3. Candidate command map

The following are suggested command names, not a finalized command contract:

| Command | Purpose |
|---|---|
| /profile | Player overview and progression |
| /team | View and edit the three-character team |
| /characters | Browse owned characters |
| /inventory | Browse owned items and materials |
| /equip | Equip or replace equipment |
| /battle | Enter a manual encounter/challenge |
| /hunt | Configure or inspect Auto Hunt |
| /crypt | Start or continue The Hollow Crypt |
| /help | Explain commands and game systems |

Commands may be renamed during implementation. Avoid creating a separate command for every tiny action if buttons can handle it contextually.

## 4. Main menu

A proposed main menu can group:
- Character Management.
- Team.
- Inventory.
- Activities (Battle, Auto Hunt, Crypt).
- Profile/Progress.

The menu should show the player's most relevant current state, not every statistic at once.

## 5. Battle interaction

A battle should use one main message where possible. Show:
- Round number.
- Three team members and their HP/Mana.
- Enemies and their health/status.
- Current acting character.
- Action controls.

When the player selects Skill, show only usable skills or clearly mark unavailable skills with their Mana requirement. Item selection should show eligible owned consumables.

After each valid action, update the battle view. Reject stale buttons after the turn changes.

## 6. Inventory and pagination

Discord component and embed limits mean large collections need pagination. Provide:
- Category filter.
- Page navigation.
- Sort order.
- Item detail view.
- Equip/unequip actions.

Never assume a player will be able to scroll a huge embed or read tiny text on a phone.

## 7. Auto Hunt UX

Suggested flow:
1. Select dungeon.
2. Select difficulty.
3. Select three characters.
4. Review session setup.
5. Start.
6. View a compact progress panel.
7. Receive a final report.

The background process should not post every run as a separate message. Provide a concise summary and a way to inspect detailed run history.

## 8. Hollow Crypt UX

Suggested flow:
1. Select difficulty and team.
2. Show map choices.
3. Select the next connected room.
4. Resolve room/event/battle.
5. Show rewards and temporary Run Relic choices.
6. Update map and team condition.
7. Continue, escape or finish.

Keep the map and run state visible through a single edited message when practical.

## 9. Interaction security

Every interaction must validate:
- The user owns the active session.
- The button belongs to the current state/version.
- The selected character/item belongs to the user.
- The action is currently legal.
- The action has not already been applied.

Do not trust a custom_id or client-submitted value as proof of ownership or eligibility.

## 10. Error messages

Errors should explain the reason and next action. Examples:
- "You don't have enough Mana. Choose Attack or Defend."
- "This item is already equipped by another character."
- "This session has ended. Start a new run to continue."
- "That menu has expired. Reopen your inventory."

## 11. Accessibility and localization

Use consistent terms, short descriptions and clear icon labels. Avoid relying only on color to communicate rarity or status. The initial project conversation is in Arabic, but code identifiers and canonical data keys should remain stable; localization can provide Arabic and English display strings later.
