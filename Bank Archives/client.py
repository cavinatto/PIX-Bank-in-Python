from pix import Pix

class Cliente:
    def __init__(self, nome:str, cpf:str, saldo:float):
        self.nome = nome  # Atributo público
        self.__cpf = cpf
        self.__saldo = saldo
        self.__extrato = []

    def get_saldo(self):
        return self.__saldo

    def get_extrato(self):
        return self.__extrato

    def get_cpf(self):
        cpf_oculto = f"{self.__cpf[:3]}.xxx.xxx-{self.__cpf[-2:]}"
        return cpf_oculto

    def depositar(self, valor):
        self.__saldo += valor

    def retirar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente para realizar a retirada.")

    def realizar_pix(self, valor, destinatario):
        transacao_pix = Pix(self, destinatario, valor)
        transacao_pix.executar()

    def registrar_transacao(self, transacao):
        self.__extrato.append(transacao)
