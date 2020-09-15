# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
    Nome:
    NUSP:

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

import ep01 

#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    # coloque aqui os seus testes

    mat = [ [1] ]
    print( ep01.to_string(mat, 'Olá Mundo!!') )

    # Testes do EP01
    maux = [ [1,2,3,4,5],[3,4,5,6,7],[2,4,6,8,1],[5,3,1,7,9],[9,6,3,1,7] ]
    print( 'Matriz maux:')
    print( maux )
    print()
    print( ep01.to_string(maux, '> maux' ) )

    nova = ep01.crie (5, 5, 10)
    print( ep01.to_string( nova, '> nova') )

    dif = ep01.subtraia( nova, maux)
    print( ep01.to_string( dif , '> dif = nova - maux') )

    clo = ep01.clone(dif)
    print( ep01.to_string( clo , '> clo') )

    ep01.limiarize(clo, 5)
    print( ep01.to_string( clo , '> clo apos limiarize') )

    print( ep01.to_string( dif , '> dif apos limiarize') )

    ##
    ## coloque aqui os seus outros testes
    ## 

#------------------------------------------------------------------
#
def erosao ( img, viz = 3 ):
    ''' (matriz, int) -> None

    RECEBE uma matriz `img` representando uma imagem em níveis de cinza e
    um inteiro `viz`.

    MODIFICA `img` de tal forma que, ao final, cada pixel 
    [lin][col] seja o valor mínimo da vizinhança de tamanho `viz`
    centrada no pixel [lin][col] da imagem original.

    Pré-condição: a função supõe que `viz` é um número ímpar 
    positivo.
    '''
    print("Vixe! Ainda não fiz a função erosao()...")

#------------------------------------------------------------------
#
def segmentacao_SME( img, viz = 3 ):
    ''' (matriz, int) -> matriz

    RECEBE uma matriz `img`. 
    APLICA o filtro de erosão com vizinhança viz.
    RETORNA a imagem resultado da subtração entre `img` e sua erosão. 
    Veja exemplos no enunciado.
    '''
    print("Vixe! Ainda não fiz a função segmentacao_SME()...")
    return ep01.crie(1,1)

#------------------------------------------------------------------
#
def dilatacao ( img, viz = 3 ):
    ''' (list, int) -> None
    recebe uma imagem img (lista de listas) em níveis de cinza e
    um inteiro viz.

    A função modifica img tal que, ao final, cada pixel 
    img[lin][col] deve ser substituido pelo valor máximo da vizinhança de
    tamanho viz x viz centrado no pixel (lin,col) da imagem original. 
    Observe que essa região é menor quando o pixel (lin,col) 
    está em um canto ou perto de uma borda.

    Você pode assumir que viz será sempre um número ímpar, que define
    um quadrado centrado em um ponto (lin,col) de lado tam.
    '''
    print("Essa função é opcional.")


#------------------------------------------------------------------
#
def segmentacao_SDM( img, viz = 3 ):
    ''' (list, int) -> list
    RECEBE uma imagem img. 
    APLICA o filtro de dilatação com vizinhança viz.
    RETORNA a imagem resultado da subtração entre a dilatação e img. 
    Veja exemplos no enunciado.
    '''
    print("Essa função é opcional.")
    return ep01.crie(1,1)

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
