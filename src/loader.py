import os
from pypdf import PdfReader

def load_file(file_path):
    documents = []
    for filename in os.listdir(file_path):
        file = os.path.join(file_path, filename)
        if filename.endswith('.txt'):
            with open(file,'r',encoding='utf-8') as f:
                content = f.read()
                # documents.append({
                #     'filename':filename,
                #     'text': content
                # })
        elif filename.endswith('.pdf'):
            reader = PdfReader(file)
            pages = []

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    pages.append(page_text)

            content = "\n".join(pages)

        else:
            continue

        documents.append({
            "filename": filename,
            "text": content
        })
            
    return documents



# with makes sure that the file is automatically closed after use — even if an error happens
# with makes sure that the file is automatically closed after use — even if an error happens
# open(path, mode, encoding)
# Other common modes (just for context):

# "w" → write (overwrite)

# "a" → append

# "rb" → read binary

# 👉 Here, "r" means:
# 📖 “I just want to read the file.”

# 5️⃣ encoding="utf-8"

# Why encoding exists:
# Computers store text as bytes, but humans use characters:

# English letters

# Hindi, emojis 😄

# Special symbols

# UTF-8 is a universal encoding that supports:

# English

# Hindi

# All Unicode characters

# 👉 Without encoding:

# You may get errors like UnicodeDecodeError

# Especially common in Indian text files

# What it does:
# as renames the opened file object.

# 8️⃣ :

# The colon means:

# “A block of code is starting.”

# Everything indented below runs while the file is open.

