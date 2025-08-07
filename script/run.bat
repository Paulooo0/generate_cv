@echo off
REM Script para executar o gerador de currículo no Windows

echo 📄 GERADOR DE CURRÍCULO
echo ======================

REM Verificar se estamos no diretório correto
if not exist "app\main.py" (
    echo ❌ Execute este script no diretório raiz do projeto
    pause
    exit /b 1
)

REM Verificar se o ambiente virtual existe
if not exist "venv" (
    echo ❌ Ambiente virtual não encontrado!
    echo 💡 Execute o setup primeiro:
    echo    python setup.py
    pause
    exit /b 1
)

REM Ativar ambiente virtual
echo 🟢 Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Verificar se a ativação foi bem-sucedida
if errorlevel 1 (
    echo ❌ Erro ao ativar ambiente virtual
    pause
    exit /b 1
)

echo 🚀 Iniciando gerador de currículo...
echo ==================================

REM Executar a aplicação
python app\main.py

if errorlevel 0 (
    echo.
    echo ✅ Currículo gerado com sucesso!
    echo 📁 Verifique a pasta 'out/' para os arquivos gerados
    echo.
    echo 🎯 Próximos passos:
    echo • Edite app\build_docx.py para personalizar seu currículo
    echo • Execute novamente para gerar um novo currículo
    echo • Use tools\test_compatibility.py para verificar problemas
) else (
    echo.
    echo ❌ Erro ao gerar currículo
    echo.
    echo 💡 Dicas de solução:
    echo • Execute: python setup.py
    echo • Verifique: python tools\test_compatibility.py
    echo • Ative o ambiente virtual manualmente se necessário
    pause
    exit /b 1
)

pause
