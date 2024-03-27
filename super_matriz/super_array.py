class SuperArray:
    def __init__(self, inicio, fim):
        if fim < inicio:
            self.__limite_inferior = fim
            self.__limite_superior = inicio
        else:
            self.__limite_inferior = inicio
            self.__limite_superior = fim
        self.__dados = [None] * (self.__limite_superior - self.__limite_inferior + 1)

    def atribuir(self, posicao, valor):
        if posicao > self.__limite_superior or posicao < self.__limite_inferior:
            raise IndexError
        else:
            self.__dados[posicao - self.__limite_inferior] = valor

    def acessar(self, posicao):
        if posicao > self.__limite_superior or posicao < self.__limite_inferior:
            raise IndexError
        else:
            return self.__dados[posicao - self.__limite_inferior]

    @property
    def limite_inferior(self):
        return self.__limite_inferior

    @property
    def limite_superior(self):
        return self.__limite_superior

    @property
    def dados(self):
        return self.__dados

    @limite_superior.setter
    def limite_superior(self, limite_superior):
        self.__limite_superior = limite_superior

    @limite_inferior.setter
    def limite_inferior(self, limite_inferior):
        self.__limite_inferior = limite_inferior


