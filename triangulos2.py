#triangulos
lado1=float(input("ingrese el primer lado del triangulo:"))
lado2=float(input("ingrese el segundo lado del triangulo:"))
lado3=float(input("ingrese el tercer lado del triangulo:"))
#verificar los lados de los triangulos 
if lado1 == lado2 == lado3:
    print("el triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("el triangulo es isosceles")
else:
    print("el triangulo es escaleno")

