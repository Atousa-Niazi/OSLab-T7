#Atousa Niazi Abkoh-98440127-python-Fraction-class-OSLAb-T7_2
# n for numerator / d for denominator

class f:
    def __init__(self, n1,d1,n2,d2):
        self.f1 = n1/d1
        self.f2 = n2/d2
    
    def Sum(self):
        s=self.f1+self.f2
        print('Sum of fractions: ', s)
    def Sub(self):
        u=self.f1 - self.f2
        print('Sub of fractions: ',u)
    def Mult(self):
        m=self.f1*self.f2
        print('Mult of fractions: ',m)
    def Div(self):
        d=self.f1 / self.f2
        print('Div of fractions: ',d)
    
print('welcome !')
print('we need 4 ints for two fractions.')
print('please enter 4 num:')
n1=int(input())
d1=int(input())
n2=int(input())
d2=int(input())
p1 = f(n1,d1,n2,d2)
p1.Sum()
p1.Sub()
p1.Mult()
p1.Div()