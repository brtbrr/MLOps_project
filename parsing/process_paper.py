import arxiv
from PyPDF2 import PdfReader
import ssl
import os

from constants import PDF_DIR, EXTRACTED_TEXT_DIR
from .clean_text import slugify, clean_paper_text

ssl._create_default_https_context = ssl._create_unverified_context


def extract_text(pdf_path) -> str:
    reader = PdfReader(pdf_path)
    pages = []

    for page in reader.pages:
        text = page.extract_text()
        pages.append(text)

    return "\n".join(pages)


def process_result(result: arxiv.arxiv.Result) -> None:
    clean_title = slugify(result.title)
    pdf_path = os.path.join(PDF_DIR, clean_title + ".pdf")
    txt_path = os.path.join(EXTRACTED_TEXT_DIR, clean_title + ".txt")

    # toDo use pipeline to check if paper is already processed
    if not os.path.exists(txt_path):
        result.download_pdf(filename=pdf_path)
        text = extract_text(pdf_path)
        with open(txt_path, "w") as f:
            f.write(clean_paper_text(text))
