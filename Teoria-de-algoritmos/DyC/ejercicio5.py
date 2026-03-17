"""
EJERCICIO: MERGE SORT (ORDENAMIENTO POR MEZCLA)
-------------------------------------------------------------------------
Implementar el algoritmo de ordenamiento Merge Sort utilizando la 
estrategia de División y Conquista.

REQUERIMIENTOS:
1. Implementar la función recursiva que divide el arreglo.
2. Implementar la lógica de mezcla (merge) de dos mitades ya ordenadas.
3. Justificar la complejidad temporal O(n log n) mediante el Teorema Maestro.
-------------------------------------------------------------------------
"""

def merge_sort(lista):
    # CASO BASE: Si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) > 1:
        # 1. DIVISIÓN: Encontramos el punto medio y dividimos
        mid = len(lista) // 2
        izq = lista[:mid]
        der = lista[mid:]

        # 2. CONQUISTA: Llamadas recursivas para ordenar cada mitad
        merge_sort(izq)
        merge_sort(der)

        # 3. COMBINACIÓN (MERGE): Unimos las mitades ordenadas
        i = j = k = 0

        # Comparamos elementos de ambas mitades
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k] = der[j]
                j += 1
            k += 1

        # Vaciamos lo que haya quedado en la lista izquierda
        while i < len(izq):
            lista[k] = izq[i]
            i += 1
            k += 1

        # Vaciamos lo que haya quedado en la lista derecha
        while j < len(der):
            lista[k] = der[j]
            j += 1
            k += 1