"""
(★★★★) Implementar una función que utilice división y conquista, de complejidad O(n), 
que dado un arreglo de n números enteros devuelva True o False según si existe algún 
elemento que aparezca más de dos tercios de las veces. 

* Justificar la complejidad de la solución.
* No utilizar ordenamiento ni tablas de hash.
"""

def obtener_candidato_recursivo(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
    
    sobrevivientes = []

    for i in range(0, len(arr) - 1, 2):
        if arr[i] == arr[i + 1]:
            sobrevivientes.append(arr[i])
    
    if len(arr) % 2 != 0:
            sobrevivientes.append(arr[-1])
    
    return obtener_candidato_recursivo(sobrevivientes)

def es_mayoritario(arr):
     
    candidato = obtener_candidato_recursivo(arr)

    if candidato is None:
        return False
     
    cantidad = 0
    for numero in arr:
        if numero == candidato:
            cantidad += 1

    n = len(arr)

    return cantidad > (2 * n // 3)