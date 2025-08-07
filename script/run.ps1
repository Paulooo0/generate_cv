# Script para executar o gerador de currículo no Windows

Write-Host "📄 GERADOR DE CURRÍCULO" -ForegroundColor Cyan
Write-Host "======================" -ForegroundColor Cyan

# Verificar se estamos no diretório correto
if (-not (Test-Path "app\main.py")) {
    Write-Host "❌ Execute este script no diretório raiz do projeto" -ForegroundColor Red
    exit 1
}

# Verificar se o ambiente virtual existe
if (-not (Test-Path "venv")) {
    Write-Host "❌ Ambiente virtual não encontrado!" -ForegroundColor Red
    Write-Host "💡 Execute o setup primeiro:" -ForegroundColor Yellow
    Write-Host "   python setup.py" -ForegroundColor Yellow
    exit 1
}

# Ativar ambiente virtual
Write-Host "🟢 Ativando ambiente virtual..." -ForegroundColor Green
try {
    & .\venv\Scripts\Activate.ps1
} catch {
    Write-Host "❌ Erro ao ativar ambiente virtual" -ForegroundColor Red
    Write-Host "Erro: $_" -ForegroundColor Red
    exit 1
}

Write-Host "🚀 Iniciando gerador de currículo..." -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green

# Executar a aplicação
try {
    python app\main.py
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ Currículo gerado com sucesso!" -ForegroundColor Green
        Write-Host "📁 Verifique a pasta 'out/' para os arquivos gerados" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "🎯 Próximos passos:" -ForegroundColor Yellow
        Write-Host "• Edite app\build_docx.py para personalizar seu currículo" -ForegroundColor White
        Write-Host "• Execute novamente para gerar um novo currículo" -ForegroundColor White
        Write-Host "• Use tools\test_compatibility.py para verificar problemas" -ForegroundColor White
    } else {
        Write-Host ""
        Write-Host "❌ Erro ao gerar currículo" -ForegroundColor Red
        Write-Host ""
        Write-Host "💡 Dicas de solução:" -ForegroundColor Yellow
        Write-Host "• Execute: python setup.py" -ForegroundColor White
        Write-Host "• Verifique: python tools\test_compatibility.py" -ForegroundColor White
        Write-Host "• Ative o ambiente virtual manualmente se necessário" -ForegroundColor White
        exit 1
    }
} catch {
    Write-Host ""
    Write-Host "❌ Erro ao executar a aplicação" -ForegroundColor Red
    Write-Host "Erro: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "💡 Dicas de solução:" -ForegroundColor Yellow
    Write-Host "• Execute: python setup.py" -ForegroundColor White
    Write-Host "• Verifique: python tools\test_compatibility.py" -ForegroundColor White
    exit 1
}
