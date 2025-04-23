
list1 = [ 'maça', 'banana', 'manga', 'uva']

list1[1:2] = ['morango']
list1.append('abacaxi')
list1.insert(0, 'amora')
list1.remove('manga')
del list1[-1]
print(list1)

car = ['bmw', 'chevrolet', 'uno']
modelo = input('Qual modelo quer consultar: ').lower()

if modelo in car :
    print('Tem em estoque')
else:
    print('Não ha estoque')

list1 = {'elisangela', 'lucas', 'daniel', 'samara', 'marcelo'}
list2 = {'elisangela', 'lucas', 'daniel'}

print()

result = list1.intersection(list2)
result2 = list1.union(list2)
result3 = list1.difference(list2)

print(result)
print(result2)
print(result3)

print()