# Reference Code
# https://geekswipe.net/technology/computing/analyze-chromes-browsing-history-with-python/

import os
import sqlite3
from urllib.parse import urlparse


def analyze(results, sort=False):
    # by default, history is chronological
    # to sort by most visited to least
    if sort:
        results = sorted(results.items(), key=lambda kv: (
            kv[1], kv[0]), reverse=True)

    # (domain, visit_count)
    for result in results:
        print(*result)


def getHistory(parseURL=False):
    # {url : visit_count}
    sites = {}

    # path to user's history database (Chrome)
    history_db = os.path.expanduser('~') + \
        r"\AppData\Local\Google\Chrome\User Data\Default\History"

    # querying the db
    c = sqlite3.connect(history_db)
    cursor = c.cursor()
    select_statement = "SELECT urls.url FROM urls"
    cursor.execute(select_statement)
    results = cursor.fetchall()  # tuple of form -> (url,)

    for url in results:
        url = url[0]
        if parseURL:
            url = urlparse(url).netloc

        if url in sites:
            sites[url] += 1
        else:
            sites[url] = 1

    return sites


history = getHistory(parseURL=True)
analyze(history, sort=True)
