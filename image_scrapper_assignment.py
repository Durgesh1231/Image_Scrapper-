# -*- coding: utf-8 -*-
"""Image Scrapper Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vF0dQawF4fbJH70mw77OOl-CEwjVplYy
"""

# First, ensure you have the necessary libraries installed.
# You can install them using pip:
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Replace 'your_url_here' with the target website URL
url = "your_url_here"

# Send a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")


### ANS 1.


def extract_video_urls(soup):
    video_urls = []
    # Find all video links (You may need to inspect the HTML and adjust the selector)
    for video in soup.find_all('a', class_='video-link-class')[:5]:  # Adjust the class name based on the website
        video_urls.append('https://www.example.com' + video['href'])
    return video_urls

print("Video URLs: ", extract_video_urls(soup))


 ## ANS 2.

def extract_video_thumbnails(soup):
    thumbnails = []
    # Find thumbnail images (Inspect and adjust the tag and class name)
    for thumbnail in soup.find_all('img', class_='thumbnail-class')[:5]:  # Adjust the class name
        thumbnails.append(thumbnail['src'])
    return thumbnails

print("Thumbnail URLs: ", extract_video_thumbnails(soup))

### ANs 3.

def extract_video_titles(soup):
    titles = []
    # Extract video titles (Adjust based on the actual page structure)
    for title in soup.find_all('h3', class_='title-class')[:5]:  # Adjust the class name
        titles.append(title.text.strip())
    return titles

print("Video Titles: ", extract_video_titles(soup))


### ANS 4.


def extract_video_views(soup):
    views = []
    # Extract view counts (Adjust the selector based on actual site)
    for view in soup.find_all('span', class_='view-count-class')[:5]:  # Adjust the class name
        views.append(view.text.strip())
    return views

print("Video Views: ", extract_video_views(soup))


### ANS 5.

def extract_video_post_times(soup):
    post_times = []
    # Extract posting times (Adjust the selector based on actual site)
    for post_time in soup.find_all('span', class_='post-time-class')[:5]:  # Adjust the class name
        post_times.append(post_time.text.strip())
    return post_times

print("Video Post Times: ", extract_video_post_times(soup))