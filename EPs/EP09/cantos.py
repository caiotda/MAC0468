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


#-------------------------------------------------------------------------- 
# programa principal

import cv2 as cv
import numpy as np
import sys

def captura_imagem():
    """
    (None) -> img/None

    DEVOLVE uma imagem openCv, ou None se não conseguir carregar a imagem. 
    Dependendo dos parametros especificados pela linha de comando, devolve uma 
    captura de uma câmera ou de uma imagem especificada na linha de comando.
    """
    if len(sys.argv) < 2:
        device = input('Digite o número dequal câmera você quer usar: ')
        try:
            num = int(device)
            print(f'Voce escolheu a camera {num}')
            camera = cv.VideoCapture(num)
            _, img = camera.read()
            cv.waitKey(0)
        except:
            print('Erro na escolha do device... digite um numero')
            return None
    else:
        path = sys.argv[1]
        img = cv.imread(path)
    return img

def main():

    img = captura_imagem()
    if img is None:
        print("Erro na abertura da imagem.")
    cv.imshow("Entrada", img)
    cv.waitKey(0)
    
if __name__== '__main__':
    main()


