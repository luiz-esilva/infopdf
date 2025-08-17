# 📄 Extração de Número da Guia em PDFs usando OCR

Este projeto Python realiza a extração automática do **número da guia** presente em arquivos PDF, utilizando **OCR** com `pytesseract` e `pdf2image`.

Seu funcionamento foi testado utilizando PDFs escaneados, funcionando perfeitamente.

Todos os testes foram realizados em máquinas Windows 10 64bits.

---

## 🧰 Pré-Requisitos

### 1. Instalar Tesseract OCR

- Vá até a pasta `Requisitos/` e execute o instalador:
tesseract-ocr-w64-setup-v5.3.0.20221214.exe

> O instalador irá instalar o Tesseract em:
C:\Users\usuario\AppData\Local\Programs\Tesseract-OCR\

---

### 2. Copiar a Pasta Poppler

- Copie a pasta `poppler-24.08.0` da pasta `Requisitos/` para o disco **C:**
C:\poppler-24.08.0\


---

### 3. Configurar Variáveis de Ambiente

Adicione os seguintes caminhos ao **Path do usuário** nas variáveis de ambiente do sistema:
C:\poppler-24.08.0\Library\bin
C:\Users\usuario\AppData\Local\Programs\Tesseract-OCR

---

### 4. Instalar Bibliotecas Python

Execute:

```bash
pip install pytesseract pdf2image Pillow
```

---

## 📂 Organização dos Arquivos

Coloque seus arquivos PDF na pasta PDF/.

PDF/
├── exemplo1.pdf
├── exemplo2.pdf

---

## 🔍 O Que o Script Faz

- Converte as páginas dos PDFs em imagens.

- Usa OCR para extrair o texto.

- Procura o padrão:
Nº Guia no Prestador: 123456789

- Ou variações como:
N° Guia no Prestador
Com ou sem espaços e dois-pontos

---

## ✅ Requisitos Incluídos

Para facilitar, todos os arquivos necessários estão na pasta:

Requisitos/
├── tesseract-ocr-w64-setup-v5.3.0.20221214.exe
└── poppler-24.08.0/