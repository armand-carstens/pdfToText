import os
from pdfminer.high_level import extract_text

pdf_directory = "pdfs"
output_directory = "output_texts"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

listPdfs = [file for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

for pdf in listPdfs:
    pdf_location = os.path.join(pdf_directory, pdf)
    text = extract_text(pdf_location)
    
    txt_filename = os.path.splitext(pdf)[0] + ".txt"
    txt_path = os.path.join(output_directory, txt_filename)
    
    # Open the output file in write mode with UTF-8 encoding
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    
    print(f"Extracted text from {pdf} to {txt_filename}")
