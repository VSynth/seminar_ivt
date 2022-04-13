#funkce x**2-1

prah = 0.00001
h = 0.00001
x_0 = 7
n = 0
lst_x = list()
lst_x.append(x_0)

while n<1000 and n == 0 or abs(lst_x[-1] - lst_x[-2]) > prah:
    f_x = pow(lst_x[-1],2)-1
    der_x = (pow(lst_x[-1]+h,2)-1 - (pow(lst_x[-1],2)-1))/h
    lst_x.append(lst_x[-1] - f_x/der_x)
    n = n+1
print(lst_x)
