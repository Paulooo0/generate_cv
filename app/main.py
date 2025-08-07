from generate_docx import generate_docx
from convert_docx_to_pdf import convert_docx_to_pdf


def main():
    print("📄 Gerando .docx...")
    docx_path = generate_docx()

    print("🌀 Convertendo .docx para .pdf...")
    pdf_path = convert_docx_to_pdf(docx_path)


if __name__ == "__main__":
    main()
