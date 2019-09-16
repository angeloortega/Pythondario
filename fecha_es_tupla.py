def fecha_es_tupla(fecha):
    if not(isinstance(fecha, tuple)):
        return False
    elif len(fecha) != 3:
        return False
    elif not(isinstance(fecha[0], int) and isinstance(fecha[1], int) and isinstance(fecha[2], int)):
        return False
    elif fecha[0] < 0 or fecha[1] < 0 or fecha[2] < 0:
        return False
    else:
        return True