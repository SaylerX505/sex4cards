# Gold

**Catalogue ID (proposed): currency.gold** · **Status:** category only; economy rules open

## Identity

| Field | Detail |
|---|---|
| Display name | Gold |
| Type | Currency |
| Inventory representation | Numeric player balance, not an equipment instance |
| Reward context | Potential Auto Hunt and encounter reward |
| Status | Proposed category |

## Known direction

Gold has been listed as a possible reward category. Its use as a spendable economy currency is expected but no specific merchant price, upgrade cost, entry fee or purchase rule has been approved.

## Economy fields still open

- Earning sources and reward ranges.
- Shops and merchant inventory.
- Upgrade, crafting or service costs.
- Whether Gold is used in the Hollow Crypt or only in the permanent economy.
- Balance cap, transfer/trading rules and anti-abuse controls.
- Refund and transaction history behavior.

## UI requirements

Show the current balance in profile/inventory views, record every credit/debit as a ledger transaction and prevent repeated Discord interactions from charging or granting the same amount twice.

## Implementation boundary

Do not invent prices, daily grants, caps or exchange ratios. Gold is a candidate economy category until its spend sinks and acquisition rules are designed.
