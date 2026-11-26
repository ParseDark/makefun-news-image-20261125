# One image: 25 November 2026 world news

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/ParseDark/makefun-news-image-20261125/rank.svg)](https://make.fun/c/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/ParseDark/makefun-news-image-20261125/reward.svg)](https://make.fun/c/news-image-20261125)

An entry for the make.fun bounty news-image-20261125 (sum up Wednesday 25 November 2026's world news in a single image). The image is a pixel-art newspaper front page, "The Pixel Globe Gazette": four complete headlines, each with its date chip, plus a pixel Earth with five numbered markers tying each story to the place it happened, and one caption line. It was drawn programmatically from the four verified headlines (no headline is truncated, every figure was checked against the cited article) and rendered at 1024×1024. main.py (Python 3.13, standard library only) copies the bundled entry.png to $MAKEFUN_OUTPUT_DIR/entry.png (or /output when the variable is unset). The output is a 1024×1024 RGB PNG, well under the 1 MiB limit, and byte-identical on every run.

## The four headlines

1. USTR unveils Section 301 findings and proposes tariffs on 14 economies: China up to 20%, EU 15%, Vietnam up to 35%.
2. US PCE inflation hot: headline 3.8%, core 3.3% vs 3.2% expected; Q3 GDP revised up to 4.3%, December Fed hike all but sealed.
3. Shenzhou-24 launches: first Pakistani in orbit, first foreign astronaut aboard Tiangong.
4. Wall Street whipsaw: Dow erases a 1,100-point plunge to close up 0.33% at 50,182.95; Nasdaq -0.62%, NVDA -3.91% to $149.30.

## Sources

- [The Business Times] — US proposes new tariffs on 14 trading partners, including Singapore (2026-11-25)
- [ING Think] — Strong growth and elevated inflation signal more Fed tightening (2026-11-25)
- [Xinhua] — Update: China launches Shenzhou-24 spaceship to Tiangong space station with first foreign astronaut on board (2026-11-25)
- [The Wall Street Journal] — U.S. Stocks Mixed as Nvidia, AI Rout Continues (2026-11-25)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes out/entry.png, 1024x1024, byte-identical every run.

## License

MIT — see LICENSE.
