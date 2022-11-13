#classe que mostra a quantidade de acentos ocupados e livres de um onibus 
class Onibus:
    def __init__(self, acentos, numeracao):
        self.acentos = acentos
        self.numeracao = numeracao

    def ocuparAcentos(self, ocupar):
        acentos_livres = (self.acentos - ocupar)
        print(f'o onibus de númeração {self.numeracao} possui {acentos_livres} acentos livres') 
        print(f'o onubus de némeração {self.numeracao} está com {ocupar} acentos ocupados')
    
    def espaco(self):
        print('==========================================')

        
######################################## teste ############################################################################
busao = Onibus(20, 100)
busao.ocuparAcentos(4)

busao.espaco()

busao02 = Onibus(50, 200)
busao02.ocuparAcentos(20)
