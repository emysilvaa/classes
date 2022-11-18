class SistemaEstacionamento:
    def __init__(self, grande, medio, pequeno):
        self.grande = grande
        self.medio = medio
        self.pequeno = pequeno
    
    def addCarro(self, tipo_carro):
        if tipo_carro == 1 and self.grande > 0:
            return True
        elif tipo_carro == 1 and self.grande == 0:
            return False
        if tipo_carro == 2 and self.medio > 0:
            return True
        elif tipo_carro == 2 and self.medio == 0:
            return False
        if tipo_carro == 3 and self.pequeno > 0:
            return True
        elif tipo_carro == 3 and self.pequeno == 0:
            return False 
