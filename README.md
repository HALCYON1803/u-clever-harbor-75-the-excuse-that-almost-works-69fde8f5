[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/HALCYON1803/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/HALCYON1803/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

# The Excuse That Almost Works

One line a gamer texts the boss to skip work on GTA 6 launch week —
at most 20 words, one line of plain text, reading like a real message
sent in a hurry.

The excuse is built on a boring, specific workplace detail: locked out
of the office, with the spare key sitting in the desk drawer inside.
No dead grandmother, no flat tyre, no sudden fever — just the kind of
self-defeating logic a tired manager would almost believe.

## Entry

> Locked out of the office, spare key's in my desk drawer

11 words, 55 characters, one line, no trailing newline.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The program asserts the gate before writing: 1–140 characters, at most
20 words, a single line, then reads the file back and verifies it is
byte-identical to the excuse, with no trailing newline.
