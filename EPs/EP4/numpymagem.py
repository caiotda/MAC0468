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

    def __init__(self, nlins, ncols, valor=0):
        """ (self, int, int/numpy array) -> Numpymagem
        RECEBE inteiros nlins, ncols e valor (opcional).
        DEVOLVE um objeto da classe Numpymagem, que representa uma imagem de
        nlins linhas e ncols colunas onde todos seus pixels possuem conteúdo 
        igual a `valor`. Se valor for um array numpy, cria uma imagem com mesmo
        conteúdo.
        """
        if type(valor) is np.ndarray:
            self.array = np.array(valor)
            self.shape = valor.shape
        else:
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

if __name__ == '__main__':
    main()
