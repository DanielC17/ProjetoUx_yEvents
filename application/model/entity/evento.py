class Evento():
    __nome: str
    __local: str
    __data: str
    __hora: str

    def __init__(self, nome, local, data, hora, imagem):
        self.__nome = nome
        self.__local = local
        self.__data = data
        self.__hora = hora
        self.__imagem = imagem

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def local(self):
        return self.__local
    @local.setter
    def local(self, local):
        self.__local = local

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def hora(self):
        return self.__hora
    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @property
    def imagem(self):
        return self.__imagem
    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem