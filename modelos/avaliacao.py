class Avaliacao:
    '''
    Classe para a representação de uma avaliação do restaurante

    Atributos

    cliente:str       nome do cliente que fez a avaliação
    nota:float        nota que o cliente deu para o restaurante    
    
    '''


    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota