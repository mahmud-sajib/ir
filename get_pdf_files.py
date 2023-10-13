import os
import requests
from bs4 import BeautifulSoup


# Function to download all pdf files
def download_pdf_files(url, folder_name="content_directory"):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Parse the pdf content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Create the directory if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Find all hyperlinks present on the webpage
        links = soup.find_all("a")
        i = 0

        for link in links:
            href = link.get("href", "")

            # Check if the link contains ".pdf" and is not an anchor link
            if ".pdf" in href and not href.startswith("#"):
                # Send an HTTP GET request to the link
                link_response = requests.get(url + href)

                if link_response.status_code != 200:
                    continue

                i += 1
                file_name = os.path.join(folder_name, f"pdf{i}.pdf")
                print(f"Downloading file {i}: {url + href}")

                # Open the file in write mode with UTF-8 encoding
                with open(file_name, "w", encoding="utf-8") as file:
                    # Write the response content to the file
                    file.write(link_response.text)
                    print(f"pdf File {i} downloaded")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Define the URL
url = "https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/"

# Call the function and specify the folder_name where you want to save the pdf files
download_pdf_files(url, folder_name="content_directory")
