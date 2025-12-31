from fastmcp import FastMCP
from scraper.jina import retrieve_webpage_content
from search.search import search as doc_search

mcp = FastMCP("Demo 🚀")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool
def fetch(url: str) -> str:
    """Retrieve the content of a webpage given its URL."""
    content = retrieve_webpage_content(url)
    return content


@mcp.tool
def search(query: str) -> str:
    """Search the FastMCP documentation for a query string."""

    results = doc_search(query, limit=3)
    formatted_results = "\n\n".join(
        [
            f"Filename: {res['filename']}\nContent Snippet: {res['content'][:500]}..."
            for res in results
        ]
    )
    return formatted_results


if __name__ == "__main__":
    mcp.run()
