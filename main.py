# Funcion para la cantidad de estudiantes de 1 y 2 semestre
def estudiantes_semestre(lista, carrer):
    total = 0
    for li in range(len(lista)):
        if carrera[li] == carrer and (semestre[li] == str(1) or (semestre[li] == str(2))):
            total += 1

    print(f"De la carrera {carrer} respondieron: {str(total-1)} estudiantes")


# Funcion para los datos de las encuentas de la pregunta # 5
def encuesta_pregunta5(lista1, lista2, dato, nu):
    pr5_resp = 0

    for se in range(len(lista1)):
        if (lista1[se] == dato) and (lista2[se] == str(nu)):
            pr5_resp += 1
    return pr5_resp


# Funcion para sacar el porcentaje
def porcentaje(nh, nf, np, animo):
    rsf = round((nf * 100) / 255)
    rsh = round((nh * 100) / 255)
    resul = rsf + rsh
    print(f"{str(resul)}% respondió {str(np)}. "
          f"{animo}, de las cuales {str(rsf)}% fueron mujeres y {str(rsh)}% fueron hombres")


# Funcion para sacar la edad promedio
def promedio_edades(genero, g):
    edades = 0
    totales = 0
    for sef in range(len(sexo)):
        if (sexo[sef] == genero) and (semestre[sef] == str("1")):
            edades = edades + int(edad[sef])
            totales += 1

    promedio = edades / totales
    print(f"La edad promedio de {g} es de {str(round(promedio))} años")


# Funcion para calcular la cantidad de estudiantes en las carreras
def carrera_estudiantes(word):
    estudiante_hombre = 0
    estudiante_mujer = 0
    for cr in range(len(carrera)):
        if (carrera[cr] == word) and (sexo[cr] == "Masculino"):
            estudiante_hombre = estudiante_hombre + 1

        elif (carrera[cr] == word) and (sexo[cr] == "Femenino"):
            estudiante_mujer = estudiante_mujer + 1

    return estudiante_hombre, estudiante_mujer


# Lee el archivo y extrae los datos en la variable lectura
file = open("datos2.csv", "r")
lectura = file.read()
file.close()


# Separa los datos
datos = []
for i in lectura.split("\n"):
    datos.append(i)

palabra = ""
nuevo = []
for i in range(len(datos)):
    palabra = datos[i].split(";")
    nuevo.append(palabra)


# Listas para almacenar los datos
carrera = []
edad = []
semestre = []
sexo = []
resp5 = []


# Ciclo para almancer los datos del documento en las listas
for numero in range(len(nuevo)):
    carrera.append(nuevo[numero][1])
    edad.append(nuevo[numero][2])
    semestre.append(nuevo[numero][3])
    sexo.append(nuevo[numero][4])
    resp5.append(nuevo[numero][9])

# Condicion para la calcular la cantidad de hombres y mujeres
masculino = 0
femenino = 0

for hm in sexo:
    if hm == "Masculino":
        masculino += 1
    else:
        femenino += 1

# Punto #1 LISTO

hombres = round((masculino * 100) / 252)
mujeres = round((femenino * 100) / 252)
print(f"El porcentaje de hombres que respondio la encuesta es de {str(hombres)} %")
print(f"El porcentaje de mujeres que respondio la encuesta es de {str(mujeres)} %")


# Punto #2 LISTO
# Carreras
estudiantes_semestre(carrera, "IMTR")
estudiantes_semestre(carrera, "ICIV")
estudiantes_semestre(carrera, "INAV")
estudiantes_semestre(carrera, "IMEC")
estudiantes_semestre(carrera, "IELE")
estudiantes_semestre(carrera, "IAMB")
estudiantes_semestre(carrera, "IIND")
estudiantes_semestre(carrera, "IQUI")
estudiantes_semestre(carrera, "IBIO")
estudiantes_semestre(carrera, "ISCO")
estudiantes_semestre(carrera, "IETR")

# Punto #3 LISTO
# Femenino
pre5_resp1_feme = encuesta_pregunta5(sexo, resp5, "Femenino", 1)
pre5_resp2_feme = encuesta_pregunta5(sexo, resp5, "Femenino", 2)
pre5_resp3_feme = encuesta_pregunta5(sexo, resp5, "Femenino", 3)
pre5_resp4_feme = encuesta_pregunta5(sexo, resp5, "Femenino", 4)

# Masculino
pre5_resp1_masc = encuesta_pregunta5(sexo, resp5, "Masculino", 1)
pre5_resp2_masc = encuesta_pregunta5(sexo, resp5, "Masculino", 2)
pre5_resp3_masc = encuesta_pregunta5(sexo, resp5, "Masculino", 3)
pre5_resp4_masc = encuesta_pregunta5(sexo, resp5, "Masculino", 4)
pre5_resp5_masc = encuesta_pregunta5(sexo, resp5, "Masculino", 5)

print()
porcentaje(pre5_resp1_masc, pre5_resp1_feme, 1, " Totalmente desacuerdo")
porcentaje(pre5_resp2_masc, pre5_resp2_feme, 2, "En desacuerdo")
porcentaje(pre5_resp3_masc, pre5_resp3_feme, 3, "Ni en acuerdo ni en desacuerdo")
porcentaje(pre5_resp4_masc, pre5_resp4_feme, 4, "De acuerdo")
porcentaje(pre5_resp4_masc, 0, 5, "Totalmente de acuerdo")


# PUNTO #4 LISTO
# Hombre
promedio_edades("Masculino", "Hombres")

# Mujer
promedio_edades("Femenino", "Mujeres")

# PUNTO #5 LISTO
h_iciv, f_iciv = carrera_estudiantes("ICIV")
porchombre = round((h_iciv * 100) / 252)
porcmujer = round((f_iciv * 100) / 252)
print(f"La carrera con mayor estudantes es:ICIV tiene {str(porchombre)}% de hombres y {str(porcmujer)}% de mujeres")
