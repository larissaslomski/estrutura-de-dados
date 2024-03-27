#  Larissa Slomski
from lista_duplamente_encadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()

print("Colocando primeiro elemento: Evair")
lista.inserirComoPrimeiro("Evair")
print("Colocando último elemento: Hipócrito")
lista.inserirComoUltimo("Hipócrito")
print("Colocando último elemento: Deusdete")
lista.inserirComoUltimo("Deusdete")
print("Colocando último elemento: Hipólito")
lista.inserirComoUltimo("Hipólito")
print("Avançando cursor pra primeira posição")
lista._irParaPrimeiro()
print(f"Imprimindo valor do cursor: {lista.cursor.dados}")
print(f"Primeiro: {lista.primeiro.dados}")
print("Excluindo primeiro")
lista.excluirPrim()
print(f"Primeiro após exclusão: {lista.primeiro.anterior}")
print(f"Valor do cursor após exclusão: {lista.cursor.dados}")
lista.listarElementos()
