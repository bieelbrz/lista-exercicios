def celsius_para_kelvin(celsius):
    return celsius + 273.15

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    print("Escolha a conversão:")
    print("1 - Converter para Kelvin")
    print("2 - Converter para Fahrenheit")
    escolha = input("Digite sua escolha (1 ou 2): ")

    if escolha == '1':
        kelvin = celsius_para_kelvin(celsius)
        print(f"A temperatura em Kelvin é: {kelvin:.2f} K")
    elif escolha == '2':
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")
    else:
        print("Escolha inválida. Tente novamente.")

    continuar = input("Deseja calcular outra temperatura? (S/N): ").upper()

    if continuar != 'S':
        print("Encerrando o programa...")
        break
