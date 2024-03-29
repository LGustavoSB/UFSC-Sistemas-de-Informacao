from abc import abstractmethod
from abc import ABC
from usuario_bu import UsuarioBU


class Funcionario(UsuarioBU, ABC): 
    @abstractmethod
    def __init__(self,departamento: str, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    def emprestar(self, titulo_livro: str):
        return f'do departamento "{self.departamento}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'

    def devolver(self, titulo_livro: str):
        return f'do departamento "{self.departamento}" devolveu o livro: {titulo_livro}'
