from numpymagem import Numpymagem
import numpy as np

def main():
    # Toda bateria de testes tem o formato:
    # 1) args pra chamar a função
    # 2) Esperado

    lista = []
    k = 0
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append(k)  
            k += 1
        lista.append(linha)
    tests = [
        (((), np.array(lista)), np.array(lista))
        ,(((2, 4), 1), np.full((2, 4), 1))
    ]
    correct = 0
    failed = 0
    total = 0
    # Teste do construtor
    for test in tests:
        params, expected = test
        shape, val = params
        res = Numpymagem(shape, val)
        if np.array_equal(res.array, expected):
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com parametros {params}. Esperava \n{expected}, recebi\n {res}")
        total += 1
    # Testes do shape
    tests = [
        (((1, 2), 1), (1,2)),
        (((3,2), 1), (3, 2)),
        (((1,1), 0), (1,1))
    ]
    for test in tests:
        params, expected = test
        shape, val = params
        res = Numpymagem(shape, val)
        if res.shape == expected:
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com parametros {params}. Esperava \n{expected}, recebi\n {res}")
        total += 1

    # Testes do get attr

    a = np.array([[1,2,3], [4,5,6]])
    b = np.array([[-1, 3, 5], [10, 12, 132]])
    tests = [
        (((0, 2), a), 3),
        (((1, 0), b), 10),
    ]

    for test in tests:
        params, expected = test
        key, val = params
        i, j = key
        res = Numpymagem((0, 0), val)
        res = res[i, j]
        if res == expected:
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com parametros {params}. Esperava \n{expected}, recebi\n {res}")
        total += 1

    # Testes do set attr
    tests = [
        (((0, 2), 5), 5),
        (((1, 2), -2), -2)
    ]
    for test in tests:
        params, expected = test
        key, val = params
        i, j = key
        teste = Numpymagem((), a)
        teste[i, j] = val
        res = teste[i, j]
        if res == expected:
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com parametros {params}. Esperava \n{expected}, recebi\n {res}")
        total += 1


    print(f"Fim dos testes. {correct}/{total} passaram")


main()