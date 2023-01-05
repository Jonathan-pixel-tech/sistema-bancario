import banco, contas, pessoas

def criarCliente():
    print(60*"*")
    nome = input("Digite o seu nome completo: ")
    idade = int(input("Digite sua idade: ")) 
    senha = input("Crie uma senha: ")

    cliente = pessoas.Cliente(nome, idade, senha)
    bancoDev.clientes.append(cliente)
    print()
    print("Cliente criado com sucesso")
    print(60*"*")
 
def checarCliente(nome, senha):
    for cliente in bancoDev.clientes:
        if cliente.nome == nome:
            if senha == cliente.senha:  
                return cliente
    print("Não existe o cliente buscado. Verifique se não há erros ou faço seu cadastro caso não possua")
    return False

def criarContaCorrente(cliente):
    if cliente.contaCorrente != None:
        print("Você já possui uma conta corrente. é impossível criar duas")
        return
    numeroContaGerada = gerarNumeroConta()
    contaCorrenteCriada = contas.ContaCorrente(agencia="111", conta=numeroContaGerada, saldo=0, limite=300)
    cliente.contaCorrente = contaCorrenteCriada
    print(f"Sua conta corrente com número de conta {contaCorrenteCriada.conta} foi criada com sucesso ")

def criarContaPoupanca(cliente):
    if cliente.contaPoupanca != None:
        print("Você já possui uma conta poupança. é impossível criar duas")
        return
    numeroContaGerada = gerarNumeroConta()
    contaPoupancaCriada = contas.ContaPoupanca(agencia="111", conta=numeroContaGerada, saldo=0)
    cliente.contaPoupanca = contaPoupancaCriada
    print(f"Sua conta poupança com número de conta {contaPoupancaCriada.conta} foi criada com sucesso ")
    
def gerarNumeroConta():
    global numero_conta
    conta_valida = str(numero_conta)
    numero_conta += 1
    return conta_valida

def criarConta(cliente):
    print("Digite 1 para criar uma conta corrente \n" + 
            "Digite 2 para criar uma conta poupança")
    resposta = int(input())
    if resposta == 1:
        criarContaCorrente(cliente)
    elif resposta == 2:
        criarContaPoupanca(cliente)

def interageConta(contaEscolhida):
    print(f"Seu saldo atual é de {contaEscolhida.saldo} ")
    resposta = 0
    while(True):
        print("Digite 1 para para fazer depósitos \n" + 
              "Digite 2 para fazer saques \n" + 
              "Digite 3 para fechar as opções da conta")
        resposta = int(input())
        if(resposta == 3):
            return
        
        if resposta == 1:
            valor = float( input("Digite o valor que deseja depositar: ").replace(",", ".") ) 
            contaEscolhida.depositar(valor)
            

        if resposta == 2:
            valor = float( input("Digite o valor que deseja sacar: ").replace(",", ".") ) 
            contaEscolhida.sacar(valor)

           
def acessarConta(cliente):
    verificador = 0
    if cliente.contaCorrente == None:
        print("Você não possui conta corrente ainda!")
        verificador += 1
    else:
        print(f"Sua conta conta corrente é {cliente.contaCorrente.conta} Digite 1 para acessá-la")

    if cliente.contaPoupanca == None:
        print("Você não possui conta poupança ainda!")
        verificador += 1
    else:
        print(f"Sua conta conta poupança é {cliente.contaPoupanca.conta} Digite 2 para acessá-la")
    
    if verificador == 2:
        print("Crie uma conta para poder acessá-la")
        return
    
    resposta = int(input("Acesse uma conta ou digite 3 para sair "))
    if resposta == 3:
        return
    if resposta == 1:
        interageConta(cliente.contaCorrente)
    elif resposta == 2:
        interageConta(cliente.contaPoupanca)
    

def acessarOpcoes():
    print(60*"*")
    nome = input("Digite o seu nome: ").upper()
    senha = input("Digite a sua senha: ")

    if checarCliente(nome, senha) == False:
        return
    while(True):
        cliente = checarCliente(nome, senha)
        print(f"Bem vindo {cliente.nome}")
        print("Para acessar contas digite 1 \n" +
        "para criar uma conta digite 2 \n" + 
        "para finalizar as opções de cliente digite 3")
        resposta = int(input())
        if resposta == 3:
            return

        if resposta == 1:
            acessarConta(cliente)
        elif resposta == 2:
            criarConta(cliente)


    print(60*"*")

   

bancoDev = banco.Banco(agencias=['111', '222', '333', '444'], clientes=[])
numero_conta = 11111
print("Bem vindo ao BancoDEV")
print(100*"*")

resposta = 0
while(True):

    print('Digite 1 para acessar suas opções no banco caso já tenha cadastro \n' 
        + 'Digite 2 para se cadastrar no BancoDev e fazer parte dessa família \n' 
        + 'Digite 3 para finalizar opções \n')
    resposta = int(input()) 

    if resposta == 3:
        break

    if resposta == 1:
        acessarOpcoes()
    elif resposta == 2:
        criarCliente()
        
