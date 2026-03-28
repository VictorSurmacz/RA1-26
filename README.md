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
6. O resultado da primeira linha aparece nos displays de 7 segmentos
7. Aperte o botão **KEY0** (Push Button 0) para avançar para o próximo resultado
8. Repita o passo 7 para cada linha do arquivo de teste
9. Após a última linha, os displays e LEDs são apagados e o programa para

### Exibição no display de 7 segmentos

O display mostra o resultado de cada linha com 2 casas decimais. O valor é multiplicado por 100 e os dois dígitos da direita representam a parte decimal. O HEX2 exibe um traço simulando o ponto decimal.

Exemplo: o resultado `5.14` aparece no display como:
```
HEX5  HEX4  HEX3  HEX2  HEX1  HEX0
  0     0     5     _     1     4
                    ↑
                  ponto
```

<img width="314" height="181" alt="image" src="https://github.com/user-attachments/assets/00c2e852-051b-44c7-b947-e272d3e193e1" />


### Navegação com Push Buttons

O programa exibe um resultado por vez no display. Para avançar para o próximo resultado, o usuário deve pressionar o botão **KEY0** no painel de Push Buttons do CPUlator DE1-SoC.

Os LEDs indicam qual linha está sendo exibida: linha 1 acende 1 LED, linha 2 acende 3 LEDs, linha 3 acende 7 LEDs, e assim por diante.

<img width="162" height="48" alt="image" src="https://github.com/user-attachments/assets/9f05b77c-f66c-482f-93e9-a03325809f51" />
*Indica que estamos na linha 4

#### Funcionamento do botão:

https://github.com/user-attachments/assets/58de7528-53f7-49d9-a19f-d15bdc9ee8fa



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
