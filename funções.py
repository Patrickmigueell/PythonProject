num = int(input('Digite um numero: '))

def quadrado(numero):
    return numero ** 2
print(f'o quadrado de {num} é {quadrado(num)}')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
def somatoria(numero,numero2):
    return numero + numero2
print(f'A soma de {num1} + {num2} é  {somatoria(num1,num2)}')

base = int(input('digite a base do numero: '))
exponete = int(input('Digite a exponenciação: '))

def calculo(num1,num2):
    if num2 <2:
        return num1 ** 2
    else:
        return num1 ** num2
print(f'o calculo da exponenciação é {calculo(base,exponete)}')