from sistema.analises import *
from sistema.estrutura import *
from time import sleep

cor = {'negrito': "\033[1m",
            'vermelho': "\033[1;31m",
            'verde': "\033[1;32m",
            'amarelo': "\033[1;33m",
            'azul': "\033[1;34m",
            'roxo': "\033[1;35m",
            'ciano': "\033[1;36m",
            'enc_cor': "\033[m"}
matrix = [[], []] # criando uma matriz 2x2 (onde cada lista tem 2 elementos : valor de um segmento  da linha 1 e um segmento  da linha 2).
print(' '* 12,f'{cor["ciano"]}CALCULADOR AUTOMÁTICO DO TEOREMA DE TALES - SIMPLES{cor["enc_cor"]}\n')
print(f'{cor["negrito"]}IMPORTANTE! Este programa trabalha apenas com números, portanto, não aceita expressões como valores para os segmentos!{cor["enc_cor"]}')
sleep(5)
print(f'{cor["negrito"]}Ao passar os valores: {cor["enc_cor"]}'
      f'Para o valor que você quer descobrir, digite {cor["verde"]}"x"{cor["enc_cor"]}, e para um valor vazio (sem nenhum valor númerico), aperte {cor["verde"]}ENTER.{cor["enc_cor"]}')
segmentos = 'AB'
representarRetas([segmentos] * 2)
validacao = False
while validacao is not True:
    for linha in range(0,2): # insere os valores de forma que se adequem com a matriz
        for segmento in range(0,2):
            while True:
                n = validarOpcoes(f'Qual o valor do segmento {cor["roxo"]}{segmentos[segmento]}{cor["enc_cor"]} da {cor["negrito"]}{linha + 1}º linha? {cor["enc_cor"]}')
                if n in ('x', '', 0): # Regra: Não pode haver 2 valores x ou nulos, e um segmento de reta não pode ser 0
                    if n in matrix[0] or n in matrix[1] or n == 0: # Se n for um dos 3 valores, checa se n está na matriz, se estiver, levanta um erro.
                        print(f'{cor["vermelho"]}ERRO!{cor["enc_cor"]}', end=' ')
                        if n == 'x':
                            print(f'{cor["vermelho"]}Você não pode digitar mais de um [x] !{cor["enc_cor"]}')
                        elif n == '':
                            print(f'{cor["vermelho"]}Você não pode mais de um valor vazio [" "]!{cor["enc_cor"]}')
                        elif n == 0:
                            print(f'{cor["vermelho"]}Você não pode colocar um segmento como tendo comprimento zero [0] !{cor["enc_cor"]}')
                    else:
                        break
                else:
                    break
            matrix[segmento].append(n) # Adiciona n à MATRIZ depois de sair do loop.
    print('Fazendo uma representação simples...')
    sleep(1.5)
    representarRetas(matrix)
    sleep(1.5)
    print(f'{cor["amarelo"]}Analisando{cor["enc_cor"]}',end='')
    for c in range(0,3):
        sleep(0.5)
        print('.',end ='')
    print()
    local_x, local_nulo = acharValores(matrix)  # Retorna 2 valores e por isso precisamos armazena-los em  2 variavéis. OBRIGATÓRIO ser na ordem: local -x ; local - nulo.
    validacao = validarExistencia(matrix,local_x,local_nulo)
    if validacao is True:
        print(f'{cor["verde"]}Tudo certo!{cor["enc_cor"]}')
    else:
        print(f'{validacao}')
        matrix = [[],[]] # limpando a matriz para que o usuário possa colocar os valores de novo

sleep(1)
if local_nulo > -1: # se for maior do que -1, quer dizer que há um valor vazio na matriz.
    representarRetas(matrix, local_nulo)
    while True:
        try:
            comp_reta_nulo = float(input(f'Há um valor vazio na {cor["amarelo"]}linha {local_nulo + 1}{cor["enc_cor"]}. Por favor, digite o comprimento completo dessa reta: '))
            if comp_reta_nulo == 0:
                raise Exception
            break
        except (ValueError, TypeError):
            print(f'{cor["vermelho"]} ERRO! Digite um número válido!{cor["enc_cor"]}')
        except Exception:
            print(f'{cor["vermelho"]} ERRO! O comprimento de uma reta não pode ser 0!{cor["enc_cor"]}')
    print('Agora vamos organizar os valores em 2 frações: A primeira com os valores da reta paralela 1, e a outra com as da paralela 2. Veja como ficaria:')
    sleep(2)
    print('Lembre se! Substituimos o valor vazio pelo comprimento da reta paralela onde o mesmo se encontra. E para igualar os dois lados da fração, substituimos o outro lado pelo comprimento da outra reta!')
    sleep(5)
    organizarVNulo(matrix,local_x, local_nulo,comp_reta_nulo)
    mostrarFracao(matrix)
else:
    print('Agora vamos organizar os valores em 2 frações: A primeira com os valores da reta paralela 1, e a outra com as da paralela 2. Veja como ficaria:')
    sleep(2)
    mostrarFracao(matrix)
    sleep(2)
sleep(1)
print('Agora é so resolvermos a regrinha de 3 para descobrir que... ', end = '')
resposta = resolverTales(matrix, local_x)
if resposta.is_integer():
    resposta = int(resposta)
    print(f'{cor["roxo"]}x = {resposta}!{cor["enc_cor"]}')
else:
    print(f'{cor["roxo"]}x ≅ {resposta:.3f}!{cor["enc_cor"]}')
sleep(1.5)
