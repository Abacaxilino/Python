#Dissecando uma variável
a = input ('digite algo:')
print ('qual o valor primitivo desse valor?', type(a))
print('é alfabético?', a.isalpha())
print('é numérico?', a.isnumeric())
print('é alfanumérico?', a.isalnum())
print('é letra, número ou simbolo?', a.isascii())
print('é decimal?', a.isdecimal())
print('está em minúsculo?', a.islower())
print('está em maiúsculo?', a.isupper())
print('está em maiúsculo e minúsculo?', a.istitle())
print('é espaço?', a.isspace())

print('programa finalizado.')
