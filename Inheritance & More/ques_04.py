#Write a class complex to represent complex numbers along with overloaded operators + and * which adds and multiplies them

class Complex:
    def __init__(self, real,img):
        self.real = real
        self.img = img
    
    def __add__(self,other):
        return Complex(self.real + other.real, self.img + other.img)
    
    def __mul__(self,other):
        return Complex(self.real * other.real - self.img * other.img, self.real * other.img + self.img * other.real)
    
    def __str__(self):
        return f"{self.real} + {self.img}i"
    
c1 = Complex(2,3)
c2 = Complex(4,5)
print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)