import requests
from bs4 import BeautifulSoup


def download_txt_pdf_file(url):
    try:
        # Send a GET request to the URL and get the response object
        response = requests.get(url)

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all hyperlinks present on the webpage
        links = soup.find_all("a")

        # Initialize counters for PDF and TXT files
        pdf_count = 0
        txt_count = 0

        # Iterate through all links to check for PDF and TXT links
        for link in links:
            href = link.get("href", "")
            if href.endswith(".pdf"):
                # Get the response object for the PDF link
                pdf_response = requests.get(url + href)

                if pdf_response.status_code != 200:
                    continue

                pdf_count += 1
                print(f"Downloading PDF file {pdf_count}: {url + href}")

                # Write the PDF content to a file
                with open(f"pdf{pdf_count}.pdf", "wb") as pdf_file:
                    pdf_file.write(pdf_response.content)
                print(f"PDF file {pdf_count} downloaded")

            if href.endswith(".txt"):
                # Get the response object for the TXT link
                txt_response = requests.get(url + href)

                if txt_response.status_code != 200:
                    continue

                txt_count += 1
                print(f"Downloading TXT file {txt_count}: {url + href}")

                # Write the TXT content to a file
                with open(f"text{txt_count}.txt", "wb") as txt_file:
                    txt_file.write(txt_response.content)
                print(f"TXT file {txt_count} downloaded")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Define the URL
url = "https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/"

# Call the function
download_txt_pdf_file(url)
