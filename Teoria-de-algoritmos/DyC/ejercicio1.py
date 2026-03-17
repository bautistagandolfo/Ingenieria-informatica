"""
1) (★) Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos 
y casi ordenado (todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento fuera 
de lugar. Indicar y justificar su complejidad temporal.
"""

def buscar_intruso(arr, inicio, fin):
    if inicio >= fin:
        return arr[inicio]
    
    medio = (inicio + fin)//2

    # Si el de la izquierda es mayor que yo, hay un lío acá
    if medio > 0 and arr[medio] < arr[medio-1]:
        # El intruso es el medio o el anterior. 
        # Si al ignorar el medio, el anterior encaja con el siguiente, el medio es el intruso.
        if medio + 1 < len(arr) and arr[medio-1] <= arr[medio+1]:
            return arr[medio]
        else:
            return arr[medio-1]

    # Si yo soy mayor que el de mi derecha, hay un lío acá
    if medio < len(arr) - 1 and arr[medio] > arr[medio+1]:
        # El intruso es el medio o el siguiente.
        if medio > 0 and arr[medio-1] <= arr[medio+1]:
            return arr[medio]
        else:
            return arr[medio+1]
        

    if arr[inicio] > arr[medio]:

        return buscar_intruso(arr,inicio, medio)
    
    else:

        return buscar_intruso(arr,medio + 1, fin)


# No esta bien hecho