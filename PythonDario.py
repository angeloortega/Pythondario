"""
[IC-6831] Tarea 3.a 
Eduardo Jirón Alvarado 2017101878
Angelo Ramírez         2017080055
Josué Canales          2017134770
Instituto Tecnológico de Costa Rica
Sede Central Cartago
Escuela de computación
Aseguramiento de la calidad de software
"""

#R4
def obtener_numero_fecha(fecha):
    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    return 365*(año - ((mes + 9) % 12) // 10) + ((año - ((mes + 9) %   12) // 10) // 4) - ((año - ((mes + 9) %   12) // 10) // 100) + ((año - ((mes + 9) %   12) // 10) // 400) + ((((mes + 9)  %   12)*306 + 5) // 10) + (dia - 1)

def dias_desde_primero_enero(fecha):
    if(fecha_es_tupla(fecha)):
        if(fecha_es_valida(fecha)):
            año = fecha[0]
            return obtener_numero_fecha(fecha) - (obtener_numero_fecha((año,1,1)))
            
#R5
def dia_semana(fecha):
    #Se utiliza la congruencia de Zeller para encontrar el día de la semana en forma de número
    #Retorna un entero entre 0 y 6 empezando en domingo.
    if(fecha_es_tupla(fecha)):
        if(fecha_es_valida(fecha)):
            año = fecha[0]
            mes = fecha[1]
            dia = fecha[2]
            k = año % 100 #año del siglo
            j = año // 100 #Siglo basado en 0. Ej. 1995 -> 19
            dia_de_semana = (((dia + ((13*(mes+ 1))//5) + k + (k//4) + (j//4) - 2*j) + 6)%7)
            return dia_de_semana