list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list1:
    if i % 2 == 0:
        print(f'{i} é par')
    else:
        print(f'{i} é impar')

city = ('salvador', ' rio de janeiro', 'são paulo')
ct = input('Digite uma cidade brasileira: ')

if ct in city:
    print('a cidade está na lista de cidades')
else:
    print('A cidade não esta na lista')

capital = {
    'brasil' : 'brasilia'
}
pais_usuario = input("Digite um pais: ")
if pais_usuario in capital:
    print(f'o pais {pais_usuario} te a capital {capital[pais_usuario]}')
else:
    print('pais e capital não localizados')