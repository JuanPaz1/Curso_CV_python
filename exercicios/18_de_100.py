import math

an = float(input('digite o angulo que você que: '))

seno=math.sin(math.radians(an))
cose=math.cos(math.radians(an))
tan=math.tan(math.radians(an))

print('o angulo de {} tem o SENO de {:.2f} e COSSENO de {:.2f} e TANGENTE {:.2f}'.format(an, seno, cose, tan))
