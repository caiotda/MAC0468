'''
### Comandos de entrada

* imread(file_name): recebe o nome de um arquivo (file_name)
* imgwrite(file_name, cvimg): salva uma imagem do open cv no arquivo especificado
    * vamos adotar imagens .png como formato de imagens sendo salvas. Adotamos o png porque esse arquivo é lossless. Isto é, o esquema de compressão não tem perda
* imshow(window_name, cvimg): mostra a imagem cvimg na janela window_name


* waitKey( t_ms): comando usado para exibir uma imagem por um tempo t_ms.
Interrompe o programa por t_ms milisegundos. se t_ms = 0, espera tempo infinito.
Quando eu apertar qualquer tecla, ele fecha. Ele armazena qual tecla foi 
digitada.

O open Cv é capaz de ler varios formatos de imagem 
'''

import cv2 as cv
import numpy as np

img1 = np.full((300, 400, 3), (255, 255, 255), np.uint8)
drawing = False

def trata_mouse(event, x, y, flags, param):
    global drawing, img
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(img1, (x, y), 5, (0, 0, 255), 3)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

def imgs():
    img1 = cv.imread('messi.png')
    if img1 is None:
        print("Não achei a imagem")
    else:
        
        bola = img1[280:340, 330:390]
        cv.imshow("bola", bola)
        
        ## Crop e paste


        img2 = np.full((100, 100, 3), (0,0,0))

        img1[273:333, 100:160] = bola
        img1[200:300, 300:400] = img2

        
        cv.imshow("janela 2", img1)


        k = cv.waitKey(0)
        print(f"A tecla digitada foi {k}")
        if k == 115:#s
            cv.imwrite('messi_cv.jpg', img1)



def shapes():
    """
        Rotinas para desenho no cv
        cv.circle(cvimg, (cx, cy), raio, cor, thickness)
        cv.rectangle(cvimg, tol_left, bottom_rigth, cor, thickness)
        cv.line(cvimg, pt1, pt2, cor, thickness)



        IMPORTANTE: O padrão do open cv é BGR, e não RGB

    """

    img1 = np.full( (300, 300, 3), (255,255,255), dtype=np.uint8)
    print(f"shape: {img1.shape}")

    cv.imshow("Janela 1", img1)
    cv.waitKey(10000)

    cv.circle(img1, (100, 100), 30, (0, 255, 0), 3) # Verde
    cv.imshow("Janela 1", img1)
    cv.waitKey(10000)

    cv.rectangle(img1, (120, 110), (200, 230), (255, 0, 0), 5) # Azul (lembre-se, trabalhamos com BGR)
    cv.imshow("Janela 1", img1)
    cv.waitKey(10000)

    cv.line(img1, (270, 30), (30, 270), (0, 0, 255), 15) #Vermelho
    cv.imshow("Janela 1", img1)
    cv.waitKey(10000)

def desenha():

    cv.imshow("Janela 1", img1)
    cv.waitKey(0)

    cv.setMouseCallback("Janela 1", trata_mouse) #Sempre que o mouse interagir 
    # com a janela 1, chama a callback trata_mouse

    while(True):
        k = cv.waitKey(10)
        if k == 27: #esc
            break
    
    cv.destroyAllWindows() #limpa tudo
#imgs()
#shapes()
desenha()