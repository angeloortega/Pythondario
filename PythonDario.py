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
from fecha_es_tupla import fecha_es_tupla as fecha_es_tupla
from bisiesto import bisiesto as bisiesto
#R4
def obtener_numero_fecha(fecha):
    """
    Conversión a fecha del calendario gregoriano a juliano
    365 dias por cada año
    Se corren los meses para que el año empiece en marzo
    más la cantidad de años bisiestos (divisibles entre 4 (las centenas no solo las divisibles entre 400))
    Al tener el inicio del año en marzo, los bisiestos se añaden el ultimo dia del año, por cuanto es posible saber cuantos dias
    han transcurrido en un año usando aritmética simple.
    Finalmente se suma el día del mes - 1, ya que el excedente fue tomado en cuenaa anteriormente
    """
    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    mes_corrido = (mes + 9) % 12
    año_complementado = año - mes_corrido // 10 #Si el mes cae en otro año entonces se resta.
    return 365 * año_complementado + (año_complementado // 4) - (año_complementado // 100) + (año_complementado // 400) + ((mes_corrido*306 + 5) // 10) + (dia - 1)

def dias_desde_primero_enero(fecha):
    """Se convierte la fecha en un número y se substrae el número de fecha del primero de Enero de la fecha."""
    if(fecha_es_tupla(fecha)):
        if(fecha_es_valida(fecha)):
            año = fecha[0]
            return obtener_numero_fecha(fecha) - (obtener_numero_fecha((año,1,1)))
    return -1
        
#R5
def dia_semana(fecha):
    """
    Se utiliza la congruencia de Zeller para encontrar el día de la semana en forma de número
    Retorna un entero entre 0 y 6 empezando en domingo.
    k representa cuanto varía la fecha en un año.
    k//4 es un dia adicional los años bisiestos.
    j se usa para representar la variación en milenios.
    j//4 es la variación de que se da cada 400 años.
    Se corren todos los meses 13 meses para evitar el conteo doble del excedente
    en febrero en años bisiestos.
    Finalmente se le suma 1 porque el algoritmo original de Zeller empieza el sabado
    Se obtiene el modulo 7 que nos da el día de la semana.
    """
    if(fecha_es_tupla(fecha)):
        if(fecha_es_valida(fecha)):
            año = fecha[0]
            mes = fecha[1]
            dia = fecha[2]
            k = año % 100 #año del siglo
            j = año // 100 #Siglo basado en 0. Ej. 1995 -> 19
            dia_de_semana = (((dia + ((13*(mes+ 1))//5) + k + (k//4) + (j//4) + 5*j) + 6)%7)
            return dia_de_semana
    return -1


