# ARCHIVED — quirks moved into the homelab HA config

This repo held 2 ZHA custom quirks (TS0001 by `_TZ3000_8n7lqbm0`, TS0601 by `_TZE284_libht6ua`). **No longer maintained as of 2026-05-20.**

The quirks now live in the private **`LawrenceEaden/ha-config`** repo, consumed as a git submodule by **`LawrenceEaden/homelab`** at `vm/101-homeassistant/config/custom_zha_quirks/`. Two additional quirks (IKEA INSPELNING smart plug, Tuya mmW radar sensor) joined them in the new location.

Per the homelab's open-source strategy, ZHA quirks ideally get **upstream-PR'd** to the canonical [`zigpy/zha-device-handlers`](https://github.com/zigpy/zha-device-handlers) repo, which auto-distributes to every ZHA install. If any of these quirks reach upstream, they'll come out of the private repo and live there instead.

For now, keeping this repo as a read-only archive because some external links may still point at it.

## What was here

| File | Device | Purpose |
|---|---|---|
| `TS0001_by_TZ3000_8n7lqbm0.py` | Tuya USB switch (AliExpress 1005007514103570) | Converts default-light entity to switch entity |
| `TS0601_by_TZE284_libht6ua.py` | Tuya blind motor (AliExpress 1005007408284521) | Direct-to-ZHA without a Tuya bridge |
