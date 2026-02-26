from langchain.tools import tool
from duckduckgo_search import DDGS

@tool
def web_search(query: str) -> str:
    """免费实时搜索工具 - 用于扫描市场机会"""
    try:
        with DDGS() as ddgs:
            results = [r['body'] for r in ddgs.text(query, max_results=5)]
        return "\n".join(results)
    except:
        return "搜索工具暂不可用，请稍后重试"