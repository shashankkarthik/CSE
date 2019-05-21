class Vector(object):
    def __init__(self,x=0,y=0):
        if type(x) is not str and type(y) is not str:
            self.x = x
            self.y = y
    
    def __str__(self):
        x_str = str(round(self.x,2))
        y_str = str(round(self.y,2))
        
        vector_str = "("+ x_str + "," + y_str + ")"
        return vector_str
    
    def __repr__(self):
        return str(self)
    
    def magnitude(self):
        x = self.x
        y = self.y
        
        mag = (x**2+y**2)**0.5
        return mag
        
    def __eq__(self,other):
        if type(other) is Vector:
            x_bool = self.x == other.x
            y_bool = self.y == other.y
            
        return x_bool and y_bool
        
    def __add__(self,other):
        if type(other) is Vector:
            x_new = self.x + other.x
            y_new = self.y + other.y
        
        return Vector(x_new,y_new)
    
    def __sub__(self,other):
        if type(other) is Vector:
            x_new = self.x - other.x
            y_new = self.y - other.y
        
        return Vector(x_new,y_new)  
    
    def __mul__(self,other):
        if type(other) is Vector:
            x_new = self.x * other.x
            y_new = self.y * other.y
            return x_new + y_new
        if type(other) is float or type(other) is int:
            x_new = self.x * other
            y_new = self.y * other
            return Vector(x_new,y_new)
    
    def __rmul__(self,other):
        if type(other) is float or type(other) is int:
            x_new = self.x * other
            y_new = self.y * other
            return Vector(x_new,y_new)
            
        
        