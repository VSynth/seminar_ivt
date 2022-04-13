import copy
class Polynom:
    def __init__(self,koeficienty):
        self.koeficienty = koeficienty
        
    def __str__(self):
        pol_out = ""
        for i in range(len(self.koeficienty)):
            if self.koeficienty[i] != 0:
                if self.koeficienty[i] > 0 and i != 0:
                    pol_out += "+"
                if i == 0:
                    pol_out += str(self.koeficienty[i])
                else:
                    if self.koeficienty[i] == -1:
                        pol_out += "-"
                    elif self.koeficienty[i] == 1:
                        pol_out += ""
                    else:
                        pol_out += str(self.koeficienty[i])                    
            if i == 1 and self.koeficienty[i] != 0:
                pol_out += "x"
            elif i > 1 and self.koeficienty[i] != 0:
                pol_out += "x^" + str(i)
        if len(pol_out) == 0:
            pol_out += "0"
        return pol_out

    def Vycisli(self,x):
        hodnota = 0
        for i in range(len(self.koeficienty)):
            hodnota += self.koeficienty[i]*x**i
        return hodnota

    def Vrat_stupen(self):
        stupen = 0
        for i in range(len(self.koeficienty)):
            if i > stupen and self.koeficienty[i] != 0:
                stupen = i
        return stupen

    def Nasob_skalarem(self,skalar):
        koef = list()
        for i in range(len(self.koeficienty)):
            koef.append(self.koeficienty[i] * skalar)
        return Polynom(koef)
    @staticmethod
    def Secti(p1,p2):
        koef = list()
        koef_p1 = copy.deepcopy(p1.koeficienty)
        koef_p2 = copy.deepcopy(p2.koeficienty)
        delka = len(koef_p1) - len(koef_p2)
        if len(koef_p2) > len(koef_p1):
            delka = len(koef_p2) - len(koef_p1)
            for i in range(delka):
                koef_p1.append(0)
        else:
            for i in range(delka):
                koef_p2.append(0)
        for i in range(len(koef_p1)):
            koef.append(koef_p1[i] + koef_p2[i])
        return Polynom(koef)
    @staticmethod
    def Odecti(p1,p2):
        return Polynom.Secti(p1, Polynom.Nasob_skalarem(p2,-1))
                
p1 = Polynom([-1,0,1])
p2 = Polynom([-1,0,1])
print(str(p1))
print(p1.Vycisli(2))
print(p1.Vrat_stupen())
print(str(p1.Nasob_skalarem(2)))
print(Polynom.Secti(p1,p2))
print(Polynom.Odecti(p1,p2))
