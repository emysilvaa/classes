from logging import exception


class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        lista_planos = ['basic', 'premium']
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception('plano inválido.')

cliente = Cliente('emilly', 'emilly.e@escolar.ifrn.edu.br' , 'basic')
print(f'o seu úsario é: {cliente.nome}')
print(f'seu plano atual é: {cliente.plano}')
