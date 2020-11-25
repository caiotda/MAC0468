'''
Filtros morfologicos -> não lineares

Tipicamente utilizados em imagens binárias.

Primeiro exemplo: erosão.

Seja (x', y') uma vizinhança do ponto (x,y) tal que (x', y') != 0

Seja dst a matriz erodida e src a matriz original.

dst(x,y) = min src(x + x', y + y')

Esse é o filtro de erosão. Percorremos uma região da matriz de original e tiramos
o minimo numa vizinhança. Se tiver algum 0 na vizinhança, o pixel central vira um 0.

Aqui entendemos pixels 0 como fundo, e o resto como objeto. O que esse filtro
faz é reduzir a area do objeto e aumentar o fundo

O filtro de erosão consegue:

* Remover ruidos
* Afinar as bordas


Analogamente, temos o filtro da dilatação:

dst(x,y) = max src(x + x', y + y')

Ou seja, se tiver qualquer pixel diferente de 0 na vizinhança, tomamos esse valor. O que 
isso faz é diminuir o fundo e aumentar o objeto.

Aplicação: preencher buracos.



A esse processo damos o nome de ABERTURA

Abertura: erosão da imagem de entrada seguida de uma 
dilatação.

Fechamento: o contrário.

Gradiente: é o processo de dilatar um objeto, dai erodir e subtrari os dois. Isso dá o contorno do objeto
'''
import cv2 as cv
import numpy as np
FNAME = './assets/img/potatoes.jpg'
win_name = 'Binaria'

def main():
    global bina, blur

    # elemento estruturante
    caixa = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    kernel = np.array(caixa)

    kernel = np.ones((5,5), dtype=np.uint8)

    img = cv.imread(FNAME)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    nlin, ncol = gray.shape
    blur = gray = cv.pyrDown(gray, (nlin//2, ncol//2))
    #blur = cv.GaussianBlur(gray, (15,15), 0)
    cv.imshow('Batatas', gray)
    cv.imshow('Batatas borradas', blur)
    
    limiar = 127

    cv.imshow(win_name, gray)
    cv.createTrackbar('track_bin', win_name, limiar, 255, on_trackbar)
    on_trackbar(limiar)

    while True:
        k = cv.waitKey()
        if k == ord('q'):
            break
        if k == ord('e'):
            bina = cv.erode(bina, kernel, iterations=1)
            cv.imshow(win_name, bina)            
        if k == ord('d'):
            bina = cv.dilate(bina, kernel, iterations=1)
            cv.imshow(win_name, bina)
        if k == ord('g'):
            bina = cv.morphologyEx(bina, cv.MORPH_GRADIENT,kernel)
            cv.imshow(win_name, bina)        

def on_trackbar(valor):
    global bina, blur
    print(f"valor: {valor}")
    _, bina = cv.threshold(blur, valor, 255, cv.THRESH_BINARY_INV)
    cv.imshow(win_name, bina)
main()