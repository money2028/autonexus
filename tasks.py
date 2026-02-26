from crewai import Task
from agents import researcher_agent, sales_agent, finance_agent, ceo_agent

research_task = Task(
    description="今天扫描最高ROI机会（微信电商客服自动化），输出3个具体方案+预计首月利润（RMB）",
    agent=researcher_agent,
    expected_output="带数字的3个方案"
)

sales_task = Task(
    description="根据research输出，生成10条微信+邮件cold outreach文案，定价499/1999/2999元/月",
    agent=sales_agent,
    expected_output="文案列表 + 发送计划"
)

finance_task = Task(
    description="假设已有1个客户，计算月利润、提出优化建议（定价/成本），输出仪表盘",
    agent=finance_agent,
    expected_output="利润报告 + 下一周行动"
)

ceo_task = Task(
    description="作为CEO最终拍板，整合所有输出，给出本周执行计划和预计利润",
    agent=ceo_agent,
    expected_output="完整董事会周报"
)
