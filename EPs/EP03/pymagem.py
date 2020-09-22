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
        self.nlins = nlins
        self.ncols = ncols
        self.matriz = []
        for i in self.nlins:
            for j in self.ncols:
                self.matriz[i][j] = valor

    def __repr__(self):
        s = ''
        for i in range(self.nlins):
            for j in range(self.ncols):
                s += '%4d '%self.matriz[i][j]
            s += '\n'
        return s
    
    def size(self):
        return (self.nlins, self.ncols)

    def __getitem__(self, index):
        lin, col = index
        return self.matriz[lin][col]

    def __setitem__(self, index, valor):
        lin, col = index
        self.matriz[lin][col] = valor

    def __isub__(self, other):
        for i in self.nlins:
            for j in self.ncols:
                self.matriz = self.matriz[i][j] - other.matriz[i][j]


    def limiarize(self, limite, alto, baixo):
        for i in self.nlins:
            for j in self.ncols:
                if self.matriz[i][j] > limite:
                    self.matriz[i][j] = alto
                else:
                    self.matriz[i][j] = baixo

    def erosao(self, viz):
        clone = self.__clone()
        for i in self.nlins:
            for j in self.ncols:
                self.matriz[i][j] = self.__pega_minimo_vizinhança(i, j, viz)
    
    def segmentacao_SME(self, viz):
        matriz_original = self.__clone()
        return self - self.erosao(matriz_original)

    def __pega_minimo_vizinhança(self, lin, col, viz):
        max_bit = self.matriz[lin][col]
        for i, j in self.__pega_vizinhança(lin, col, viz)
            if self.matriz[i][j] > max_bit
                max_bit = self.matriz[i][j]
        return max_bit

    def __pega_vizinhança(self, lin, col, viz):
        min_x = max(lin - viz//2, 0)
        max_x = min(len(self.img) - 1, lin + viz//2)

        min_y = max(col - viz//2, 0)
        max_y = min(len(self.img[0]) - 1, col + viz//2)


        pixels = []
        for i in range(min_x, max_x + 1):
            # Escolhe linhas no intervalo fechado [min_x, max_x]
            for j in range(min_y, max_y + 1): 
                # Escolhe colunas no intervalo fechado [min_y, max_y]
                if self.img[lin][col] != self.img[i][j]:
                    pixels.append((i, j))
        return set(pixels)

    def __clone(self):
        clone = []
        for i in self.nlins:
            linha = []
            for j in self.ncols:
                linha.append(self.matriz[i][j])
            clone.append(linha)
        return clone

    
    
