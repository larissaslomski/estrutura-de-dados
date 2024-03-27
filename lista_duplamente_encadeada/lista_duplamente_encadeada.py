#  Larissa Slomski
from no import No


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__cursor = None
        self.__tamanho = 0

    @property
    def primeiro(self):
        return self.__primeiro

    @property
    def ultimo(self):
        return self.__ultimo

    @property
    def cursor(self):
        return self.__cursor

    @property
    def tamanho(self):
        return self.__tamanho

    def _acessarAtual(self):
        if self.__cursor is not None:
            return self.__cursor.dados

    def inserirAposAtual(self, elemento):
        if self.__cursor is not None:
            no = No(elemento)
            if self.__cursor.proximo is not None:
                self.__cursor.proximo.anterior = no
                no.proximo = self.__cursor.proximo
            else:
                self.__ultimo = no
            no.anterior = self.__cursor
            self.__cursor.proximo = no
            self.__tamanho += 1

    def inserirAntesDoAtual(self, elemento):
        if self.__cursor is not None:
            node = No(elemento)
            if self.__cursor.anterior is not None:
                self.__cursor.anterior.proximo = node
                node.anterior = self.__cursor.anterior
            else:
                self.__primeiro = node
            node.proximo = self.__cursor
            self.__cursor.anterior = node
            self.__tamanho += 1

    def inserirNaPosicao(self, k, novo):
        if k < 1 or k >= self.__tamanho - 1:
            raise ValueError("Posição inválidan insira outro valor")
        elif k == 1:
            self.inserirAposAtual(novo)
        else:
            no = No(novo)
            atual = self.__cursor
            for i in range(1, k):
                atual = atual.proximo
            no.anterior = atual
            no.proximo = atual.proximo
            atual.proximo.anterior = no
            atual.proximo = no
            self.__tamanho += 1

    def inserirComoPrimeiro(self, elemento):
        no = No(elemento)
        if self.__primeiro is not None:
            self.__primeiro.anterior = no
            no.proximo = self.__primeiro
        else:
            self.__ultimo = no
        self.__primeiro = no
        self.__tamanho += 1

    def inserirComoUltimo(self, elemento):
        no = No(elemento)
        if self.__ultimo is not None:
            self.__ultimo.proximo = no
            no.anterior = self.__ultimo
        else:
            self.__primeiro = no
        self.__ultimo = no
        self.__tamanho += 1

    def _avancarKPosicoes(self, k):
        if not self.__cursor:
            return

        for i in range(k):
            if not self.__cursor.proximo:
                break
            self.__cursor = self.__cursor.proximo

    def _retrocederKPosicoes(self, k):
        if not self.__cursor:
            return

        for i in range(k):
            if not self.__cursor.anterior:
                break
            self.__cursor = self.__cursor.anterior

    def _irParaPrimeiro(self):
        self.__cursor = self.__primeiro

    def _irParaUltimo(self):
        self.__cursor = self.__ultimo

    def vazia(self):
        if self.__tamanho == 0:
            return True
        else:
            return False

    # MÉTODOS DE EXCLUSÃO
    def excluirAtual(self):
        if self.vazia():
            return

        if self.__primeiro is self.__ultimo:
            self.resetList()
            return

        if self.__cursor == self.__ultimo:
            self.excluirUlt()
            return

        if self.__cursor == self.__primeiro:
            self.excluirPrim()
            return

        if self.__cursor.proximo is not None and self.__cursor.anterior is not None:
            proximo = self.__cursor.proximo
            anterior = self.__cursor.anterior
            self.__cursor = self.__cursor.anterior
            self.__cursor.proximo = proximo
            self._avancarKPosicoes(1)
            self.__cursor.anterior = anterior
            self.__tamanho -= 1
            return

    def excluirPrim(self):
        if self.vazia():
            return

        if self.__primeiro is self.__ultimo:
            self.resetList()
            return
        else:
            if self.__cursor == self.__primeiro:
                self._avancarKPosicoes(1)
            self.__primeiro = self.__primeiro.proximo
            self.__primeiro.anterior = None
            self.__tamanho -= 1
            return

    def excluirUlt(self):
        if self.vazia():
            return

        if self.__ultimo is self.__primeiro:
            self.resetList()
            return

        else:
            if self.__cursor == self.__ultimo:
                self._retrocederKPosicoes(1)
            self.__ultimo = self.__ultimo.anterior
            self.__primeiro.anterior = None
            self.__tamanho -= 1
            return

    def excluirElem(self, chave):
        if chave is None or self.vazia():
            return

        cursor_atual = self.__cursor
        self._irParaPrimeiro()
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dados):
                self.excluirAtual()
                break
            self._avancarKPosicoes(1)

        self.__cursor = cursor_atual
        return

    def excluirDaPos(self, posicao):
        if 0 > posicao or posicao is None or self.vazia():
            return
        cursor_atual = self.__cursor
        self._irParaPrimeiro()
        if posicao <= (self.__tamanho - 1):
            self._avancarKPosicoes(posicao)
            self.excluirAtual()

        self.__cursor = cursor_atual
        return

    def buscarBool(self, chave):
        if chave is None or self.vazia():
            return False
        cursor_atual = self.__cursor
        self._irParaPrimeiro()
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dados):
                self.__cursor = cursor_atual
                return True
            self._avancarKPosicoes(1)

        self.__cursor = cursor_atual
        return False

    def buscar(self, chave):
        if chave is None or self.vazia():
            return False
        cursor_atual = self.__cursor
        self._irParaPrimeiro()
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dados):
                retorno = self.cursor.dados
                self.__cursor = cursor_atual
                return retorno
            self._avancarKPosicoes(1)
        self.__cursor = cursor_atual
        return None

    def buscarPosicao(self, chave):
        if (chave is None) or (self.vazia()):
            return
        cursor_atual = self.__cursor
        self._irParaPrimeiro()
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dados):
                self.__cursor = cursor_atual
                return i
            self._avancarKPosicoes(1)

        self.__cursor = cursor_atual
        return

    def resetList(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__cursor = None
        self.__tamanho = 0
        return

    def listarElementos(self):
        for i in range(self.tamanho):
            print(
                f"Elemento {i}: {self._acessarAtual()}, anterior: "
                f"{self.cursor.anterior.dados if self.cursor.anterior is not None else None}, próximo: "
                f"{self.cursor.proximo.dados if self.cursor.proximo is not None else None}")
            self._avancarKPosicoes(1)
        print()
        print(f"Quantidade de elementos na lista: {self.tamanho}")

