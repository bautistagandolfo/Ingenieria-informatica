"""
(★★) EJERCICIO 13: TESTEO DE COVID-19 (Group Testing)

Consigna:
- Tenemos n personas y una función pcr(grupo) que devuelve True si 
  hay al menos un contagiado.
- Objetivo: Encontrar a la persona contagiada con la MENOR cantidad de tests.
- Supuesto: Hay una única persona contagiada.
- Tarea: Implementar el algoritmo (D&C) e indicar cuántos tests se usan en Big Oh.
"""
def pcr(grupo):

    if grupo == 1:
        return False
    return True
#la hice para que no me tome pcr como algo inexistente
#(el conteido de dicha funcion no tiene importancia)

def encontrar_contagiado(personas):

    if len(personas) == 1:
        return personas[0]
    
    medio = len(personas) // 2
    mitad_izq = personas[:medio]
    mitad_der = personas[medio:]

    if pcr(mitad_izq):
        return encontrar_contagiado(mitad_izq)
    else:
        return encontrar_contagiado(mitad_der)