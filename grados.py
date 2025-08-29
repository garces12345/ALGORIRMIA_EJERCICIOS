#indentificar los grados 
num=int(input("ingrese temperatura en °c:"))
#verificar gardos 
if num  <= 0:
    print(num,"°c - temperatura adecuada para congelacion")
else:
    print(num,"°C - temperatura no adecuada para congelacion")