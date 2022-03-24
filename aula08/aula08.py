import fileinput
contador = 1
while contador <= 5:
    print('Hey joe')
    contador = contador+1

a = 0
for nome in fileinput.input('/Users/guilhermetourinho/Downloads/CTD_2021-2023/3B_infraestrutura1/aula08/lista_nomes.txt'):
    if nome.strip() == 'Marcel':
        print('Encontrei o Marcel')
    else:
        a += 1

print('Encontrei outros', a, 'nomes.')
