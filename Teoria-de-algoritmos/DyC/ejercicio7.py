"""
EJERCICIO: PAR DE PUNTOS MÁS CERCANOS (Closest Pair of Points)
-------------------------------------------------------------------------
ENUNCIADO:
Dados 'n' puntos en un plano 2D, buscar la pareja que se encuentre a la 
distancia mínima entre sí, utilizando la técnica de División y Conquista.

REQUERIMIENTOS:
1. Lograr una complejidad mejor que O(n^2).
2. Justificar la complejidad mediante el Teorema Maestro.
3. Asumir que no hay puntos con coordenadas X o Y repetidas.
-------------------------------------------------------------------------
"""

def par_mas_cercano(puntos):
    n = len(puntos)
    
    # 1. ORDENAMIENTO INICIAL (Por X)
    # Lo hacemos siempre al principio para asegurar la división
    puntos.sort(key=lambda p: p[0])

    def resolver(pts):
        cant = len(pts)
        
        # CASO BASE: Fuerza bruta para 3 puntos o menos
        if cant <= 3:
            dist_min = float('inf')
            for i in range(cant):
                for j in range(i + 1, cant):
                    # Distancia Euclídea manual: raíz de (dx² + dy²)
                    d = ((pts[i][0] - pts[j][0])**2 + (pts[i][1] - pts[j][1])**2)**0.5
                    if d < dist_min:
                        dist_min = d
            return dist_min

        # 2. DIVISIÓN
        medio = cant // 2
        izq = pts[:medio]
        der = pts[medio:]
        
        # 3. CONQUISTA (Recursión)
        d_izq = resolver(izq)
        d_der = resolver(der)
        
        delta = d_izq if d_izq < d_der else d_der

        # 4. COMBINACIÓN (La Franja)
        punto_medio_x = pts[medio][0]
        # Filtramos puntos en la franja y los ordenamos por Y
        franja = [p for p in pts if (p[0] - punto_medio_x)**2 < delta**2]
        franja.sort(key=lambda p: p[1])

        mejor_en_franja = delta
        for i in range(len(franja)):
            # El truco de los 7 vecinos
            for j in range(i + 1, min(i + 8, len(franja))):
                d = ((franja[i][0] - franja[j][0])**2 + (franja[i][1] - franja[j][1])**2)**0.5
                if d < mejor_en_franja:
                    mejor_en_franja = d
                    
        return mejor_en_franja

    return resolver(puntos)