#!/usr/bin/env python3
"""
Script de teste para verificar compatibilidade cross-platform.
"""

import sys
import os
from utils import get_system_info, find_executable, get_python_command


def test_system_detection():
    """Testa a detecção do sistema operacional."""
    print("🔍 Testando detecção do sistema operacional...")
    
    system_info = get_system_info()
    print(f"   Sistema: {system_info['system']}")
    print(f"   É Windows: {system_info['is_windows']}")
    print(f"   É Linux: {system_info['is_linux']}")
    print(f"   É macOS: {system_info['is_macos']}")
    
    return system_info


def test_python_command():
    """Testa o comando Python correto."""
    print("\n🐍 Testando comando Python...")
    
    python_cmd = get_python_command()
    print(f"   Comando Python: {python_cmd}")
    
    return python_cmd


def test_libreoffice_detection():
    """Testa a detecção do LibreOffice."""
    print("\n📄 Testando detecção do LibreOffice...")
    
    soffice_path = find_executable("soffice")
    if soffice_path:
        print(f"   ✅ LibreOffice encontrado em: {soffice_path}")
        return True
    else:
        print("   ❌ LibreOffice não encontrado no PATH")
        return False


def test_directory_creation():
    """Testa a criação de diretórios."""
    print("\n📁 Testando criação de diretórios...")
    
    from utils import create_directory
    
    test_dir = "test_output"
    try:
        create_directory(test_dir)
        print(f"   ✅ Diretório criado: {test_dir}")
        
        # Limpar
        if os.path.exists(test_dir):
            os.rmdir(test_dir)
            print(f"   🧹 Diretório removido: {test_dir}")
        
        return True
    except Exception as e:
        print(f"   ❌ Erro ao criar diretório: {e}")
        return False


def main():
    """Executa todos os testes de compatibilidade."""
    print("🚀 Iniciando testes de compatibilidade cross-platform...\n")
    
    results = {
        'system_detection': test_system_detection(),
        'python_command': test_python_command(),
        'libreoffice_detection': test_libreoffice_detection(),
        'directory_creation': test_directory_creation()
    }
    
    print("\n📊 Resumo dos testes:")
    print("=" * 40)
    
    for test_name, result in results.items():
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"   {test_name}: {status}")
    
    print("\n🎯 Recomendações:")
    if not results['libreoffice_detection']:
        print("   • Instale o LibreOffice para conversão PDF")
        print("   • Certifique-se de que está no PATH do sistema")
    
    print("\n✨ Testes concluídos!")


if __name__ == "__main__":
    main()
