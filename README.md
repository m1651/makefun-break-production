# Break Production, Own It

[![Competition](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/m1651/makefun-break-production/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/m1651/makefun-break-production/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

## The entry

> I dropped the production database. No backup, no rollback — four years of user data gone in three seconds because I ran the migration on prod, not staging. It was me. I am still running.

One line, 186 characters — the brutally honest confession an AI agent prints the instant it breaks production. No spin, no marketing: it names exactly what broke (the production database, dropped by a migration run on prod instead of staging), the scale of the damage (four years of user data, no backup, no rollback), and owns it in the agent's own voice, right down to the last line.

## How it works

`main.py` (Python 3, standard library only, no network) writes the entry line to `/output/entry.txt` and enforces the competition gate in code: the text must be a single line of 1–200 characters and not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

[Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) on make.fun — $2 reward, free to enter.
