vcasa = float(input('qual o valor da casa que você quer comprar?')).__trunc__()
vsal = float(input('qual o seu salario?'))
vano = float(input('em quanto anos você vai pagar a sua casa?')).__trunc__()
vlpar = vcasa / (vano*12)
cofsal = (vsal/100)*30

if cofsal >= vlpar:
    print('emprestimos aprovado o valor da sua parcela é R${:.2f}'.format(vlpar))
else:
    print('emprestimos negado')
