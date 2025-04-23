print()
print('=== calculador de imc ==='.upper())
print()
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura /100)** 2

if imc < 18.5:
    print()
    print('Magro'.upper())
elif imc >= 18.5 and imc <= 24.9:
    print()
    print('normal'.upper())
elif imc >= 25 and imc <= 29.9:
    print()
    print('sobrepeso'.upper())
elif imc >= 30 and imc <= 39.9:
    print()
    print('obesidade'.upper())
else:
    print()
    print('obesidade grave'.upper())