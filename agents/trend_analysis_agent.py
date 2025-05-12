import json
from collections import Counter

class TrendAnalysisAgent:
    def __init__(self, input_file="structured_jobs.json", output_file="trend_summary.json"):
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        print("[TrendAnalysisAgent] Loading structured job data...")
        with open(self.input_file, "r", encoding="utf-8") as f:
            jobs = json.load(f)

        print(f"[TrendAnalysisAgent] Analyzing {len(jobs)} job entries...")

        title_counter = Counter()
        location_counter = Counter()
        skill_counter = Counter()

        for job in jobs:
            title_counter[job.get("title", "Unknown")] += 1
            location_counter[job.get("location", "Unknown")] += 1
            # لو في مرحلة لاحقة فيها skills ممكن تحللها هنا

        summary = {
            "top_titles": title_counter.most_common(10),
            "locations_distribution": location_counter.most_common(),
            "total_jobs": len(jobs)
        }

        with open(self.output_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        print(f"[TrendAnalysisAgent] Trend summary saved to {self.output_file}")
