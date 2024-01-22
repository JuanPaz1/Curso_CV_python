import calendar

ano = int(input('qual o ano que você nasceu?'))
anot = calendar.datetime.datetime.now().year
c = anot - ano

if c <= 9 :
    print('mirim')
elif c > 9 and c <= 14:
    print('infantil')
elif c > 14 and c <= 19 :
    print('junior')
elif c > 20:
    print('master')
else:
    print('revisar')