kg = float(input('qual o seu peso?')).__trunc__()
alt = float(input('qual sua altura?'))

imc = kg / (alt**2)

if imc < 18.5 :
    print('abaixo do peso')
elif imc >=18.5 and imc < 25 :
    print('peso ideal')
elif imc >= 25 and imc < 30 :
    print('sobrepeso')
elif imc >= 30 and imc < 40:
    print('obesidade')
elif imc > 40:
    print('obesidade morbida')
else:
    print('erro script')
