# Aula 01

### Introdução ao processamento de imagem

Modelo mental de processamento de imagem:

* A visão computacional recebe uma imagem, faz uma análise e chega em um modelo computacional (informação semnântica). 
* Já a computação gráfica, ela parte de um modelo e gera uma imagem.

A disciplina vai ser mais focada em visão computacional, especificamente em elaborar modelos a partir de imagens.



### O que é uma imagem?

* Uma imagem pode ser representada no computador como  um objeto bidimensional de largura W e altura H. 
* A imagem é quebrada em pedacinhos, chamamos esses pedaços de **pixels**. Cada Pixel possui um valor, esse valor é a **cor** do pixel. Esse valor pode, por exemplo, assumir valores entre 0 e 255 para podermos representar a cor na escala rgb
* Alguns conceitos importantes de uma imagem:
  * Aspect ratio: $\frac{W}{H}$. Muitas telas HD hoje em dia são 16:9, por exemplo
  * Densidade de pixels: quantidade de pixels por unidade de medida (usa-se bastante ppi, que é pixels por polegada)

## Uma breve revisão de python

Usaremos python3 no curso.

Revisão básica de alguns comandos de python:

```python
print('Hello, world') #print

2 + 2 * 4 #operador aritmetico

2 + 3* 4 > 20 # operador booleano

def main(): # Função
	'''
	Comentario de função. Documentação.
	'''
    #...

```

### Imagens em python

* Podemos representar imagens em python usando listas de listas:

  ```python
  imagem = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
  ]
  ```

  

* Criando uma imagem:

  ```python
  def cria_matriz (nlins, ncols, valor):
  	lista = []
      for lin in range(nlins):
          lista.append(valor * ncols)
  	return lista
  ```

  