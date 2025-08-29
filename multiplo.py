#indentificar el multiplo
numero1=int(input("ingrese el primer numero:"))
numero2=int(input("ingrese el segundo numero:"))
#verificar si el numero1 es multiplo de numero2
if numero2 != 0:#evitamos divisiones entre cero
    if numero1 % numero2 == 0:
        print("el primer numero  es multiplo del segundo:")
    else:
         print("no es multiplo:")
else:
    print("no se puede dividir entre cero:")
