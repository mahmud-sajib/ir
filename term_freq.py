import re
import fitz
import html2text
from nltk.stem import PorterStemmer


def read_text_file(filename):
    with open(filename) as f:
        text = f.read()
    words = re.findall(r"\w+", text)
    return words


def read_pdf_file(filename):
    doc = fitz.open(filename)
    text = ""
    for page in doc:
        text += page.get_text()
    words = re.findall(r"\w+", text)
    return words


def read_html_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    converter = html2text.HTML2Text()
    text = converter.handle(content)
    text = re.sub(r"https://\S+", "", text)
    words = re.findall(r"\w+", text)
    return words


def process_words(words, stop_words):
    filtered_words = [
        word.lower()
        for word in words
        if not re.search(r'[0-9!@#$%^&*()_+{}[\]:;"\'<>,.?/~`|\\]', word)
        and len(word) >= 3
        and word not in stop_words
    ]
    return filtered_words


def main():
    # Read text documents
    text_docs = ["text1.txt", "text2.txt", "text3.txt", "text4.txt"]
    word_lists_text = [read_text_file(doc) for doc in text_docs]

    # Read PDF documents
    pdf_docs = ["pdf1.pdf", "pdf2.pdf", "pdf3.pdf", "pdf4.pdf"]
    word_lists_pdf = [read_pdf_file(doc) for doc in pdf_docs]

    # Read HTML documents
    html_docs = [
        "yahoo1.html",
        "yahoo2.html",
        "yahoo3.html",
        "yahoo4.html",
        "yahoo5.html",
        "yahoo6.html",
        "yahoo7.html",
        "yahoo8.html",
        "yahoo9.html",
        "yahoo10.html",
    ]
    word_lists_html = [read_html_file(doc) for doc in html_docs]

    # Read the main webpage text document
    word_list_main_page = read_text_file("main_page_text.txt")

    # Read stop words
    stop_word_doc = "stop_words.txt"
    stop_word_list = read_text_file(stop_word_doc)
    custom_stop_list = ["απs", "πiai", "πihi", "πiqi", "πjcj", "πjqj", "繁體中文"]
    stop_word_list += custom_stop_list

    # Process and clean the words
    all_word_lists = (
        word_lists_text + word_lists_pdf + word_lists_html + [word_list_main_page]
    )

    # Create PorterStemmer instance
    ps = PorterStemmer()

    # Calculate term frequency for each word in each document
    term_frequency_dict = {}

    for i, word_list in enumerate(all_word_lists, start=1):
        doc_term_frequency = {}
        for word in word_list:
            stemmed_word = ps.stem(word.lower())
            if stemmed_word not in doc_term_frequency:
                doc_term_frequency[stemmed_word] = 1
            else:
                doc_term_frequency[stemmed_word] += 1
        term_frequency_dict[f"doc{i}"] = doc_term_frequency

    # Printing result
    print("Term Frequency Dictionary:")
    print("\n")
    print(term_frequency_dict)


if __name__ == "__main__":
    main()
