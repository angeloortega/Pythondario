from fecha_es_valida import dias_de_mes as dias_de_mes

def dia_siguiente(fecha):
	dm = dias_de_mes(fecha)
	anno,mes,dia = fecha
	dia = dia + 1
	if (dia > dm):
		dia = 1
		mes +=1
	if (mes > 12):
		mes = 1
		anno +=1
	return (anno,mes,dia)   
