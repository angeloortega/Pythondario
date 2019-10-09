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

#R0 Fecha es tupla

def fecha_es_tupla(*arg):
    #Verifica que la fecha recibe un único argumento, de lo contrario es falso.
    if(len(arg) == 1):
        return fecha_es_tupla_aux(arg[0])
    return False

def fecha_es_tupla_aux(fecha):
    #Se verifica que la entrada sea una tupla, de tres elementos que sean números enteros positivos.
    if not(isinstance(fecha, tuple)):
        return False
    elif len(fecha) != 3:
        return False
    elif not(isinstance(fecha[0], int) and isinstance(fecha[1], int) and isinstance(fecha[2], int)):
        return False
    elif fecha[0] < 0 or fecha[1] < 0 or fecha[2] < 0:
        return False
    
    return True

#R1

def bisiesto(año):
    #Los años bisiestos solo son aquellos que son divisibles entre 4, pero no aquellos que son divisibles entre 100
    #Se recibe un año y se retorna o True o False.
    if(año < 1582):
        return False
    else:
        return (año % 4 == 0 and año % 100 != 0) or año % 400 == 0

#R2

# Entrada: fecha (yyyy, m, d)
# Salida: booleano, determina si la fecha dada existe en el calendario gregoriano
def fecha_es_valida(fecha):
    if (not fecha_es_tupla(fecha)):
        return False
    anno, mes, dia = fecha
    if (mes < 1 or dia < 1 or anno < 1):
        return False
    elif (dia <= (dias_de_mes(fecha)) and mes <= 12):
        if(anno <= 1582): #El 15 de Octubre de 1582 es el primer dia del calendario Gregoriano
            if(anno == 1582 and mes <= 10):
                if(mes < 10):
                    return False
                return not(mes == 10 and dia <= 14)
            return False
        return True
    return False

# Entrada: fecha (yyyy, d, m)
# Salida: entero positivo, numero de dias que tiene el mes de la fecha
def dias_de_mes(fecha):
	if (not fecha_es_tupla(fecha)):
		return -1
	anno, mes, dia = fecha
	if (mes ==2):
		if (bisiesto(anno)):
			return 29
		return 28
	if (mes%2 == 1 and mes < 7) or (mes%2 == 0 and mes > 7) or mes == 7:
		return 31
	elif mes <= 12:
		return 30
	else: 
		return -1

#R3
def dia_siguiente(fecha):

    if(not fecha_es_valida(fecha)):
        return -1
    
    dm = dias_de_mes(fecha)
    anno, mes, dia = fecha
    dia = dia + 1
    
    if (dia > dm):
        dia = 1
        mes +=1
    if (mes > 12):
        mes = 1
        anno +=1
    return (anno,mes,dia)   

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
    Algoritmo tomado de: Meyer, P. (1998)
    https://www.hermetic.ch/cal_stud/jdn.htm
    """
    año, mes, dia = fecha
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
            año, mes, dia = fecha
            j = año // 100 #Siglo basado en 0. Ej. 1995 -> 19
            if(mes < 3):
                mes += 12
                año -= 1
            dia_de_semana = ((( dia + 13 * (mes +1) // 5 + año + año // 4 - j + año // 400 ))+6)%7
            return dia_de_semana
    return -1

#R6

# Entrada: mes, anno, dia_actual
# Salida: tupla, (string de la semana, dia en el que quedo)
def imprimir_semana(mes, anno, dia_actual):
    resultado = ''
    dia_sem = dia_semana((anno, mes, dia_actual))
    dias_mes = dias_de_mes((anno, mes, dia_actual))
    for i in range(7):
        resultado += '  '
        if i < dia_sem or dias_mes < dia_actual:
            resultado += '  '
        else:
            resultado += '%2d' % dia_actual
            dia_actual += 1
    return (resultado, dia_actual)

# Entrada: mes, empezando en 0
# Salida: string
def encabezado_mes(mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    len_mes = len(meses[mes])
    string = ""
    if(len_mes <= 5):
        string += "%16s%10s" % (meses[mes], " ")
    elif(len_mes <= 7):
        string += "%17s%9s" % (meses[mes], " ")
    else:
        string += "%18s%8s" % (meses[mes], " ")
    return string

# Entrada: dia_actual, matriz de 1 de modelo de meses
#          anno, anno deseado a imprimir
# Salida: string con el anno formado
def formar_string_impresion(dia_actual, anno):
    impresion = ""
    len_dia_actual = len(dia_actual) #cantidad de filas
    len_i = len(dia_actual[0]) #cantidad de columnas
    for i in range(len_dia_actual):
        j = 0
        sigue = True
        for k in range(len_i):
            impresion += "  " + encabezado_mes((i * len_i) + k)
            if k < len_i - 1:
                impresion += '  |  '
        impresion += "\n"
        for k in range(len_i):
            impresion += "   D   L   K   M   J   V   S"
            if k < len_i - 1:
                impresion += '  |  '
        impresion += "\n"
        while sigue or j < len_i - 1: #verifica si ya se completo la fila
            if(j == 0):
                sigue = False
            temp, dia_actual[i][j] = imprimir_semana((i * len_i) + j + 1, anno, dia_actual[i][j]) #extrae la semana del mes
            impresion += temp #agrega la semana al string de impresion
            if j < len_i - 1:
                impresion += '  |  '
            else:
                impresion += '\n'
            j += 1
            j %= len_i
            sigue = sigue or dia_actual[i][j] <= dias_de_mes((anno, (i * len_i) + j + 1, 1)) #verifica que no se falten dias del mes
        impresion += '\n'
    return impresion

# Entrada: anno
# Salida: es un print o un mensaje de error
def imprimir_4x3(anno):
    if(anno < 1583):
        print("El año mínimo imprimible del calendario Gregoriano es 1583")
    else:
        dia_actual = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        print(formar_string_impresion(dia_actual, anno))


#R7

# Entrada: una fecha valida y la cantidad de dias por ser aumentados
# Salida: la fecha resultante o el valor de error "-1"
def fecha_futura(fecha, n):
    #Se incrementa dia por dia en fechas validas hasta encontrar la fecha final
    if(fecha_es_valida(fecha) and n >= 0):
        while(n > 0):
            fecha = dia_siguiente(fecha)
            n-=1
        return fecha
    else:
        return -1


#R8

# Entrada: Dos fechas validas en el formato (a,m,d)
# Salida: la catniadd de dias entre ambas fechas o el valor de error "-1"
def dias_entre(fecha1, fecha2):
    #Se restan las fechas transformadas a su dia juliano.
    if(fecha_es_valida(fecha1) and fecha_es_valida(fecha2)):
        return abs(obtener_numero_fecha(fecha1) - obtener_numero_fecha(fecha2))
    else:
        return -1
