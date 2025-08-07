#!/bin/bash

# Script para executar o gerador de currículo no Linux/macOS

echo "📄 GERADOR DE CURRÍCULO"
echo "======================"

# Verificar se estamos no diretório correto
if [ ! -f "app/main.py" ]; then
    echo "❌ Execute este script no diretório raiz do projeto"
    exit 1
fi

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo "💡 Execute o setup primeiro:"
    echo "   python3 setup.py"
    exit 1
fi

# Ativar ambiente virtual
echo "🟢 Ativando ambiente virtual..."
source venv/bin/activate

# Verificar se a ativação foi bem-sucedida
if [ $? -ne 0 ]; then
    echo "❌ Erro ao ativar ambiente virtual"
    exit 1
fi

echo "🚀 Iniciando gerador de currículo..."
echo "=================================="

# Executar a aplicação
python3 app/main.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Currículo gerado com sucesso!"
    echo "📁 Verifique a pasta 'out/' para os arquivos gerados"
    echo ""
    echo "🎯 Próximos passos:"
    echo "• Edite app/build_docx.py para personalizar seu currículo"
    echo "• Execute novamente para gerar um novo currículo"
    echo "• Use tools/test_compatibility.py para verificar problemas"
else
    echo ""
    echo "❌ Erro ao gerar currículo"
    echo ""
    echo "💡 Dicas de solução:"
    echo "• Execute: python3 setup.py"
    echo "• Verifique: python3 tools/test_compatibility.py"
    echo "• Ative o ambiente virtual manualmente se necessário"
    exit 1
fi
