# ================= INTEGRANTES ======================
#Grupo -> RA1 - 26
#Github -> https://github.com/VictorSurmacz/RA1-26
#Renan Felipe Straub Czervinski
#Renan de Rocco Pamplona
#Victor Eduardo Surmacz
# ====================================================

import sys
 
 
def lerArquivo(nome_arquivo, linhas):
    try:
        with open(nome_arquivo, "r") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    linhas.append(linha)
    except FileNotFoundError:
        print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
        sys.exit(1)
 
 
def exibirResultados(resultados):
    for i, valor in enumerate(resultados):
        print(f"Linha {i + 1}: {valor:.2f}")
 