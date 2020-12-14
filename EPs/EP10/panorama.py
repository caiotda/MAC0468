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
    n = len(files)
    if METODO == 'SIFT':
        forcabruta = cv.BFMatcher( normType=cv.NORM_L2, crossCheck=True)
        metodo = cv.SIFT_create()
    else:
        forcabruta = cv.BFMatcher( normType=cv.NORM_HAMMING, crossCheck=True)
        metodo = cv.ORB_create()

    if n == 0:
        print(f"Não achei nenhuma imagem usando {files}")
        return
    else:
        print(f"Achei as seguintes {n} imagens para processar:\n")
        img_prev = cv.imread(files[0])

        IMG0_GRAY = cv.cvtColor(img_prev, cv.COLOR_BGR2GRAY)
        kp_prev, des_prev = metodo.detectAndCompute(IMG0_GRAY, None )

        w, h, _ = img_prev.shape
        w = w * ESCALA_W
        h = h * ESCALA_H

        if DELTA_W:
            offset_horizontal = DELTA_W
        else:
            offset_horizontal = 3*w//8

        if DELTA_H:
            offset_vertical = DELTA_H
        else:
            offset_vertical = 3*h//8

        H0 = np.eye(3)
        H0[0,2] =  offset_horizontal
        H0[1,2] = offset_vertical

        BASE = cv.warpPerspective(img_prev, H0, (w, h))
        files = files[1:]
        H_acc = H0
        # Itero pelas imagens restantes e anexando a base
        for i, f in enumerate( files ):
            print(f"{i} : {f}")
            img = cv.imread(f)
            img_g = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            kp, des = metodo.detectAndCompute(img_g, None )
            matches = forcabruta.match(des_prev, des)

            pts0 = np.zeros( (len(matches), 2), dtype=np.float32)
            pts1 = np.zeros( (len(matches), 2), dtype=np.float32)


            for j, match in enumerate(matches):
                pts0[j,:] = kp_prev[match.queryIdx].pt
                pts1[j,:] = kp[match.trainIdx].pt

            # Mapeia pontos da imagem 2 para o sistema de coordenadas da imagem 1

            height, width = img_prev.shape[:2]
            H_curr, _ = cv.findHomography(pts1, pts0, method=cv.RANSAC)
            img2prev = cv.warpPerspective( img, H_curr, (width, height) )

            H_acc = H_acc @ H_curr
            w,h,_ = BASE.shape
            aux = cv.warpPerspective(img, H_acc, (h, w))
            BASE = np.logical_and(BASE==0, aux)*aux + BASE
            img_prev = img
            kp_prev = kp
            des_prev = des
            while DEBUG and True:
                cv.imshow(f"Resultado intermediario na iteracao {i}", BASE)
                k = cv.waitKey(0)
                if k == 13:
                    break
        # Mapeia a imagem 2 para o sistema de coordenadas da imagem 1, então
        # mapeia para a imagem base




        cv.imshow("Resultado final", BASE)
        cv.waitKey(0)


if __name__== '__main__':
    main()


