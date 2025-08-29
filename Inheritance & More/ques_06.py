#Override the __len__() method on Vector of problem 5 to display the dimension of the Vector

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
    
    def __len__(self):
        return 3
    
v1 = Vector(2,3,4)
v2 = Vector(5,6,7)  

print("Addition:", v1 + v2)
print("Dot Product:", v1 * v2)
print("Dimension of Vector:", len(v1))