import pdfplumber

pdf_path = ''
keyword = "AMOUNT"

amount_tables = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if keyword in page_text.lower():
            # You can implement a more advanced table extraction method here
            # This is a basic example to identify pages with the keyword
            amount_tables.append(page.extract_tables())

# Now, 'amount_tables' contains the tables from pages containing the keyword "amount"
