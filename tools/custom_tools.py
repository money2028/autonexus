from langchain.tools import tool

@tool
def web_search(query: str) -> str:
    """免费搜索工具"""
    from duckduckgo_search import DDGS
    with DDGS() as ddgs:
        results = [r['body'] for r in ddgs.text(query, max_results=5)]
    return "\n".join(results)
