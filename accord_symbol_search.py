

import fitz  # PyMuPDF

def extract_text_with_chars(pdf_path, characters):
    doc = fitz.open(pdf_path)
    text_with_chars = []

    for page in doc:
        text = page.get_text()
        for line in text.split('\n'):
            if any(char in line for char in characters):
                text_with_chars.append(line)

    doc.close()
    return text_with_chars

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_path = r"C:/Users/SUMMANA SUBRAMANIAN/Downloads/Acord 1-2.pdf"

# Define the characters to filter for
characters = [",",  ".", "-","✓"]


text_containing_chars = extract_text_with_chars(pdf_path, characters)

for line in text_containing_chars:
    print(line)
