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


    ## Testes da função subtraia:
    matriz1 = [[1,2,3], [4,5,6], [7,8,9]]
    matriz2 = [[1,2,3], [4,5,6], [7,8,9]]
    resultado_esperado = [[0,0,0], [0,0,0], [0,0,0]]
    resultado = subtraia(matriz1, matriz2)
    veredito = igualdade(resultado, resultado_esperado)
    if(veredito == False):
        print("Teste falhou!")
    else:
        print("Passou!")
    matriz2 = [[3,2,1], [6,5,4], [9,8,7]]
    resultado = subtraia(matriz1, matriz2)
    resultado_esperado = [[-2,0,2], [-2,0,2], [-2,0,2]]
    veredito = igualdade(resultado, resultado_esperado)
    if(veredito == False):
        print("Teste falhou!")
    else:
        print("Passou!")
    mat = [ [1] ]
    print( to_string(mat, 'Olá Mundo!!') )


#------------------------------------------------------------------
#

def igualdade( matriz1, matriz2 ):
    ''' (list, list) -> bool
    
    RECEBE duas matrizes `matriz1` e `matriz2`
    RETORNA True se todos matriz1[i][j] = matriz2[i][j], para todo i
    e j validos.
    '''

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if(matriz1[i][j] != matriz2[i][j]):
                return False
    return True

#------------------------------------------------------------------
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
def prepara (item):
    ''' (numero) -> str 
    
    RECEBE um numero
    RETORNA uma string com 4 caracteres.


    - O número recebido deve ter no máximo 4 caracteres.

    - Se o número possuir menos do que 4 caracteres, a diferença 
    em caracteres é preenchida com espaços em branco. 
    - Do contrário, retorna uma string com 4 espaços
    '''
    resultado = str(item)
    diferença = 4 - len(resultado)
    if(diferença >= 0):
        return resultado + diferença*' '
    return '    '

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
    resultado = nome + '\n'
    for linha in matriz:
        nova_linha = ''
        for item in linha:
            substring = prepara(item)
            nova_linha += substring + ' '
        nova_linha = nova_linha + '\n'
        resultado += nova_linha
    resultado = resultado.rstrip('\n')
    return resultado

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
    for lin in range(len(matriz)):
        for col in range(len(matriz[0])):
            item = matriz[lin][col]
            if(item > limite):
                matriz[lin][col] = alto
            else:
                matriz[lin][col] = baixo

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
