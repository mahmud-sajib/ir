import html2text
import re
import fitz
import nltk
from nltk.stem import PorterStemmer

"""
Extract texts from txt
"""


# Extract texts from text docs into list of words
def txt_to_list(d):
    with open(d) as f:
        t = f.read()

    # use regular expressions to split the text into list of words
    w = re.findall(r"\w+", t)
    return w


# Reading text documents
doc1 = "text1.txt"
word_list1 = txt_to_list(doc1)

doc2 = "text2.txt"
word_list2 = txt_to_list(doc2)

doc3 = "text3.txt"
word_list3 = txt_to_list(doc3)

doc4 = "text4.txt"
word_list4 = txt_to_list(doc4)


# Extract texts from pdf docs into list of words
def pdf_to_list(d):
    t = ""
    for page in d:
        t += page.get_text()

    # use regular expressions to split the text into list of words
    w = re.findall(r"\w+", t)

    return w


"""
Extract texts from pdf
"""

# Reading pdf documents
doc5 = fitz.open("pdf1.pdf")
word_list5 = pdf_to_list(doc5)

doc6 = fitz.open("pdf2.pdf")
word_list6 = pdf_to_list(doc6)

doc7 = fitz.open("pdf3.pdf")
word_list7 = pdf_to_list(doc7)

doc8 = fitz.open("pdf4.pdf")
word_list8 = pdf_to_list(doc8)

"""
Extract texts from html
"""


# Extract texts from html docs into list of words
def html_to_list(doc):
    with open(doc, "r", encoding="utf-8") as f:
        content = f.read()

    # create an instance of the html2text converter
    converter = html2text.HTML2Text()

    # Convert HTML to plaintext
    text = converter.handle(content)
    text = re.sub(r"https://\S+", "", text)

    # use regular expressions to split the text into list of words
    word_list = re.findall(r"\w+", text)

    return word_list


# Reading html documents
doc9 = "yahoo1.html"
word_list9 = html_to_list(doc9)

doc10 = "yahoo2.html"
word_list10 = html_to_list(doc10)

doc11 = "yahoo3.html"
word_list11 = html_to_list(doc11)

doc12 = "yahoo4.html"
word_list12 = html_to_list(doc12)

doc13 = "yahoo5.html"
word_list13 = html_to_list(doc13)

doc14 = "yahoo6.html"
word_list14 = html_to_list(doc14)

doc15 = "yahoo7.html"
word_list15 = html_to_list(doc15)

doc16 = "yahoo8.html"
word_list16 = html_to_list(doc16)

doc17 = "yahoo9.html"
word_list17 = html_to_list(doc17)

doc18 = "yahoo10.html"
word_list18 = html_to_list(doc18)

"""
Extract texts from main webpage txt file
"""


# Extract texts from website main page into list of words
def main_txt_to_list(d):
    with open(d) as f:
        t = f.read()

    # use regular expressions to split the text into list of words
    w = re.findall(r"\w+", t)
    return w


# Reading text documents
doc19 = "main_page_text.txt"
word_list19 = txt_to_list(doc19)


# Extract stop words from website main page into list of words
def stop_words_to_list(d):
    with open(d) as f:
        t = f.read()

    # use regular expressions to split the text into list of words
    w = re.findall(r"\w+", t)
    return w


# Reading stop words text documents
stop_word_doc = "stop_words.txt"
stop_word_list = txt_to_list(stop_word_doc)
custom_stop_list = ["απs", "πiai", "πihi", "πiqi", "πjcj", "πjqj", "繁體中文"]
stop_word_list = stop_word_list + custom_stop_list

# Concatenate the lists
full_list = (
    word_list1
    + word_list2
    + word_list3
    + word_list4
    + word_list5
    + word_list6
    + word_list7
    + word_list8
    + word_list9
    + word_list10
    + word_list11
    + word_list12
    + word_list13
    + word_list14
    + word_list15
    + word_list16
    + word_list17
    + word_list18
    + word_list19
)

# Remove digit & punctuations
filtered_list = [
    word
    for word in full_list
    if not re.search(r'[0-9!@#$%^&*()_+{}[\]:;"\'<>,.?/~`|\\]', word)
]

# Convert to lowercase
filtered_list = [item.lower() for item in filtered_list]

# Keep unique words
filtered_list = list(set(filtered_list))

# Create a new list
new_list = []


# Process the list
def process_list(filtered_list):
    for word in filtered_list:
        if word.isnumeric():
            continue
        if len(word) < 3:
            continue
        if word in stop_word_list:
            continue

        new_list.append(word)


process_list(filtered_list)

# Create PorterStemmer instance
ps = PorterStemmer()

# Create the final list of words
final_list = []

for w in new_list:
    w = ps.stem(w)
    final_list.append(w)

final_list = set(final_list)
final_list = sorted(final_list)

# Initialize the outer dictionary
word_frequency_dict = {}

# Loop through the words in w_list
for word in final_list:
    if word[0].isnumeric():
        continue
    # Initialize the inner dictionary for each word
    word_doc_frequency = {}

    # Count the frequency of the word in word_doc1
    word_doc_frequency["doc1"] = word_list1.count(word)

    # Count the frequency of the word in word_doc2
    word_doc_frequency["doc2"] = word_list2.count(word)

    # Count the frequency of the word in word_doc3
    word_doc_frequency["doc3"] = word_list3.count(word)

    # Count the frequency of the word in word_doc4
    word_doc_frequency["doc4"] = word_list4.count(word)

    # Count the frequency of the word in word_doc5
    word_doc_frequency["doc5"] = word_list5.count(word)

    # Count the frequency of the word in word_doc6
    word_doc_frequency["doc6"] = word_list6.count(word)

    # Count the frequency of the word in word_doc7
    word_doc_frequency["doc7"] = word_list7.count(word)

    # Count the frequency of the word in word_doc8
    word_doc_frequency["doc8"] = word_list8.count(word)

    # Count the frequency of the word in word_doc9
    word_doc_frequency["doc9"] = word_list9.count(word)

    # Count the frequency of the word in word_doc10
    word_doc_frequency["doc10"] = word_list10.count(word)

    # Count the frequency of the word in word_doc11
    word_doc_frequency["doc11"] = word_list11.count(word)

    # Count the frequency of the word in word_doc12
    word_doc_frequency["doc12"] = word_list12.count(word)

    # Count the frequency of the word in word_doc13
    word_doc_frequency["doc13"] = word_list13.count(word)

    # Count the frequency of the word in word_doc14
    word_doc_frequency["doc14"] = word_list14.count(word)

    # Count the frequency of the word in word_doc15
    word_doc_frequency["doc15"] = word_list15.count(word)

    # Count the frequency of the word in word_doc16
    word_doc_frequency["doc16"] = word_list16.count(word)

    # Count the frequency of the word in word_doc17
    word_doc_frequency["doc17"] = word_list17.count(word)

    # Count the frequency of the word in word_doc18
    word_doc_frequency["doc18"] = word_list18.count(word)

    # Count the frequency of the word in word_doc19
    word_doc_frequency["doc19"] = word_list19.count(word)

    # Add the inner dictionary to the outer dictionary
    word_frequency_dict[word] = word_doc_frequency


# Printing result
print("Vocabulary Dictionary:")
print("\n")
print(word_frequency_dict)
