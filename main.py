from crewai import Crew, Process
from agents import ceo_agent, researcher_agent, sales_agent, executor_agent, finance_agent
from tasks import research_task, sales_task, finance_task, ceo_task
from dotenv import load_dotenv
load_dotenv()

crew = Crew(
    agents=[ceo_agent, researcher_agent, sales_agent, executor_agent, finance_agent],
    tasks=[research_task, sales_task, finance_task, ceo_task],
    process=Process.sequential,  # CEO最后决策
    verbose=2,
    memory=True
)

if __name__ == "__main__":
    print("🚀 AutoNexus AI 启动！海南纯盈利机器运行中...")
    result = crew.kickoff()
    print("\n=== 本周AI董事会报告 ===\n")
    print(result)
