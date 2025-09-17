#NOMBRE
#Verificar si un empleado recibe bono

#ENTRADA
#Ingresar el salario del usuario

#SALIDA
#Mostrar si recibe o no recibe bono

#PROCESO
#Calcula si recibe bono > 2000 o no recibe 
Bono = float(input("Ingrese su salario:"))
if Bono > 2000:
    print("Usted recibe bono.")
else:
    print("Usted no recibe bono.")