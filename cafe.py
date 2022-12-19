class Cafe:
    notasSensorias = []
    def __init__(self, fazenda, altitude):
        self.fazenda = fazenda
        self.altitude = altitude
    
    def notas(self, notasSensoriais):
        self.notas = notasSensoriais     
    
    def relatorios(self):
        print(f'fazenda {self.fazenda}')
        print(f'{self.altitude}m')        
        notas =  "Notas: "
        cont = 0
        for c in self.notas:
            if cont == 0:
                notas = notas + c
            else:
                if cont == len(self.notas)-1:
                    notas += ' ' + 'e ' + c
                else:
                    notas += ', ' + c
            cont += 1
        print(notas)

mundo = Cafe('mundo', 300)
mundo.notas(['morango', 'uva', 'maça'])
mundo.relatorios()
