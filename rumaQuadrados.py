class Quadrilatero:
    def __init__(self, b, h):
        self.base = b
        self.altura = h

    def area(self):
        area = self.base * self.altura
        print('Area:', area)

    def perimetro(self):
        p = self.base*2 + self.altura*2
        print('Perimetro:', p)

class Quadrado(Quadrilatero):
    def __init__(self, lado):
        super().__init__(lado, lado)
    
    def area(self):
        super().area()

    def perimetro(self):
        super().perimetro()

class Retangulo(Quadrilatero):
    def __init__(self, b, h):
        super().__init__(b, h)
    
    def area(self):
        super().area()

    def perimetro(self):
        super().perimetro()

class Trapezio(Quadrilatero):
    def __init__(self, b, B, h):
        self.B = B
        super().__init__(b, h)

    def area(self):
        area = ((self.B + self.base) * self.altura) / 2
        print('Area:', area)
    
    def perimetro(self):
        resto = (self.B - self.base)/2
        pitagoras = (resto**2 + self.altura**2)
        hipotenusa = pitagoras**0.5
        perimetro = ((hipotenusa * 2) + self.B + self.base)
        print(f'Perimetro: {perimetro:.2f}')


t = Trapezio(3, 5, 2)
t.area()
t.perimetro()


