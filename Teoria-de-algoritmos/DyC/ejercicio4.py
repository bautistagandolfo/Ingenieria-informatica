"""
EJERCICIO: BÚSQUEDA DEL PICO (PUNTO MÁXIMO)
-------------------------------------------------------------------------
Se tiene un arreglo de N >= 3 elementos en forma de pico.
Esto es: estrictamente creciente hasta una posición 'p', 
y estrictamente decreciente a partir de ella (0 < p < N-1).

Ejemplo: [1, 2, 3, 1, 0, -2] -> p = 2 (el valor es 3)

REQUERIMIENTOS:
1. Implementar algoritmo por División y Conquista.
2. Complejidad temporal O(log n).
3. Justificación por Teorema Maestro.
-------------------------------------------------------------------------
"""

def buscar_pico(arr, inicio, fin,):

    if inicio >= fin:
        return inicio
    
    medio = (inicio + fin) // 2

    if arr[medio] > arr[medio + 1]:
        return buscar_pico(arr,inicio, medio)
    
    if arr[medio] < arr[medio + 1]:
        return buscar_pico(arr, medio + 1, fin)