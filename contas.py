from abc import ABC, abstractclassmethod
class ContaBancaria(ABC):
    def __init__(self, agencia: str, conta: str, saldo: float =0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractclassmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'DEPÓSITO {valor}')

    def detalhes(self, msg: str) -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print(20*"_")

        def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r} )'
            return f'{class_name}{attrs}'


class ContaPoupanca(ContaBancaria):

    def sacar(self, valor) -> float:
        if(self.saldo >= valor):
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor:.2f} ')
            return self.saldo

        print('Não foi possível sacar o valor desejado. O seu saldo é insuficiente')
        self.detalhes(f'SAQUE NEGADO {valor}')
        return self.saldo

class ContaCorrente(ContaBancaria):
    def __init__(self, agencia, conta, saldo=0, limite=50):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor) -> float:
        if(valor > (self.saldo + self.limite)):
            print(f'Não foi possível sacar o valor desejado. O seu saldo é insuficiente')
            self.detalhes(f'SAQUE NEGADO {valor}')
            return self.saldo
        self.saldo -= valor
        self.detalhes(f'SAQUE {valor:.2f} ')
        return self.saldo
    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r} )'
            return f' {class_name}{attrs}'
        


