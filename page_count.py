import PyPDF2
import os

def get_total_pages(pdf_files):
    total_pages = 0
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages += len(reader.pages)
    return total_pages

# Specify the directory containing the PDF files
directory = '/directory/'

# Get a list of all PDF files in the directory
pdf_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')]

# Calculate the total number of pages
total_pages = get_total_pages(pdf_files)

print(f'Total number of pages in all PDF files: {total_pages}')
