#Problem 20: Web Scraper (Advanced)
#Create a program that extracts information from a website using a web scraping library like BeautifulSoup.

from bs4 import BeautifulSoup
import requests

# Example URL to scrape
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the title of the page
title = soup.title
print("Title of the page:", title.text)

# Find all the paragraph tags
paragraphs = soup.find_all("p")

# Print the text inside the first paragraph
if paragraphs:
    first_paragraph = paragraphs[0].text
    print("First paragraph:", first_paragraph)

