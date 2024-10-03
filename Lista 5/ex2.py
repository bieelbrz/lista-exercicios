def soma_dois_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"A soma dos números é: {resultado}\n")

def celsius_para_fahrenheit():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit} °F\n")

def verificar_par_ou_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.\n")
    else:
        print(f"O número {numero} é ímpar.\n")

def calcular_perimetro_retangulo():
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    perimetro = 2 * (largura + altura)
    print(f"O perímetro do retângulo é: {perimetro}\n")

def menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Calcular a soma de dois números")
        print("2 - Converter Celsius para Fahrenheit")
        print("3 - Verificar se um número é par ou ímpar")
        print("4 - Calcular o perímetro de um retângulo")
        print("5 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            soma_dois_numeros()
        elif opcao == '2':
            celsius_para_fahrenheit()
        elif opcao == '3':
            verificar_par_ou_impar()
        elif opcao == '4':
            calcular_perimetro_retangulo()
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

menu()
