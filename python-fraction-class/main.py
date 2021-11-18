#Atousa Niazi Abkoh-98440127-python-Fraction-class-OSLAb-T7_2
# n for numerator / d for denominator

class fraction:
    def __init__(self, n=0,d=None):
        self.n = n
        self.d=d
    def show(self):
        print(self.n,"/",self.d)
    def Sum(self,other):
        numerator=self.n*other.d+self.d*other.n
        denominator=self.d*other.d
        result=fraction(numerator,denominator)
        return result
    def Sub(self,other):
        numerator=self.n*other.d-self.d*other.n
        denominator=self.d*other.d
        result=fraction(numerator,denominator)
        return result
    def Mult(self,other):
        numerator=self.n*other.n
        denominator=self.d*other.d
        result=fraction(numerator,denominator)
        return result
    def Div(self,other):
        numerator=self.n*other.d
        denominator=self.d*other.n
        result=fraction(numerator,denominator)
        return result

    
print('welcome !')
print('we need 4 ints for two fractions.')
print('please enter 4 num:')
n1=int(input())
d1=int(input())
while d1==0:
    print('wrong num, try again:')
    d1=int(input())
n2=int(input())
d2=int(input())
while d2==0:
    print('wrong num, try again:')
    d2=int(input())
f1=fraction(n1,d1)
f1.show()

f2=fraction(n2,d2)
f2.show()

f3=f1.Sum(f2)
print('Sum:')
f3.show()

f3=f1.Sub(f2)
print('Sub:')
f3.show()

f3=f1.Mult(f2)
print('Mult:')
f3.show()

f3=f1.Div(f2)
print('Div:')
f3.show()
