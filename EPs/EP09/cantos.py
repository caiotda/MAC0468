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

def seleciona_pontos(event, x, y, flags, param):
    global selecionados, quant, corners, img
    if event == cv.EVENT_LBUTTONDOWN and quant < 4:
        poix, poiy = x,y
        for corner in corners:
            xc, yc = corner.ravel()
            if abs(x - xc) <= 3 and abs(y - yc) <= 3:
                poix, poiy = xc, yc
                cv.circle(img,(poix,poiy), 5,(0, 0, 255), -1)
                cv.imshow("Selecione Cantos", img)
                selecionados.append((poix, poiy))
                break
        if (poix, poiy) not in selecionados:
            selecionados.append((poix, poiy))
            cv.circle(img,(poix,poiy),3,255,-1)
            cv.imshow("Selecione Cantos", img)        
        quant += 1

        if quant == 4:
            print(selecionados)
            selecionados.sort(key=lambda sel: sel[0])
            l = sorted([selecionados[0], selecionados[1]], key=lambda sel: sel[1])
            r = sorted([selecionados[2], selecionados[3]], key=lambda sel: sel[1])
            tl, bl = l
            tr, br = r
            selecionados = [tl, tr, br, bl]




def captura_imagem():
    """
    (None) -> img/None

    DEVOLVE uma imagem openCv, ou None se não conseguir carregar a imagem. 
    Dependendo dos parametros especificados pela linha de comando, devolve uma 
    captura de uma câmera ou de uma imagem especificada na linha de comando.
    """
    if len(sys.argv) < 2:
        device = input('Digite o número de qual câmera você quer usar: ')
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
    global selecionados, quant, rois, corners, img
    selecionados = []
    quant = 0
    img = captura_imagem()
    if img is None:
        print("Erro na abertura da imagem.")

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray,100,0.01,7)
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv.circle(img,(x,y),3,255,-1)
    cv.imshow("Selecione Cantos", img)
    
    cv.setMouseCallback("Selecione Cantos", seleciona_pontos)
    cv.waitKey(0)
    
if __name__== '__main__':
    main()


