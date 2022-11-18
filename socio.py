class Socio:
    def __init__(self, nome, cpf, rg, nascimento, telefone, endereco):
        self.nome = nome
        self.cpf = cpf 
        self.rg = rg 
        self.nascimento = nascimento
        self.telelfone = telefone
        self.endereco = endereco

    def cadastro(self, nome, senha):
        self.nome = nome
        self.senha = senha
        
    def confimarCadastro(self, nome, senha):
        if self.nome == nome and self.senha == senha:
            print(f'Parabens {self.nome} seu cadastro está válido! ')
        else:
            print('Cadastro inválido!!')

    def alterar(self, novaSenha ):
        self.senha = novaSenha

        
        
        

  

thiago = Socio('Thiago', '1111', '2222', '30/08/2005', '9911863', 'rua bahia 608')
thiago.cadastro('Thiago', '12345')
thiago.confimarCadastro('Thiago', '12345')
thiago.alterar('1234')
print(thiago.senha)