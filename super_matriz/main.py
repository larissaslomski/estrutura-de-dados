from super_matriz import SuperMatriz

matriz1 = SuperMatriz(3, 4)
matriz2 = SuperMatriz(5, 5)
matriz3 = SuperMatriz(2, 7)

matriz1.atribuir(2, 3, 1)
print(matriz1.acessar(2, 3))

matriz2.atribuir(5, 5, 2)
print(matriz2.acessar(5, 5))

matriz3.atribuir(1, 7, 3)
print(matriz3.acessar(1, 7))
