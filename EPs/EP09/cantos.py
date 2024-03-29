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
    """
    (None) -> None
    CALLBACK acionada em eventos associados ao mouse. A função apenas realiza
    alguma operação se a ação do mouse for um clique do botom esquerdo e se o
    usuario selecionou no maximo 4 pontos.

    A função armazena os pontos selecionados pelo usuario e, depois de
    selecionar 4 pontos, realiza uma transformação de perspectiva utilizando o
    quadrilatero determinado pelos pontos escolhidos.
    """
    global selecionados, quant, corners, img
    if event == cv.EVENT_LBUTTONDOWN and quant < 4:
        poix, poiy = x,y
        for corner in corners:
            xc, yc = corner.ravel()
            if abs(x - xc) <= 3 and abs(y - yc) <= 3:
                # Se o ponto selecionado estiver dentro de uma janela 7x7
                # centrada em (xc, yc), interpretamos o clique do usuario como
                # um clique em (xc, yc), logo, tomamos essas coordenadas como
                # pontos de interesse e mudamos a cor do ponto detectado.
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
            # Ao atingirmos a quantidade de 4 pontos selecionados, realizamos a
            # operação de transformação de perspectiva.

            # Primeiro, obtemos os pontos top left, top right, bottom right e
            # bottom left. Isto é feito ordenando os pontos em ordem crescente
            # de x (ou seja, separando pontos em esquerda e direita) e então
            # ordenando em ordem crescente de y (logo, tomando os pontos no topo
            # da imagem seguido pelos pontos mais abaixo da imagem.)
            selecionados.sort(key=lambda sel: sel[0])
            l = sorted([selecionados[0], selecionados[1]],\
                key=lambda sel: sel[1])
            r = sorted([selecionados[2], selecionados[3]],\
                key=lambda sel: sel[1])
            tl, bl = l
            tr, br = r
            selecionados = [tl, tr, br, bl]

            altura_esq = abs(tl[1] - bl[1])
            altura_dir = abs(tr[1] - br[1])

            largura_sup = abs(tl[0] - tr[0])
            largura_inf = abs(bl[0] - br[0])

            # Calculamos altura e largura media para determinar a dimensão da
            # imagem com perspectiva corrigida.
            altura_media = (altura_esq + altura_dir)//2
            largura_media = (largura_sup + largura_inf)//2

            pontos_perspectiva = \
                np.float32(\
                    [(0, 0), \
                    (largura_media, 0), \
                    (largura_media, altura_media), \
                    (0, altura_media)])
            selecionados = np.float32(selecionados)

            M = cv.getPerspectiveTransform(selecionados,pontos_perspectiva)
            dst = cv.warpPerspective(original,M,(largura_media, altura_media))
            cv.imshow("Document", dst)







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
    global selecionados, quant, corners, img, original

    quant = 0
    selecionados = []

    img = captura_imagem()
    original = np.copy(img)
    # Copia da imagem de entrada, utilizada para limparmos os circulos
    # desenhados sobre ela e realizarmos a operação de transformação de
    # perspectiva.

    if img is None:
        print("Erro na abertura da imagem.")

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # Seleciona 100 pontos acima de uma qualidade 0.01; Aqui limitamos a
    # distancia euclidiana entre pontos em 7 para garantir que a janela 7x7
    # de um canto não se sobreponha a outra janela.
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
