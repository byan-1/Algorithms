def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         assert isinstance(top,int) and isinstance(bottom,int), "Whole integers only"
         if top < 0 and bottom < 0:
            top = abs(top)
            bottom = abs(bottom)
         elif bottom < 0:
            top = -top
            bottom = abs(bottom)
         common = gcd(top,bottom)
         self.num = top//common
         self.den = bottom//common
         

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def getNum(self):
         return self.num
        
     def getDen(self):
         return self.den

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + self.den*otherfraction.num
         newden = self.den*otherfraction.den
         return Fraction(newnum,newden)

     def __radd__(self,otherfraction):
         return self.__add__(otherfraction)

     def __sub__(self, otherfraction):
         newnum = self.num*otherfraction.den - self.den*otherfraction.num
         newden = self.den*otherfraction.den
         return Fraction(newnum,newden)

     def __mul__(self, otherfraction):
         newnum = self.num*otherfraction.num
         newden = self.den*otherfraction.den
         return Fraction(newnum,newden)

     def __truediv__(self, otherfraction):
         newnum = self.num*otherfraction.den
         newden = self.den*otherfraction.num
         return Fraction(newnum,newden)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum == secondnum

     
     def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.__add__(other)

     def __repr__(self):
        return 'Fraction(%s, %s)' % (self.num, self.den)

x = Fraction(1,2)
y = Fraction(2,-3)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
z = Fraction(1, 2)
z += 5
print(z)
print(z.__repr__())
