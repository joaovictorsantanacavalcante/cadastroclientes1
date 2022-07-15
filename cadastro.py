class Cliente():
    def __init__(self, nomecli, datanascimento, cpf, email, endereço, divida):
        self.nome=nomecli
        self.datanascimento=datanascimento
        self.__cpf=cpf
        self.email=email
        self.__endereço=endereço
        self.__divida=divida

