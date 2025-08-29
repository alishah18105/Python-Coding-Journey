#Create a class vector representing a vector of 3 dimensions. overload the + and * operators which calculates the sum
# and dot productor of them

class Vector:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z 

    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z) 
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
v1 = Vector(2,3,4)
v2 = Vector(5,6,7)  

print("Addition:", v1 + v2)
print("Dot Product:", v1 * v2)