# ================= INTEGRANTES ======================
#Grupo -> RA1 - 26
#Github -> https://github.com/VictorSurmacz/RA1-26
#Renan Felipe Straub Czervinski
#Renan de Rocco Pamplona
#Victor Eduardo Surmacz
# ====================================================

# =============================================================================
# lexico.py , analisador lexico com automato finito deterministico (AFD)
#
# cada estado do AFD eh uma funcao separada
# nao usa regex, nao usa bibliotecas de expressoes regulares
# o analisador percorre a linha caractere por caractere
# e cada funcao de estado decide oq fazer com o caractere atual
# =============================================================================

# lista dos operadores que tem so 1 caractere
# o '/' nao ta aqui pq precisa de tratamento especial (pode ser / ou //)
operadorSimples = ['+', '-', '*', '%', '^',]

# funcoes auxiliares pra classificar caracteres
# usadas pelas funcoes de estado pra saber oq eh cada caractere

def ehDigito(c): 
    return c >= '0' and c <= '9'

def ehLetra(c): 
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

def ehOperadorSimples(c):
    return c in operadorSimples

def ehEspaco(c): 
    return c == ' ' or c == "\t"


# =============================================================================
# funcoes de estado do AFD
#
# cada funcao recebe:
#   linha -> a string inteira sendo analisada
#   pos   -> posicao atual (indice do caractere)
#   token -> lista onde os tokens emitidos sao adicionados
#
# cada funcao retorna uma tupla:
#   (proxima_funcao_de_estado, nova_posicao)
# =============================================================================

def estado_inicio(linha, pos, token):
 
    c = linha[pos]
    
    # espaco ou tab -> ignora e continua
    if ehEspaco(c):
        return estado_inicio, pos + 1
    
    # digito -> comeca um numero, vai pro estado_numero
    if ehDigito(c): 
        return estado_numero(linha, pos, token)
    
    # parenteses -> emite token e volta pra ca
    elif c == '(' or c == ')':
        token.append(("PAREN", c))
        return estado_inicio, pos + 1
    
    # barra -> precisa verificar se eh / ou //
    # olha o proximo caractere pra decidir
    elif c == '/':
        if pos + 1 < len(linha) and linha[pos + 1] == '/':
            token.append(("OP", "//"))      # divisao inteira, avanca 2
            return estado_inicio, pos + 2
        else:
            token.append(("OP","/"))         # divisao real, avanca 1
            return estado_inicio ,pos + 1

    # operadores simples de 1 caractere (+ - * % ^)
    elif ehOperadorSimples(c):
        token.append(("OP", c))
        return estado_inicio, pos + 1 

    # letra -> comeca um identificador (nome de variavel ou RES)
    elif ehLetra(c):       
        return estado_identificador(linha,pos,token)    
    
    # nada casou -> caractere invalido, emite erro
    else:
        token.append(("ERRO", c))
        return estado_inicio, pos + 1


def estado_numero(linha,pos,token):

    acumulador = ""

    # vai consumindo digitos enquanto tiver
    while pos < len(linha) and ehDigito(linha[pos]):
        acumulador += linha[pos]
        pos += 1
    
    # se o proximo caractere eh ponto, tem parte decimal
    if pos < len(linha) and linha[pos] == '.':
        acumulador += '.'
        pos += 1
        # chama estado_decimal direto passando o acumulador
        # pq estado_decimal precisa saber oq ja foi lido (ex: "3.")
        return estado_decimal(linha, pos, token, acumulador)
    
    # nao tem ponto, eh numero inteiro, emite e volta
    token.append(("NUM", acumulador))
    return estado_inicio, pos


def estado_decimal(linha, pos, token, acumulador):

    # consome digitos da parte decimal
    while pos < len(linha) and ehDigito(linha[pos]):
        acumulador += linha[pos]
        pos += 1

    # se apareceu outro ponto, eh numero malformado (ex: 3.14.5)
    if  pos < len(linha) and  linha[pos] == ".":
        token.append(("ERRO", acumulador + linha[pos]))
        return estado_inicio, pos + 1
    else:
        # numero real completo, emite o token
        token.append(("NUM", acumulador))
        return estado_inicio, pos
    

def estado_identificador(linha, pos, token):

    nome = ""

    # consome letras enquanto tiver
    while pos < len(linha) and ehLetra(linha[pos]):
        nome += linha[pos]
        pos += 1

    # RES eh a unica keyword da linguagem nesta fase
    if nome == "RES":
        token.append(("RES", "RES"))
    else:
        # qualquer outro nome eh identificador de variavel (PI, RAIO, X, etc)
        token.append(("ID", nome))

    return estado_inicio, pos


# =============================================================================
# funcao principal 
# =============================================================================

def parseExpressao(linha):

    tokens = []
    pos = 0
    estado = estado_inicio  # comeca no estado hub

    # percorre a linha inteira caractere por caractere
    while pos < len(linha):
        estado, pos = estado(linha, pos, tokens)

    return tokens


# =============================================================================
# testes rapidos , roda so se executar este arquivo diretamente
# =============================================================================

if __name__ == "__main__":
   
    testes = [
        "(3.14 2.0 +)",
        "((1.5 2.0 *) (3.0 4.0 *) /)",
        "(5 RES)",
        "(10.5 CONTADOR MEM)",
    ]
 
    for expr in testes:
        print(f"\nEntrada: {expr}")
        resultado = parseExpressao(expr)
        for tok in resultado:
            print(f"  {tok[0]:6s} → {tok[1]}")