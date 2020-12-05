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
from matplotlib import pyplot as plt

import pandas as pd

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
    global selecionados, quant, corners, entrada
    if event == cv.EVENT_LBUTTONDOWN and quant < 4:
        poix, poiy = x,y
        if (poix, poiy) not in selecionados:
            selecionados.append((poix, poiy))
            cv.circle(entrada,(poix,poiy),3,255,-1)
            cv.imshow("Selecione Cantos", entrada)
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
            quant = 0


def extrai_matriz_homografia(row):
    """(PANDAS ROW) -> Matriz
    """
    params = ['h00', 'h01', 'h02', 'h10', 'h11', 'h12', 'h20', 'h21', 'h22']
    M = []
    for p in params:
        val = row[p]
        M.append(val)
    M = np.array(M)
    M = M.reshape((3,3))
    return M


def inverte_homografia(row, M):
    """(pandas row, Matriz) -> Vetor
    Recebe uma linha de um dataframe e uma matriz de homografia.
    Inverte a matriz de homografia e obtem os pontos utilizados para gerar
    a matriz de homografia.
    """
    saida = abre_imagem(row['saida'])
    h, w, _ = saida.shape
    poi = np.float32([[[0,0]], [[w, 0]], [[w, h]], [[0, h]]])
    M_inv = np.linalg.inv(M)
    poi = cv.perspectiveTransform(poi, M_inv)
    return poi

def calcula_score(csv):
    global selecionados, quant, corners, entrada, original
    quant = 0
    """
    (csv) -> lista de valores

    RECEBE um csv pandas e calcula o score usando a matriz H na planilha e comparando
    com as imagens gabarito

    o que eu quero fazer aqui é abrir a imagem gabarito,
    abrir a imagem de entrada e aplicar a matriz de homeografia
    """


    acc = 0
    total = 0
    y_shi = []
    y_sub = []
    x_ambos = []
    for i, row in csv.iterrows():
        # Itera as linhas da tabela
        selecionados = []
        #M = extrai_matriz_homografia(row)
        #poi = inverte_homografia(row, M)
        entrada = abre_imagem(row['entrada'])
        original = np.copy(entrada)
        cv.imshow("Selecione Cantos", entrada)
        cv.setMouseCallback("Selecione Cantos", seleciona_pontos)
        cv.waitKey(0)
        print(selecionados)
        gray = cv.cvtColor(entrada, cv.COLOR_BGR2GRAY)
        corners_shi = cv.goodFeaturesToTrack(gray,100,0.01,7)
        proximos_shi = [20, 20, 20, 20]
        proximos_sub = [20, 20, 20, 20]


        corners = cv.goodFeaturesToTrack(gray,100,0.01,7)

        winSize = (5, 5)
        zeroZone = (-1, -1)
        criteria = (cv.TERM_CRITERIA_EPS + cv.TermCriteria_COUNT, 40, 0.001)
        corners_subpix = cv.cornerSubPix(gray, corners, winSize, zeroZone, criteria)

        for idx, p in enumerate(selecionados):
            for c in corners_shi:
                dist = cv.norm(p - c, cv.NORM_L2)
                if  dist < 20 and dist < proximos_shi[idx]:
                    #Verifica se o ponto está numa distancia de 20 pixels
                    proximos_shi[idx] = dist
            print(f"Proximos_shi: {proximos_shi}")

            for c in corners_subpix:
                dist = cv.norm(p - c, cv.NORM_L2)
                if  dist < 20 and dist < proximos_sub[idx]:
                    #Verifica se o ponto está numa distancia de 20 pixels
                    proximos_sub[idx] = dist
            print(f"Proximos_sub: {proximos_sub}")
        media_shi = np.mean(proximos_shi)
        media_sub = np.mean(proximos_sub)
        y_shi.append(media_shi)
        y_sub.append(media_sub)
        x_ambos.append(i)
    x_ambos = np.array(x_ambos)
    y_shi = np.array(y_shi)
    y_sub = np.array(y_sub)

    y_diff = y_shi - y_sub
    #print(f"Shapes. x: {x_ambos.shape}; y_shi: {y_shi.shape}; y_sub: {y_sub.shape}")
    print(y_shi)
    print(y_sub)
    plt.plot(x_ambos, y_shi, label="Shi Tomasi")

    plt.plot(x_ambos, y_sub,label="Acuracia sub pixel")
    plt.xlabel("Número da imagem")
    plt.ylabel("Média da distancia dos 4 cantos mais proximos")

    plt.title("Comparação entre métodos de detecção de bordas")
    plt.legend(loc='best')
    plt.show()


    # gray = cv.cvtColor(entrada, cv.COLOR_BGR2GRAY)


    return 0



def abre_imagem(path):
    """
    (string) -> img/None
    """
    try:
        file_path = "./dataset/" + path
        img = cv.imread(file_path)
    except:
        print("Algo deu errado na abertura da imagem")
    return img

def main():
    debug = True
    data = pd.read_csv('./tabela.csv', skipinitialspace=True)
    entrada = data['entrada']
    if debug:
        score_entrada = calcula_score(data)
    else:
        path = ''
        img = abre_imagem(path)
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


if __name__== '__main__':
    main()
