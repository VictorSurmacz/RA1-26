# essa funcao eh apenas pra validar em python nossas expressoes, nao eh o resultado do trabalho
# apenas para verificacao, com operacoes explicitas em python

def executarExpressao(tokens, resultados, memoria):
    pilha = []

    for i, (tipo,valor) in enumerate(tokens):
     
        if tipo == "NUM":
            valor_em_float = float(valor)
            pilha.append(valor_em_float)

        elif tipo == "OP":
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
            
        elif tipo == "PAREN":
            continue
        elif tipo == "RES":
            N = pilha.pop()
            valor_buscado = resultados[len(resultados) - N]
            pilha.append(valor_buscado)


        elif tipo == "ID":
            nome = valor

            if len(pilha) > 0 and isinstance(pilha[-1], float):
                v = pilha.pop()
                memoria[nome] = v
                pilha.append(v)

            else:
                pilha.append(memoria.get(nome,0.0))

        
    if pilha:
        return pilha[-1]
    return 0.0


