"""
EJERCICIO 14 (★★) - Raíz por Teorema de Bolzano

Consigna:
- Implementar una función `raiz(f, a, b)` que reciba una función univariable 
  y los extremos 'a' y 'b'.
- f(a) y f(b) tienen signos opuestos (uno positivo, otro negativo).
- El algoritmo debe devolver UNA raíz dentro del intervalo [a, b].
- Requisito: Complejidad LOGARÍTMICA O(log n) respecto al largo del intervalo.
- Nota: Trabajar con ints para simplificar la lógica de la complejidad.
- Tarea extra: Justificar la complejidad mediante el Teorema Maestro.
"""

def raiz(f, a, b):
    if a == b:
        return a
    
    medio = (a + b) // 2

    if f(medio) == 0:
        return medio
    
    if f(a) * f(medio) < 0:
        return raiz(f, a, medio)
    
    else:
        return raiz(f,medio + 1, b)