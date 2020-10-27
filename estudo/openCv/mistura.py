import cv2 as cv
import numpy as np
import sys

MAX_VALOR = 20


def on_trackbar(valor):
    alfa = valor/ MAX_VALOR
    beta = 1.0 - alfa
    res = img1 * beta + img2 * alfa #cv.addWeighted 
    res = res * (1/(np.max(res))) #Normaliza para manter o valor de pixels <= 1.0 (branco)
    cv.imshow("resultado", res)


def main():
    global img1, img2
    '''
    '''
    if len(sys.argv) != 3:
        print("Voce deve passar 3 argumentos para o script. python mistura.py <img1> <img2>")
        return
    fname1 = sys.argv[1]
    fname2 = sys.argv[2]
    
    print(f"fname1: {fname1}")
    print(f"fname2: {fname2}")

    img1 = cv.imread(fname1)
    img2 = cv.imread(fname2)
    if img1 is None or img2 is None:
        print("Erro na abertura das imagens")
        return
    else:
        cv.imshow("janela1", img1)

        cv.imshow("janela1", img2)
        cv.imshow("resultado", img1)
        cv.createTrackbar("mistura", "resultado", 0, MAX_VALOR, on_trackbar)

        cv.waitKey(0)

main()
