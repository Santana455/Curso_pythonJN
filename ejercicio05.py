#Escribe un programa que solicite al usuario dos numero y muestre
#suma, resta, multiplicacion, division, division entera y residuo (modulo)
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
#suma
suma = num1 + num2
#resta
resta = num1 - num2
#multiplicacion
multiplicacion = num1 * num2
#Division
division = num1/num2 if num2!=0 else "No se puede ejecutar"
#Division entera
division_entera = num1//num2 if num2!=0 else "No se puede dividir por 0"
#Residuo 
residuo = num1%num2 if num2!=0 else "No se puede calcular el residuo con 0"
print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"division: {division}")
print(f"dicision_entresa: {division_entera}")
print(f"residuo: {residuo}")
