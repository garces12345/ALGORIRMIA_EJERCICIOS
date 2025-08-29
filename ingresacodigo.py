#indentificar un codigo 
codigo_admin = 1234 # codigo correcto
codigo=int(input("ingrese el codigo:"))
#verificar el codigo
if codigo == codigo_admin:
    print("acceso concedido.usuario administrador:")
else:
    print("acceso denegado. no tiene permiso de administrador:")