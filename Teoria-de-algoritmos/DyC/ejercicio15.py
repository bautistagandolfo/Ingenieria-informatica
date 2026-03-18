"""
EJERCICIO 15 (★) - La Joya de la Corona Británica (Año 1700)

Consigna:
- Tenemos 'n' piedras. Una es la VERDADERA (pesa más).
- Las demás son IMITACIONES (todas pesan lo mismo entre sí).
- Herramienta: Balanza de platillos (compara dos grupos).
- Función disponible: balanza(grupo1, grupo2)
    * Devuelve > 0 si grupo1 pesa más.
    * Devuelve < 0 si grupo2 pesa más.
    * Devuelve 0 si pesan igual.
- Tarea: 
    a. Implementar algoritmo de División y Conquista para hallar la joya.
    b. Justificar complejidad Big O.
"""
def balanza(g1,g2):
    return 0


def buscar_joya(piedras):
    if len(piedras) == 1:
        return piedras[0]
    
    mitad = len(piedras)  // 2

    grupo1 = piedras[ : mitad]
    grupo2 = piedras[mitad : mitad*2 ]

    if (balanza(grupo1, grupo2) > 0):
        return buscar_joya(grupo1)
    elif (balanza(grupo1, grupo2) < 0):
        return buscar_joya(grupo2)
    else:
        return piedras[-1]