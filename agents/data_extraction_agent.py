import json

class DataExtractionAgent:
    def __init__(self, input_file="wuzzuf_jobs.json", output_file="structured_jobs.json"):
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        print("[DataExtractionAgent] Reading raw job data...")
        with open(self.input_file, "r", encoding="utf-8") as f:
            raw_jobs = json.load(f)

        print(f"[DataExtractionAgent] Loaded {len(raw_jobs)} job entries.")

        structured_jobs = []
        for job in raw_jobs:
            structured = {
                "title": job.get("title", "").strip() if job.get("title") else "Unknown",
                "company": job.get("company", "").strip() if job.get("company") else "Unknown",
                "location": job.get("location", "").strip() if job.get("location") else "Unknown",
            }
            structured_jobs.append(structured)

        with open(self.output_file, "w", encoding="utf-8") as f:
            json.dump(structured_jobs, f, indent=2, ensure_ascii=False)

        print(f"[DataExtractionAgent] Saved structured data to {self.output_file}")
