import os

folder_path = os.getcwd()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith((".html", ".txt", ".pdf")):
            os.remove(os.path.join(root, file))
