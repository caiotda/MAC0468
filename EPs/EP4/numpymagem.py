# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
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
import numpy as np

#-------------------------------------------------------------------------- 

def main():
    '''
    programa para testar a classe Numpymagem
    '''

    lista = []
    k = 0
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append(k)  
            k += 1
        lista.append(linha)

    img1 = Numpymagem( (), np.array(lista))  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}")

    img2 = Numpymagem( (4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}")

    print("\nChamadas do método crop")
    img3 = img2.crop() ## cria uma cópia
    print(f"img3:\n{img3}")

    img4 = img1.crop(1, 1, 5, 4)  
    print(f"img4:\n{img4}")

    img5 = img4 + img3 * 0.5
    print(f"img5:\n{img5}")

    img6 = Numpymagem( (5,5) )
    print(f"img6:\n{img6}")
    img6.paste(img5, -1, 1)
    print(f"img6 paste img5:\n{img6}")

    img7 = Numpymagem( (9, 9), 0.0)
    img8 = img7.crop()

    img7.pinte_disco(0, 4, 3, 1.1)
    print(f"teste disco:\n{img7}")

    img8.pinte_retangulo(4, -1, 8, 5, 8.8)
    print(f"teste retangulo:\n{img8}")

    print("teste disco com retangulo:")
    print(img7 + img8 * 0.5)

    ### TESTE O SEU PROGRAMA COM OUTROS EXEMPLOS
    ### PODE COLOCA-LOS NO FORUM

#-------------------------------------------------------------------------- 

class Numpymagem:
    '''
    Implementação da classe Numpymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Numpymagem

    def __init__(self, shape, valor=0):
        """ (self, tuple, int/numpy array) -> Numpymagem
        RECEBE uma tupla de inteiros shape e um inteiro ou array
        nupy valor (opcional).
        DEVOLVE um objeto da classe Numpymagem, que representa uma imagem de
        nlins linhas e ncols colunas onde todos seus pixels possuem conteúdo 
        igual a `valor`. Se valor for um array numpy, cria uma imagem com mesmo
        conteúdo.
        """
        if type(valor) is np.ndarray:
            self.array = np.array(valor)
            self.shape = valor.shape
        else:
            nlins, ncols = shape
            self.array = np.full((nlins, ncols), valor)
            self.shape = (nlins, ncols)

    def __str__(self):
        """ (self) -> string
        DEVOLVE uma representação em string do objeto self
        """
        s = ''
        nlins, ncols = self.shape
        for i in range(nlins):
            for j in range(ncols):
                s += '%4d '%self.array[i, j]
            s += '\n'
        return s

    def __getitem__(self, key):
        """ (par inteiros) -> pixel
        RECEBE um par de inteiros simbolizados por key e 
        DEVOLVE o pixel com a coordenada especificada pelos dois inteiros
        """
        i, j = key
        return self.array[i, j]

    def __setitem__(self, key, val):
        """(par de inteiros, valor) -> None
        RECEBE um par de inteiros e um valor
        MODIFICA o objeto referenciado por self, modificando
        o pixel referenciado por 'key', trocando seu valor para `val`.
        O tipo de `val` deve ser o mesmo dos itens armazenados em self.array
        """

        i, j = key
        self.array[i, j] = val

    def __add__(self, other):
        """ (Numpymagem) -> Numpymagem
        RECEBE uma numpymagem other e
        DEVOLVE um Numpymagem na qual o valor de cada pixel com coordenada (i,j)
        consiste na soma de todo pixel (i,j) em self com o pixel (i,j)
        correspondente em other
        """
        soma = self.array + other.array
        return Numpymagem((), soma)

    def __mul__(self, escalar):
        """ (number) -> Numpymagem
        RECEBE uma numero  escalar e
        DEVOLVE um Numpymagem na qual o valor de cada pixel com coordenada (i,j)
        consiste na multiplicacção de todo pixel (i,j) em self com pelo escalar
        """

        mul = self.array * escalar
        return Numpymagem((), mul)

    def crop(self,tlx = 0 ,tly = 0, brx = None, bry = None):
        """(int, int, int, int) -> Numpymagem
        RECEBE dois pares de inteiros (opcionais) tlx, tly, brx e bry
        DEVOLVE uma região da imagem referenciada por self delimitada 
        pelos pontos tl e br, onde tl = (tlx, tly) e br = (brx, bry).
        Essa região consiste de um quadrilátero com canto superior 
        esquerdo = tl (top left) e canto inferior direito br (bottom right). 
        """
        if brx is None:
            brx = self.shape[0]
        if bry is None:
            bry = self.shape[1]
        vetor_cropado = self.array[tlx:brx, tly:bry]
        #print(f"vetor cropado: {vetor_cropado}")
        return Numpymagem((), vetor_cropado)

    def paste(self, other, lin, col):
        """ (Numpymagem, tupla de inteiros) -> None
        RECEBE uma numpymagem e dois inteiros representando uma coorde-
        nada.
        MODIFICA self, sobrepondo a imagem other de forma que o canto superior
        esquerdo de other fica alinhado com coords. Modifica a intersecção entre
        other e self copiando os valores pertinentes de other para a imagem 
        self.
        """
        tlx = max(lin, 0)
        tlx_intersect = abs(min(lin, 0))
        #Verifica quantas linhas de other não entraram na intersecção
        tly_intersect = abs(min(col, 0))
        #Verifica quantas colunas de other não entraram na intersecção
        tly = max(col, 0)
        brx = min(tlx + other.shape[0], self.shape[0]) - 1
        bry = min(tly + other.shape[1], self.shape[1]) - 1
        nlins = brx - tlx + 1
        ncols = bry - tly + 1
        
        intersect = other.crop(tlx_intersect, tly_intersect, nlins, ncols)
        self.array[tlx:(brx+1 - tlx_intersect),tly :(bry+1 - tly_intersect)] =\
            intersect.array

    def pinte_disco(self, lin, col, raio, valor):
        """ (int, int, int, int) -> None
        RECEBE inteiros lin, col, raio, valor
        MODIFICA a imagem self pintando um disco centrado em  lin, col com raio
        igual a 'raio' modificando a intersecção desse disco com self com o
        valor `valor`.
        """

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.__in_circunference(i, j, lin, col, raio):
                    self.array[i, j] = valor

    def __in_circunference(self, x, y, a, b, r):
        """ (int, int, int, int, int) -> Bool
        RECEBE inteiros x, y, a, b, r e 
        DEVOLVE um booleano avaliando se o ponto(x,y) está dentro da 
        circunferencia centrada em (a,b) e com raio r. Isto é, se
        (x - a)^2 + (y - b)^2 <= r^2
        """

        return (x - a)**2 + (y - b) **2 <= r**2

    def pinte_retangulo(self, tlx, tly, brx, bry, valor):
        """(int, int, int, int, int) -> None
        RECEBE dois pares de inteiros  tlx, tly, brx, bry e um inteiro valor.
        MODIFICA a imagem self na região de intersecção entre o retângulo
        definido pelas coordenadas (tlx, tly) e (brx, bry) com a imagem,
        pintando a intersecção com o valor `valor`
        """
        tlx = max(tlx, 0)
        tly = max(tly, 0)
        nlins = brx - tlx
        ncols = bry - tly
        retangulo = Numpymagem((nlins, ncols), valor)
        self.paste(retangulo, tlx, tly)


if __name__ == '__main__':
    main()
