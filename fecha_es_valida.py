from fecha_es_tupla import fecha_es_tupla as fecha_es_tupla
from bisiesto import bisiesto as bisiesto


# Entrada: fecha (yyyy, m, d)
# Salida: booleano, determina si la fecha dada existe en el calendario gregoriano
def fecha_es_valida(fecha):
	if (not fecha_es_tupla(fecha)):
		return False
	anno, dia, mes = fecha
	if (mes < 1 or dia < 1 or anno < 1):
		return False
	if (dia <= (dias_de_mes(fecha)) and mes < 12):
		return True
	else:
		return False

# Entrada: fecha (yyyy, m, d)
# Salida: entero positivo, numero de dias que tiene el mes de la fecha
def dias_de_mes(fecha):
	if ( not fecha_es_tupla(fecha)):
		return -1
	anno, mes = (fecha[0],fecha[-1])
	if (mes ==2):
		if (bisiesto(fecha)):
			return 29
		return 28
	if (mes%2 == 1 and mes < 7) or (mes%2 == 0 and mes > 7):
		return 31
	elif mes <= 12:
		return 30
	else: 
		return -1