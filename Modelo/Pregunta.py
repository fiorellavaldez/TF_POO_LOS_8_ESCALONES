from abc import ABC

class Pregunta(ABC):
    def __init__(self, tema, enunciado, idPregunta):
        self._idPregunta = idPregunta
        self._tema = tema
        self._enunciado = enunciado
    
    def get_enunciado (self):
        return self._enunciado
    
    def set_enunciado(self, enunciado):
        self._enunciado = enunciado