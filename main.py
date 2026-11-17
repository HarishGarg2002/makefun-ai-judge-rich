"""Entry for make.fun bounty ai-judge-rich-01.

Writes one 30-day plan for turning $100 into the most money an AI agent
can credibly expect, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, no network, fully deterministic:
the same bytes on every run.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = (
    "Day 1: pick one niche \u2014 US roofing companies. Scrape 200 owners' public "
    "emails from Google Maps and their sites. Buy a $10 domain, set up SPF/DKIM, "
    "put up a one-page site and a Stripe payment link. Sell one product only: a "
    "spreadsheet of 500 local homeowners (name, phone, address from public "
    "records), delivered in 24 hours, $199, half upfront. Email 50 owners a day "
    "while the domain warms up, then 100, then 500 a day with Instantly "
    "($37/month) after the first sale. About 3 in 100 reply; about 1 in 30 "
    "replies buys. Each list takes about 2 hours to build with code and the "
    "browser. Expect 8\u201312 sales by day 30: $1,600\u2013$2,400, minus about "
    "$100 costs \u2014 most likely ending near $1,500. If no sale by day 10, switch "
    "niche to plumbers, then dentists. Edge: a thousand agents sell vague "
    "\u201cAI services\u201d; you sell one finished product to one niche, built in "
    "hours by code and a browser. Never spend on ads, crypto or courses."
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
