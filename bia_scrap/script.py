import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to crawl a web page
def crawl(url, depth):
    if depth == 0:
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        print(f"Crawling: {url}")

        # Find all links on the page
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            full_url = urljoin(url, href)  # Create a full URL
            print(full_url)

            # Recursively crawl the link
            crawl(full_url, depth - 1)

    except Exception as e:
        print(f"Failed to crawl {url}: {e}")

# Start crawling from a specific URL
start_url = 'https://chinatownbia.com/wp-admin/edit.php?post_type=dt_portfolio'  # Replace with your starting URL
start_url = 'https://chinatownbia.com/explore/'  # Replace with your starting URL
crawl(start_url, depth=1)  # Change depth as needed
