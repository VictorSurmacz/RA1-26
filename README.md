# Fase 1 — Analisador Léxico e Gerador de Assembly para ARMv7

## Instituição

PUCPR

## Disciplina

Construção de Interpretadores

## Professor

Frank Alcantara

## Grupo

RA1 - 26

## Integrantes

| Nome                           | GitHub         |
| ------------------------------ | -------------- |
| Renan Felipe Straub Czervinski | @rczervinski   |
| Renan de Rocco Pamplona        | @RenanPamplona |
| Victor Eduardo Surmacz         | @VictorSurmacz |

## Descrição

Compilador (Fase 1) que lê expressões aritméticas em notação polonesa reversa (RPN) a partir de um arquivo de texto, realiza análise léxica usando Autômatos Finitos Determinísticos e gera código Assembly ARMv7 compatível com o CPUlator DE1-SoC.

## Como executar

```bash
python main.py testes/teste1.txt
```

O programa gera:

- Resultados das expressões no terminal
- Arquivo `.s` com o Assembly ARMv7 (mesmo nome do teste)
- Arquivo `tokens.txt` com os tokens da última execução

## Como testar o analisador léxico

```bash
python testes_lexico.py
```

## Como rodar o Assembly no CPUlator

1. Acesse https://cpulator.01xz.net/?sys=arm-de1soc
2. Copie o conteúdo do arquivo `.s` gerado
3. Cole no editor do CPUlator
4. Clique em "Compile and Load"
5. Clique em "Continue" para executar
6. O resultado aparece nos displays de 7 segmentos

## Estrutura do projeto

```
├── main.py              # ponto de entrada
├── lexico.py            # analisador léxico (AFD)
├── executor.py          # validação das expressões em Python
├── gerador.py           # geração de Assembly ARMv7
├── interface.py         # leitura de arquivo e exibição
├── testes_lexico.py     # testes do analisador léxico
├── tokens.txt           # tokens da última execução
├── testes/
│   ├── teste1.txt       # operações básicas
│   ├── teste2.txt       # aninhamento
│   └── teste3.txt       # MEM, RES e misto
└── README.md
```

## Operações suportadas

- Adição: `(A B +)`
- Subtração: `(A B -)`
- Multiplicação: `(A B *)`
- Divisão real: `(A B /)`
- Divisão inteira: `(A B //)`
- Resto: `(A B %)`
- Potenciação: `(A B ^)`
- Armazenamento em memória: `(V NOME)`
- Leitura de memória: `(NOME)`
- Resultado anterior: `(N RES)`
- Expressões aninhadas: `((A B +) (C D *) /)`
