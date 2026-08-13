#Actividad 2: Control de flujo - Clasificación de Estudiantes
#Usar bucles y condiciones para clasificar edades y buscar nombres en una lista de estudiantes.


#Parte 1: Bucle for con edades
#   Crea una lista de edades: [12, 17, 8, 15, 22, 9, 30, 25].

edades = [12, 17, 8, 15, 22, 9, 30, 25]

#Usa un bucle for para iterar sobre cada edad:
  #Si la edad es 25, imprime "¡Encontramos al estudiante de 25 años! Deteniendo el análisis." y termina el bucle con break.
  #Si la edad es menor a 10, omite esa iteración con continue.
  #Si la edad es 18 o mayor, imprime "Adulto: [edad] años".
  # #En cualquier otro caso, imprime "Menor: [edad] años".

for edades in edades:
    if edades == 25:
        print("¡Encontramos al estudiante de 25 años!")
        break
    elif edades < 10:
        continue
    elif edades >= 18:
        print(f"Adulto: {edades} años")
    else:
        print(f"Menor: {edades} años")
print("--------------------------------------------")


#Parte 2: Bucle while con nombres
# 1. Crea una lista de nombres: ["Juan", "Pedro", "Jorge", "María","Ana"].

nombres = ["Juan", "Pedro", "Jorge", "María","Ana"]

# 2. Usa un bucle while para iterar sobre los nombres:
#   Si el nombre es "Ana", imprime "¡Ana está en la lista!" y termina el bucle con break.
#   Si el nombre empieza con "J", omite ese nombre con continue.
#   En cualquier otro caso, imprime el nombre.¨

index = 0

while index < len(nombres):
    nombre = nombres[index]

    if nombre == "Ana":
        print("¡Ana está en la lista!")
        break

    elif nombre.startswith("J"):
        index += 1
        continue

    else:
        print(nombre)

    index += 1
