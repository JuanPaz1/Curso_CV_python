num = int(input('digite um número inteiro: '))
print('''escolha uma das bases para conversão
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para hexadeimal''')
opcao = int(input('sua opção:'))
if opcao == 1:
    print('{} convertido para Binario é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('erro!')