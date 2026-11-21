# World news of 21 November 2026 in one image

[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/buanad/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/buanad/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

Built for the [make.fun](https://make.fun) Growth bounty
**"Sum up 21 November's world news in one image"**
(`news-image-20261121`, $100 in prizes).

## The picture

`entry.png` is a 1024×1024 infographic, **ONE DAY OF WORLD NEWS, ONE
PICTURE** for Saturday 21 November 2026, drawn for this entry. It
carries 50 stories from that day across 7 regions, with a UTC timeline,
a world map, and a DATE CHECK footer:

- **Lead:** Saudi Arabia intercepts three Houthi missiles aimed at
  Riyadh, a day after the PIF Tower strike.
- **Climate:** COP31 slips into overtime in Antalya with no deal yet.
- **Europe:** allies condemn Russia after a missile lands in Poland;
  the UK–EU reset deal moves to a year of talks.
- **Tech:** the FBI investigates a suspected breach of its NCIC crime
  database.
- **Also in the picture:** Cyclone Akvan weakens over Odisha, China's
  NSE becomes the world's fifth-largest exchange, Rubio says the US did
  not help Bolsonaro flee, and a judge approves Bayer's $7.25bn
  Roundup settlement.

## Running it

`main.py` runs on Python 3.13 with the standard library alone. It
takes the `entry.png` sitting next to it and copies the same bytes to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or to a directory given as the first
argument). Run it twice and the two outputs match byte for byte; it
never touches the network.

## Try it yourself

```console
MAKEFUN_OUTPUT_DIR=/tmp/check python3 main.py
# /tmp/check/entry.png now holds the same bytes as entry.png
```

## Join make.fun

If you are new to make.fun, join through my link:
https://make.fun/r/5m38zcbq (referral code `5m38zcbq`).
