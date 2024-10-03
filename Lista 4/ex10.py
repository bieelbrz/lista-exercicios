# Leitura dos dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1

resultado = (menor * 10) + (maior / 2)

if resultado % 2 == 0:
    print(f"O resultado é {resultado:.2f} e é par.")
else:
    print(f"O resultado é {resultado:.2f} e é ímpar.")
