from Pymagem import Pymagem

def main():
    ''' (None) -> None
    Essa função apenas testa a classe Pymagem.
    Coloque aqui outros testes que desejar.
    '''
    # testa construtor
    img1 = Pymagem(4, 5)
    img2 = Pymagem(3, 3, 88)

    print("\nChamadas da função print()")
    print("Conteúdo de img1:")
    print(img1)
    print("Conteúdo de img2:")
    print(img2)

    print("\nChamadas do método size()")
    lins1, cols1 = img1.size()
    print("Resolução de img1: %d x %d"%(lins1, cols1))
    lins2, cols2 = img2.size()
    print("Resolução de img2: %d x %d"%(lins2, cols2))

    print("\nChamadas do método crop")
    img3 = img1.crop() ## cria uma cópia
    print("Conteúdo de img3:")
    print(img3)
    img4 = img2.crop(0, 1, lins2-1, cols2)  
    print("Conteúdo de img4:")
    print(img4)

    print("\nChamadas para testar o acesso e atribuição")
    col = 2
    img1[0, col] = 11
    for lin in range(1, lins1):
        img1[lin, col] = img1[lin-1, col] + 10
    print("Conteúdo de img1:")
    print(img1)
    # não deve alterar img3
    print("Conteúdo de img3:")
    print(img3)

    # modifica a linha 1 de img2
    lin = 1
    for col in range(0, cols2):
        img2[lin, col] = 11
    print("Conteúdo de img2:")
    print(img2)
    # não deve alterar img4
    print("Conteúdo de img4:")
    print(img4)

    # mais testes inclusive os seus...
    print("Outro crop")
    print(img1.crop(1,1,3,4))

    print("Testando um bagulhete...")
    print(img1.crop().matriz)

    print("Testando segmentação SME"):


if __name__ == '__main__':
    main()