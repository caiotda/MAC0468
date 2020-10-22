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

import cv2 as cv
import numpy as np
import sys

#-------------------------------------------------------------------------- 
# global vars
global gaussian_kernel_size
gaussian_kernel_size = 3
#-------------------------------------------------------------------------- 

def on_trackbar(valor):
    gaussian_kernel_size = 2*valor + 1 # O tamanho do kernel não pode ser multiplo de dois
    blurred = \
    cv.GaussianBlur(img_cinza, (gaussian_kernel_size, gaussian_kernel_size), 0)
    cv.imshow("blur", blurred)

# programa principal

def main():

    global img_cinza

    if len(sys.argv) != 2:
        print("Digite: python bordas.py arquivo_imagem")
        return

    fname = sys.argv[1]
    img1 = cv.imread(fname)
    if img1 is None:
        print("Não consegui abrir o arquivo: ", fname )
        return

    # resto do seu programa
    cv.imshow("Entrada", img1)
    cv.waitKey(0)

    # Imagem em tons de cinza

    img_cinza = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    cv.imshow("Cinza", img_cinza)
    cv.waitKey(0)

    # Imagem borrada. Adicionamos um trackbar e sempre que há um evento de 
    # mudança no valor da trackbar, alteramos a imagem.
    blurred = \
        cv.GaussianBlur\
            (img_cinza, (gaussian_kernel_size, gaussian_kernel_size), 0)
    cv.imshow("blur", blurred)
    cv.createTrackbar("blurTrackbar", "blur", 3, 15, on_trackbar)
    cv.waitKey(0)
if __name__== '__main__':
    main()

