# Classes
class Node():  # Nó que conterá o valor e as Refs
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class Arvore():  # Estrutura da arvore
    def __init__(self):
        self.raiz = None

    # Função publica para insercao de valores na arvore
    def inserir(self, valor):
        if self.raiz:  # Arvore existe
            self._inserir(valor, self.raiz)
        else:
            self.raiz = Node(valor)

    # Funcao recursiva de insercao de valor
    def _inserir(self, valor, node):  # Funcao recursiva(privada)
        if valor < node.valor:  # Verifica se alocara valor a esquerda
            if not node.esquerda:
                node.esquerda = Node(valor)
            else:
                self._inserir(valor, node.esquerda)
        else:  # Alocara valor a direita
            if not node.direita:
                node.direita = Node(valor)
            else:
                self._inserir(valor, node.direita)

    # Funcao publica de busca, retorno booleano
    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    # Funcao recursiva de busca de valor
    def _buscar(self, valor, node):
        if not node:
            return False

        elif node.valor == valor:
            return True

        elif node.valor > valor:
            return self._buscar(valor, node.esquerda)

        else:
            return self._buscar(valor, node.direita)

    # Funcao publica de deletar
    def deletar(self, valor):
        self.raiz = self._deletar(valor, self.raiz)

    # Funcao recursiva para percorrer e deletar
    def _deletar(self, valor, node):
        if not node:
            return node
        elif valor < node.valor:  # Verifica se continuara a busca pela esquerda
            node.esquerda = self._deletar(valor, node.esquerda)
            return node
        elif valor > node.valor:  # Verifica se continuara a busca pela direita
            node.direita = self._deletar(valor, node.direita)
            return node
        else:
            if not node.esquerda:  # valor nao encontrado
                return node.direita
            elif not node.direita:  # valor nao encontrado
                return node.esquerda
            else:
                min_node = self._busca_min(node.direita)
                node.valor = min_node.valor
                node.direita = self._deletar(min_node.valor, node.direita)
                return node

    # Funcao de busca do valor minimo
    def _busca_min(self, node):
        while node.esquerda:  # Caso de erro adiciona 'is not None' e teste
            node = node.esquerda
        return node

    # Impressao dos dados contidos na arvore e sua profundidade
    def imprime_arvore(self):
        if self.raiz.valor:  # Verificacao de existencia de valores na arvore
            valores = [(1, self.raiz.valor)]  # Listca contendo profundidade do valor na arvore e valor
            if self.raiz.esquerda or self.raiz.direita:
                self._layer(self.raiz, 2, valores)
            print(valores)
        else:
            print('Arvore vazia!')

    # Funcao recursiva que percorre a arvore e salva informacoes para impressao
    def _layer(self, node, profundidade, lista):  # Privado
        if node.esquerda:
            # Adiciona valores em uma lista contendo a profundidade na raiz e o valor
            lista.append((profundidade, node.esquerda.valor))
            self._layer(node.esquerda, profundidade + 1, lista)
        if node.direita:
            # Adiciona valores em uma lista contendo a profundidade na raiz e o valor
            lista.append((profundidade, node.direita.valor))
            self._layer(node.direita, profundidade + 1, lista)
