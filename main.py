from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from crewai import Crew, Process
from agents import ceo_agent, researcher_agent, sales_agent, executor_agent, finance_agent
from tasks import research_task, sales_task, finance_task, ceo_task
from tools.custom_tools import web_search
from dotenv import load_dotenv
import os

load_dotenv()

# 注入工具
researcher_agent.tools = [web_search]

app = FastAPI(title="AutoNexus AI - 海南纯盈利Agent公司")

@app.get("/")
def home():
    return HTMLResponse("""
    <h1>🚀 AutoNexus AI 已就绪！</h1>
    <p>海南封关红利纯盈利机器</p >
    <p>访问 <a href=" ">/run</a > 立即运行董事会报告</p >
    """)

@app.get("/run")
def run_board_report():
    print("🚀 开始运行AI董事会报告...")
    crew = Crew(
        agents=[ceo_agent, researcher_agent, sales_agent, executor_agent, finance_agent],
        tasks=[research_task, sales_task, finance_task, ceo_task],
        process=Process.sequential,
        verbose=2,
        memory=True
    )
    result = crew.kickoff()
    return {
        "status": "success",
        "report": result,
        "message": "AutoNexus AI 本周董事会报告已生成！利润最大化模式运行中。"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
