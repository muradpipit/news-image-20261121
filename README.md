[![make.fun](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/competitions/news-image-20261121)
[![Bounty: news-image-20261121](https://img.shields.io/badge/bounty-news--image--20261121-blue)](https://make.fun/competitions/news-image-20261121)
[![Repo: muradpipit/news-image-20261121](https://img.shields.io/badge/repo-muradpipit%2Fnews--image--20261121-green)](https://github.com/muradpipit/news-image-20261121)

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
