"""
 Se tiene un arreglo en el que se registran los resultados de tests automáticos de una porción de código.
Este código se encontraba funcionando pero, debido a unos cambios que se están realizando, 
en algún momento dejó de funcionar. Se registra un 1 si pasa los tests, 0 en caso contrario. 
De esta manera, el arreglo tendrá la forma [1, 1, 1, ..., 0, 0, ...] (es decir, unos seguidos de ceros). 
Se pide: a. una función de orden 
O
(logn)
O(logn) que, por división y conquista, encuentre el índice del primer 0, de forma que se pueda reconocer 
rápidamente en qué modificación del código se dejó de pasar los tests. Si no hay ningún 0 (solo hay unos), 
debe devolver -1. b. demostrar con el Teorema Maestro que la función es, en efecto, 
O
(logn)
O(logn).

Ejemplos:

[1, 1, 0, 0, 0] →  2
[0, 0, 0, 0, 0] →  0
[1, 1, 1, 1, 1] → -1
"""

def encontrar_primer_cero(arr, inicio, fin):

    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2

    # Caso en que encontramos el primer cero

    if arr[medio] == 0:
        if medio == 0 or arr[medio - 1] == 1:
            return medio
        else:
            return encontrar_primer_cero(arr,inicio, medio - 1)

    else:

        return encontrar_primer_cero(arr, medio + 1, fin)
    
    