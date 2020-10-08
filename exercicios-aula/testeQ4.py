

from vetor3D import Vetor3D

def main():
    pos = [11, 22, 33]
    print("1 -------------------")
    print("Vetor3D.coord()")
    p0 = Vetor3D(pos)
    print(f"p0 = {p0}")
    pos[0] = 44
    print(f"p0 = {p0}")

    print("\n2 ------------------------")
    print("Vetor3D + Vetor3D")
    p1 = Vetor3D()
    print(f"p1 = {p1}")
    p2 = Vetor3D([11, 22, 33])
    print(f"p2 = {p2}")
    p1 = p1 + p2
    print(f"p1 = p1 + p2 = {p1 + p2}")
    p1 += p2
    print(f"p1 = p1 + p2 = {p1 + p2}")

    print("\n3 ------------------------")
    print("Vetor3D * const")
    p3 = Vetor3D([44, 55, 66])
    print(f"p3 = {p3}")
    print(f"p3 * 0.5 = {p3 * 0.5}")

    print("\n4 ------------------------")
    print("const * Vetor3D")
    p4 = Vetor3D([77, 88, 99])
    print(f"p4 = {p4}")
    print(f"2 * p4 = {2 * p4}")

    print("\n5 ------------------------")
    print("Vetor3D.soma()")
    p5 = Vetor3D([-1, 2, -3] )
    print(f"p5 = {p5}")
    print(f"p5.soma() = {p5.soma()}")  # somatória dos elementos
    print(f"p5 = {p5}")

    print("\n6 ------------------------")
    print("Vetor3D.dot()")
    p6 = Vetor3D([3, 2, -1] )
    print(f"p6 = {p6}")
    print(f"p6.dot(p5) = {p6.dot(p5)}") # somatória do produto elemento a elemento

main()

""" A saída do programa deve ser:

1 -------------------
Vetor3D.coord()
p0 = (11, 22, 33)
p0 = (11, 22, 33)

2 ------------------------
Vetor3D + Vetor3D
p1 = (0, 0, 0)
p2 = (11, 22, 33)
p1 = p1 + p2 = (22, 44, 66)
p1 = p1 + p2 = (33, 66, 99)

3 ------------------------
Vetor3D * const
p3 = (44, 55, 66)
p3 * 0.5 = (22.0, 27.5, 33.0)

4 ------------------------
const * Vetor3D
p4 = (77, 88, 99)
2 * p4 = (154, 176, 198)

5 ------------------------
Vetor3D.soma()
p5 = (-1, 2, -3)
p5.soma() = -2
p5 = (-1, 2, -3)

6 ------------------------
Vetor3D.dot()
p6 = (3, 2, -1)
p6.dot(p5) = 4

 """