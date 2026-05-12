from PyPDF2 import PdfMerger
import os

# Folder containing PDF files
pdf_folder = "pdfs"

# Output file name
output_file = "combined.pdf"

# Create merger object
merger = PdfMerger()

# Get all PDF files from folder
pdf_files = sorted([
    file for file in os.listdir(pdf_folder)
    if file.lower().endswith(".pdf")
])

# Append PDFs
for pdf in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf)
    print(f"Adding: {pdf_path}")
    merger.append(pdf_path)

# Write combined PDF
merger.write(output_file)
merger.close()

print(f"\nCombined PDF saved as: {output_file}")