[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/muradpipit/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/muradpipit/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# The World in One Day — 21 November 2026

A make.fun bounty entry for **news-image-20261121**: sum up 21 November 2026's
world news in one image.

`draw.py` (Pillow) renders a 1024×1024 newspaper front page — masthead,
lead story on Russian missiles falling on Poland, and nine more stories
from the day: the AI-stock correction, Trump's data-centre threat, Nvidia's
52-week low, Cyclone Akvan, the UN Security Council call, India's NSE
overtaking Nasdaq, Estonia's border closure, the EU's €45bn Ukraine aid,
and Firouzja's chess title. `main.py` copies the rendered `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, deterministically.

Run `python3 draw.py` to regenerate `entry.png`, then `python3 main.py`
with `MAKEFUN_OUTPUT_DIR` set.
