from scholarly import scholarly, ProxyGenerator
import json
import os
import sys
import time

SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']
SCRAPER_API_KEY = os.environ.get('SCRAPER_API_KEY')
MAX_RETRIES = 3


def setup_proxy():
    """Route scholarly through ScraperAPI (residential proxies) to bypass Google's block."""
    if not SCRAPER_API_KEY:
        print("SCRAPER_API_KEY not set; trying direct connection.", file=sys.stderr)
        return False
    pg = ProxyGenerator()
    if pg.ScraperAPI(SCRAPER_API_KEY):
        scholarly.use_proxy(pg)
        return True
    print("ScraperAPI proxy setup failed.", file=sys.stderr)
    return False


def fetch_author():
    setup_proxy()
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            author = scholarly.search_author_id(SCHOLAR_ID)
            scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
            return author
        except Exception as exc:
            print(f"Attempt {attempt}/{MAX_RETRIES} failed: {exc}", file=sys.stderr)
            time.sleep(min(5 * attempt, 20))
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
