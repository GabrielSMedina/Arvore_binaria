import tkinter as tk

# Classes
class Node():  # Nó que conterá o valor e as Refs
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore():  # Estrutura da arvore
    def __init__(self):
        self.raiz = None
        #self.raiz = Node(10)

    def inserir(self, valor):
        if self.raiz:
            self._inserir(valor, self.raiz)
        else:
            self.raiz = Node(valor)

    def _inserir(self, valor, node):  # Funcao recursiva(privada)
        if valor < node.valor:
            if node.esquerda is None:
                node.esquerda = Node(valor)
            else:
                self._inserir(valor, node.esquerda)
        else:
            if node.direita is None:
                node.direita = Node(valor)
            else:
                self._inserir(valor, node.direita)


    def imprime_arvore(self):
        if self.raiz.valor:
            valores = [(1 ,self.raiz.valor)]
            if self.raiz.esquerda or self.raiz.direita:
                self._layer(self.raiz, 2, valores)
            print(valores)
        else:
            print('Arvore vazia!')

    def _layer(self, node, profundidade, lista):

        if node.esquerda:
            lista.append((profundidade, node.esquerda.valor))
            self._layer(node.esquerda ,profundidade+1, lista)
        if node.direita:
            lista.append((profundidade, node.direita.valor))
            self._layer(node.direita, profundidade + 1, lista)


# Execucao
def teste():
    arvore = Arvore()
    arvore.inserir(5)
    arvore.inserir(8)
    arvore.inserir(-5)
    arvore.inserir(65)
    arvore.inserir(12)
    arvore.inserir(7)
    arvore.inserir(9)
    arvore.inserir(58)


    arvore.imprime_arvore()

teste()
