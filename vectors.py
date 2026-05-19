class Vector2():
    def __init__(self,vec):
        self.x = vec[0]
        self.y = vec[1]
    def perp(self):
        return Vector2([self.y, -self.x])
    
class Vector3():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def DimensionDown(self):
        return [round(self.x/self.z), round(self.y/self.z)]
    
def DirVector(vec2,vec1):
    x = vec2[0] - vec1[0]
    y = vec2[1] - vec1[1]
    return Vector2([x,y])
    

def Normalise(num):
    return 1 if num > 0 else -1

def DotProd(vec1, vec2):
    x = vec1.x * vec2.x
    y = vec1.y * vec2.y
    return x+y