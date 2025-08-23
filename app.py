import pytesseract
from pdf2image import convert_from_path
import re
import os
import logging

# Configuração de logging
logging.basicConfig(
    filename='log.txt',
    filemode='a',
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

# Caminho opcional se o Tesseract não estiver no PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_numero_guia(pdf_path):
    nome_arquivo = os.path.basename(pdf_path)
    pasta = os.path.dirname(pdf_path)

    try:
        paginas = convert_from_path(pdf_path, dpi=300)

        for i, pagina in enumerate(paginas):
            texto = pytesseract.image_to_string(pagina, lang='por')

            padrao = r'N[º°] Guia no Prestador[:\s]*([\d]+)'
            resultado = re.search(padrao, texto, re.IGNORECASE)

            if resultado:
                numero = resultado.group(1)
                novo_nome = f"{numero}.pdf"
                novo_caminho = os.path.join(pasta, novo_nome)

                # Renomeia o arquivo PDF
                os.rename(pdf_path, novo_caminho)

                msg = f"Arquivo: {nome_arquivo} | Página: {i + 1} | Número da guia encontrado: {numero} | Renomeado para: {novo_nome}"
                print(msg)
                logging.info(msg)
                return numero

        # Se não encontrar em nenhuma página
        msg = f"Arquivo: {nome_arquivo} | Número da guia NÃO encontrado."
        print(msg)
        logging.info(msg)
        return None

    except Exception as e:
        msg = f"Arquivo: {nome_arquivo} | Erro ao processar o PDF: {e}"
        print(msg)
        logging.error(msg)
        return None

# Caminho da pasta onde estão os PDFs
pasta_pdf = 'PDF'

# Verifica todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta_pdf):
    if nome_arquivo.lower().endswith('.pdf'):
        caminho_completo = os.path.join(pasta_pdf, nome_arquivo)
        extrair_numero_guia(caminho_completo)