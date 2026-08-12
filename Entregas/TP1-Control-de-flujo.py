#1. Registro de estudiantes: crea una lista de estudiantes. 
# Cada elemento de la lista debe ser una tupla con la siguiente estructura:
# (nombre, edad, nota) min 8 estudiantes.

estudiantes = [
    ("Ana Martínez", 18, 4.5),
    ("Carlos Rodríguez", 20, 3.8),
    ("Laura Gómez", 19, 4.2),
    ("David Pérez", 21, 3.5),
    ("Sofía Hernández", 18, 4.8),
    ("Andrés López", 22, 3.9),
    ("Valentina Torres", 20, 4.6),
    ("Mateo Ramírez", 19, 3.7)
]

#2. Mostrar la informacion: Utiliza un ciclo FOR para recorrer la lista e
# imprimir la informacion de cada estudiante en un formato similar al siguiente
# Ana tiene 20 anos y obtuvo una nota de 4.5

for nombre, edad, nota in estudiantes:
    print(f"{nombre} tiene {edad} años y obtuvo una nota de {nota}")


#3. Clasificacion de estudiantes: utilizando if, elif y else, clasifica a cada estudiante segun su nota
print("\nEmpezando clasificacion de notas......\n")

for nombre, edad, nota  in estudiantes:
    nota = float(nota)

    if nota >= 4.5:
        print(f"Estudiante {nombre} tiene una nota de {nota} Excelente")
    elif 3.0 <= nota <= 3.9:
        print(f"Estudiante {nombre} tiene una nota de {nota} Aceptable")
    elif  3.0 <= nota:
        print(f"Estudiante {nombre} tiene una nota de {nota} Reprobo")
    else:
        print(f"Estudiante {nombre} tiene una nota de {nota} Excelente")    

#4. Promedio general: calcula el promedio de todas las notas utilizando un ciclo y una varaibles acumuladora
# al final imprimir el promedio optenido
print("\nCalculando promedio general......\n")

total = 0

for nombre, edad, nota  in estudiantes:
    total += nota 

cant = len(estudiantes)
promedio = total / cant 

print(f"El promedio general es: {promedio} \n")

#5. Solicitar al usuario el nombre del estudiante mediante input()
# si el estudiante existe en la lista, imprime un mensaje indicando que fue encontrado
# SI no existe, informa que no se encontro ningun estudiante con ese nombre.

estudiante = input("Busca estudiante por NOMBRE:  ")

for nombre, edad, nota  in estudiantes:
    if estudiante == nombre:
        print( "Estudiante encontrado" )
        break          
    else:
        print( " ERROR: No se encontro estudiante con ese nombre")
        break


#6. Diccionario de ciudades, crear un diccionario donde: 
#   - La llave sea el nombre del estudiante.
#   - El valor sea la ciudad donde vive
# Recorre el diccionario utilizando un ciclo e imprime la informacion con el siguiente formato
# Ana vive en Bogota


ciudades = {
    "Ana Martínez": "Bogotá",
    "Carlos Rodríguez": "Manizales",
    "Laura Gómez": "Medellín",
    "David Pérez": "Cali"
} 

for nombre, ciudad in ciudades.items():
    print(f"{nombre} vive en {ciudad}")