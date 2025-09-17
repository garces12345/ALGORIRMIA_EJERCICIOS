#NOMBRE
#Verificar descuento transporte

#ENTRADA
#Edad ingresada por el usuario

#SALIDA
#Verificar si tiene descuento o no tiene

#PROCESO
#Calcular  la edad y verificar  si tiene descuento o no tiene
Edad = int(input("Ingrese su edad:"))
if Edad < 12 or Edad > 60:
  print("Usted tiene descuento")
else:
  print("Usted no tiene descuento")