import subprocess
import os
import platform
import shutil
import sys
sys.path.append('../tools')


def find_libreoffice():
    """
    Encontra o executável do LibreOffice no sistema.
    """
    system = platform.system().lower()
    
    if system == "windows":
        # Caminhos comuns do LibreOffice no Windows
        possible_paths = [
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
            r"C:\Program Files\LibreOffice*\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice*\program\soffice.exe"
        ]
        
        # Verificar se soffice está no PATH
        soffice_path = shutil.which("soffice")
        if soffice_path:
            return soffice_path
            
        # Verificar caminhos específicos
        for path in possible_paths:
            if os.path.exists(path):
                return path
                
        # Tentar encontrar usando glob (para versões com números)
        import glob
        for pattern in possible_paths:
            matches = glob.glob(pattern)
            if matches:
                return matches[0]
                
        raise FileNotFoundError("LibreOffice não encontrado. Instale o LibreOffice primeiro.")
    else:
        # Linux/Mac - usar PATH
        soffice_path = shutil.which("soffice")
        if soffice_path:
            return soffice_path
        else:
            raise FileNotFoundError("LibreOffice não encontrado. Instale o LibreOffice primeiro.")


def convert_docx_to_pdf(docx_path, output_path=None):
    """
    Converte um arquivo .docx para .pdf usando LibreOffice (soffice).
    """
    if not os.path.isfile(docx_path):
        raise FileNotFoundError(f"O arquivo {docx_path} não foi encontrado.")

    # Caminho da pasta onde o PDF será salvo
    output_dir = output_path if output_path else os.path.dirname(docx_path)

    pdf_name = os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"

    try:
        # Encontrar o executável do LibreOffice
        soffice_path = find_libreoffice()
        
        subprocess.run(
            [
                soffice_path,
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                output_dir,
                docx_path,
            ],
            check=True,
        )
        print(f"✅ PDF gerado com sucesso em: {pdf_name}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao converter: {e}")
    except FileNotFoundError as e:
        print(f"❌ {e}")
        print("💡 Dica: Instale o LibreOffice e certifique-se de que está no PATH do sistema.")

    return os.path.join(output_dir, pdf_name)
