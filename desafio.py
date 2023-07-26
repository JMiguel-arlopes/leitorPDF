import os
import glob
import re

def lerArquivo(file):
    return open(file, 'r', encoding='utf-8', errors='ignore').read()

def buscarPalavra(texto, palavraProcurada):
    return re.search(palavraProcurada, texto, re.IGNORECASE)

def procurarPalavraEmPdf(caminhoPasta, palavraProcurada):
    arquivosComPalavra = []

    arquivosPDF = glob.glob(os.path.join(caminhoPasta, '**/*.pdf'), recursive=True)

    for arquivoPdf in arquivosPDF:
        textoCompleto = lerArquivo(arquivoPdf)
        if buscarPalavra(textoCompleto, palavraProcurada):
            arquivosComPalavra.append(arquivoPdf)

    return arquivosComPalavra

def main():
    caminhoPasta = input("Digite o caminho da pasta onde deseja procurar os arquivos PDF: ")
    palavraProcurada = input("Digite a palavra que deseja procurar nos arquivos PDF: ")

    arquivosComPalavra = procurarPalavraEmPdf(caminhoPasta, palavraProcurada)

    if arquivosComPalavra:
        print("A palavra foi encontrada nos seguintes arquivos:")
        for arquivo in arquivosComPalavra:
            print(arquivo)
    else:
        print("A palavra não foi encontrada em nenhum arquivo PDF na pasta especificada.")

main()
