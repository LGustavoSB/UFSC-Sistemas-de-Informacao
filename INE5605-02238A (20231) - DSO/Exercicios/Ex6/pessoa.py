from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    @abstractmethod
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
