# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
    Nome: Caio Túlio de Deus Andrade
    NUSP: 9797232

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

# 
# =================================================================------------------------------------------------------------------
# 
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    ## Coloque aqui os seus testes.

    mat = [ [1] ]
    print( to_string(mat, 'Olá Mundo!!') )


#------------------------------------------------------------------
#
def crie (nlins, ncols, vini = 0):
    ''' (int, int, int) -> list

    RECEBE três inteiros, `nlins`, `ncols` e `vini`. 
    RETORNA uma matriz de dimensão `nlins` x `ncols` em que o valor 
    do elemento em cada posição é `vini`.
    '''
    # Substitua o código abaixo com a sua solução
    resultado = []
    for _ in range(nlins):
        nova_linha = [vini] * ncols
        resultado.append(nova_linha)

    return resultado

#------------------------------------------------------------------
#
def clone ( matriz ):
    ''' (list) -> matriz

    RECEBE uma matriz `matriz`.
    RETORNA um clone da matriz.
    '''
    resultado = []
    for lin in range(len(matriz)):
        nova_linha = []
        for col in range(len(matriz[0])):
            nova_linha.append(matriz[lin][col])
        resultado.append(nova_linha)

    return resultado
#------------------------------------------------------------------
#
def subtraia ( matriz1, matriz2 ):
    ''' (matriz, matriz) -> matriz

    RECEBE matrizes `matriz1` e `matriz2`, de dimensões iguais, 
    de números inteiros.  
    RETORNA a matriz resultante da subtração de `matriz1` por `matriz2`.
    '''
    resultado = []
    for lin in range(len(matriz1)):
        nova_linha = []
        for col in range(len(matriz1[0])):
            nova_linha.append(matriz1[lin][col] - matriz2[lin][col])
        resultado.append(nova_linha)
    return resultado

#------------------------------------------------------------------
#
def to_string ( matriz , nome = 'matriz'):
    ''' (matriz, str) -> str

    RECEBE uma matriz `matriz` de números inteiros e uma string `nome`.  
    RETORNA uma string utilizada por print() para exibir a `matriz`.

    No que segue, por linha da string retornada entenda uma substring 
    seguida pelo caractere "\n" de mudança de linha.

    A string retornada deve ter o seguinte formato:

      - a primeira linha da string contém a string `nome`;
      - as demais linhas da string contém uma a uma as linhas de `matriz`.

    Os valores da matriz devem ser representados na string retornada por substrings 
    de comprimento 4 com um espaço entre elas. O efeito será que ao exibirmos 
    uma matriz `bla` através de print(to_string(bla)) os valores de cada 
    coluna estarão alinhados.
    '''
    # Substitua o código abaixo com a sua solução
    print("Vixe! Ainda não fiz a função to_string :-(")
    return ''

#------------------------------------------------------------------
#
def limiarize ( matriz, limite, alto=255, baixo=0 ):
    ''' (matriz, int, int, int) -> None

    RECEBE uma matriz `matriz` de números inteiros e três inteiros 
    `limite`, `alto` e baixo.

    A função deve MODIFICAR `matriz` da seguinte forma. 
    Portanto, está função é mutadora.
 
    Cada posição da `matriz` em com valor maior que `limite` 
    deve receber o valor `alto`. 
    As demais posições devem receber o valor `baixo`.
    '''
    # Substitua o código abaixo com a sua solução
    print("Vixe! Ainda não fiz a função limiarize :-(")

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
