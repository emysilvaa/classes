class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        print('Hello, my dear', self.nome)

class Aluno(Pessoa):
    def __init__(self, nome, curso):
        self.curso = curso
        super().__init__(nome)

    def saudacao(self):
        super().saudacao()
        print("E faço o curso de ", self.curso)


pedro = Aluno('Pedro', 'Informática')
pedro.saudacao()