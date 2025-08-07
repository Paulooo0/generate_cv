#!/usr/bin/env python3
"""
Script específico para verificar a instalação do LibreOffice no Windows.
"""

import os
import platform
import shutil
import glob
import subprocess


def check_system():
    """Verifica se estamos no Windows."""
    system = platform.system().lower()
    if system != "windows":
        print(f"❌ Este script é específico para Windows. Sistema atual: {system}")
        return False
    print(f"✅ Sistema Windows detectado: {platform.system()} {platform.release()}")
    return True


def check_path():
    """Verifica se soffice está no PATH do sistema."""
    print("\n🔍 Verificando se 'soffice' está no PATH...")
    
    soffice_path = shutil.which("soffice")
    if soffice_path:
        print(f"✅ LibreOffice encontrado no PATH: {soffice_path}")
        return soffice_path
    else:
        print("❌ LibreOffice não encontrado no PATH")
        return None


def check_common_paths():
    """Verifica caminhos comuns de instalação do LibreOffice."""
    print("\n📁 Verificando caminhos comuns de instalação...")
    
    common_paths = [
        r"C:\Program Files\LibreOffice\program\soffice.exe",
        r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
        r"C:\Program Files\LibreOffice*\program\soffice.exe",
        r"C:\Program Files (x86)\LibreOffice*\program\soffice.exe"
    ]
    
    found_paths = []
    
    for path in common_paths:
        if "*" in path:
            # Usar glob para versões com números
            matches = glob.glob(path)
            for match in matches:
                if os.path.exists(match):
                    found_paths.append(match)
                    print(f"✅ Encontrado: {match}")
        else:
            if os.path.exists(path):
                found_paths.append(path)
                print(f"✅ Encontrado: {path}")
    
    if not found_paths:
        print("❌ LibreOffice não encontrado nos caminhos comuns")
    
    return found_paths


def check_registry():
    """Verifica o registro do Windows para LibreOffice."""
    print("\n🔧 Verificando registro do Windows...")
    
    try:
        import winreg
        
        registry_paths = [
            r"SOFTWARE\LibreOffice\LibreOffice\*\Path",
            r"SOFTWARE\WOW6432Node\LibreOffice\LibreOffice\*\Path"
        ]
        
        found_in_registry = []
        
        for reg_path in registry_paths:
            try:
                # Tentar abrir a chave do registro
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path.replace(r"\*\Path", ""))
                print(f"✅ Chave do registro encontrada: {reg_path}")
                found_in_registry.append(reg_path)
                winreg.CloseKey(key)
            except FileNotFoundError:
                print(f"❌ Chave não encontrada: {reg_path}")
            except Exception as e:
                print(f"⚠️ Erro ao acessar registro: {e}")
        
        return found_in_registry
        
    except ImportError:
        print("⚠️ Módulo winreg não disponível (pode não ser Windows)")
        return []


def test_soffice_execution():
    """Testa se o soffice pode ser executado."""
    print("\n▶️ Testando execução do soffice...")
    
    # Primeiro, tentar encontrar o soffice
    soffice_path = shutil.which("soffice")
    if not soffice_path:
        # Tentar caminhos comuns
        common_paths = [
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"
        ]
        for path in common_paths:
            if os.path.exists(path):
                soffice_path = path
                break
    
    if not soffice_path:
        print("❌ Não foi possível encontrar o soffice para teste")
        return False
    
    try:
        # Testar com --version (comando seguro)
        result = subprocess.run(
            [soffice_path, "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print(f"✅ LibreOffice executado com sucesso!")
            print(f"   Versão: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ Erro ao executar LibreOffice: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Timeout ao executar LibreOffice")
        return False
    except Exception as e:
        print(f"❌ Erro ao executar LibreOffice: {e}")
        return False


def add_to_path(libreoffice_path):
    """
    Adiciona o LibreOffice ao PATH do sistema Windows.
    Requer privilégios de administrador.
    """
    print(f"\n🔧 Tentando adicionar ao PATH: {libreoffice_path}")
    
    try:
        import winreg
        
        # Extrair o diretório do programa (remover soffice.exe)
        program_dir = os.path.dirname(libreoffice_path)
        
        # Abrir a chave do registro para PATH do sistema
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
            0,
            winreg.KEY_READ | winreg.KEY_WRITE
        )
        
        # Ler o PATH atual
        current_path, _ = winreg.QueryValueEx(key, "Path")
        
        # Verificar se já está no PATH
        if program_dir in current_path:
            print("✅ LibreOffice já está no PATH do sistema")
            winreg.CloseKey(key)
            return True
        
        # Adicionar ao PATH
        new_path = current_path + ";" + program_dir
        
        # Escrever o novo PATH
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
        winreg.CloseKey(key)
        
        print("✅ LibreOffice adicionado ao PATH do sistema com sucesso!")
        print("🔄 Reinicie o prompt de comando para que as mudanças tenham efeito.")
        
        return True
        
    except PermissionError:
        print("❌ Erro de permissão. Execute o script como administrador.")
        return False
    except Exception as e:
        print(f"❌ Erro ao modificar PATH: {e}")
        return False


def add_to_user_path(libreoffice_path):
    """
    Adiciona o LibreOffice ao PATH do usuário (não requer admin).
    """
    print(f"\n🔧 Tentando adicionar ao PATH do usuário: {libreoffice_path}")
    
    try:
        import winreg
        
        # Extrair o diretório do programa
        program_dir = os.path.dirname(libreoffice_path)
        
        # Abrir a chave do registro para PATH do usuário
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Environment",
            0,
            winreg.KEY_READ | winreg.KEY_WRITE
        )
        
        # Ler o PATH atual do usuário
        try:
            current_path, _ = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            current_path = ""
        
        # Verificar se já está no PATH
        if program_dir in current_path:
            print("✅ LibreOffice já está no PATH do usuário")
            winreg.CloseKey(key)
            return True
        
        # Adicionar ao PATH
        if current_path:
            new_path = current_path + ";" + program_dir
        else:
            new_path = program_dir
        
        # Escrever o novo PATH
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
        winreg.CloseKey(key)
        
        print("✅ LibreOffice adicionado ao PATH do usuário com sucesso!")
        print("🔄 Reinicie o prompt de comando para que as mudanças tenham efeito.")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao modificar PATH do usuário: {e}")
        return False


def check_installation_methods():
    """Verifica métodos de instalação disponíveis."""
    print("\n📦 Verificando métodos de instalação...")
    
    # Verificar winget
    winget_available = shutil.which("winget")
    if winget_available:
        print("✅ winget disponível - pode instalar via: winget install TheDocumentFoundation.LibreOffice")
    else:
        print("❌ winget não disponível")
    
    # Verificar chocolatey
    choco_available = shutil.which("choco")
    if choco_available:
        print("✅ Chocolatey disponível - pode instalar via: choco install libreoffice")
    else:
        print("❌ Chocolatey não disponível")
    
    # Verificar scoop
    scoop_available = shutil.which("scoop")
    if scoop_available:
        print("✅ Scoop disponível - pode instalar via: scoop install libreoffice")
    else:
        print("❌ Scoop não disponível")


def main():
    """Executa todas as verificações."""
    print("🔍 VERIFICAÇÃO DO LIBREOFFICE NO WINDOWS")
    print("=" * 50)
    
    if not check_system():
        return
    
    results = {
        'path': check_path(),
        'common_paths': check_common_paths(),
        'registry': check_registry(),
        'execution': test_soffice_execution()
    }
    
    print("\n📊 RESUMO DA VERIFICAÇÃO")
    print("=" * 30)
    
    if results['path'] or results['common_paths']:
        print("✅ LibreOffice está instalado no sistema")
        if results['execution']:
            print("✅ LibreOffice pode ser executado corretamente")
        else:
            print("⚠️ LibreOffice instalado mas pode ter problemas de execução")
    else:
        print("❌ LibreOffice não está instalado")
        print("\n💡 COMO INSTALAR:")
        print("1. Baixe em: https://www.libreoffice.org/download/download/")
        print("2. Ou use winget: winget install TheDocumentFoundation.LibreOffice")
        print("3. Ou use Chocolatey: choco install libreoffice")
    
    check_installation_methods()
    
    print("\n🎯 RECOMENDAÇÕES:")
    if not results['path'] and results['common_paths']:
        print("• Adicione o LibreOffice ao PATH do sistema")
        print("• Ou use o caminho completo nos scripts")
        
        # Oferecer para adicionar ao PATH automaticamente
        print("\n🔧 OPÇÃO: Adicionar LibreOffice ao PATH automaticamente")
        print("1. PATH do sistema (requer admin)")
        print("2. PATH do usuário (não requer admin)")
        print("3. Não adicionar")
        
        try:
            choice = input("\nEscolha uma opção (1-3): ").strip()
            
            if choice == "1":
                # Tentar adicionar ao PATH do sistema
                if results['common_paths']:
                    add_to_path(results['common_paths'][0])
                else:
                    print("❌ Não foi possível encontrar o caminho do LibreOffice")
                    
            elif choice == "2":
                # Adicionar ao PATH do usuário
                if results['common_paths']:
                    add_to_user_path(results['common_paths'][0])
                else:
                    print("❌ Não foi possível encontrar o caminho do LibreOffice")
                    
            elif choice == "3":
                print("✅ Operação cancelada")
                
            else:
                print("❌ Opção inválida")
                
        except KeyboardInterrupt:
            print("\n✅ Operação cancelada pelo usuário")
            
    elif not results['path'] and not results['common_paths']:
        print("• Instale o LibreOffice primeiro")
        print("• Certifique-se de que está no PATH")


if __name__ == "__main__":
    main()
