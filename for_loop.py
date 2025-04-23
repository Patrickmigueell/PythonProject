list1 = ['maça', 'maça', 'maça', 'pera', 'uva']

for x in list1:
    print(f'eu goste de {x}')

print()

for i in range(1,11):
    if i > 5:
        break
    print(i)

print()

for i in range(1,11):
    if i == 5:
        continue
    print(i)

print()
contador = 0
for x in list1:
    if x == 'maça':
        contador += 1
print(contador)