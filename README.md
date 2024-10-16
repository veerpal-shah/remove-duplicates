# remove-duplicates

Author: Veerpal Shah

Ever have a large PDF/PPT where you know there's tons of duplicates but you don't want to remove them manually? Save as PDF and run this script and save several minutes if your life! 

## Features
- Extracts text from each page.
- Detects duplicate pages using MD5 hashing.
- Generates a new PDF with only unique pages.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/remove-duplicate-pages-pdf.git
   cd remove-duplicate-pages-pdf
    ```

  To Install required packages:
   ```bash
  pip install PyMuPDF
 ```
    
  To run:
   ```bash
  python remove-duplicates.py <input_document.pdf> <output_document_no_duplicates.pdf>

 ```
