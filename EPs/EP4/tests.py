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

    # Testes do __add__

    a = np.array([1,2,3])
    b = np.array([1,1,1])
    a_b = np.array([2,3,4])
    c = np.array([0,0,0])
    a_c = a
    a = Numpymagem((), a)
    b = Numpymagem((), b)
    a_b = Numpymagem((), a_b)
    c = Numpymagem((), c)
    a_c = Numpymagem((), a_c)
    tests = [
        ((a, b), a_b),
        ((a,c), a_c),
    ]
    for test in tests:
        params, expected = test
        left, right = params
        res = left + right
        if np.array_equal(res.array, expected.array):
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com parametros {params}. Esperava \n{expected}, recebi\n {res}")
        total += 1

    # Testes do mul

    tests = [
        ((a, 2), Numpymagem((), np.array([2, 4, 6]))),
        ((a, 0),Numpymagem((), np.array([0, 0, 0]))),
    ]

    for test in tests:
        params, expected = test
        left, escalar = params
        res = left * escalar
        if np.array_equal(res.array, expected.array):
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com parametros {params}. Esperava \n{expected}, recebi\n {res}")
        total += 1

    # Testes do crop
    a = [[1,2,3,4,5], [6, 7, 8, 9, 10], [11, 12 ,13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    a_1 = Numpymagem((), np.array(a))
    a_2 = Numpymagem((), np.array([[7, 8, 9], [12, 13, 14], [17, 18, 19]]))
    a_3 = Numpymagem((), np.array([[1,2], [6,7]]))
    a_4 = Numpymagem((), np.array([[1,2,3,4], [6,7,8,9]]))

    a_crop = Numpymagem((), np.array(a))

    tests = [
        ((1, 1, 4, 4), a_2),
        ((), a_1),
        ((0, 0, 2, 2), a_3),
        ((0, 0, 2, 4), a_4)
    ]

    for test in tests:
        params, expected = test
        if len(params) > 0:
            tlx, tly, brx, bry = params
            res = a_crop.crop(tlx, tly, brx, bry)
        else:
            res = a_crop.crop()
        if np.array_equal(res.array, expected.array):
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com parametros {params}. Esperava \n{expected}, recebi\n {res}")
        total += 1


    a = [
        [1, 1, 2, 2, 2, 2, 2, 1],
        [1, 1, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]

    b = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 2, 2],
    ]
    # Testes do paste
    target1 = Numpymagem((), np.array([[1,2,3], [4,5,6], [7,8,9]]))
    target2 = Numpymagem((6,8), 1)
    pasted1 = Numpymagem((), np.array([[0,1], [1,0]]))
    pasted2 = Numpymagem((), np.array([[9, 9, 9, 9], [9,9,9,9], [9,9,9,9], [9,9,9,9]]))
    pasted4 = Numpymagem((), np.array([[5, 5, 5], [5, 5, 5]]))
    pasted5 = Numpymagem((), np.array([[-1]]))
    tests = [
        (( (0, 0),target1,  pasted1), Numpymagem((), np.array([[0, 1, 3], [1, 0, 6], [7,8,9]]))),
        (( (1, 1),target1,  pasted1), Numpymagem((), np.array([[1, 2, 3], [4, 0, 1], [7,1,0]]))),
        (( (0, 1),target1,  pasted1), Numpymagem((), np.array([[1, 0, 1], [4, 1, 0], [7,8,9]]))),
        (( (2, 2),target1,  pasted1), Numpymagem((), np.array([[1, 2, 3], [4, 5, 6], [7,8,0]]))),
        (( (0, 0),target1,  pasted2), Numpymagem((), np.array([[9,9,9], [9,9,9], [9,9,9]]))),
        (( (0, 0),target1,  pasted4), Numpymagem((), np.array([[5,5,5], [5,5,5], [7,8,9]]))),
        (( (0, 0),target1,  pasted5), Numpymagem((), np.array([[-1, 2, 3], [4, 5, 6], [7,8,9]]))),
        (( (1, 1),target1,  pasted5), Numpymagem((), np.array([[1, 2, 3], [4, -1, 6], [7,8,9]]))),
        (( (-1, 2), target2, Numpymagem((3, 5), 2)), Numpymagem((), np.array(a))),
        (( (5, 6), target2, Numpymagem((3, 5), 2)), Numpymagem((), np.array(b)))
    ]

    for test in tests:
        args, expected = test
        coords, target, pasted = args
        lin, col = coords
        test = target.crop()
        test.paste(pasted, lin, col)
        res = test.crop()
        if np.array_equal(test.array, expected.array):
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com parametros {coords}. Esperava \n{expected}, recebi\n{res}")
        total += 1

    # Testes do pinte_retangulo

    canvas1 = Numpymagem((4, 4), 0.0)
    ret1 = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0 ,0 ,0 ,0]])
    ret2 = np.array([[1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [1 ,1 ,0 ,0]])
    ret3 = np.array([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0 ,0 ,0 ,0]])
    ret4 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1 ,1 ,1 ,1]])

    tests = [
        (( (0, 0, 1, 3), 1), Numpymagem((), ret1)),
        (( (0, 0, 3, 1), 1), Numpymagem((), ret2)),
        (( (0, 0, 0, 0), 1), Numpymagem((), ret3)),
        (( (3, 0, 3, 3), 1), Numpymagem((), ret4)),
    ]

    for test in tests: 
        params, expected = test
        coords, val = params
        tlx, tly, brx, bry = coords
        res = canvas1.crop()
        res.pinte_retangulo(tlx, tly, brx, bry, val)
        if np.array_equal(expected.array, res.array):
            correct += 1
        else:
            failed += 1
            print(f"Teste falhou com coordenadas {coords}, valor {val}. Esperava \n{expected}, \nrecebi \n{res}")
        total += 1


    print(f"Fim dos testes. {correct}/{total} passaram. {failed} testes falharam.")


main()