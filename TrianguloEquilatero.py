#NOMBRE
#Verificar  el tipo de triangulo que es

#ENTRADA
#Tres números ingresados por el usuario

#SALIDA
#Mostrar  si el triangulo es equlatero,escaleno o isosceles 

#PROCESO
#Comprobar si el triangulo es equilatero, escaleno o isosceles

lado1 = float(input("Ingresa un numero:"))
lado2 = float(input("Ingresa el segundo numero:"))
lado3 = float(input("Ingresa el tercer numero:"))


if lado1 == lado2 and lado2 == lado3:
  print("El triangulo es EQUILATERO.")
elif lado1 == lado2 and lado2 != lado3:
  print("El triangulo es ISOSCELES.")
else:
  print("El triangulo es ESCALENO.")