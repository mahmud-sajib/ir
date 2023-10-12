import requests
from bs4 import BeautifulSoup


def download_page_content(url):
    try:
        # Send a GET request to the URL and get the response object
        response = requests.get(url)

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, "html.parser")

        text_content = soup.get_text()

        # Write the TXT content to a file
        with open(f"main_page_text.txt", "w", encoding="utf-8") as txt_file:
            txt_file.write(text_content)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Define the URL
url = "https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/"

# Call the function
download_page_content(url)
