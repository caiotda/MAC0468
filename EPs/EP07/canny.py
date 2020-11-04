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
import sys
import numpy as np
import matplotlib.pyplot as plt

## Constantes
FUNDO = 0
DEBUG = True


def tenta_abrir(caminho):
    try:
        img = cv.imread(caminho)
        return img
    except:
        print(f"Erro ao abrir a imagem de caminho {caminho}")
        return


def processa_gab(gab):
    gray = cv.cvtColor(gab, cv.COLOR_BGR2GRAY)
    _, res = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)

    return res
def main():
    ''' 
    Carregue as imagens gere o gráfico Recall x Precision
    '''

    if len(sys.argv) < 5:
        print('Quantidade de argumentos passada incorreta. Para executar o programa corretamente, digite:\
                \
                python imagem gabarito1 gabarito2 gabarito3')
        return
    else:
        img = tenta_abrir(sys.argv[1])
        gab1 = tenta_abrir(sys.argv[2])
        gab2 = tenta_abrir(sys.argv[3])
        gab3 = tenta_abrir(sys.argv[4])

        gab1 = processa_gab(gab1)
        gab2 = processa_gab(gab2)
        gab3 = processa_gab(gab3)

        gab = crie_gabarito([gab1, gab2, gab3])
        blur = cv.GaussianBlur(img, (5, 5), 0)

        borda = cv.Canny(blur, 60, 120)

        if DEBUG:
            cv.imshow("imagem principal", img)
            cv.imshow("imagem gabarito 1", gab1)
            cv.imshow("imagem gabarito 2", gab2)
            cv.imshow("imagem gabarito 3", gab3)

            cv.imshow("Combinacao dos gabaritos", gab)
            cv.imshow("Imagem borrada", blur)
            cv.imshow("Imagem segmentada por canny", borda)
            cv.waitKey(0)


        arr = avalie_canny(blur, gab)

    
        


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


    gab1, gab2, gab3 = imgs
    res = cv.bitwise_or(gab1, gab2)
    return cv.bitwise_or(res, gab3)
    

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
