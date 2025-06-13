import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_amazon(book_title, book_author):
    query = f"{book_title} {book_author} book"
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.amazon.in/s?k={encoded_query}"

    # Use a generic browser user-agent
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Failed to fetch Amazon page: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select_one("a.a-link-normal.s-no-outline")

    if result:
        href = result.get("href")
        return "https://www.amazon.in" + href
    else:
        return "No link found on Amazon"


# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# def search_flipkart(book_title, book_author):
#     query = f"{book_title} {book_author}"
#     encoded_query = urllib.parse.quote_plus(query)
#     url = f"https://www.flipkart.com/search?q={encoded_query}"

#     headers = {
#         "User-Agent": (
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#             "AppleWebKit/537.36 (KHTML, like Gecko) "
#             "Chrome/120.0.0.0 Safari/537.36"
#         )
#     }

#     response = requests.get(url, headers=headers)

#     if response.status_code != 200:
#         return f"Failed to fetch Flipkart page: {response.status_code}"

#     soup = BeautifulSoup(response.text, "html.parser")
#     link_tag = soup.select_one("a._1fQZEK, a.IRpwTa")

#     if link_tag and link_tag.get("href"):
#         return "https://www.flipkart.com" + link_tag["href"]
#     else:
#         return "No link found on Flipkart"


import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_flipkart(book_title, book_author):
    query = f"{book_title} {book_author}"
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.flipkart.com/search?q={encoded_query}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    with requests.Session() as session:
        response = session.get(url, headers=headers)
        if response.status_code != 200:
            return f"Failed to fetch Flipkart page: {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")
        link_tag = soup.select_one("a._1fQZEK, a.IRpwTa")

        if link_tag and link_tag.get("href"):
            return "https://www.flipkart.com" + link_tag["href"]
        else:
            return "No link found on Flipkart"
