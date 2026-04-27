login = input('Digite seu Login:')
senha = '1234'
senha_input = input('Digite sua senha:')
if login == 'Jonathas@gmail.com' and senha_input == senha:
    print('autenticação realizada com sucesso!')

elif login != login:
    print('Login errado, senha correta')
elif senha_input != senha:
    print('Senha errada, login correto')

else: login != login and senha_input != senha
print('credenciais inválidas!')
 