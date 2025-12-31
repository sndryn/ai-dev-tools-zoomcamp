from jina import retrieve_webpage_content
import argparse


arg = argparse.ArgumentParser(description="Test webpage content retrieval")
arg.add_argument("url", type=str, help="The URL of the webpage to retrieve")

url = arg.parse_args().url
content = retrieve_webpage_content(url)
print(
    "Number of characters in the webpage:",
    len(content) if content else "Failed to retrieve content",
)
