# ================= INTEGRANTES ======================
#Grupo -> RA1 - 26
#Github -> https://github.com/VictorSurmacz/RA1-26
#Renan Felipe Straub Czervinski
#Renan de Rocco Pamplona
#Victor Eduardo Surmacz
# ====================================================


# gera o codigo assembly ARMv7 a partir dos tokens
# essa funcao nao faz nenhum calculo, ela so monta o texto do programa assembly
# que vai rodar no cpulator

def gerarAssembly(todos_tokens):
    linhas = []          # cada item eh uma linha do assembly final
    constantes = []      # guarda os numeros pra declarar no .data (nome, valor)
    contador = 0         # serve pra criar nomes unicos: const_0, const_1...
    variaveis = set()    # nomes das variaveis de memoria (PI, RAIO, X...)
    linha_atual = 0      # qual linha do arquivo .txt estamos processando

    # cabecalho do assembly - todo programa precisa disso
    linhas.append(".global _start")
    linhas.append(".section .text")
    linhas.append("_start:")

    # percorre cada linha do arquivo (cada linha eh uma lista de tokens)
    for tokens in todos_tokens:
        for (tipo, valor) in tokens:

            # parenteses nao geram nada no assembly, so servem pro lexico
            if tipo == "PAREN":
                pass

            # quando eh um numero, carrega ele pro registrador e empilha
            # eh sempre o mesmo padrao: busca o endereco, carrega o valor, empilha
            if tipo == "NUM":
                nome = f"const_{contador}"
                contador += 1
                constantes.append((nome, valor))

                linhas.append(f"   LDR R0, ={nome}")       # R0 recebe o endereco da constante
                linhas.append(f"   VLDR.F64 D0, [R0]")     # D0 recebe o valor float que ta nesse endereco
                linhas.append(f"   VPUSH {{D0}}")           # joga D0 na pilha
                
            # quando eh operador, desempilha dois valores, faz a operacao, empilha resultado
            elif tipo == "OP":
                linhas.append(f"    VPOP {{D1}}")           # D1 = topo da pilha (B)
                linhas.append(f"    VPOP {{D0}}")           # D0 = segundo da pilha (A)
            
                if valor == "+":
                    linhas.append(f"  VADD.F64 D0, D0, D1")    # D0 = A + B

                elif valor == "-":
                    linhas.append(f"   VSUB.F64 D0, D0, D1")   # D0 = A - B

                elif valor == "*": 
                    linhas.append(f"   VMUL.F64 D0, D0, D1")   # D0 = A * B

                # divisao inteira: divide e trunca (joga fora os decimais)
                # precisa converter pra inteiro e voltar pra float
                elif valor == "//":
                    linhas.append(f"   VDIV.F64 D0, D0, D1")       # D0 = A / B (com decimais)
                    linhas.append(f"   VCVT.S32.F64 S2, D0")       # converte float -> inteiro (trunca)
                    linhas.append(f"   VCVT.F64.S32 D0, S2")       # converte inteiro -> float (sem decimais)
             
                elif valor == "/":
                    linhas.append(f"   VDIV.F64 D0, D0, D1")   # D0 = A / B (divisao real)

                # resto da divisao: formula eh A - (A // B) * B
                elif valor == "%":
                    linhas.append(f"   VMOV.F64 D2, D0")           # salva A em D2 pq vamos precisar depois
                    linhas.append(f"   VDIV.F64 D0, D0, D1")       # D0 = A / B
                    linhas.append(f"   VCVT.S32.F64 S4, D0")       # trunca pra inteiro (A // B)
                    linhas.append(f"   VCVT.F64.S32 D0, S4")       # volta pra float
                    linhas.append(f"   VMUL.F64 D0, D0, D1")       # D0 = (A // B) * B
                    linhas.append(f"   VSUB.F64 D0, D2, D0")       # D0 = A - (A // B) * B = resto

                # potencia: multiplica A por si mesmo B vezes usando loop
                elif valor == "^":
                    label_id = contador         # numero unico pro label do loop
                    contador += 1
                    linhas.append(f"   VMOV.F64 D2, D0")           # D2 = copia de A (base)
                    linhas.append(f"   VCVT.S32.F64 S4, D1")       # converte B pra inteiro
                    linhas.append(f"   VMOV R1, S4")                # R1 = B (contador do loop)
                    linhas.append(f"pot_loop_{label_id}:")           # inicio do loop
                    linhas.append(f"   CMP R1, #1")                 # compara contador com 1
                    linhas.append(f"   BLE pot_fim_{label_id}")      # se <= 1, acabou
                    linhas.append(f"   VMUL.F64 D0, D0, D2")       # D0 = D0 * A (multiplica mais uma vez)
                    linhas.append(f"   SUBS R1, R1, #1")            # contador = contador - 1
                    linhas.append(f"   B pot_loop_{label_id}")       # volta pro inicio do loop
                    linhas.append(f"pot_fim_{label_id}:")            # fim do loop
                
                # depois de qualquer operacao, o resultado fica em D0
                # entao empilha pra proxima operacao poder usar
                linhas.append(f"  VPUSH {{D0}}")
                     
            # RES busca o resultado de N linhas atras
            elif tipo == "RES":
                    n_valor = int(float(constantes[-1][1]))     # pega o N da ultima constante
                    resultado_idx = linha_atual - n_valor        # calcula qual linha buscar
    
                    # remove as 3 instrucoes do NUM anterior (que era o N)
                    linhas.pop()    # remove VPUSH {D0}
                    linhas.pop()    # remove VLDR.F64 D0, [R0]
                    linhas.pop()    # remove LDR R0, =const_X
    
                    # carrega o resultado da linha correta
                    linhas.append(f"    LDR R0, =resultado_{resultado_idx}")
                    linhas.append(f"    VLDR.F64 D0, [R0]")
                    linhas.append(f"  VPUSH {{D0}}")

            # ID eh nome de variavel de memoria (PI, RAIO, X, etc)
            elif tipo == "ID":
                    variaveis.add(valor)    # registra o nome pra declarar no .data

                    # olha o token anterior pra decidir se eh armazenamento ou leitura
                    idx_atual = tokens.index((tipo, valor))
                    token_anterior = tokens[idx_atual - 1] if idx_atual > 0 else None
    
                    # se antes veio NUM ou OP, eh armazenamento: (V NOME)
                    if token_anterior and token_anterior[0] in ("NUM", "OP"):
                        linhas.append(f"    VPOP {{D0}}")               # pega o valor da pilha
                        linhas.append(f"    LDR R0, =var_{valor}")      # endereco da variavel
                        linhas.append(f"    VSTR.F64 D0, [R0]")         # guarda o valor na memoria
                    else:
                        # se antes veio PAREN, eh leitura: (NOME)
                        linhas.append(f"    LDR R0, =var_{valor}")      # endereco da variavel
                        linhas.append(f"    VLDR.F64 D0, [R0]")         # carrega o valor da memoria
            
                    linhas.append(f"  VPUSH {{D0}}")

        # no fim de cada linha do arquivo, salva o resultado
        # assim o RES consegue acessar depois
        linhas.append(f"    @ resultado da linha {linha_atual}")
        linhas.append(f"    VPOP {{D0}}")                           # pega resultado da pilha
        linhas.append(f"    LDR R0, =resultado_{linha_atual}")      # endereco pra salvar
        linhas.append(f"    VSTR.F64 D0, [R0]")                     # salva na memoria
        linhas.append(f"    VPUSH {{D0}}")                           # devolve pra pilha
        linha_atual += 1

    # =========================================================================
    # exibicao no display de 7 segmentos do DE1-SoC
    # pega o resultado da ultima linha e mostra nos HEX displays
    # o resultado eh um float, entao convertemos pra inteiro pra mostrar
    # =========================================================================
    linhas.append("")
    linhas.append("    @ --- exibir resultado no display de 7 segmentos ---")
    linhas.append("    VPOP {D0}")                          # pega o ultimo resultado
    linhas.append("    VCVT.S32.F64 S0, D0")               # converte float pra inteiro
    linhas.append("    VMOV R4, S0")                        # R4 = resultado como inteiro

    # verifica se eh negativo
    linhas.append("    MOV R8, #0")                         # R8 = flag de sinal (0 = positivo)
    linhas.append("    CMP R4, #0")
    linhas.append("    BGE positivo")
    linhas.append("    MOV R8, #1")                         # marca como negativo
    linhas.append("    RSB R4, R4, #0")                     # inverte o sinal (R4 = -R4)
    linhas.append("positivo:")

    # extrai cada digito dividindo por 10 repetidamente
    # a funcao div10 ta la embaixo: divide R4 por 10, quociente em R2, resto em R3
    linhas.append("    LDR R5, =tabela_7seg")              # endereco da tabela de conversao
    linhas.append("    MOV R6, #0")                         # R6 = valor acumulado pro HEX3-0
    linhas.append("    MOV R7, #0")                         # R7 = valor acumulado pro HEX5-4

    # digito 0 (unidade) -> HEX0
    linhas.append("    BL div10")                           # chama subrotina: R2=quociente, R3=resto
    linhas.append("    LDR R0, [R5, R3, LSL #2]")          # busca padrao 7seg do digito
    linhas.append("    ORR R6, R6, R0")                     # coloca no HEX0 (bits 0-6)
    linhas.append("    MOV R4, R2")                         # R4 = quociente (pro proximo digito)

    # digito 1 (dezena) -> HEX1
    linhas.append("    BL div10")
    linhas.append("    LDR R0, [R5, R3, LSL #2]")
    linhas.append("    LSL R0, R0, #8")                     # desloca 8 bits pra posicao do HEX1
    linhas.append("    ORR R6, R6, R0")
    linhas.append("    MOV R4, R2")

    # digito 2 (centena) -> HEX2
    linhas.append("    BL div10")
    linhas.append("    LDR R0, [R5, R3, LSL #2]")
    linhas.append("    LSL R0, R0, #16")                    # desloca 16 bits pra posicao do HEX2
    linhas.append("    ORR R6, R6, R0")
    linhas.append("    MOV R4, R2")

    # digito 3 (milhar) -> HEX3
    linhas.append("    BL div10")
    linhas.append("    LDR R0, [R5, R3, LSL #2]")
    linhas.append("    LSL R0, R0, #24")                    # desloca 24 bits pra posicao do HEX3
    linhas.append("    ORR R6, R6, R0")
    linhas.append("    MOV R4, R2")

    # digito 4 (dez milhar) -> HEX4
    linhas.append("    BL div10")
    linhas.append("    LDR R0, [R5, R3, LSL #2]")
    linhas.append("    ORR R7, R7, R0")                     # coloca no HEX4 (bits 0-6)
    linhas.append("    MOV R4, R2")

    # digito 5 -> HEX5 (mostra sinal negativo se precisar)
    linhas.append("    CMP R8, #1")                         # eh negativo?
    linhas.append("    BNE mostrar_digito5")
    linhas.append("    MOV R0, #0x40")                      # padrao do '-' no 7seg (segmento G)
    linhas.append("    LSL R0, R0, #8")
    linhas.append("    ORR R7, R7, R0")
    linhas.append("    B escrever_display")

    linhas.append("mostrar_digito5:")
    linhas.append("    BL div10")
    linhas.append("    LDR R0, [R5, R3, LSL #2]")
    linhas.append("    LSL R0, R0, #8")                     # desloca 8 bits pra posicao do HEX5
    linhas.append("    ORR R7, R7, R0")

    # escreve nos enderecos dos displays
    linhas.append("escrever_display:")
    linhas.append("    LDR R0, =0xFF200020")                # endereco HEX3-HEX0
    linhas.append("    STR R6, [R0]")                       # escreve os 4 digitos de baixo
    linhas.append("    LDR R0, =0xFF200030")                # endereco HEX5-HEX4
    linhas.append("    STR R7, [R0]")                       # escreve os 2 digitos de cima

    # tambem acende LEDs com o valor do resultado
    linhas.append("")
    linhas.append("    @ --- acender LEDs ---")
    linhas.append("    LDR R0, =0xFF200000")                # endereco dos LEDs
    linhas.append(f"    LDR R1, =resultado_{linha_atual - 1}")
    linhas.append("    VLDR.F64 D0, [R1]")
    linhas.append("    VCVT.S32.F64 S0, D0")
    linhas.append("    VMOV R2, S0")                        # R2 = resultado como inteiro
    linhas.append("    CMP R2, #0")
    linhas.append("    BGE leds_positivo")
    linhas.append("    RSB R2, R2, #0")                     # valor absoluto
    linhas.append("leds_positivo:")
    linhas.append("    LDR R3, =0x3FF")                     # mascara de 10 bits (carregada da memoria)
    linhas.append("    AND R2, R2, R3")                     # limita a 10 bits (10 LEDs)
    linhas.append("    STR R2, [R0]")                       # acende os LEDs

    # fim do programa - loop infinito que para a execucao
    linhas.append("")
    linhas.append("    B _halt")

    # =========================================================================
    # subrotina div10: divide R4 por 10 usando subtracao repetida
    # entrada: R4 = numero a dividir
    # saida: R2 = quociente, R3 = resto
    # =========================================================================
    linhas.append("")
    linhas.append("div10:")
    linhas.append("    MOV R2, #0")                         # R2 = quociente, comeca em 0
    linhas.append("    MOV R3, R4")                         # R3 = copia do numero (vai virar o resto)
    linhas.append("div10_loop:")
    linhas.append("    CMP R3, #10")                        # ainda cabe 10?
    linhas.append("    BLT div10_fim")                      # se menor que 10, acabou
    linhas.append("    SUB R3, R3, #10")                    # subtrai 10
    linhas.append("    ADD R2, R2, #1")                     # quociente += 1
    linhas.append("    B div10_loop")                       # repete
    linhas.append("div10_fim:")
    linhas.append("    BX LR")                              # retorna pra quem chamou

    linhas.append("")
    linhas.append("_halt:")
    linhas.append("    B _halt")

    # =========================================================================
    # secao de dados
    # =========================================================================
    linhas.append("")
    linhas.append(".section .data")

    # tabela de conversao pra display de 7 segmentos
    linhas.append("tabela_7seg:")
    linhas.append("    .word 0x3F")     # 0 = segmentos a,b,c,d,e,f
    linhas.append("    .word 0x06")     # 1 = segmentos b,c
    linhas.append("    .word 0x5B")     # 2 = segmentos a,b,d,e,g
    linhas.append("    .word 0x4F")     # 3 = segmentos a,b,c,d,g
    linhas.append("    .word 0x66")     # 4 = segmentos b,c,f,g
    linhas.append("    .word 0x6D")     # 5 = segmentos a,c,d,f,g
    linhas.append("    .word 0x7D")     # 6 = segmentos a,c,d,e,f,g
    linhas.append("    .word 0x07")     # 7 = segmentos a,b,c
    linhas.append("    .word 0x7F")     # 8 = todos os segmentos
    linhas.append("    .word 0x6F")     # 9 = segmentos a,b,c,d,f,g

    # declara cada numero que apareceu no codigo como float 64 bits
    for (nome, valor) in constantes:
        linhas.append(f"{nome}: .double {valor}")

    # reserva espaco pra cada variavel de memoria (8 bytes = 1 float 64 bits)
    for var in variaveis:
        linhas.append(f"var_{var}: .space 8")

    # reserva espaco pra guardar o resultado de cada linha (pra RES usar)
    for i in range(linha_atual):
        linhas.append(f"resultado_{i}: .space 8")

    # junta tudo com quebra de linha e retorna o assembly completo
    return "\n".join(linhas)