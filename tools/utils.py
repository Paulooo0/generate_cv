import platform
import os
import shutil
import subprocess


def get_system_info():
    """
    Retorna informações sobre o sistema operacional.
    """
    system = platform.system().lower()
    return {
        'system': system,
        'is_windows': system == 'windows',
        'is_linux': system == 'linux',
        'is_macos': system == 'darwin'
    }


def create_directory(path):
    """
    Cria um diretório de forma cross-platform.
    """
    os.makedirs(path, exist_ok=True)


def find_executable(executable_name):
    """
    Encontra um executável no sistema.
    """
    return shutil.which(executable_name)


def run_command(command, shell=False):
    """
    Executa um comando de forma cross-platform.
    """
    try:
        result = subprocess.run(command, shell=shell, check=True, capture_output=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar comando: {e}")
        return None


def get_python_command():
    """
    Retorna o comando Python apropriado para o sistema.
    """
    system_info = get_system_info()
    
    if system_info['is_windows']:
        return 'python'
    else:
        return 'python3'
