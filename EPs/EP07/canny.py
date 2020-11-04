# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
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

##
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

## Constantes
FUNDO = 0
DEBUG = False

def main():
    ''' 
    Carregue as imagens gere o gráfico Recall x Precision
    '''
## 

def mostre_resultado( array ):
    ''' (array) -> None
    Recebe um array com pares 
    '''
    rc = array.T
    plt.plot( rc[0], rc[1] )
    plt.ylabel('Precision')
    plt.xlabel('Recall')
    plt.show()

## 

def crie_gabarito( imgs ):
    ''' (lista de imagens) -> imagem
    Constrói a imagem gabarito a partir de uma lista de imagens com
    anotações de bordas.
    ''' 

def avalie_canny(blur, gab, ini=0, fim=256, passo=5, delta=60):
    ''' (imagem, imagem, int, int, int, int) -> array
    Recebe a imagem blur e um gabarito de bordas gab. 
    Deve gerar imagens de  borda usando o método de Canny para o intervalo
    de limiar inferior [ini: fim: passo]. O limiar superior do método de 
    Canny deve ser o inferior + delta. Observe que o limiar superior não deve
    ser maior que o valor de fim.
    A função retorna um numpy.ndarray com os pares (recall, precision)
    para cada par de limiares calculados.
    '''

if __name__ == '__main__':
    main()
