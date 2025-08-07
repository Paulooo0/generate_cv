import os
import sys
sys.path.append('../tools')
from build_docx import build_docx
from utils import create_directory


def generate_docx():
    doc = build_docx()

    output_path = "./out/cv.docx"

    # Criar diretório de forma cross-platform
    output_dir = os.path.dirname(output_path)
    create_directory(output_dir)
    
    doc.save(output_path)

    return output_path
