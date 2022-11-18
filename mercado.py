class Mercado:
    caixas = []
    clientes = []
    estoque = []
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


class Item:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def addEstoque(self, mercado):
        mercado.estoque.append(self.produto)
        

class Cliente:
    carrinho = []
    total_preco = 0.0

    def __init__(self, nome):
        self.nome = nome
    
    def serAtendido(self, mercado, caixas):
        print(f'o cliente {self.nome} está sendo atendido pelo caixa: {mercado.caixas[caixas].nome}(caixa {mercado.caixas[caixas].numero})')

    def addCarro(self, item, preco):
        self.total_preco += preco
        self.carrinho.append(item)
        print(f'@ cliente {self.nome} está adicionando {item} em seu carrinho.')

class Caixa:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def atender(self, mercado, clientes):
        print(f'@ caixa {self.nome} está atendendo o cliente {mercado.clientes[clientes].nome}')
    

    def passarCompras(self, mercado, clientes):
        print(f'O valor final da compra do cliente {mercado.clientes[clientes].nome} foi {mercado.clientes[clientes].total_preco}.')
