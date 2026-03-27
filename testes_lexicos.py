# ================= INTEGRANTES ======================
#Grupo -> RA1 - 26
#Github -> https://github.com/VictorSurmacz/RA1-26
#Renan Felipe Straub Czervinski
#Renan de Rocco Pamplona
#Victor Eduardo Surmacz
# ====================================================

# =============================================================================
# testes_lexico.py -> testes do analisador lexico
#
# roda com: python testes_lexico.py
# testa se o parseExpressao gera os tokens certos pra entradas validas
# e se detecta erros em entradas invalidas
# =============================================================================

from lexico import parseExpressao


# ---- testes de entradas validas ----

def teste_numero_inteiro():
    tokens = parseExpressao("42")
    assert tokens == [("NUM", "42")], f"esperado NUM 42, obteve {tokens}"
    print("  ✓ numero inteiro")


def teste_numero_real():
    tokens = parseExpressao("3.14")
    assert tokens == [("NUM", "3.14")], f"esperado NUM 3.14, obteve {tokens}"
    print("  ✓ numero real")


def teste_numero_comeca_com_zero():
    tokens = parseExpressao("0.5")
    assert tokens == [("NUM", "0.5")], f"esperado NUM 0.5, obteve {tokens}"
    print("  ✓ numero comecando com zero")


def teste_operador_soma():
    tokens = parseExpressao("(3.0 2.0 +)")
    ops = [t for t in tokens if t[0] == "OP"]
    assert ops == [("OP", "+")], f"esperado OP +, obteve {ops}"
    print("  ✓ operador soma")


def teste_operador_subtracao():
    tokens = parseExpressao("(10.0 3.0 -)")
    ops = [t for t in tokens if t[0] == "OP"]
    assert ops == [("OP", "-")], f"esperado OP -, obteve {ops}"
    print("  ✓ operador subtracao")


def teste_operador_multiplicacao():
    tokens = parseExpressao("(4.0 2.0 *)")
    ops = [t for t in tokens if t[0] == "OP"]
    assert ops == [("OP", "*")], f"esperado OP *, obteve {ops}"
    print("  ✓ operador multiplicacao")


def teste_operador_divisao():
    tokens = parseExpressao("(10.0 2.0 /)")
    ops = [t for t in tokens if t[0] == "OP"]
    assert ops == [("OP", "/")], f"esperado OP /, obteve {ops}"
    print("  ✓ operador divisao")


def teste_operador_divisao_inteira():
    tokens = parseExpressao("(17.0 5.0 //)")
    ops = [t for t in tokens if t[0] == "OP"]
    assert ops == [("OP", "//")], f"esperado OP //, obteve {ops}"
    print("  ✓ operador divisao inteira")


def teste_operador_resto():
    tokens = parseExpressao("(17.0 5.0 %)")
    ops = [t for t in tokens if t[0] == "OP"]
    assert ops == [("OP", "%")], f"esperado OP %, obteve {ops}"
    print("  ✓ operador resto")


def teste_operador_potencia():
    tokens = parseExpressao("(2.0 8 ^)")
    ops = [t for t in tokens if t[0] == "OP"]
    assert ops == [("OP", "^")], f"esperado OP ^, obteve {ops}"
    print("  ✓ operador potencia")


def teste_parenteses():
    tokens = parseExpressao("()")
    assert tokens == [("PAREN", "("), ("PAREN", ")")], f"falhou: {tokens}"
    print("  ✓ parenteses")


def teste_expressao_simples():
    tokens = parseExpressao("(3.14 2.0 +)")
    esperado = [
        ("PAREN", "("),
        ("NUM", "3.14"),
        ("NUM", "2.0"),
        ("OP", "+"),
        ("PAREN", ")"),
    ]
    assert tokens == esperado, f"falhou: {tokens}"
    print("  ✓ expressao simples completa")


def teste_expressao_aninhada():
    tokens = parseExpressao("((1.5 2.0 *) (3.0 4.0 *) /)")
    esperado = [
        ("PAREN", "("),
        ("PAREN", "("),
        ("NUM", "1.5"),
        ("NUM", "2.0"),
        ("OP", "*"),
        ("PAREN", ")"),
        ("PAREN", "("),
        ("NUM", "3.0"),
        ("NUM", "4.0"),
        ("OP", "*"),
        ("PAREN", ")"),
        ("OP", "/"),
        ("PAREN", ")"),
    ]
    assert tokens == esperado, f"falhou: {tokens}"
    print("  ✓ expressao aninhada")


def teste_keyword_res():
    tokens = parseExpressao("(5 RES)")
    assert ("RES", "RES") in tokens, f"RES nao encontrado em {tokens}"
    print("  ✓ keyword RES")


def teste_identificador_mem():
    tokens = parseExpressao("(3.14 PI)")
    ids = [t for t in tokens if t[0] == "ID"]
    assert ids == [("ID", "PI")], f"esperado ID PI, obteve {ids}"
    print("  ✓ identificador PI")


def teste_identificador_longo():
    tokens = parseExpressao("(10.5 CONTADOR)")
    ids = [t for t in tokens if t[0] == "ID"]
    assert ids == [("ID", "CONTADOR")], f"esperado ID CONTADOR, obteve {ids}"
    print("  ✓ identificador longo (CONTADOR)")


def teste_comando_res_completo():
    tokens = parseExpressao("(5 RES)")
    esperado = [
        ("PAREN", "("),
        ("NUM", "5"),
        ("RES", "RES"),
        ("PAREN", ")"),
    ]
    assert tokens == esperado, f"falhou: {tokens}"
    print("  ✓ comando RES completo")


def teste_comando_mem_completo():
    tokens = parseExpressao("(10.5 CONTADOR)")
    esperado = [
        ("PAREN", "("),
        ("NUM", "10.5"),
        ("ID", "CONTADOR"),
        ("PAREN", ")"),
    ]
    assert tokens == esperado, f"falhou: {tokens}"
    print("  ✓ comando MEM completo")


def teste_leitura_variavel():
    tokens = parseExpressao("(PI)")
    esperado = [
        ("PAREN", "("),
        ("ID", "PI"),
        ("PAREN", ")"),
    ]
    assert tokens == esperado, f"falhou: {tokens}"
    print("  ✓ leitura de variavel")


def teste_espacos_multiplos():
    tokens = parseExpressao("(  3.14   2.0   + )")
    nums = [t for t in tokens if t[0] == "NUM"]
    assert len(nums) == 2, f"esperado 2 numeros, obteve {nums}"
    print("  ✓ espacos multiplos")


# ---- testes de entradas invalidas ----

def teste_numero_malformado():
    tokens = parseExpressao("3.14.5")
    erros = [t for t in tokens if t[0] == "ERRO"]
    assert len(erros) > 0, f"esperado ERRO pra 3.14.5, obteve {tokens}"
    print("  ✓ numero malformado (3.14.5) detectado")


def teste_caractere_invalido():
    tokens = parseExpressao("&")
    erros = [t for t in tokens if t[0] == "ERRO"]
    assert len(erros) > 0, f"esperado ERRO pra &, obteve {tokens}"
    print("  ✓ caractere invalido (&) detectado")


def teste_arroba_invalido():
    tokens = parseExpressao("@")
    erros = [t for t in tokens if t[0] == "ERRO"]
    assert len(erros) > 0, f"esperado ERRO pra @, obteve {tokens}"
    print("  ✓ caractere invalido (@) detectado")


def teste_virgula_invalida():
    tokens = parseExpressao("3,14")
    # virgula nao eh ponto decimal, deve gerar erro ou tokens separados
    tem_erro = any(t[0] == "ERRO" for t in tokens)
    nao_tem_num_correto = not any(t == ("NUM", "3,14") for t in tokens)
    assert tem_erro or nao_tem_num_correto, f"nao detectou problema em 3,14: {tokens}"
    print("  ✓ virgula ao inves de ponto detectada")


# ---- executa todos os testes ----

def rodar_todos_os_testes():
    testes = [
        # validos
        teste_numero_inteiro,
        teste_numero_real,
        teste_numero_comeca_com_zero,
        teste_operador_soma,
        teste_operador_subtracao,
        teste_operador_multiplicacao,
        teste_operador_divisao,
        teste_operador_divisao_inteira,
        teste_operador_resto,
        teste_operador_potencia,
        teste_parenteses,
        teste_expressao_simples,
        teste_expressao_aninhada,
        teste_keyword_res,
        teste_identificador_mem,
        teste_identificador_longo,
        teste_comando_res_completo,
        teste_comando_mem_completo,
        teste_leitura_variavel,
        teste_espacos_multiplos,
        # invalidos
        teste_numero_malformado,
        teste_caractere_invalido,
        teste_arroba_invalido,
        teste_virgula_invalida,
    ]

    print("rodando testes do analisador lexico...\n")
    passou = 0
    falhou = 0

    for teste in testes:
        nome = teste.__name__
        try:
            teste()
            passou += 1
        except Exception as e:
            print(f"  ✗ {nome}: {e}")
            falhou += 1

    print(f"\nresultado: {passou} passaram, {falhou} falharam")


if __name__ == "__main__":
    rodar_todos_os_testes()
