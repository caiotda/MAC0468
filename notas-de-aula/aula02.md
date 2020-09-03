# Aula 02

### Revisão de listas/matrizes

***

### Listas



São estruturas sequenciais indexadas

* Usamos colchetes pra representar listas.

  * [] -> lista vazia

  * [2]

  * [1,2,3]

  * [1,2,'a', [35, -1, 'e']]: listas podem ter vários tipos de dados dentro dela, 

    inclusive mais listas

Comandos úteis:

* len: retorna p número de elementos da lista

### ìndices

* Usados para acessar um elemento da lista
* Primeiro elemento: indice 0
* Índices negativos: úteis pra varrer a lista de tras pra frente:
  * Primeiro indice negativo: -1

### Concatenação

Um shorthand de concatenação é o operador +:

* [1,2] + [3,4] = [1,2,3,4

Um atalho é usar o *, que equivale a varias concetenações:

* [1,2] * 3 = [1,2,1,2,1,2]

Um operador mais computacionalmente eficiente é o metodo append: ele insere um elemento no fim da lista

### Matrizes

Lista de listas: forma de abstrair estruturas 2D

Cada elemento da lista é outra lista.