# Leitura do número
dia_numero = int(input("Digite um número (1 a 7) correspondente ao dia da semana: "))

match dia_numero:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido. Digite um número entre 1 e 7.")
