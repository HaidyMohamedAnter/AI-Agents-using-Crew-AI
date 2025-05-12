import requests
from bs4 import BeautifulSoup
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

class WebSearchAgent:
    def __init__(self, keyword="AI ML", pages=3, output_file="wuzzuf_jobs.json"):
        self.keyword = keyword
        self.pages = pages
        self.output_file = output_file

    def scrape_jobs_from_wuzzuf(self):
        jobs = []
        for page in range(0, self.pages):
            url = f"https://wuzzuf.net/search/jobs/?a=hpb&q={self.keyword}&start={page}"
            try:
                response = requests.get(url, headers=HEADERS)
                soup = BeautifulSoup(response.content, "html.parser")

                for card in soup.select(".css-1gatmva"):  # job card
                    title = card.select_one("h2 a")
                    company = card.select_one(".css-17s97q8")
                    location = card.select_one(".css-5wys0k")
                    job = {
                        "title": title.text.strip() if title else None,
                        "company": company.text.strip() if company else None,
                        "location": location.text.strip() if location else None,
                    }
                    jobs.append(job)
            except Exception as e:
                print(f"[WebSearchAgent] Failed to fetch page {page}: {e}")

        return jobs

    def run(self):
        print("[WebSearchAgent] Starting job scraping from Wuzzuf...")
        results = self.scrape_jobs_from_wuzzuf()
        with open(self.output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"[WebSearchAgent] Scraped {len(results)} jobs and saved to {self.output_file}")
