def representarRetas(matriz, linha_nulo = -1):
    """
    Função que formata os valores passados pelo usuário em uma visualização simples dos mesmos no estilo de retas e paralelas, como no Teorema de Tales.
    :param listas: conjunto de valores passados pelo usuário (armazenados em uma matriz).
    :param nulo: se há um valor vazio(nulo) no conjunto de valores (-1 = não há).
    """

    encontro_retas = '\t      __|____|__'
    n1_estilo = "\033[1m"
    n2_estilo = "\033[1m"

    if linha_nulo == 0:
        n1_estilo = '\033[1;33m' # se a condição for atendida, muda a variavél para um novo código de formatação. Usado para apontar em qual linha o valor nulo está presente.
    elif linha_nulo == 1:
        n2_estilo = '\033[1;33m'

    print(f'\t{n1_estilo}        1\033[m    {n2_estilo}2\033[m  ') # n1 e n2 mudam o estilo caso haja um valor vazio em uma das duas linhas
    cont_itens = 0
    for linha in matriz:
        item_index = 0 # a var linha representa cada item da matriz, que no caso são 2 listas (ou seja, 2 linhas) com 2 valores em cada lista.
        for valor in linha:
            item_index += 1
            cont_itens += 1
            quant_espacos = 12 - len(str(valor))
            if item_index == 1:
                print(f'{encontro_retas}')
                print(f'{" "*quant_espacos}{valor}{"|    |"}',end='')
            else:
                print(f' {valor}')
            if cont_itens == 4:
                print('            |    |') # coloquei esse if para printar essa string para manter o padrão, onde cada segmento da linha é representado por 2 caracteres "|", uma embaixo da outra.


def organizarVNulo(matriz, x_local, local_nulo = -1, comp_reta = 0):
    """
    Chamada caso haja um valor nulo na matriz. Reorganiza os valores para que se adequem a regra de 3,
    mudando o valor nulo para o comprimento da reta e o igualando com a fração ao lado.
    :param matriz: matriz que será usada como base da organização
    :param x_local: obrigatório para que ocorra a troca de 'x' por 1.
    :param local_nulo: usado para trocar o valor nulo por 'comp_reta', caso exista um valor nulo. [-1 = não há]
    :param comp_reta: comprimento da reta em que se encontra o valor nulo, caso haja um.
    :return: A matriz organizada de forma a se adequar às operações do Teorema.
    """
    # trocando o valor de x para 1 para que possamos realizar futuras operações.
    for index,linha in enumerate(matriz): # leve em consideração que linha é o mesmo que cada lista dentro da matriz, e não referente a linha dada na representação
        if '' in linha:
            matriz[index][local_nulo] = comp_reta
            if local_nulo == 0:
                matriz[index][local_nulo + 1] = matriz[0][1] + matriz[1][1]
            elif local_nulo == 1:
                matriz[index][local_nulo -1] = matriz[0][0] + matriz [1][0]


def mostrarFracao(matriz):
    """
    Organiza a matriz em fração, através da variavél "espacos", padronizando os espaços dos segmentos, evitando mudanças de espaçamento entre as duas frações.
    :param matriz: conjunto de valores a serem mostrados
    :return: valores passados em uma representação de fração
    """
    for index, item in enumerate(matriz):
        espacos = 14 - len(str(item[0]))
        print(f'{item[0]}{" "*espacos}{item[1]}')
        if index == 0:
            print('-'* 6,"x".center(5),'-' * 6)


def resolverTales(matriz,local_x):
    matriz[local_x[0]][local_x[1]] = 1
    resposta = 0
    if local_x[0] == local_x[1]: # se forem iguais, quer dizer que x está no primeiro segmento da 1 linha paralela, ou no ultimo segmento da 2 linha paralela
        resposta = (matriz[0][1] * matriz [1][0])/(matriz[0][0] * matriz[1][1])  # dessa forma, sabemos se x irá estar no primeiro ou segundo lado da equação
        return resposta
    else:
        resposta = (matriz[0][0] * matriz[1][1]) / (matriz[0][1] * matriz [1][0])
        return resposta
