print("Bem vindo à calcubobbie!")
usuario = input("Qual é o seu nome?:  ")
print(F"Olá {usuario}, eu realizo algumas operações matemáticas. Como a adição(+), subtração(-), multiplicação(*) e a divisão(/).")
print("Se a caso você queira sair da calculadora, digite a palavra sair.")

while True:

    operacao = input("Escolha a operação da sua preferência: ")

    if operacao == 'sair':
                print("Encerrando a calculadora. Até depois!")
                break  # Sai do loop infinito

    if operacao in ['+', '-', '*', '/']:
            try:
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, digite números válidos.")
                continue # Volta para o início do loop
            
    if operacao == '+':
        resultado = numero1 + numero2
        print(f"{numero1} + {numero2} = {resultado}")

    elif operacao == '-':
        resultado = numero1 - numero2
        print(f"{numero1} - {numero2} = {resultado}")

    elif operacao == '*':
        resultado = numero1 * numero2
        print(f"{numero1} * {numero2} = {resultado}")

    elif operacao == '/':
        if numero2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = numero1 / numero2
            print(f"{numero1} / {numero2} = {resultado}")

    else:
            print("Operação inválida. Escolha + (adição), - (subtração), * (multiplicação) ou / (divisão).")