import fitz  # PyMuPDF
import os
import sys

def extract_text_from_pdf(pdf_path):
    """
    Estrae il testo da un singolo PDF.

    Args:
    - pdf_path: Percorso del file PDF da cui estrarre il testo.

    Returns:
    - Una stringa contenente il testo estratto dal PDF.
    """
    text_content = []
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text_content.append(page.get_text())
    except Exception as e:
        print(f"Errore durante l'estrazione del testo da {pdf_path}: {e}", file=sys.stderr)
    return "\n".join(text_content)

def extract_text_from_directory(directory_path):
    """
    Estrae il testo da tutti i PDF in una directory.

    Args:
    - directory_path: Percorso della directory contenente i file PDF.

    Returns:
    - Un dizionario con il percorso del file come chiave e il testo estratto come valore.
    """
    extracted_texts = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            extracted_texts[pdf_path] = extract_text_from_pdf(pdf_path)
    return extracted_texts

if __name__ == "__main__":
    # Esempio di uso per estrarre testo da un singolo file PDF
    pdf_path = "path/to/your_pdf_file.pdf"
    text_data = extract_text_from_pdf(pdf_path)
    print(text_data)
    
    # Esempio di uso per estrarre testo da tutti i PDF in una directory
    # directory_path = "path/to/your_directory_with_pdfs"
    # texts_from_directory = extract_text_from_directory(directory_path)
    # for path, text in texts_from_directory.items():
    #     print(f"Testo estratto da {path}:\n{text}\n")