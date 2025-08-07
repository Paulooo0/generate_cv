$ErrorActionPreference = "Stop"

Write-Host 'Iniciando setup da automacao de curriculo...'

# Verifica se o winget está disponível
if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    Write-Host "winget nao encontrado. Atualize seu Windows ou instale o App Installer pela Microsoft Store."
    exit 1
}

# Instalar Python, se não estiver instalado
Write-Host '🐍 Verificando/Instalando Python...'
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host 'Instalando Python...'
    winget install --id Python.Python.3 --accept-package-agreements --accept-source-agreements
} else {
    Write-Host 'Python ja esta instalado.'
}

# Instalar LibreOffice, se não estiver instalado
Write-Host 'Verificando/Instalando LibreOffice...'
try {
    winget install --id TheDocumentFoundation.LibreOffice --accept-package-agreements --accept-source-agreements --silent
    Write-Host 'LibreOffice instalado/verificado.'
} catch {
    Write-Host "Ignorando erro (provavelmente ja instalado)."
}

# Criar ambiente virtual
Write-Host 'Criando ambiente virtual em .\venv'
python -m venv venv

# Ativar ambiente virtual
Write-Host 'Ativando ambiente virtual...'
& .\venv\Scripts\Activate.ps1

# Instalar dependências
Write-Host 'Instalando dependencias do Python...'
python -m pip install --upgrade pip
python -m pip install -r app\requirements.txt

# Verificações de compatibilidade
Write-Host 'Executando verificacoes de compatibilidade...'
try {
    python tools\test_compatibility.py
} catch {
    Write-Host "Erro ao executar verificacoes de compatibilidade: $_"
}

# Verificar LibreOffice especificamente
Write-Host '📄 Verificando LibreOffice...'
try {
    python tools\check_libreoffice.py
} catch {
    Write-Host "Erro ao verificar LibreOffice: $_"
}

Write-Host '✅ Setup finalizado!'
Write-Host '🎯 Use python run.py para gerar o curriculo facilmente.'
Write-Host '🔧 Use python tools\check_libreoffice.py para verificar o LibreOffice.'