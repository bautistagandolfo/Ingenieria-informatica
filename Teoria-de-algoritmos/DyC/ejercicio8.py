"""
EJERCICIO: CONTEO DE INVERSIONES
-------------------------------------------------------------------------
ENUNCIADO:
Dados dos arreglos A y B de longitud 'n' con los mismos elementos. 
A está ordenado de menor a mayor. B está desordenado.
Encontrar la cantidad de inversiones necesarias en B para que quede 
ordenado como A, usando División y Conquista en O(n log n).

DEFINICIÓN:
Una inversión es un par de índices (i, j) tal que i < j pero B[i] > B[j].
-------------------------------------------------------------------------
"""
def contar_y_ordenar(B):
    if len(B) <= 1:
        return B,0
    
    medio = len(B) // 2
    parte_izquierda = B[:medio]
    parte_derecha = B[medio:]

    resultado_izq = contar_y_ordenar(parte_izquierda)
    izq = resultado_izq[0]      # La lista ordenada
    inv_izq = resultado_izq[1]  # El conteo

    resultado_der = contar_y_ordenar(parte_derecha)
    der = resultado_der[0]      # La lista ordenada
    inv_der = resultado_der[1]  # El conteo

    # 3. COMBINACIÓN (El Merge)
    lista_final = []
    i = 0
    j = 0
    inv_cruzadas = 0

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            lista_final.append(izq[i])
            i = i + 1
        else:
            lista_final.append(der[j])
            # Sumamos las inversiones
            inv_cruzadas = inv_cruzadas + (len(izq) - i)
            j = j + 1

    # Terminamos de pasar lo que quede
    while i < len(izq):
        lista_final.append(izq[i])
        i = i + 1
    
    while j < len(der):
        lista_final.append(der[j])
        j = j + 1

    # Devolvemos los dos datos al final
    total_inversiones = inv_izq + inv_der + inv_cruzadas
    return lista_final, total_inversiones