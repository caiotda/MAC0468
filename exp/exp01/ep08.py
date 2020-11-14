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
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

import exp01_utils as ut

## Edite essas constantes para o seu ambiente
CJTO_TREINO = 'treinamento.txt'
CJTO_TESTE  = 'teste.txt'
DATA_PATH   = './dataset/'

## Outras constantes
FUNDO = 0
DEBUG = False
TREINO = True
USE_BORDAS_BASELINE = True

BOTTOM_THRESHOLD = 0
DELTA = 60

def bordas2( img ):
    ''' ( BGR ) -> binária
    Implemente aqui o seu método para calcular valores para os limiares
    de Canny. A função deve aplicar esses valores e retornar uma imagem
    binária com fundo FUNDO.    
    '''
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur  = cv.GaussianBlur(gray, (5, 5), 0)
    img = cv.Canny(blur, 60, 120)

    return img

def main():
    ''' 
    Programa para ajudar no treinamento e teste da sua função bordas
    '''

    # modifique a constante para False para usar a sua função bordas
    if USE_BORDAS_BASELINE:
        bordas = ut.bordas_baseline
    else:
        bordas = bordas2

    # ao terminar o seu treino com a sua função bordas, 
    # altera a constante TREINO para False
    if TREINO:
        f, s = ut.avaliacao( CJTO_TREINO, DATA_PATH, bordas)
    else:
        f, s = ut.avaliacao( CJTO_TESTE, DATA_PATH, bordas)

    for i in sorted(s.keys()):
        print(f"{s[i]:.3} \t: {i}")
    print(f"{f:.3} \t: F-score médio")
    ut.mostre_resultado( s )

##  -----------------------------------------------------------------
##
##  Escreva as suas funções a seguir. 
##  Copie ou adapte algumas delas do EP07.
##
##  -----------------------------------------------------------------
def processa_gab(gab):
    """ (imagem) -> imagem
    RECEBE uma imagem de gabarito e 
    DEVOLVE a imagem de gabarito limiarizada e com fundo preto. Fazemos isso
    para evitar eventuais ruidos na imagem de gabarito.
    """
    _, res = cv.threshold(gab, 125, 255, cv.THRESH_BINARY_INV)

    return res
##  -----------------------------------------------------------------

def crie_gabarito( imgs ):
    ''' (lista de imagens) -> imagem
    Constrói a imagem gabarito a partir de uma lista de imagens com
    anotações de bordas.
    '''
    gab1, gab2, gab3 = imgs

    gab1 = processa_gab(gab1)
    gab2 = processa_gab(gab2)
    gab3 = processa_gab(gab3)
    res = cv.bitwise_or(gab1, gab2)
    res =  cv.bitwise_or(res, gab3)
    return res
##  -----------------------------------------------------------------

def prec_rec(teste, gabarito):
    ''' (img, img) -> float, float
    Recebe duas imagens com fundo escuro (pixels com valor 0) 
    e bordas diferente de 0. Calcula e retorna o par (Precision, Recall)
    '''

    comparacao = np.subtract(teste.astype(np.int16), gabarito.astype(np.int16))

    # Verifica regiões que são borda tanto na imagem de entrada quanto no 
    # gabarito
    intersecta = cv.bitwise_and(teste, gabarito)

    # Seleciona todo pixel (i,j) que é 255 em teste e 0 no gabarito
    # (falso positivo)
    FP = np.sum(comparacao == 255)

    # Aqui, pegamos pixels que são 0 na teste e 255 no gabarito
    # (falso negativo)
    FN = np.sum(comparacao == -255)

    # Finalmente, pixels que são 255 tanto na imagem quando no gabarito
    # (positivos verdadeiros)
    TP = np.sum(intersecta == 255)

    recall = TP / (TP + FN)
    precision = TP / (TP + FP)

    return (precision, recall)

if __name__ == '__main__':
    main()
