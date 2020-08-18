import math




class color:
    """class permettant de manipuler avec simplicité des couleurs"""
    
    def __init__(self, r=0.0, g=0.0, b=0.0):
        self.r = r
        self.g = g
        self.b = b
    
    def __str__(self):
        return f"({self.r}r, {self.g}g, {self.b}b)"
        
    def __repr__(self):
        return f"couleur({self.r}r, {self.g}g, {self.b}b)"
    
    
    
    def __add__(self,other):
        """surcharge de l'addition pour les couleurs"""
        
        r = self.r + other.r
        g = self.g + other.g
        b = self.b + other.b
        
        return color(r,g,b)
        
    def __sub__(self,other):
        """surcharge de la soustraction pour les couleurs"""
        
        r = self.r - other.r
        g = self.g - other.g
        b = self.b - other.b
        
        return color(r,g,b)
    
    
    def __truediv__(self,value):
        """surcharge de la division pour les couleurs"""
        

        
        if type(value) == int or type(value) == float:
        
            r = self.r / value
            g = self.g / value
            b = self.b / value
            return color(r,g,b)
        
        else:
            raise TypeError("pas possible de multiplier une couleur avec autre chose qu'un entier ou flottant")


    def __mul__(self,value):
        """surcharge de la multiplication pour les couleurs"""
    
        if type(value) == int or type(value) == float:
        
            r = self.r * value
            g = self.g * value
            b = self.b * value
            return color(r,g,b)
        
        else:
            raise TypeError("pas possible de multiplier une couleur avec autre chose qu'un entier ou flottant'")
            
           
        
    def __rmul__(self,value):
        return self.__mul__(value)
