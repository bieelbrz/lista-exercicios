num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    num1 += 10
    num2 += 5
else: 
    num1 += 5
    num2+= 10

if num1 > num2:
    print(f"O maior número após as somas é: {num1}")
else: 
    print(f"O maior número após as somas é: {num2}")
