#!/usr/bin/env python3
"""Generate static/api/statistics.json for the Download -> Statistics page.

The numbers come from the AWStats of build.openmodelica.org: every counter is
the sum row of one extra section (see scripts/awstats/extra-sections.conf),
read from awstats.pl?output=allextraN for each month.

Finished months never change, so they are taken from the previous
statistics.json and only the current and the previous month are asked for.
Without a previous file the script walks back through the whole history.

The AWStats login is read from the environment (AWSTATS_USER, AWSTATS_PASSWORD).
Without it, or when AWStats cannot be reached, the previous file is kept as it
is, so that the web page can always be built.
"""

import argparse
import base64
import datetime
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

# JSON key -> name of the AWStats extra section (ExtraSectionNameN)
SECTIONS = {
    "exe": ".exe downloads",
    "deb": ".deb downloads",
    "playground": "Playground hits",
}
MAX_SECTIONS = 20
# Walking back through the history stops after this many months without data.
EMPTY_MONTHS_TO_STOP = 12
FIRST_YEAR = 2005

TITLE_RE = re.compile(r'<td class="aws_title"[^>]*>(.*?)</td>', re.S)
ROW_RE = re.compile(r"<tr>\s*<td class=\"aws\">(.*?)</td>\s*<td>([^<]*)</td>", re.S)


def log(msg):
    print("statistics.py: " + msg, file=sys.stderr)


class AWStats:
    def __init__(self, url, config, user, password, timeout):
        self.url = url
        self.config = config
        self.timeout = timeout
        token = base64.b64encode(("%s:%s" % (user, password)).encode()).decode()
        self.headers = {"Authorization": "Basic " + token, "Accept-Language": "en"}
        self.numbers = None

    def fetch(self, year, month, output):
        query = urllib.parse.urlencode({
            "config": self.config, "year": year, "month": "%02d" % month,
            "output": output, "framename": "mainright", "lang": "en"})
        req = urllib.request.Request(self.url + "?" + query, headers=self.headers)
        with urllib.request.urlopen(req, timeout=self.timeout) as f:
            return f.read().decode("utf-8", errors="replace")

    def section_numbers(self, year, month):
        """Map our keys to the N of allextraN, from the section titles."""
        if self.numbers is None:
            self.numbers = {}
            names = {name: key for key, name in SECTIONS.items()}
            for n in range(1, MAX_SECTIONS + 1):
                title = parse_title(self.fetch(year, month, "allextra%d" % n), n)
                if title is None:
                    break
                if title in names:
                    self.numbers[names[title]] = n
            for key in SECTIONS:
                if key not in self.numbers:
                    log("AWStats has no extra section named '%s'" % SECTIONS[key])
        return self.numbers

    def month(self, year, month):
        res = {}
        for key, n in self.section_numbers(year, month).items():
            total = parse_total(self.fetch(year, month, "allextra%d" % n), n)
            if total:
                res[key] = total
        return res


def extra_table(page, n):
    pos = page.find('<a name="extra%d">' % n)
    return None if pos < 0 else page[pos:]


def parse_title(page, n):
    table = extra_table(page, n)
    m = TITLE_RE.search(table) if table else None
    if not m:
        return None
    # "NAME (Top 20) " -> "NAME"
    return re.sub(r"\s*\([^()]*\)\s*$", "", html.unescape(m.group(1))).strip()


def parse_total(page, n):
    """The hits of the sum row, which is the row with the bold first cell."""
    table = extra_table(page, n)
    if table is None:
        return None
    total = None
    for first, hits in ROW_RE.findall(table):
        if first.startswith("<b>"):
            digits = re.sub(r"[^0-9]", "", hits)
            total = int(digits) if digits else None
    return total


def prev_month(year, month):
    return (year - 1, 12) if month == 1 else (year, month - 1)


def load_previous(path, url):
    try:
        if path and os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        if url:
            with urllib.request.urlopen(url, timeout=60) as f:
                return json.load(f)
    except (OSError, ValueError) as e:
        log("cannot read the previous statistics: %s" % e)
    return None


def update(aws, months, today):
    """months: {"YYYY-MM": {key: hits}}, updated in place."""
    year, month = today.year, today.month
    full = not months
    empty = 0
    count = 0
    while year >= FIRST_YEAR:
        name = "%04d-%02d" % (year, month)
        data = aws.month(year, month)
        if data:
            months[name] = data
            empty = 0
        else:
            months.pop(name, None)
            empty += 1
        count += 1
        if full:
            if empty >= EMPTY_MONTHS_TO_STOP:
                break
        elif count >= 2:
            break
        year, month = prev_month(year, month)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--output", default="static/api/statistics.json")
    ap.add_argument("--previous", help="statistics.json of the previous run")
    ap.add_argument("--previous-url", default="https://openmodelica.org/api/statistics.json",
                    help="where to get the previous run from if --previous does not exist")
    ap.add_argument("--url", default="https://build.openmodelica.org/cgi-bin/awstats.pl")
    ap.add_argument("--config", default="build.openmodelica.org")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--full", action="store_true", help="read the whole history again")
    args = ap.parse_args()

    previous = load_previous(args.previous, args.previous_url) or {}
    months = {} if args.full else {m["month"]: {k: v for k, v in m.items() if k != "month"}
                                   for m in previous.get("months", [])}
    result = previous
    user, password = os.environ.get("AWSTATS_USER"), os.environ.get("AWSTATS_PASSWORD")
    if not user or not password:
        log("AWSTATS_USER/AWSTATS_PASSWORD are not set, keeping the previous statistics")
    else:
        today = datetime.datetime.now(datetime.timezone.utc).date()
        try:
            update(AWStats(args.url, args.config, user, password, args.timeout), months, today)
            result = {
                "updated": today.isoformat(),
                "months": [dict(month=name, **months[name]) for name in sorted(months)],
            }
        except (OSError, ValueError) as e:  # urllib errors are OSErrors
            log("cannot read AWStats (%s), keeping the previous statistics" % e)
    if not result:
        result = {"updated": None, "months": []}
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=1)
        f.write("\n")
    log("wrote %s with %d months" % (args.output, len(result.get("months", []))))


if __name__ == "__main__":
    main()
