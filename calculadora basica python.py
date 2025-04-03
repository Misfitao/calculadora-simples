
operacao = input("escolha sua operação ? '+, -, *, ou /' ou digite sair para encerrar ").lower()

while operacao != "sair":
    if operacao == "+":
        print("você escolheu adição")
    elif operacao == "-":
        print("você escolheu subtração")
    elif operacao == "*":
        print("você escolheu multiplicação")
    elif operacao == "/":
        print("você escolheu divisão")
    else:
        print("comando invalido")


    numero1 = int(input("digite o seu numero: "))
    numero2 = int(input("digite o seu numero: "))

    if operacao == "+":
        resultado = numero1 +numero2
    elif operacao == "-":
        resultado = numero1 -numero2
    elif operacao == "*":
        resultado = numero1 *numero2
    elif operacao == "/":
        resultado = numero1 /numero2
    else:
        resultado = print("comando invalido ? ")
    print(f"o resultado é {resultado}")
        
    operacao = input("qual operação você gostaria ? +, -, *, ou / ? digite sair para encerrar ").lower()
