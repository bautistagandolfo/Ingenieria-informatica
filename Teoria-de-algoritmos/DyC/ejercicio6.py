"""
EJERCICIO: MULTIPLICACIÓN DE NÚMEROS GRANDES (KARATSUBA)
-------------------------------------------------------------------------
Implementar un algoritmo de multiplicación de dos números de longitud n
utilizando División y Conquista con una complejidad mejor que O(n^2).

REQUERIMIENTOS:
1. Implementar la división de los números en mitades (partes alta y baja).
2. Utilizar el truco de Karatsuba para reducir la cantidad de productos recursivos.
3. Justificar la complejidad mediante el Teorema Maestro.
-------------------------------------------------------------------------
"""

def Multiplicacion(X, Y):
    # Caso Base: números de un solo dígito
    if X < 10 or Y < 10:
        return X * Y

    # Determinamos el tamaño n y la mitad m
    n = max(len(str(X)), len(str(Y)))
    m = n // 2

    # DIVISIÓN: Separamos los números en mitades (Parte Alta y Parte Baja)
    # x1 y y1 son las "mitades izquierdas", x0 y y0 las "derechas"
    x1 = X // (10**m)
    x0 = X % (10**m)
    y1 = Y // (10**m)
    y0 = Y % (10**m)

    # CONQUISTA: Los 3 llamados recursivos del Teorema
    # 1. Producto de las partes altas
    p1 = Multiplicacion(x1, y1)
    
    # 2. Producto de las partes bajas
    p2 = Multiplicacion(x0, y0)
    
    # 3. Producto de las sumas (el "truco" algebraico)
    p3 = Multiplicacion(x1 + x0, y1 + y0)

    # COMBINACIÓN: Reensamblamos usando la fórmula de Karatsuba
    # p1 es x1*y1
    # p2 es x0*y0
    # El término central (x1*y0 + x0*y1) es p3 - p1 - p2
    termino_central = p3 - p1 - p2
    
    resultado = (p1 * 10**(2*m)) + (termino_central * 10**m) + p2
    
    return resultado