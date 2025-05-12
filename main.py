import os
import sys

# أضف مسار agents إلى sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
agents_dir = os.path.join(project_root, "agents")
if agents_dir not in sys.path:
    sys.path.insert(0, agents_dir)

# استيراد الوكلاء
from agents.web_search_agent import WebSearchAgent
from agents.data_extraction_agent import DataExtractionAgent
from agents.trend_analysis_agent import TrendAnalysisAgent
from agents.report_writer_agent import ReportWriterAgent

def main():
    print("📊 Starting Market Intelligence Pipeline for AI/ML Jobs in MENA\n")

    # 1. Web Search Agent
    print("🔍 Running WebSearchAgent...")
    web_agent = WebSearchAgent(keyword="AI ML", pages=3, output_file="wuzzuf_jobs.json")
    web_agent.run()

    # 2. Data Extraction Agent
    print("📄 Running DataExtractionAgent...")
    extract_agent = DataExtractionAgent(input_file="wuzzuf_jobs.json", output_file="structured_jobs.json")
    extract_agent.run()

    # 3. Trend Analysis Agent
    print("📈 Running TrendAnalysisAgent...")
    trend_agent = TrendAnalysisAgent(input_file="structured_jobs.json", output_file="trend_summary.json")
    trend_agent.run()

    # 4. Report Writer Agent
    print("📝 Running ReportWriterAgent...")
    report_agent = ReportWriterAgent(input_file="trend_summary.json", output_file="Top_AI_ML_Jobs_Report_May2025.md")
    report_agent.run()

    print("\n✅ All agents completed successfully. Report generated.")

if __name__ == "__main__":
    main()

