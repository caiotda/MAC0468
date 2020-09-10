# Aula 03

## Programação orientada a objetos em python

***

Digamos que queremos escrever um programa que soma frações. As frações podem ser representadas como a/b. Para somar frações a/b + c/d precisamos resolver muitas burocracias: Primeiro, tirar o mmc entre b e d, acertar os denominadores...



Para um programa qualquer, não faz sentido conhecer como essa conta é feita. Um cliente precisa apenas saber que as operações existem, não como elas são implementadas



Para isso, podemos criar uma **classe** que representa o **objeto** da fração. Nessa classe, podemos implementar como funciona a soma, por exemplo. A implementação, é feita por meio de um **método**, que é uma função utilizada para manipular um objeto.

Qualquer característica utilizada para caracterizar um objeto é chamada de **atributo**.



```python
class Fracao:
    """
    Cria o tipo fração
    """
    
    def __init__(self, n, d): # construtor
        self.num = n
        self.den = d
        
    def __str__(self): # usado pelo print
        s = f'{self.n}/{self.d}'
        return s
    
    def __add__(self, other): # Implementa a operação de soma com o 
        # objeto
        
		#...
    def __mul__(self, other): #Implementa a operação de multiplicação
        num = self.num * other.num
        den = self.den * other.den
        return Fracao(num, den)
    
 # ...

fracao = Fracao(2,3) # Cria um objeto Fracao 2/3
```

