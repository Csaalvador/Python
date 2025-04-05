print("Digite o numero correspondente a operação...")
operacao = int(input("1: Adição, 2: Subtração, 3: Multiplicação, 3: Divisão: "))
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

def switch(operacao, x, y):
    if(operacao == 1):
        return x + y

    elif(operacao == 2):
         return x - y
    
    elif(operacao == 3):
        return x * y
    
    elif(operacao == 1):
        return x / y
    
    else :
        return "Error"
    
resultado = switch(operacao, n1, n2)
print(resultado)