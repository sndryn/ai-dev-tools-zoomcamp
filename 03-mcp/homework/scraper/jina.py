import requests


def retrieve_webpage_content(url):
    """Retrieve the content of a webpage given its URL."""
    try:
        response = requests.get(f"https://r.jina.ai/{url}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
