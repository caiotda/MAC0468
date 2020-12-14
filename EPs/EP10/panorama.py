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
import argparse

# glob pega os nomes dos arquivos em uma pasta
from glob import glob

#--------------------------------------------------------------------------
# programa principal

def main():

    # PARSING
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--imagens', required=True, help = "imagens de entrada como '../figs/*.png'")
    ap.add_argument('-d', '--debug', required=False, action='store_true', help = 'liga o modo debug')
    ap.add_argument('-s', '--sift', required=False,  action='store_true', help = 'usa SIFT, default é ORB')
    ap.add_argument('-sw', '--escalaW', required=False, help = 'muda a escalaW')
    ap.add_argument('-sh', '--escalaH', required=False, help = 'muda a escalaH')
    ap.add_argument('-dw', '--deltaW', required=False, help = 'posição horizontal da 1a imagem')
    ap.add_argument('-dh', '--deltaH', required=False, help = 'posição vertical da 1a imagem')
    ap.add_argument('-c', '--crosscheck', required=False, action='store_false', help = 'desliga crosscheck no cálculo de matches')

    args = ap.parse_args()
    print(args)

    ## SET DEFAULTS
    METODO = 'ORB'
    ESCALA_W = 3
    ESCALA_H = 3
    CROSSCHECK = True
    DELTA_W = args.deltaW   ### CUIDADO, DELTA_W é um str ou None
    DELTA_H = args.deltaH   ### CUIDADO, DELTA_H é um str ou None

    ## ATUALIZA O QUE PRECISAR
    DEBUG = args.debug
    CROSSCHECK = args.crosscheck

    if args.sift: METODO = 'SIFT'
    if args.escalaW is not None: ESCALA_W = int(args.escalaW)
    if args.escalaH is not None: ESCALA_H = int(args.escalaH)

    # AGORA VAMOS COMEÇAR

    files = glob(args.imagens)
    files = sorted(files)
    imgs = []
    n = len(files)
    if n == 0:
        print(f"Não achei nenhuma imagem usando {files}")
        return
    else:
        print(f"Achei as seguintes {n} imagens para processar:\n")
        for i, f in enumerate( files ):
            print(f"{i} : {f}")
            img = cv.imread(f)
            imgs.append(img)
        if DEBUG:
            for i, img in enumerate(imgs):
                cv.imshow(f"Imagem {i}", img)
                cv.waitKey(0)
        IMG_0 = imgs[0]
        w, h, _ = IMG_0.shape
        w = w * ESCALA_W
        h = h * ESCALA_H
        print(f"Width: {w}; Height: {h}")
        BASE = np.zeros((h, w), dtype='uint8')
        print(BASE.shape)

        H0 = np.eye(3)
        if DELTA_W:
            offset_horizontal = DELTA_W
        else:
            offset_horizontal = 3*w//8

        if DELTA_H:
            offset_vertical = DELTA_H
        else:
            offset_vertical = 3*h//8
        H0[0,2] =  offset_horizontal
        H0[1,2] = offset_vertical

        res1 = cv.warpPerspective(IMG_0, H0, (w, h))
        cv.imshow("Teste", res1)
        cv.imshow("Teste imagem 1", IMG_0)
        cv.waitKey(0)
    print("Vixe! ainda não fiz o EP10 ;-(")


if __name__== '__main__':
    main()


