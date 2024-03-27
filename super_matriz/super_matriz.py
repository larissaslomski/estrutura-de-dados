from super_array import SuperArray


class SuperMatriz:
    def __init__(self, linhas, colunas):
        self.__matriz = []
        self.__linhas = linhas
        self.__colunas = colunas
        contador = 1
        while contador <= self.__linhas:
            super_array = SuperArray(0, self.__colunas - 1)
            self.__matriz.append(super_array)
            contador += 1

    def atribuir(self, linha, coluna, valor):
        indice_linha = linha - 1
        indice_coluna = coluna - 1
        if not isinstance(indice_linha, int) or not isinstance(indice_coluna, int):
            raise TypeError
        if indice_linha > self.__linhas or indice_linha < 0:
            if indice_coluna > self.__colunas or indice_coluna < 0:
                raise IndexError
        else:
            super_array = self.__matriz
            linha_matriz = super_array[indice_linha].dados
            linha_matriz[indice_coluna] = valor

    def acessar(self, linha, coluna):
        indice_linha = linha - 1
        indice_coluna = coluna - 1
        if not isinstance(indice_linha, int) or not isinstance(indice_coluna, int):
            raise TypeError
        if indice_linha > self.__linhas or indice_linha < 0:
            if indice_coluna > self.__colunas or indice_coluna < 0:
                raise IndexError
        else:
            super_array = self.__matriz
            linha_matriz = super_array[indice_linha].dados
            return linha_matriz[indice_coluna]


    @property
    def matriz(self):
        return self.__matriz

    @property
    def colunas(self):
        return self.__colunas

    @property
    def linhas(self):
        return self.__linhas
