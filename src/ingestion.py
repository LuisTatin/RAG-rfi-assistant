from pypdf import PdfReader

def extrair_texto_pdf(caminho):
    reader = PdfReader(caminho)
    texto = ""

    for page in reader.pages:
        texto += page.extract_text() + "\n"

    return texto

def chunkar_texto(texto, tamanho=500):
    chunks = []

    for i in range(0, len(texto), tamanho):
        chunks.append(texto[i:i + tamanho])

    return chunks