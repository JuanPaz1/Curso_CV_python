def escreva(palavra):
    print('-' * (len(palavra) + 4))
    print(f' {palavra}')
    print('-' * (len(palavra) + 4))

palavra = input('Digite algo: ')
escreva(palavra)
