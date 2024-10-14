t = 10
def calcularinteres(p,r,t,n):
    A = p*(1+r/n)**(n*t)

    return A
p = float(input("capital inicial"))
r = float(input("interés anual en porcentaje"))
n = float(input("nº de periodo por años"))



capitalfinal = calcularinteres(p,r,n,10)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1

capitalfinal = calcularinteres(p,r,n,9)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1

capitalfinal = calcularinteres(p,r,n,8)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1

capitalfinal = calcularinteres(p,r,n,7)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1

capitalfinal = calcularinteres(p,r,n,6)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1

capitalfinal = calcularinteres(p,r,n,5)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1

capitalfinal = calcularinteres(p,r,n,4)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1

capitalfinal = calcularinteres(p,r,n,3)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1

capitalfinal = calcularinteres(p,r,n,2)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1

capitalfinal = calcularinteres(p,r,n,1)
print(f"la cantidad final desués de {t} años sería {capitalfinal}")
t = t-1 
