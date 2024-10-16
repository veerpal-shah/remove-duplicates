import fitz  # PyMuPDF
from hashlib import md5
import sys
import os

'''
To run: python remove-duplicates.py "input.pdf" "output_document_no_duplicates.pdf"

'''

def page_to_hash(page):
    """
    Extract text from a PDF page and convert it to an MD5 hash.
    This helps detect duplicate pages based on content.
    """
    text = page.get_text("text")  # Extract page content as plain text
    return md5(text.encode('utf-8')).hexdigest()

def remove_duplicate_pages(input_pdf, output_pdf):
    """
    Remove duplicate pages from a PDF and save the result to a new file.
    """
    # Check if input file exists
    if not os.path.exists(input_pdf):
        print(f"Error: '{input_pdf}' does not exist.")
        sys.exit(1)

    doc = fitz.open(input_pdf)
    seen_hashes = set()  # Store unique page hashes
    pages_to_keep = []   # Track the indices of non-duplicate pages

    # Iterate through each page and check for duplicates
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # Load the page
        page_hash = page_to_hash(page)

        if page_hash not in seen_hashes:
            seen_hashes.add(page_hash)  # Mark the page as seen
            pages_to_keep.append(page_num)

    # Create a new PDF with only the unique pages
    new_doc = fitz.open()
    for page_num in pages_to_keep:
        new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)

    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()
    print(f"Duplicates removed. Saved to: {output_pdf}")

if __name__ == "__main__":
    # Ensure correct usage
    if len(sys.argv) != 3:
        print("Usage: python remove_duplicates.py <input_pdf> <output_pdf>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    remove_duplicate_pages(input_file, output_file)
