# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Caio Túlio de Deus Andrade
    NUSP: 979723

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
import numpy as np
from numpymagem import Numpymagem
from numpymutil import mostre_video
from numpymutil import salve_video
import math

# Escreva aqui outras constantes que desejar
ALTURA  = 200
LARGURA = 320
BLACK = 0
WHITE = 250

#-------------------------------------------------------------------------- 

def main():
    ''' (None) -> None
    Escreva o seu programa que cria o vídeo como descrito no enunciado.
    
    O código abaixo serve para ilustrar como usar a função mostre_video()
    que recebe uma lista com NumPymagens e as mostra em um vídeo na tela
    do seu computador usando PyGame. Por isso lembre-se de seguir as 
    instruções para instalar PyGame no seu computador.

    Remova ou altere o código para gerar o seu próprio vídeo. Não se esqueça
    de criar funções para facilitar o entendimento do seu vídeo.

    Você pode (mas não precisa!) salvar o seu vídeo em um formato mp4, para
    mostrar sua obra no fórum da disciplina. Para isso, antes de salvar, 
    você deve instalar o software ffmpeg que você pode baixar de 
    https://ffmpeg.org/download.html. 
    '''
    
    video = []
    preto = Numpymagem( (ALTURA, LARGURA), BLACK)    
    branco = Numpymagem( (ALTURA, LARGURA), WHITE)
    print(f"Está compatível com numpymutil: {type(preto.data) is np.ndarray}")
    cor = BLACK

    for i in range(120):
        RAIO = LARGURA // 7
        canvas = Numpymagem((ALTURA, LARGURA), BLACK)
        canvas.pinte_disco(ALTURA//2, LARGURA//2, RAIO//2, WHITE)

        Y = ALTURA//2
        X = LARGURA//2
        RAIO_C = 7*RAIO/4

        canvas.pinte_disco(Y + math.floor(RAIO_C*math.sin(i*math.pi/60)), X + math.floor(RAIO_C*math.cos(i*math.pi/60)), RAIO//4, WHITE)
        video.append(canvas)
    mostre = True
    if mostre:
        mostre_video(video)

    salve = False
    if salve:
        print("Salvando vídeo")
        salve_video(video)

#-------------------------------------------------------------------------- 
#
# ESCREVA OUTRAS FUNÇÕES E CLASSES QUE DESEJAR
#
#-------------------------------------------------------------------------- 


#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()