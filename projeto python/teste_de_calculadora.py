def numeros(): # numeros escolhidos
    n1 = float (input("escolha o primeiro número: "))
    n2 = float (input("escolha o segundo núnermo: "))
    return n1, n2

def escolha():
    n1, n2 = numeros() #captura de valores
    operação = input("Você gostaria de somar, multiplicar, dividir ou subtrair?  ")
    if operação == "somar":    # operação de soma
        resultado = n1 + n2
        print (f"O resultado da soma foi:{resultado}")

    elif operação == "multiplicar":    # operação de multiplicação
          resultado = n1 * n2
          print (f"O resultado da multiplicação foi:{resultado}")

    elif operação == "dividir":
         resultado = n1 / n2
         print(f"O resultado da divisão foi:{resultado}")
    
    elif operação == "subtrair":
         resultado = n1 - n2
         print(f"O resultado da subtração foi:{resultado}")
    else:
        print ("não foi possivel fazer a operação")


escolha()
