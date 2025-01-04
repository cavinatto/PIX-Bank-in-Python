class Pix:
    def __init__(self, remetente:str, destinatario:str, valor:float):
        self.__remetente = remetente
        self.__destinatario = destinatario
        self.__valor = valor

    def executar(self):
        if self.__remetente.get_saldo() >= self.__valor:
            self.__remetente.retirar(self.__valor)
            self.__destinatario.depositar(self.__valor)
            self.__remetente.registrar_transacao(self)
            self.__destinatario.registrar_transacao(self)
        else:
            print("Saldo insuficiente para realizar a transferência.")

    def exibir_informacoes(self):
        print(f"Remetente: {self.__remetente.get_cpf()}")
        print(f"Destinatário: {self.__destinatario.get_cpf()}")
        print(f"Valor: R${self.__valor:.1f}")