#!/bin/bash

set -e # Para o script se der erro

echo "🚀 Iniciando setup da automação de currículo..."

echo "🔄 Atualizando pacotes..."
sudo apt update -y

echo "📦 Instalando LibreOffice (soffice)..."
sudo apt install -y libreoffice

echo "📦 Instalando python3-venv (caso necessário)..."
sudo apt install -y python3-venv

echo "🐍 Criando ambiente virtual em ./venv"
python3 -m venv venv

source venv/bin/activate

echo "📦 Instalando dependências do Python..."
pip install --upgrade pip
pip install -r app/requirements.txt

# Verificações de compatibilidade
echo "🔍 Executando verificações de compatibilidade..."
if python3 tools/test_compatibility.py; then
    echo "✅ Verificações de compatibilidade concluídas"
else
    echo "⚠️ Algumas verificações falharam, mas o setup continuará"
fi

echo "✅ Setup finalizado!"
echo "🎯 Use 'python3 run.py' para gerar o currículo facilmente."
echo "🔧 Use 'python3 tools/test_compatibility.py' para verificar a compatibilidade."
