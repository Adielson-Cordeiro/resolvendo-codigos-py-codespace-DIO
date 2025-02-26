n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja (+, -, *, /): ")


if operacao == '+':
   print (n1 + n2) 

elif operacao == '-':
   print (n1 - n2)

elif operacao == '*':
   print (n1 * n2)

elif operacao == '/':
   print (n1 / n2)

else:
   print ("Operação Invalida")