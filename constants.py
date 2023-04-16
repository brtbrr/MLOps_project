import os

SOURCE_BERT = "allenai/scibert_scivocab_uncased"

DATA_DIR = "data"
PDF_DIR = os.path.join(DATA_DIR, "pdf")
EXTRACTED_TEXT_DIR = os.path.join(DATA_DIR, "text")

os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(EXTRACTED_TEXT_DIR, exist_ok=True)
