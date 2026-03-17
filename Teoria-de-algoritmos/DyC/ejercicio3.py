"""
EJERCICIO: RAÍZ CUADRADA ENTERA
-------------------------------------------------------------------------
Implementar un algoritmo que, por división y conquista, permita obtener 
la parte entera de la raíz cuadrada de un número 'n', en tiempo O(log n).

Ejemplos:
- Si n = 10, debe devolver 3 (porque 3^2 = 9 y 4^2 = 16).
- Si n = 25, debe devolver 5.

REQUERIMIENTOS:
1. Implementación por División y Conquista.
2. Justificación de complejidad O(log n) mediante Teorema Maestro.
-------------------------------------------------------------------------
"""


def raiz_entera(n, inicio, fin, candidato_actual = 0):

    if inicio > fin:
        return candidato_actual
    
    medio = (inicio + fin) // 2
    cuadrado = medio * medio

    if cuadrado == n:
        return cuadrado
    
    if cuadrado < n:
        return raiz_entera(n, medio + 1, fin, medio)
    
    else:
        return raiz_entera(n,inicio, medio - 1, candidato_actual)