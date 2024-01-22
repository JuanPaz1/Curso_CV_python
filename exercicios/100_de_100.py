import random

def sorteio():
    for c in range(0, 5 + 1):
        n = random.randint(1, 6)
        print(n)
        lista.append(n)

def somapar():
    global totpar  # Declare a variável totpar como global
    for c in lista:
        if c % 2 == 0:
            totpar += c
    print(f'A soma de todos os valores pares na lista é {totpar}')

# Inicializando variáveis
totpar = 0
lista = list()

# Chamando as funções
sorteio()
somapar()
