import Arvore


class Teste_arvore():  # Classe de testes
    def __init__(self):
        self.arvore = Arvore.Arvore()

    def teste_inserir(self):  # Teste da funcao de inserir e de buscar
        self.arvore.inserir(5)

        if self.arvore.buscar(5):
            print('Teste inserir: Passou!')
            print('Teste buscar: Passou!')
        else:
            print('Teste inserir: Reprovou!')
            print('Teste buscar: Reprovou!')

    def teste_deletar(self):  # Teste da funcao deletar
        self.arvore.inserir(8)

        if self.arvore.buscar(8):
            self.arvore.deletar(8)
            if not self.arvore.buscar(8):
                print('Teste deletar: Passou!')
            else:
                print('Teste deletar: Reprovou!')


# Execucao

teste = Teste_arvore()
teste.teste_inserir()
teste.teste_deletar()
