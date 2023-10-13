import os
import re
import fitz
import html2text
from nltk.stem import PorterStemmer


# Function to read different types of files
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
    return list(filtered_words)


def calculate_frequency(directory="content_directory"):
    # Read text documents
    text_docs = [f for f in os.listdir(directory) if f.endswith(".txt")]
    word_lists_text = [
        read_text_file(os.path.join(directory, doc)) for doc in text_docs
    ]

    # Read PDF documents
    pdf_docs = [f for f in os.listdir(directory) if f.endswith(".pdf")]
    word_lists_pdf = [read_pdf_file(os.path.join(directory, doc)) for doc in pdf_docs]

    # Read HTML documents
    html_docs = [f for f in os.listdir(directory) if f.endswith(".html")]
    word_lists_html = [
        read_html_file(os.path.join(directory, doc)) for doc in html_docs
    ]

    # Read stop words
    stop_word_doc = "stop_words.txt"
    stop_word_list = read_text_file(stop_word_doc)
    custom_stop_list = ["απs", "πiai", "πihi", "πiqi", "πjcj", "πjqj", "繁體中文"]
    stop_word_list += custom_stop_list

    # Concatenate the lists
    all_word_lists = word_lists_text + word_lists_pdf + word_lists_html

    # Process and clean the words
    filtered_words = []
    for word_list in all_word_lists:
        filtered_words += process_words(word_list, stop_word_list)

    # Create PorterStemmer instance
    ps = PorterStemmer()

    # Stem and sort the final list of words
    final_list = sorted([ps.stem(word) for word in filtered_words])

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

    # Create a dictionary to store word frequencies
    word_frequency_dict = {}

    # Loop through the words in the final list
    for word in final_list:
        if word[0].isnumeric():
            continue
        word_doc_frequency = {}
        for i, word_list in enumerate(all_word_lists, start=1):
            word_doc_frequency[f"doc{i}"] = word_list.count(word)
        word_frequency_dict[word] = word_doc_frequency

    # Printing result
    print("Vocabulary Dictionary:")
    print("\n")
    print(word_frequency_dict)


calculate_frequency()
