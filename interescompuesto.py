def calcularinteres(p,r,t,n):
    A = p*(1+r/n)**(n*t)
    return A
p = float(input("capital inicial"))
r = float(input("interés anual en porcentaje"))
t = float(input("número de años"))
n = float(input("nº de periodo por años"))

capitalfinal = calcularinteres(p,r,t,n)

print(f"la cantidad final desués de {t} años sería {capitalfinal}")