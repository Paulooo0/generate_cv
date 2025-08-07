#!/usr/bin/env python3
"""
Script para adicionar o LibreOffice ao PATH do Windows.
"""

import os
import platform
import shutil
import glob
import sys


def check_windows():
    """Verifica se estamos no Windows."""
    if platform.system().lower() != "windows":
        print("❌ Este script é específico para Windows.")
        return False
    return True


def find_libreoffice():
    """Encontra o LibreOffice instalado no sistema."""
    print("🔍 Procurando LibreOffice...")
    
    # Verificar se já está no PATH
    soffice_path = shutil.which("soffice")
    if soffice_path:
        print(f"✅ LibreOffice já está no PATH: {soffice_path}")
        return soffice_path
    
    # Verificar caminhos comuns
    common_paths = [
        r"C:\Program Files\LibreOffice\program\soffice.exe",
        r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
        r"C:\Program Files\LibreOffice*\program\soffice.exe",
        r"C:\Program Files (x86)\LibreOffice*\program\soffice.exe"
    ]
    
    for path in common_paths:
        if "*" in path:
            matches = glob.glob(path)
            for match in matches:
                if os.path.exists(match):
                    print(f"✅ LibreOffice encontrado: {match}")
                    return match
        else:
            if os.path.exists(path):
                print(f"✅ LibreOffice encontrado: {path}")
                return path
    
    print("❌ LibreOffice não encontrado no sistema")
    return None


def add_to_system_path(libreoffice_path):
    """Adiciona ao PATH do sistema (requer admin)."""
    try:
        import winreg
        
        program_dir = os.path.dirname(libreoffice_path)
        
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
            0,
            winreg.KEY_READ | winreg.KEY_WRITE
        )
        
        current_path, _ = winreg.QueryValueEx(key, "Path")
        
        if program_dir in current_path:
            print("✅ LibreOffice já está no PATH do sistema")
            winreg.CloseKey(key)
            return True
        
        new_path = current_path + ";" + program_dir
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
        winreg.CloseKey(key)
        
        print("✅ LibreOffice adicionado ao PATH do sistema!")
        print("🔄 Reinicie o prompt de comando para que as mudanças tenham efeito.")
        return True
        
    except PermissionError:
        print("❌ Erro de permissão. Execute como administrador.")
        return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def add_to_user_path(libreoffice_path):
    """Adiciona ao PATH do usuário (não requer admin)."""
    try:
        import winreg
        
        program_dir = os.path.dirname(libreoffice_path)
        
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Environment",
            0,
            winreg.KEY_READ | winreg.KEY_WRITE
        )
        
        try:
            current_path, _ = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            current_path = ""
        
        if program_dir in current_path:
            print("✅ LibreOffice já está no PATH do usuário")
            winreg.CloseKey(key)
            return True
        
        if current_path:
            new_path = current_path + ";" + program_dir
        else:
            new_path = program_dir
        
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
        winreg.CloseKey(key)
        
        print("✅ LibreOffice adicionado ao PATH do usuário!")
        print("🔄 Reinicie o prompt de comando para que as mudanças tenham efeito.")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def main():
    """Função principal."""
    print("🔧 ADICIONAR LIBREOFFICE AO PATH DO WINDOWS")
    print("=" * 50)
    
    if not check_windows():
        return
    
    libreoffice_path = find_libreoffice()
    if not libreoffice_path:
        print("\n💡 Instale o LibreOffice primeiro:")
        print("• Baixe em: https://www.libreoffice.org/download/download/")
        print("• Ou use: winget install TheDocumentFoundation.LibreOffice")
        return
    
    print(f"\n📁 Caminho do LibreOffice: {libreoffice_path}")
    print("\n🔧 Escolha onde adicionar ao PATH:")
    print("1. PATH do sistema (requer privilégios de administrador)")
    print("2. PATH do usuário (não requer admin)")
    print("3. Cancelar")
    
    try:
        choice = input("\nEscolha uma opção (1-3): ").strip()
        
        if choice == "1":
            print("\n⚠️ Tentando adicionar ao PATH do sistema...")
            if add_to_system_path(libreoffice_path):
                print("\n✅ Sucesso! O LibreOffice agora está disponível globalmente.")
            else:
                print("\n💡 Dica: Execute o PowerShell como administrador e tente novamente.")
                
        elif choice == "2":
            print("\n⚠️ Adicionando ao PATH do usuário...")
            if add_to_user_path(libreoffice_path):
                print("\n✅ Sucesso! O LibreOffice agora está disponível para este usuário.")
            else:
                print("\n❌ Falha ao adicionar ao PATH do usuário.")
                
        elif choice == "3":
            print("✅ Operação cancelada")
            
        else:
            print("❌ Opção inválida")
            
    except KeyboardInterrupt:
        print("\n✅ Operação cancelada pelo usuário")
    
    print("\n🎯 Para testar, execute: soffice --version")


if __name__ == "__main__":
    main()
