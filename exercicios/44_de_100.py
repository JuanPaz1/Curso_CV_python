n1 = float(input('qual o valor do produlto que quer pagar?'))
fp = str(input('qual forma de pagamento?')).upper()

if fp =='DINHEIRO' or fp == 'CHEQUE':
    print('voce tera que pagar R${} pois com o pagamento de {} voce tem 10% de desconto'.format(n1-(n1/100)*10, fp))
elif fp == 'CARTÃO' or fp == 'CREDITO' or fp == 'CARTAO':
    par = float(input('em quantas vezes no cartão voce quer fazer?')).__trunc__()
    if par == 0:
        print('vote tera que pagar R${} pois obteve 5% de desconto'.format(n1-((n1/100)*5)))
    elif par <= 2:
        print('o total que voce pagara sera R$ {} com as parcelas de R$ {}'.format(n1, n1/par))
    elif par >= 3:
        print('o total que voce pagara sera R$ {} com parcelas de R$ {}'.format(n1+(n1/100)*20, n1/par))
    else:
        print('erro cartão')
else:
    print('erro def')

