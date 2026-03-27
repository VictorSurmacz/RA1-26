# ================= INTEGRANTES ======================
#Grupo -> RA1 - 26
#Github -> https://github.com/VictorSurmacz/RA1-26
#Renan Felipe Straub Czervinski
#Renan de Rocco Pamplona
#Victor Eduardo Surmacz
# ====================================================


# essa funcao eh apenas pra validar em python nossas expressoes, nao eh o resultado do trabalho
# apenas para verificacao, com operacoes explicitas em python

def executarExpressao(tokens, resultados, memoria):
    pilha = []

    for i, (tipo,valor) in enumerate(tokens): #percorre pelos tokens, pegano tipo e valor
        #comparacao de tipos, num, op, paren, res, id
        if tipo == "NUM":
            valor_em_float = float(valor)
            pilha.append(valor_em_float)

        elif tipo == "OP": #se operacao, fazemos a operacao com base no valor na tupla
            B = pilha.pop()
            A = pilha.pop()
            
            if valor == "+":
                pilha.append(A + B)
            elif valor == "-":
                pilha.append(A - B)
            elif valor == "*":
               pilha.append(A * B)
            elif valor == "/":
                pilha.append(A / B)
            elif valor == "//":
                pilha.append(A // B)
            elif valor == "%":
                pilha.append(A % B)
            elif valor == "^":
                pilha.append(A ** B)
            
        elif tipo == "PAREN": #parenteses ignoramos
            continue
        elif tipo == "RES": # buscamos o resultado de N linhas
            N =int(pilha.pop())
            valor_buscado = resultados[len(resultados) - N]
            pilha.append(valor_buscado)


        elif tipo == "ID": #adicionamos na memoria pelo ID, caso o token anterior seja um numero
            nome = valor
            token_anterior = tokens[i - 1] if i > 0 else None

            if token_anterior and token_anterior[0] == "NUM":
                v = pilha.pop()
                memoria[nome] = v
                pilha.append(v)
            else: 
                pilha.append(memoria.get(nome, 0.0))
        
    if pilha:
        return pilha[-1]
    return 0.0


