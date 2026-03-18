"""
(★★★) Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, 
tal que la cantidad total de elementos del arreglo es potencia de 2. 
Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma 
que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional.

* Indicar y justificar su complejidad temporal.
* Pista: Pensar en 4 elementos {C1, C2, D1, D2} y luego en 8.
"""

def modificar_arreglo(arr, inicio, fin):
    
    n_tramo = fin - inicio
    if n_tramo <= 2:
        return
    
    medio = (inicio + n_tramo) // 2
    cuarto = (n_tramo) // 4

    for i in range(cuarto):
        pos_izq = inicio + cuarto + i
        pos_der = medio + i

        arr[pos_izq], arr[pos_der] = arr[pos_der], arr[pos_izq]
    
    modificar_arreglo(arr, inicio, medio)
    modificar_arreglo(arr, medio , fin)
