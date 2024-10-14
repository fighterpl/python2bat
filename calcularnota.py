def calcularNotaAcceso(notaBachillerato,notaFaseGeneral):
    notaAcceso = 0.6*notaBachillerato+0.4*notaFaseGeneral
    return notaAcceso
def calcularNotaAdmisión(notaAcceso,m1,m2):
    notaAdmisión = notaAcceso+m1*a+m2*b
    return notaAdmisión

notaBachillerato = float(input("Nota de bachillerato"))
notaFaseGeneral = float(input("Nota de la fase general"))

notaAcceso = calcularNotaAcceso(notaBachillerato,notaFaseGeneral)
print(f"Tu nota de acceso es {notaAcceso}.")

m1 = float(input("Nota de la materia específica 1"))
m2 = float(input("Nota de la materia específica 2"))
a = float(input("Coeficiente de ponderación de materia 1"))
b = float(input("Coeficiente de ponderación de materia 2"))

notaAdmisión = calcularNotaAdmisión(notaAcceso,m1,m2)
print(f"Tu nota de admisión es {notaAdmisión}.")