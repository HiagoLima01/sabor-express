from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    '''
    Classe que herda ItemCardapio para a representação de pratos no cardapio

    Atributos

    descricao:str       Descrição do produto    
    
    '''

    def __init__(self, nome, preco, descricao) -> None:
        super().__init__(nome,preco)
        self._descricao = descricao
    
    def __str__(self) -> str:
        return super().__str__()