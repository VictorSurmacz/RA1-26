operadorSimples = ['+', '-', '*', '%', '^',]

def ehDigito(c): 
    return c >= '0' and c <= '9'

def ehLetra(c): 
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

def ehOperadorSimples(c):
    return c in operadorSimples

def ehEspaco(c): 
    return c == ' ' or c == "\t"

def estado_inicio(linha, pos, token):
    c = linha[pos]
    
    if ehEspaco(c):
        return estado_inicio, pos + 1
    
    if ehDigito(c): 
        return estado_numero(linha, pos, token)
    
    elif c == '(' or c == ')':
        token.append(("PAREN", c))
        return estado_inicio, pos + 1
    
    elif c == '/':
        if pos + 1 < len(linha) and linha[pos + 1] == '/':
            token.append(("OP", "//"))
            return estado_inicio, pos + 2
        else:
            token.append(("OP","/")) 
            return estado_inicio ,pos + 1

    elif ehOperadorSimples(c):
        token.append(("OP", c))
        return estado_inicio, pos + 1 

    elif ehLetra(c):       
        return estado_identificador(linha,pos,token)    
    

    else:
        token.append(("ERRO", c))
        return estado_inicio, pos + 1


def estado_numero(linha,pos,token):
    acumulador = ""

    while pos < len(linha) and ehDigito(linha[pos]):
        acumulador += linha[pos]
        pos += 1
    
    if pos < len(linha) and linha[pos] == '.':
        acumulador += '.'
        pos += 1
        return estado_decimal(linha, pos, token, acumulador)
    

    token.append(("NUM", acumulador))
    return estado_inicio, pos

def estado_decimal(linha, pos, token, acumulador):
    while pos < len(linha) and ehDigito(linha[pos]):
        acumulador += linha[pos]
        pos += 1
    if  pos < len(linha) and  linha[pos] == ".":
        token.append(("ERRO", acumulador + linha[pos]))
        return estado_inicio, pos + 1
    else:
        token.append(("NUM", acumulador))
        return estado_inicio, pos
    

def estado_identificador(linha, pos, token):
    nome = ""

    while pos < len(linha) and ehLetra(linha[pos]):
        nome += linha[pos]
        pos += 1

    if nome == "RES":
        token.append(("RES", "RES"))
    
    else:
        token.append(("ID", nome))

    return estado_inicio, pos

def parseExpressao(linha):

    tokens = []
    pos = 0
    estado = estado_inicio

    while pos < len(linha):
        estado, pos = estado(linha,pos,tokens)

    return tokens

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