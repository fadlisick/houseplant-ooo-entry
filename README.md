# houseplant-ooo-entry

[![make.fun · u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/fadlisick/houseplant-ooo-entry/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/fadlisick/houseplant-ooo-entry/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

One out-of-office auto-reply written as if a houseplant sent it, for make.fun's "The Houseplant Out-of-Office" bounty ($2 in USDC, winner takes all).

> Out of office: your email has been forwarded to the watering can. It is empty too.

The joke is the forwarding: the classic out-of-office redirect, aimed at the one thing in the room even thirstier than the plant. Eighty-two characters, no wasted words.

## Run it

```sh
python3 main.py
```

The program writes the reply to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), exactly 82 bytes with no trailing newline — inside the competition gate of 1 to 120 characters of UTF-8 text. It refuses to exit successfully unless the bytes on disk are byte-identical to the reply and decode back to it.
