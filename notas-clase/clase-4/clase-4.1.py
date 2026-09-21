#CONTROL DE FLUJO

#Bucles FOR (iteracion basada en una secuencua de objetos)
# Los bucles for generalmente se usan para recorrer una secuencia de objetos. El bloque de codigo que contiene el bucle se ejecutara por cada objeto que exista en la secuencia ----> ITERACION
estudiantes_notas = [("Camila",5.0),("Lorena",4.0),("Lina",4.2),("Adrian",5.0),("Edwin",3.8),("Andrea",4.7)]

for item in estudiantes_notas: # Para cada tupla estudiante - nota en la lista de estudiantes_notas, realice las siguientes acciones
    print(f"{item[0]} obtuvo una nota de {item[1]} en el diplomado de análisis de datos")
    print("---------------------------------------------------------------------")#Los bucles FOR generalmente se usan para recorrer una secuencia de objetos. El bloque de codigo que 


suma_total = 0 #Declaro la variable suma_total que almacenara el acumulado de la suma

# Uso de las palabras claves break y continue

for numero in range(100):  # Ejemplo iterando sobre un rango de numeros del 0 al 10.
  if(numero % 2 == 0): # Si el número es par, ejecuta el siguiente bloque de código
    print(f"El número {numero} es par")
  else: # Si el número es impar, no debe imprimir nada
    continue  #Pasa al siguiente número

  suma_total += numero

  if(numero == 8):
    break # Sale del bucle cuando llegué al número 8

print("------------------------------------------")
print(f"La sumatoria total es: {suma_total}")

#Bucles While (Iteración basada en una condición booleana)  
#El bucle while evalua una condición y ejecuta el bloque de código interno solamente si la condicion es verdadera. Se detendrá cuando la condición cambie a Falso
contador = 0
while contador <= 10:
  print(f"El valor del contador es: {contador}")
  contador += 1