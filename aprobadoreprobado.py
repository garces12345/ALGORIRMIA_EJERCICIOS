#NOMBRE
#Verificar la nota aprobada y reprobada

#ENTRADA
#Nota ingresada por el usuario

#SALIDA
#Mostrar si Aprobó o Reprobó

#PROCESO
#Mostrar si la nota es aprobada  >= 60 o reprobada < 60

nota1 =int(input("Ingresa tu nota:"))
if nota1 >= 60:
    print("La nota es aprobada.")
elif nota1 < 60:
    print("la nota es reprobada.")