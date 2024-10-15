#calculadora em python
print("\n********* Calculadora *******")
def adicao (x,y):
    return x + y
def subtracao(x,y):
    return x - y
def multiplicacao (x,y):
    return x * y
def divisao (x,y):
    return x/y
print("\n selecione a operacao:")
print("+ = soma")
print("- = subitracao")
print("* = multiplicacao")
print("/ = divisao")
escolha = input("\n sua escolha e: ")
if escolha == "+" or escolha =="-" or escolha=="*" or escolha=="/":

 num1 = int(input("digite o primeiro numero: "))
 num2 = int(input("digite o segundo numero: "))
 if escolha =="+":
    print("\n")
    print(num1,"+", num2, "=", adicao(num1, num2))
    print("\n")
 elif escolha == "-":
    print("\n")
    print(num1,"-", num2, "=", subtracao(num1, num2))
    print("\n")
 elif escolha =="*":
    print("\n")
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
    print("\n")
 elif escolha == "/":
    print("\n")
    print(num1, "/", num2, "=", divisao(num1, num2))
 else:
    print("\n")
else:
   print("\n opcao invalida")
     