import os
import requests
from bs4 import BeautifulSoup


def download_page_content(url, folder_name="content_directory"):
    try:
        # Send a GET request to the URL and get the response object
        response = requests.get(url)

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, "html.parser")

        text_content = soup.get_text()

        # Create the directory if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Write the text content to a file in the specified directory
        with open(
            os.path.join(folder_name, "main_page_text.txt"), "w", encoding="utf-8"
        ) as txt_file:
            txt_file.write(text_content)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Define the URL
url = "https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/"

# Call the function and specify the folder_name where you want to save the text file
download_page_content(url, folder_name="content_directory")
