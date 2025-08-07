#!/usr/bin/env python3
"""
Script de setup universal que detecta o sistema operacional e executa o setup apropriado.
"""

import os
import platform
import subprocess
import sys


def get_system_info():
    """Retorna informações sobre o sistema operacional."""
    system = platform.system().lower()
    return {
        'system': system,
        'is_windows': system == 'windows',
        'is_linux': system == 'linux',
        'is_macos': system == 'darwin'
    }


def run_setup_script(script_path):
    """Executa um script de setup."""
    try:
        if platform.system().lower() == 'windows':
            # Windows - usar PowerShell
            result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', script_path], 
                                  check=True, capture_output=True, text=True)
        else:
            # Linux/Mac - usar bash
            result = subprocess.run(['bash', script_path], check=True, capture_output=True, text=True)
        
        print(result.stdout)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar script de setup: {e}")
        print(f"Stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"❌ Script de setup não encontrado: {script_path}")
        return False


def main():
    """Função principal."""
    print("🚀 SETUP UNIVERSAL - GERADOR DE CURRÍCULO")
    print("=" * 50)
    
    system_info = get_system_info()
    print(f"🖥️ Sistema detectado: {system_info['system'].title()}")
    
    # Determinar qual script usar
    if system_info['is_windows']:
        setup_script = "script/setup.ps1"
        print("📋 Usando script PowerShell para Windows")
    elif system_info['is_linux']:
        setup_script = "script/setup.sh"
        print("📋 Usando script Bash para Linux")
    elif system_info['is_macos']:
        setup_script = "script/setup.sh"
        print("📋 Usando script Bash para macOS")
    else:
        print("❌ Sistema operacional não suportado")
        return False
    
    # Verificar se o script existe
    if not os.path.exists(setup_script):
        print(f"❌ Script de setup não encontrado: {setup_script}")
        return False
    
    # Executar o setup
    print(f"\n🔧 Executando setup...")
    success = run_setup_script(setup_script)
    
    if success:
        print("\n✅ Setup concluído com sucesso!")
        print("\n🎯 Próximos passos:")
        print("1. Ative o ambiente virtual:")
        if system_info['is_windows']:
            print("   .\\venv\\Scripts\\Activate.ps1")
        else:
            print("   source venv/bin/activate")
        print("2. Gere seu currículo:")
        if system_info['is_windows']:
            print("   python run.py")
        else:
            print("   python3 run.py")

    else:
        print("\n❌ Setup falhou. Verifique os erros acima.")
        return False
    
    return True


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n✅ Setup cancelado pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)
