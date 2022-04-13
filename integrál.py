#y = x^2
def vratHodnotu(x):
    return x**2

def obdelnikovaMetoda(a,b):
    hodnota = (b-a)*pow((a+b)/2,2)
    return hodnota
print(obdelnikovaMetoda(1,3))

def lichobeznikovaMetoda(a,b):
    f_b = vratHodnotu(b)
    f_a = vratHodnotu(a)
    hodnota = (b-a)*(f_a+f_b)/2
    return hodnota
print(lichobeznikovaMetoda(1,3))

def slozenaObdelnikovaMetoda(a,b,n):
    hodnota = 0
    Δx = (b-a)/n
    for o in range(n):
        hodnota += obdelnikovaMetoda(a + o*Δx, a + (o+1)*Δx)
    return hodnota
print(slozenaObdelnikovaMetoda(1,3,10))

def slozenaLichobeznikovaMetoda(a,b,n):
    hodnota = 0
    Δx = (b-a)/n
    for o in range(n):
        hodnota += lichobeznikovaMetoda(a + o*Δx, a + (o+1)*Δx)
    return hodnota
print(slozenaLichobeznikovaMetoda(1,3,10))
