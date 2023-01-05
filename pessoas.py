import contas
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        nome = nome.upper()
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        if idade < 18:
            print("Atenção, é altamente recomendável a criação de contas somente por maiores de idade")
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r} )'
        return f' {class_name}{attrs} '

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, senha: str, contaCorrente: contas.ContaCorrente or None =None, contaPoupanca: contas.ContaPoupanca or None = None) -> None:
        super().__init__(nome, idade)
        self.senha = senha
        self.contaCorrente = contaCorrente 
        self.contaPoupanca = contaPoupanca 

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha: int):
        self._senha = senha
    



if __name__ == '__main__':
    cliente = Cliente("João", 55, 7889)
   # print(cliente.nome)
    print(cliente.idade)
    cliente.idade = 80
    print(cliente.idade)
    cliente.senha