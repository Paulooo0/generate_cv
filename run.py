#!/usr/bin/env python3
"""
Script universal para executar o gerador de currículo.
Detecta automaticamente o sistema e configura o ambiente.
"""

import os
import sys
import platform
import subprocess
from pathlib import Path



def get_system_info():
    """Retorna informações sobre o sistema operacional."""
    system = platform.system().lower()
    return {
        'system': system,
        'is_windows': system == 'windows',
        'is_linux': system == 'linux',
        'is_macos': system == 'darwin'
    }


def check_venv():
    """Verifica se o ambiente virtual existe e está ativo."""
    venv_path = Path("venv")
    if not venv_path.exists():
        print("❌ Ambiente virtual não encontrado!")
        print("💡 Execute o setup primeiro:")
        print("   python3 setup.py")
        return False
    
    # Verificar se está ativo
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Ambiente virtual ativo")
        return True
    else:
        print("⚠️ Ambiente virtual não está ativo")
        return False


def activate_venv():
    """Ativa o ambiente virtual."""
    system_info = get_system_info()
    
    if system_info['is_windows']:
        activate_script = "venv\\Scripts\\activate"
    else:
        activate_script = "venv/bin/activate"
    
    if not os.path.exists(activate_script):
        print(f"❌ Script de ativação não encontrado: {activate_script}")
        return False
    
    return True


def run_application():
    """Executa a aplicação principal."""
    system_info = get_system_info()
    
    # Verificar se o ambiente virtual existe
    if not check_venv():
        return False
    
    # Verificar se a aplicação existe
    app_path = Path("app/main.py")
    if not app_path.exists():
        print("❌ Aplicação não encontrada: app/main.py")
        return False
    
    print("🚀 Iniciando gerador de currículo...")
    print("=" * 40)
    
    try:
        # Executar a aplicação
        if system_info['is_windows']:
            # Windows - usar python
            result = subprocess.run([sys.executable, "app/main.py"], check=True)
        else:
            # Linux/Mac - usar python3
            result = subprocess.run([sys.executable, "app/main.py"], check=True)
        
        print("\n✅ Currículo gerado com sucesso!")
        print("📁 Verifique a pasta 'out/' para os arquivos gerados")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar a aplicação: {e}")
        return False
    except KeyboardInterrupt:
        print("\n✅ Execução cancelada pelo usuário")
        return False


def main():
    """Função principal."""
    print("📄 GERADOR DE CURRÍCULO")
    print("=" * 30)
    
    system_info = get_system_info()
    print(f"🖥️ Sistema: {system_info['system'].title()}")

    # Verificar se estamos no diretório correto
    if not os.path.exists("app/main.py"):
        print("❌ Execute este script no diretório raiz do projeto")
        return False
    
    # Executar a aplicação
    success = run_application()
    
    if success:
        print("\n🎯 Próximos passos:")
        print("• Edite app/build_docx.py para personalizar seu currículo")
        print("• Execute novamente para gerar um novo currículo")
        print("• Use tools/test_compatibility.py para verificar problemas")
    else:
        print("\n💡 Dicas de solução:")
        print("• Verifique se o ambiente virtual está ativo:")
        if system_info['is_windows']:
            print("  .\\venv\\Scripts\\Activate.ps1")
        else:
            print("  source venv/bin/activate")
        if system_info['is_windows']:
            print("• Execute: python run.py")
        else:
            print("• Execute: python3 run.py")
        if system_info['is_windows']:
            print("• Verifique: python tools/test_compatibility.py")
        else:
            print("• Verifique: python3 tools/test_compatibility.py")
    
    return success


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n✅ Execução cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)
