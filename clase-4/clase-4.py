#Actividad 1 - Estructuras y tipos de datos


inventario = [ 
    {"producto": "camisa", "precio": 25900, "stock": "11"},
    {"producto": "Pantalon", "precio": 39900, "stock": "23"}
]

#Añadir un nuevo producto al inventario
inventario.append({"producto": "abrigo", "precio": 50000, "stock": "2"})
print(inventario)

#Convertir los valores del stock en numero enteros

#producto 0
inventario[0]["stock"] = int(inventario[0]["stock"])

for item in inventario:
    item["precio"] += 10000


for item in inventario:
    item["precio"] += 10000

for item in inventario:
    product = item["producto"]
    precio = item["precio"]
    stock = item["stock"]
    print(f"Hay {stock} unidades del producto {product}. Su precio por unidad es de {precio}")


#CONTROL DE FLUJO

#Conficiones if, elif y else

mi_numero = int(input("ingresa tu numero: "))

if mi_numero < 10:
    print("Tu numero es menos que 10")
elif mi_numero > 60:

    if mi_numero % 2 == 0:
        print("Tu numero es mayor que 60 y es par")
    else:
        print("Tu numero es mayot que 60 y es impar")

elif mi_numero > 40:
    print("Tu numero es mayor que 40")