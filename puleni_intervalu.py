# x^3-5x^2+5x
f = lambda x: (x**3)-5*(x**2)+5*x

a = 0.02
b = 3
n = 0
pres = 0.0000001

if f(a)*f(b)<0:
    print("f(a)*f(b) < 0 -> plati")
    s = (a+b)/2
    while abs(f(s))>pres or n < 1000 and abs(f(s))>pres:
        if f(a)*f(s)<0:
            b = s
        elif f(s)*f(b)<0:
            a = s
        s = (a+b)/2
        n += 1
    print("x="+str(s))
    
else:
    print("f(a)*f(b) < 0 -> neplati")
