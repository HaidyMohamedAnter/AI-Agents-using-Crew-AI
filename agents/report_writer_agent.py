import json

class ReportWriterAgent:
    def __init__(self, input_file="trend_summary.json", output_file="Top_AI_ML_Jobs_Report_May2025.md"):
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        print("[ReportWriterAgent] Loading trend summary data...")
        with open(self.input_file, "r", encoding="utf-8") as f:
            summary = json.load(f)

        print(f"[ReportWriterAgent] Generating report to {self.output_file}...")

        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write("# 📊 Top AI/ML Jobs in MENA – May 2025\n\n")
            f.write(f"**Total Jobs Analyzed:** {summary.get('total_jobs', 0)}\n\n")

            f.write("## 🏆 Top 10 AI/ML Job Titles:\n")
            for title, count in summary.get("top_titles", []):
                f.write(f"- {title} ({count} postings)\n")

            f.write("\n## 🌍 Job Distribution by Country/City:\n")
            for location, count in summary.get("locations_distribution", []):
                f.write(f"- {location} ({count} postings)\n")

        print(f"[ReportWriterAgent] Report saved to {self.output_file}")
