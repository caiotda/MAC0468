class Vetor3D:
    def __init__(self, pos=None):
        if pos is None:
            pos = (0,0,0)
        self.pos = tuple(pos)

    def __str__(self):
        return str(self.pos)

    def __add__(self, other):
        res = []
        for i in range(len(self.pos)):
            res.append(self.pos[i] + other.pos[i])
        return Vetor3D(res)

    def __mul__(self, escalar):
        res = []
        for item in self.pos:
            res.append(item * escalar)
        return Vetor3D(res)

    __rmul__ = __mul__ 
    # A implementação do rmul é identica, então vamos simplesmente referenciar
    # a implementação do método magico __mul__ para lidar com casos como
    # escalar * (1,2,3)
    
    def soma(self):
        soma = 0
        for item in self.pos:
            soma += item
        return soma

    def dot(self, other):
        produto = 0
        for i in range(len(self.pos)):
            produto += self.pos[i] * other.pos[i]
        return produto