from application.model.entity.evento import Evento


class EventoDAO():
    __lista_eventos: list

    def __init__(self, lista_eventos):
        self.__lista_eventos = lista_eventos

    @property
    def lista_eventos(self):
        return self.__lista_eventos
    @lista_eventos.setter
    def lista_eventos(self, lista_eventos):
        self.__lista_eventos = lista_eventos