import requests
from bs4 import BeautifulSoup

def scrape_article_titles(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the article titles
        titles = soup.find_all('h3')  # Adjust the tag and class based on the website structure

        # Print the titles
        print("Article Titles:")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.get_text()}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage:
news_url = 'https://www.bbc.com/news'  # Replace with the URL you want to scrape
scrape_article_titles(news_url)
