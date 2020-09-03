#-----------------------------------------------------
def main():
    '''
    Programa que lê n e uma matriz de inteiros n x n
    e verifica se a matriz é simétrica.
    '''
    # 1. leia a matriz
    a_mat = leia_matriz_arq()

    # 2. imprima a matriz
    mostre_matriz(a_mat) 

    # 3. verifique se a matriz é simétrica
    if simetrica(a_mat):
        print("Matriz é simétrica.")
    else:
        print("Matriz não é simétrica.")

    # 4. mostre imagem da matriz
    mostre_imagem(a_mat)

#------------------------------------------------------
def crie_matriz(n_lin, n_col, valor):
    ''' (int, int, valor) -> matriz (lista de listas)

    Cria e retorna uma matriz com n_lin linhas e n_col
    colunas em que cada elemento é igual ao valor dado.
    '''

#-------------------------------------------------------
def leia_matriz_arq():
    '''(None) -> matriz (list de list)

    RETORNA uma matriz lida de um arquivo.

    A função supõe que os dois primeiros valores do arquivo 
    são número inteiros representando a dimensão da matriz:

        número de linha n_lin e número de coluna n_col.

    Em seguida devem estar dispostos o n_lin por n_col 
    elementos da matriz, linha a linha.

    Todos os valores devem estar separados por pelo menos
    um branco.
    '''

#----------------------------------------------------------
def simetrica(matriz):
    '''(matriz) -> bool

    Recebe uma matriz e returna True se a matriz for simétrica,
    em caso contrário retorna False.

    Pré-condição: a função supões que a matriz e quadrada

    >>> a = [[1,2,3],[2,1,4],[3,4,1]]
    >>> a
    [[1, 2, 3], [2, 1, 4], [3, 4, 1]]
    >>> imprima_matriz(a)
    Matriz: 3 x 3
         1     2     3
         2     1     4
         3     4     1
    >>> simetrica(a)
    True
    '''
#-------------------------------------------------------
def crie(nlin, ncols, valor = 0):
    m = []
    for _ in range(nlin):
        linha = [valor] * ncols
        for _ in range(ncols):
            m.append(linha)

#-------------------------------------------------------
def mostre_matriz(matriz):
    '''(matriz) -> None

    Recebe e imprime uma matriz de inteiros.
    '''
    for i in lista:
        print(i)


    
#------------------------------------------------------
# início da execução do programa
if __name__ == "__main__":
    main()
