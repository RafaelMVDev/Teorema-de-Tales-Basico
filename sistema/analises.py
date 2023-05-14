def validarOpcoes(mensagem):
    """Função responsavél por validar o valor passado pelo usuário, que poderá ser apenas x ou um número inteiro/decimal.
    Mensagem[str]: Qual mensagem será passada ao usuário para que ele digite os valores."""
    while True:
        valor = input(mensagem).lower().strip()  # Usei as funções strip e lower para padronizar as entradas de valores.
        if valor == 'x' or valor == '':
            return valor
        else:
            try:
                valor = float(valor)
                return valor
            except:
                print('\033[1;31mVALOR INVÁLIDO, digite um número válido ou x!\033[m')  # Se nenhuma das condições acima forem executadas, retorna uma mensagem de erro.


def acharValores(matriz):
    """
    função que faz uma análise dos valores passados. Onde checa se há um valor nulo ('') e 'x'.
    :param matriz: [list] valores que irão passar pela análise
    :return: retorna a posição do valor se uma das condições forem atendidas. 0 para a linha 1, e 1 para a linha 2
    """
    local_x = [-1,-1]
    local_nulo = -1
    for index,lista in enumerate(matriz):
        for segmento in lista:
            if segmento == '':
                local_nulo = lista.index(segmento)
            elif segmento == 'x':
                local_x = [index,lista.index(segmento)] # [IMPORTANTE] Valor 1 da lista: Em qual lista da matriz está x [0 ou 1]; 2: Posição de x dentro dessa lista [0 ou 1].
    return local_x, local_nulo

def validarExistencia(matriz, posicao_x, posicao_nulo = -1):
    """
    Aplica algumas condições de existência para checar se é possivél realizar o Teorema com os valores dados pelo usuário [última análise].
    :param matriz: base de dados a serem validados
    :param posicao_x: localização exata de x dentro da matriz [-1 -> não há].
    :param posicao_nulo: localização de valor nulo dentro da matriz [-1 -> não há]
    :return: False se não for possível, e True caso seja.
    """
    if posicao_nulo > -1 and posicao_x[0] > -1:
        if posicao_x[1] == posicao_nulo:
            return True
        else:
            return "\033[1;31mINVÁLIDO! Um valor nulo e x sempre devem estar na mesma reta paralela. Digite os valores novamente!\033[m"
    else:
        if posicao_x[1] == -1:
            return "\033[1;31mINVÁLIDO! [x] não foi passado. Digite os valores novamente!\033[m"
        else:
            return True

