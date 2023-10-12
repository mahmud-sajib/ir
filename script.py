import subprocess

files_to_run = [
    "get_main_page_content.py",
    "get_txt_pdf_files.py",
    "get_html_files.py",
    "get_stop_words.py",
    "read_content.py",
]

for file in files_to_run:
    subprocess.run(["python", file])
