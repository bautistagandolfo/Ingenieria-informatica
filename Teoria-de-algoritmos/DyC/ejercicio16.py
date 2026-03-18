def encontrar_maximo_local(matriz, f_min, f_max, c_min, c_max):
    # Caso base: La sub-matriz se redujo a un solo elemento
    if f_min == f_max and c_min == c_max:
        return matriz[f_min][c_min]

    # Decidimos si dividir por columna (si es más ancha) o por fila (si es más alta)
    es_mas_ancha = (c_max - c_min) >= (f_max - f_min)

    if es_mas_ancha:
        # 1. Buscamos el máximo en la COLUMNA del medio
        col_medio = (c_min + c_max) // 2
        fila_max = f_min
        for i in range(f_min + 1, f_max + 1):
            if matriz[i][col_medio] > matriz[fila_max][col_medio]:
                fila_max = i
        
        val_max = matriz[fila_max][col_medio]
        
        # 2. Comparamos con vecinos IZQUIERDA y DERECHA
        v_izq = matriz[fila_max][col_medio - 1] if col_medio > c_min else -1
        v_der = matriz[fila_max][col_medio + 1] if col_medio < c_max else -1

        if val_max >= v_izq and val_max >= v_der:
            return val_max # ¡Encontrado!
        elif v_izq > val_max:
            return encontrar_maximo_local(matriz, f_min, f_max, c_min, col_medio - 1)
        else:
            return encontrar_maximo_local(matriz, f_min, f_max, col_medio + 1, c_max)

    else:
        # 1. Buscamos el máximo en la FILA del medio
        fila_media = (f_min + f_max) // 2
        col_max = c_min
        for j in range(c_min + 1, c_max + 1):
            if matriz[fila_media][j] > matriz[fila_media][col_max]:
                col_max = j
        
        val_max = matriz[fila_media][col_max]

        # 2. Comparamos con vecinos ARRIBA y ABAJO
        v_arr = matriz[fila_media - 1][col_max] if fila_media > f_min else -1
        v_aba = matriz[fila_media + 1][col_max] if fila_media < f_max else -1

        if val_max >= v_arr and val_max >= v_aba:
            return val_max # ¡Encontrado!
        elif v_arr > val_max:
            return encontrar_maximo_local(matriz, f_min, fila_media - 1, c_min, c_max)
        else:
            return encontrar_maximo_local(matriz, fila_media + 1, f_max, c_min, c_max)  