import requests
from bs4 import BeautifulSoup


# Function to download all HTML files
def download_html_files(url, limit=10):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all hyperlinks present on the webpage
        links = soup.find_all("a")
        i = 0

        for link in links:
            href = link.get("href", "")

            # Check if the link contains ".html" and is not an anchor link
            if ".html" in href and not href.startswith("#"):
                # Send an HTTP GET request to the link
                link_response = requests.get(url + href)
                print(link_response)

                if link_response.status_code != 200:
                    continue

                i += 1
                print(f"Downloading file {i}: {url + href}")

                # Open the file in write mode with UTF-8 encoding
                with open(f"yahoo{i}.html", "w", encoding="utf-8") as file:
                    # Write the response content to the file
                    file.write(link_response.content.decode("utf-8"))
                    print(f"HTML File {i} downloaded")

                if i >= limit:
                    break

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Define the URL
url = "https://news.yahoo.com/"

# Call the function
download_html_files(url, limit=10)
