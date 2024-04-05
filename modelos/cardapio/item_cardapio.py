class ItemCardapio:
    '''
    Classe para a criação de um modelo de item no cardápio

    Atributos

    Nome:Str        Nome do produto
    Preco:float     Peço do produto

    '''

    def __init__(self,nome, preco) -> None:
        self._nome = nome
        self._preco = preco

    def __str__(self) -> str:
        return self._nome