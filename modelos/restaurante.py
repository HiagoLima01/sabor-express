from modelos.avaliacao import Avaliacao
from cardapio.item_cardapio import ItemCardapio

class Restaurante:
    '''
    Classe para a representação de um restaurante no aplicativo

    Atributos

    nome:str            Nome do restaurante       
    categoria:str       Categoria do restaurante
    ativo:boolean       Define se um restaurante está ativo ou não
    avaliacao:list      Lista de avaliações do restaurante
    cardapio:list       Lista de itens do cardapio do restaurante
    restaurantes:list   Se adiciona na lista de restaurantes presentes no app


    Métodos

    listar_restaurantes(cls)
        Lista todos restaurantes presentes no app

    alternar_estado(self)
        Alterna o estado do restaurante entre ativo e inativo

    
    '''


    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''
        Printa todos restaurantes presentes no app

        Para cada restaurante presentente em restaurantes[] ele executa o loop

        Parâmetros

        cls:Class   A Própria classe restaurantes 
        
        '''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        '''
        Alterna o estado do restaurante entre ativo e inativo

        Parâmetros

        self:Obj   O próprio Restaurante
        
        '''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''
        Regitra uma avaliação na lista de avaliações

        A avaliação deve ser maior que 0 e menor ou igual a 5 senão ela não é registrada

        Esse método instancia um objeto da classe Avaliação para registrar nome e nota do cliente

        Parâmetros

        self:Obj      O próprio Restaurante
        cliente:str   Nome do cliente vindo da instancia de avaliação
        nota:float    Nota do cliente vindo da instancia de avaliação     
        
        '''
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        '''
        Adiciona um novo item no cardapio do restaurante

        Checa se o parametro item realmente é um objeto da classe ItemCardapio

        
        
        '''


        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)