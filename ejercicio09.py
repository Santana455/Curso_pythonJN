#Ejerccio
calificacion = int(input("Ingresa la calificacion entre (0-100): "))
if 90<=calificacion<=100:
    print(f"{calificacion} Calificacion A")
elif 80<=calificacion<90:
    print(f"{calificacion} Calificacion B ")  
elif 70<=calificacion<80:
    print(f"{calificacion} Calificacion C ")  
elif 60<=calificacion<70:
    print(f"{calificacion} Calificacion D ")  
else:
    print("Calificacion es F")
    