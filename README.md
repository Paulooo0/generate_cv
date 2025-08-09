# 📄 Gerador de Currículo Automatizado

Um projeto Python que automatiza a criação de currículos profissionais em formato DOCX e PDF, com suporte para Linux e Windows.

## 🚀 Funcionalidades

- **Geração automática de currículo** em formato DOCX
- **Conversão automática** de DOCX para PDF
- **Template personalizável** com seções estruturadas
- **Suporte multiplataforma** (Linux e Windows)
- **Setup automatizado** com scripts de instalação

## 📋 Pré-requisitos

- **Python 3.7+**
- **LibreOffice** (para conversão DOCX → PDF)
- **Git** (para clonar o repositório)

## 🛠️ Instalação

### Setup Universal (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/Paulooo0/generate_cv
cd generate_cv

# Execute o setup universal (detecta automaticamente o sistema)
python3 setup.py
```

### Setup Manual por Sistema

#### Linux (Ubuntu/Debian)

```bash
# Clone o repositório
git clone https://github.com/Paulooo0/generate_cv
cd generate_cv

# Execute o script de setup
chmod +x script/setup.sh
./script/setup.sh
```

#### Windows

```powershell
# Clone o repositório
git clone https://github.com/Paulooo0/generate_cv
cd generate_cv

# Execute o script de setup (PowerShell)
.\script\setup.ps1
```

### Verificações e Ferramentas

Após a instalação, você pode usar as ferramentas de verificação:

```bash
# Verificação geral de compatibilidade
python3 tools/test_compatibility.py

# Verificação específica do LibreOffice (Windows)
python3 tools/check_libreoffice.py

# Adicionar LibreOffice ao PATH (Windows)
python3 tools/add_libreoffice_to_path.py
```

### Instalação Manual

Se preferir instalar manualmente:

1. **Instale o LibreOffice:**
   - Linux: `sudo apt install libreoffice`
   - Windows: Baixe em [libreoffice.org](https://www.libreoffice.org/)

2. **Crie um ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux
   # ou
   .\venv\Scripts\Activate.ps1  # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r app/requirements.txt
   ```

## 📝 Uso

### Gerar o Currículo (Formas Fáceis)

#### **Opção 1: Script Universal (Recomendado)**
```bash
# Funciona em qualquer sistema
python3 run.py
```

#### **Opção 2: Scripts Específicos por Sistema**

**Linux/macOS:**
```bash
./script/run.sh
# ou
bash ./script/run.sh
```

**Windows:**
```powershell
# PowerShell
.\script\run.ps1

# Command Prompt
.\script\run.bat
```

#### **Opção 3: Manual (Avançado)**
```bash
# Ative o ambiente virtual (se necessário)
source venv/bin/activate  # Linux
# ou
.\venv\Scripts\Activate.ps1  # Windows

# Execute o gerador
python3 app/main.py  # Linux
# ou
python app/main.py   # Windows
```

### Personalizar o Currículo

Edite o arquivo `app/build_docx.py` para personalizar:

- **Informações pessoais** (nome, contato, links)
- **Resumo profissional**
- **Experiência profissional**
- **Educação**
- **Certificações**
- **Habilidades técnicas**
- **Idiomas**

Ou crie sessões novas como desejar

## 📄 Formato do Currículo

O currículo gerado inclui as seguintes seções:

1. **Cabeçalho** - Nome e informações de contato
2. **Resumo Profissional** - Descrição concisa do perfil
3. **Certificações** - Certificações relevantes
4. **Experiência Profissional** - Histórico de trabalho
5. **Educação** - Formação acadêmica
6. **Idiomas** - Proficiência em idiomas
7. **Habilidades Técnicas** - Competências técnicas

## 🔧 Dependências

- **python-docx** - Manipulação de arquivos DOCX
- **LibreOffice** - Conversão para PDF

## 🌐 Compatibilidade Cross-Platform

O projeto foi desenvolvido para funcionar em múltiplas plataformas:

### ✅ **Linux**
- Suporte completo
- Detecção automática do LibreOffice via PATH
- Scripts de setup otimizados para Ubuntu/Debian

### ✅ **Windows**
- Suporte completo
- Detecção automática do LibreOffice em caminhos padrão
- Scripts PowerShell para setup automatizado
- Compatibilidade com diferentes versões do LibreOffice

### ✅ **macOS**
- Suporte básico
- Detecção do LibreOffice via PATH
- Setup manual recomendado

### 🔧 **Melhorias de Compatibilidade**

- **Detecção automática de sistema operacional**
- **Busca inteligente do LibreOffice** em múltiplos caminhos
- **Criação de diretórios cross-platform**
- **Scripts de teste de compatibilidade**
- **Tratamento de erros específicos por plataforma**

## 📁 Arquivos Gerados

Após a execução, os seguintes arquivos serão criados na pasta `out/`:

- `cv.docx` - Currículo em formato DOCX
- `cv.pdf` - Currículo em formato PDF

## 🆘 Suporte

Se encontrar problemas:

1. **Execute o teste de compatibilidade:**
   ```bash
   python3 tools/test_compatibility.py
   ```

2. **Verifique se o LibreOffice está instalado:**
   - Windows: Execute `python3 tools/check_libreoffice.py`
   - Linux: Execute `sudo apt install libreoffice`

3. **Confirme que todas as dependências Python estão instaladas:**
   ```bash
   pip install -r app/requirements.txt
   ```

4. **Verifique se o ambiente virtual está ativado:**
   - Linux: `source venv/bin/activate`
   - Windows: `.\venv\Scripts\Activate.ps1`

5. **Problemas específicos do Windows:**
   - Execute `python3 tools/add_libreoffice_to_path.py` para adicionar ao PATH
   - Execute o PowerShell como administrador se necessário
   - Verifique se o Windows Defender não está bloqueando os scripts

6. **Reexecute o setup universal:**
   ```bash
   python3 setup.py
   ```
