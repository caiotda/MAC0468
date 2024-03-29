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

#-------------------------------------------------------------------------- 

class Pymagem:
    '''
    Implementação da classe Pymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem

    def __init__(self, nlins, ncols, valor = 0):
        """ (int, int, int) -> Pymagem
        RECEBE inteiros nlins, ncols e valor (opcional)

        RETORNA um objeto da classe Pymagem com 3 campos:
        1. nlins: número de linhas da imagem
        2. ncols: número de colunas da imagem
        3. matriz: representação em matriz da imagem, onde 
        todo elemento da matriz vale `valor` e a imagem possui
        nlins linhas e ncols colunas.

        """
        self.nlins = nlins
        self.ncols = ncols
        self.matriz = []
        for _ in range(self.nlins):
            linha = []
            for _ in range(self.ncols):
                linha.append(valor)
            self.matriz.append(linha)

    def __repr__(self):
        """(None) -> string
        RETORNA uma string utilizada por print() para exibir a `matriz`.
        """
        s = ''
        for i in range(self.nlins):
            for j in range(self.ncols):
                s += '%4d '%self.matriz[i][j]
            s += '\n'
        return s

    def __getitem__(self, index):
        """ (lista) -> number
        RECEBE uma lista contendo uma coordenada da imagem e
        DEVOLVE o valor do pixel associado à coordenada
        """
        lin, col = index
        return self.matriz[lin][col]

    def __setitem__(self, index, valor):
        """ (lista, value) -> None
        RECEBE uma lista contendo uma coordenada da imagem e um valor.
        MODIFICA a imagem, alterando o valor do pixel
        associado à coordenada, alterando seu valor para `valor`.
        """
        lin, col = index
        self.matriz[lin][col] = valor

    def __sub__(self, other):
        """(Pymagem) -> Pymagem
        RECEBE um objeto da classe Pymagem e 
        RETORNA um objeto da classe Pymagem contendo o resultado da
        subtração das imagens self e other.

        Implementa a operação de subtração entre dois objetos.

        """
        resultado = Pymagem(self.nlins, self.ncols)
        for i in range(self.nlins):
            for j in range(self.ncols):
                resultado.matriz[i][j] = self.matriz[i][j] - other.matriz[i][j]
        return resultado

    def size(self):
        """ (None) -> int
        RETORNA uma tupla contendo o par(nlins, ncols), respectivamente o número 
        de linhas e colunas da imagem.
        """
        return (self.nlins, self.ncols)

    def crop(self, top_lin=0, top_col=0, bottom_lin=None, bottom_col=None):
        """ (int, int, int, int) -> Pymagem
        RECEBE inteiros bottom_lin, bottom_col, top_lin e top_col
        (todos opcionais).

        DEVOLVE um objeto Pymagem que representa uma região da Pymagem `self`: 
        pega todos elementos self.matriz[i][j], onde i e j satisfazem 
        top_lin <=i < bottom_lin e top_col <= j < bottom_col

        Se nenhum parâmetro é passado, devolve um clone de self.

        """
        if bottom_lin is None:
            bottom_lin = len(self.matriz) 
        if bottom_col is None:
            bottom_col = len(self.matriz[0])

        nlins = bottom_lin - top_lin
        ncols = bottom_col - top_col
        imagem_com_crop = Pymagem(nlins, ncols)
        for i in range(top_lin, bottom_lin):
            for j in range(top_col, bottom_col):
                imagem_com_crop.matriz[i-top_lin][j-top_col] = self.matriz[i][j]
        return imagem_com_crop


    def limiarize(self, limite, alto, baixo):
        """ (int, int, int) -> None
        RECEBE inteiros limite, alto, baixo e 
        MODIFICA  o objeto Pymagem de forma que todo pixel da imagem
        com valor acima de limite deve receber o valor `alto`; 
        Do contrário, recebe o valor `baixo`.
        """
        for i in range(self.nlins):
            for j in range(self.ncols):
                if self.matriz[i][j] > limite:
                    self.matriz[i][j] = alto
                else:
                    self.matriz[i][j] = baixo

    def erosao(self, viz):
        """(int) -> None
        RECEBE um inteiro viz e 
        MODIFICA a imagem, aplicando um filtro de erosão com vizinhaça de
        tamanho viz.
        """
        clone = self.crop()
        for i in range(self.nlins):
            for j in range(self.ncols):
                self.matriz[i][j] = clone.__pega_minimo_vizinhança(i, j, viz)
    
    def segmentacao_SME(self, viz):
        """ (int) -> Pymagem
        RECEBE um inteiro viz e 
        DEVOLVE a matriz self subtraida da matriz self com um filtro de erosão
        aplicado.
        """
        matriz_erodida = self.crop()
        matriz_erodida.erosao(viz)
        return self - matriz_erodida
    ## ---------------------- Métodos privados --------------------------------
    def __pega_minimo_vizinhança(self, lin, col, viz):
        """ (int, int, int)-> number
        RECEBE inteiros lin, col e viz, representando uma vizinhança de tamanho
        viz e centrada nas coordenadas (lin,col).

        DEVOLVE o valor do pixel de menor valor na vizinhança centrada em
        (lin, col) com vizinhança de tamanho viz.
        """
        min_bit = self.matriz[lin][col]
        for i, j in self.__pega_vizinhança(lin, col, viz):
            if self.matriz[i][j] < min_bit:
                min_bit = self.matriz[i][j]
        return min_bit

    def __pega_vizinhança(self, lin, col, viz):
        """ (int, int, int)-> set
        RECEBE inteiros lin, col e viz, representando uma vizinhança de tamanho
        viz e centrada nas coordenadas (lin,col).

        DEVOLVE todos pares (linha,coluna) que estão na vizinhança centrada em
        (lin,col) com vizinhança de tamanho viz.
        """
        min_x = max(lin - viz//2, 0)
        max_x = min(len(self.matriz) - 1, lin + viz//2)

        min_y = max(col - viz//2, 0)
        max_y = min(len(self.matriz[0]) - 1, col + viz//2)


        pixels = []
        for i in range(min_x, max_x + 1):
            # Escolhe linhas no intervalo fechado [min_x, max_x]
            for j in range(min_y, max_y + 1): 
                # Escolhe colunas no intervalo fechado [min_y, max_y]
                if self.matriz[lin][col] != self.matriz[i][j]:
                    pixels.append((i, j))
        return set(pixels)
