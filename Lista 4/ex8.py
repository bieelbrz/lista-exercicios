num = int(input("Digite um número: "))

if num > 10:
    num += 5
else: 
    num += 20

if num > 25:
    print(f"O resultado {num} é maior que 25.")
else:
    print(f"O resultado {num} não é maior que 25.")