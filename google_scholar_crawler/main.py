from scholarly import scholarly, ProxyGenerator
import json
import os
import sys
import time

SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']
MAX_RETRIES = 5


def use_free_proxies():
    """Route scholarly through rotating free proxies to dodge Google's block."""
    try:
        pg = ProxyGenerator()
        if pg.FreeProxies():
            scholarly.use_proxy(pg)
            return True
    except Exception as exc:
        print(f"Proxy setup failed: {exc}", file=sys.stderr)
    return False


def fetch_author():
    """Try direct first, then proxies, retrying on Google blocks."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            if attempt > 1:
                use_free_proxies()
            author = scholarly.search_author_id(SCHOLAR_ID)
            scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
            return author
        except Exception as exc:
            print(f"Attempt {attempt}/{MAX_RETRIES} failed: {exc}", file=sys.stderr)
            time.sleep(min(5 * attempt, 30))
    raise SystemExit("Failed to fetch Google Scholar data after retries.")


author = fetch_author()
author['updated'] = time.strftime('%Y-%m-%d %H:%M:%S')
author['publications'] = {v['author_pub_id']: v for v in author['publications']}
print(json.dumps(author, indent=2))

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
