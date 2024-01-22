def maior (* numero):
     print(f'o maior valor da listagem foi {max(lista)} e foram informados {len(lista)} valores')


lista = list()
while True:
    valor = int(input('digite um valor:'))
    lista.append(valor)
    vl = str(input('DESEJA CONTINUAR? [S/N]')).upper()
    if vl != 'S':
        break
maior(lista)
