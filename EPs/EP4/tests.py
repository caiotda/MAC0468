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
        (((5, 5), np.array(lista)), np.array(lista))
        ,(((2, 4), 1), np.full((2, 4), 1))
    ]
    correct = 0
    failed = 0
    for test in tests:
        params, expected = test
        shape, val = params
        nlins, ncols = shape
        res = Numpymagem(nlins, ncols, val)
        if np.array_equal(res.array, expected):
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com parametros {params}. Esperava \n{expected}, recebi\n {res}")
    print(f"Fim dos testes. {correct}/{len(tests)} passaram")


main()