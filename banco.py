import contas
import pessoas
class Banco:
    def __init__(self, agencias: list[int] or None =None, clientes: list[pessoas.Pessoa] or None =None) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []



    def checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False


    def checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def autenticar(self, cliente, conta):
        if self.checa_agencia(conta) == False:
            print("Não foi possível fazer a transação. A agência não é compatível com o banco")
            return
        
        if self.checa_cliente(cliente) == False:
            print("Não foi possível fazer a transação. O cliente não possui conta no banco")

        if self.checa_conta(conta) == False:
            print("Não foi possível fazer a transação. A conta não é compatível com o banco")
        return True






