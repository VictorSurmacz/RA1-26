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

        # =====================================================================
        # mostra o resultado desta linha no display e espera botao pra avancar
        # assim o usuario ve cada resultado antes de ir pro proximo
        # =====================================================================
        linhas.append(f"    @ --- mostrar linha {linha_atual} no display ---")
        linhas.append(f"    VPOP {{D0}}")                           # pega o resultado

        # multiplica por 100 pra ter 2 casas decimais no display
        linhas.append(f"    LDR R0, =const_cem")
        linhas.append(f"    VLDR.F64 D1, [R0]")
        linhas.append(f"    VMUL.F64 D0, D0, D1")                  # D0 = resultado * 100
        linhas.append(f"    VCVT.S32.F64 S0, D0")                  # converte pra inteiro
        linhas.append(f"    VMOV R4, S0")                           # R4 = resultado * 100

        # verifica se eh negativo
        linhas.append(f"    MOV R8, #0")
        linhas.append(f"    CMP R4, #0")
        linhas.append(f"    BGE positivo_{linha_atual}")
        linhas.append(f"    MOV R8, #1")
        linhas.append(f"    RSB R4, R4, #0")
        linhas.append(f"positivo_{linha_atual}:")

        # prepara pra extrair digitos
        linhas.append(f"    LDR R5, =tabela_7seg")
        linhas.append(f"    MOV R6, #0")                            # HEX3-0
        linhas.append(f"    MOV R7, #0")                            # HEX5-4

        # digito 0 (centesimo) -> HEX0
        linhas.append(f"    BL div10")
        linhas.append(f"    LDR R0, [R5, R3, LSL #2]")
        linhas.append(f"    ORR R6, R6, R0")
        linhas.append(f"    MOV R4, R2")

        # digito 1 (decimo) -> HEX1
        linhas.append(f"    BL div10")
        linhas.append(f"    LDR R0, [R5, R3, LSL #2]")
        linhas.append(f"    LSL R0, R0, #8")
        linhas.append(f"    ORR R6, R6, R0")
        linhas.append(f"    MOV R4, R2")

        # HEX2 = ponto decimal (segmento D = traco embaixo)
        linhas.append(f"    MOV R0, #0x08")
        linhas.append(f"    LSL R0, R0, #16")
        linhas.append(f"    ORR R6, R6, R0")

        # digito 2 (unidade) -> HEX3
        linhas.append(f"    BL div10")
        linhas.append(f"    LDR R0, [R5, R3, LSL #2]")
        linhas.append(f"    LSL R0, R0, #24")
        linhas.append(f"    ORR R6, R6, R0")
        linhas.append(f"    MOV R4, R2")

        # digito 3 (dezena) -> HEX4
        linhas.append(f"    BL div10")
        linhas.append(f"    LDR R0, [R5, R3, LSL #2]")
        linhas.append(f"    ORR R7, R7, R0")
        linhas.append(f"    MOV R4, R2")

        # digito 4 -> HEX5 (sinal negativo ou centena)
        linhas.append(f"    CMP R8, #1")
        linhas.append(f"    BNE digito5_{linha_atual}")
        linhas.append(f"    MOV R0, #0x40")
        linhas.append(f"    LSL R0, R0, #8")
        linhas.append(f"    ORR R7, R7, R0")
        linhas.append(f"    B display_{linha_atual}")

        linhas.append(f"digito5_{linha_atual}:")
        linhas.append(f"    BL div10")
        linhas.append(f"    LDR R0, [R5, R3, LSL #2]")
        linhas.append(f"    LSL R0, R0, #8")
        linhas.append(f"    ORR R7, R7, R0")

        # escreve nos displays
        linhas.append(f"display_{linha_atual}:")
        linhas.append(f"    LDR R0, =0xFF200020")
        linhas.append(f"    STR R6, [R0]")
        linhas.append(f"    LDR R0, =0xFF200030")
        linhas.append(f"    STR R7, [R0]")

        # acende LEDs com o numero da linha atual (pra saber qual linha eh)
        # linha 0 = 1 LED, linha 1 = 2 LEDs, etc
        linhas.append(f"    LDR R0, =0xFF200000")
        linhas.append(f"    LDR R1, =led_linha_{linha_atual}")
        linhas.append(f"    LDR R2, [R1]")
        linhas.append(f"    STR R2, [R0]")

        # espera o usuario apertar KEY0 (botao 0) pra avancar pra proxima linha
        # o botao fica no endereco 0xFF200050, bit 0
        # fica num loop lendo o botao ate ele ser pressionado
        linhas.append(f"espera_botao_{linha_atual}:")
        linhas.append(f"    LDR R0, =0xFF20005C")                  # edge capture register dos botoes
        linhas.append(f"    LDR R1, [R0]")                         # le quais botoes foram apertados
        linhas.append(f"    TST R1, #1")                            # testa se KEY0 foi apertado (bit 0)
        linhas.append(f"    BEQ espera_botao_{linha_atual}")        # se nao, volta a esperar
        linhas.append(f"    STR R1, [R0]")                          # limpa o edge capture (escreve 1 pra resetar)

        linha_atual += 1

    # =========================================================================
    # fim do programa — apaga displays e para
    # =========================================================================
    linhas.append("")
    linhas.append("    @ --- fim: apaga displays ---")
    linhas.append("    MOV R6, #0")
    linhas.append("    LDR R0, =0xFF200020")
    linhas.append("    STR R6, [R0]")
    linhas.append("    LDR R0, =0xFF200030")
    linhas.append("    STR R6, [R0]")
    linhas.append("    LDR R0, =0xFF200000")
    linhas.append("    STR R6, [R0]")

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

    # constante 100.0 pra multiplicar antes de mostrar no display
    linhas.append("const_cem: .double 100.0")

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

    # padrao de LEDs pra cada linha (indica qual linha ta sendo mostrada)
    # linha 0 = 1 LED, linha 1 = 3 LEDs, linha 2 = 7 LEDs, etc
    for i in range(linha_atual):
        led_val = (1 << (i + 1)) - 1       # 1, 3, 7, 15, 31...
        if led_val > 0x3FF:
            led_val = 0x3FF                 # maximo 10 LEDs
        linhas.append(f"led_linha_{i}: .word {led_val}")

    # junta tudo com quebra de linha e retorna o assembly completo
    return "\n".join(linhas)