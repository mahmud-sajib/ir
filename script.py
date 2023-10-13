import subprocess

files_to_run = [
    "get_main_page_content.py",
    "get_text_files.py",
    "get_pdf_files.py",
    "get_html_files.py",
    "get_stop_words.py",
    # "doc_freq.py",
]

for file in files_to_run:
    subprocess.run(["python", file])
