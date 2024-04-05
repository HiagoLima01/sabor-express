from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    '''
    Classe que herda ItemCardapio para a representação de bebidas no cardapio

    Atributos

    tamanho:str       Tamanho do produto
    
    '''


    def __init__(self, nome, preco, tamanho) -> None:
        super().__init__(nome,preco)
        self._tamanho = tamanho