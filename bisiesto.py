from fecha_es_tupla import fecha_es_tupla as fecha_es_tupla
def bisiesto(fecha):
    if not fecha_es_tupla(fecha):
        return -1
    else:
        return (fecha[0] % 4 == 0 and fecha[0] % 100 != 0) or fecha[0] % 400 == 0