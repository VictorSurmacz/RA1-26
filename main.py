# ================= INTEGRANTES ======================
#Grupo -> RA1 - 26
#Github -> https://github.com/VictorSurmacz/RA1-26
#Renan Felipe Straub Czervinski
#Renan de Rocco Pamplona
#Victor Eduardo Surmacz
# ====================================================


# =============================================================================
# main.py -> ponto de entrada do programa
#
# uso: python main.py teste1.txt
#
# esse arquivo junta todos os modulos e executa na ordem certa:
# ler arquivo → analise lexica → executar (validar) → exibir → gerar assembly
# =============================================================================

import sys
from interface import lerArquivo, exibirResultados
from lexico import parseExpressao
from executor import executarExpressao
from gerador import gerarAssembly


def main():
    # verifica se o usuario passou o nome do arquivo na linha de comando
    # se nao passou, mostra como usar e encerra
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_de_teste>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]

    # 1. le o arquivo de teste -> cada linha eh uma expressao RPN
    linhas = []
    lerArquivo(nome_arquivo, linhas)

    # 2. analise lexica -> transforma cada linha em uma lista de tokens
    # todos_tokens eh uma lista de listas: uma lista de tokens por linha
    todos_tokens = []
    for linha in linhas:
        tokens = parseExpressao(linha)
        todos_tokens.append(tokens)

    resultados = [] # 3. executa as expressoes em python pra validar os resultados
    memoria = {}    # dicionario compartilhado entre todas as linhas pra MEM
    for tokens in todos_tokens:
        valor = executarExpressao(tokens, resultados, memoria)
        resultados.append(valor)    # cada resultado entra na lista pra RES acessar

    # 4. mostra os resultados formatados no terminal
    exibirResultados(resultados)

    # 5. gera o codigo assembly ARMv7 a partir dos tokens
    codigo_assembly = gerarAssembly(todos_tokens)

    # 6. salva o assembly num arquivo .s 
    nome_saida = nome_arquivo.replace(".txt", "") + ".s"
    with open(nome_saida, "w") as f:
        f.write(codigo_assembly)
    print(f"\nAssembly salvo em: {nome_saida}")

    # 7. salva os tokens num arquivo txt 

    with open("tokens.txt", "w") as f:
        for i, tokens in enumerate(todos_tokens):
            f.write(f"Linha {i + 1}: {tokens}\n")
    print("Tokens salvos em: tokens.txt")


if __name__ == "__main__":
    main()