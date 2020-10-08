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
        if isinstance(escalar, Vetor3D):
            esq = escalar
            dir = self
        else:
            esq = self
            dir = escalar
        res = []
        for item in esq.pos:
            res.append(item * dir)
        return Vetor3D(res)
    __rmul__ = __mul__
    
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