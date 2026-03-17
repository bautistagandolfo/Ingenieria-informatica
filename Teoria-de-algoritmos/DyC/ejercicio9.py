"""
EJERCICIO: ELEMENTO MAYORITARIO (Majority Element)
-------------------------------------------------------------------------
ENUNCIADO:
Dado un arreglo de 'n' números, determinar si existe un elemento que 
aparezca más de n/2 veces usando División y Conquista.

REQUERIMIENTOS:
1. Complejidad O(n log n).
2. Devolver True o False.
3. Justificar con Teorema Maestro.
-------------------------------------------------------------------------
"""

def buscar_mayoritario(arreglo):
    n = len(arreglo)
    
    # Caso base: un solo elemento es el mayoritario de sí mismo
    if n == 1:
        return arreglo[0]

    # 1. DIVISIÓN
    medio = n // 2
    izq = arreglo[:medio]
    der = arreglo[medio:]

    # 2. CONQUISTA (Buscamos candidatos)
    # Aquí no necesitamos "cajas" complejas, solo el valor
    cand_izq = buscar_mayoritario(izq)
    cand_der = buscar_mayoritario(der)

    # 3. COMBINACIÓN
    # Si ambos ayudantes coinciden, ese es el candidato de este nivel
    if cand_izq == cand_der:
        return cand_izq

    # Si son distintos, contamos cuántas veces aparece cada uno en TODO el bloque actual
    count_izq = 0
    count_der = 0
    for num in arreglo:
        if num == cand_izq: count_izq = count_izq + 1
        if num == cand_der: count_der = count_der + 1

    # Verificamos si alguno supera la mitad del bloque actual
    if count_izq > n // 2:
        return cand_izq
    if count_der > n // 2:
        return cand_der

    # Si nadie gana, devolvemos None (o un valor que indique "nadie")
    return None

def existe_mayoritario(arreglo):
    resultado = buscar_mayoritario(arreglo)
    if resultado is None:
        return False
    
    # Verificación final obligatoria sobre el arreglo completo original
    total = 0
    for x in arreglo:
        if x == resultado:
            total = total + 1
            
    return total > len(arreglo) // 2