import math

class coordinate:
    """class permettant de manipuler avec simplicité des coordonnées, seul les opérations mathématiques utiles au programme seront implémentées"""
    
    def __init__(self,*args):
        if len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
            
        elif len(args) == 2:
            self.x = args[1].x - args[0].x
            self.y = args[1].y - args[0].y
            self.z = args[1].z - args[0].z
    
    def to_vector(self):
        return vector(self.x,self.y,self.z)
    
    
    def create(self,x,y,z):
        """ méthode permettant de créer un objet du même type que celui utilisé pour faire les opérations, grâce à sa surcharge """
        return coordinate(x,y,z)
    
    def __str__(self):
        return self.__repr__()
        
    def __repr__(self):
        return f"coordinate({self.x}, {self.y}, {self.z})"
    
   
    
    def __add__(self,other):
        """surcharge de l'addition pour les vecteurs"""
        
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        
        return self.create(x,y,z)
        
    def __sub__(self,other):
        """surcharge de la soustraction pour les vecteurs"""
        
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        
        return coordinate(x,y,z)
    
    
    def __truediv__(self,value):
        """surcharge de la division pour les vecteurs"""
        
        if not(type(value) in [vector,coordinate]):
            try:
                x = self.x / value
                y = self.y / value
                z = self.z / value
                return self.create(x,y,z)
            except:
                raise TypeError("pas possible de diviser par 0")
            
        
        else:
            raise TypeError("pas possible de diviser 2 vecteurs/coordonnées")

    def __mul__(self,value):
        """surcharge de la multiplication pour les vecteurs"""
        
        
        if not(type(value) in [vector,coordinate]):

            x = self.x * value
            y = self.y * value
            z = self.z * value

            return self.create(x,y,z)
        
        else:
            raise TypeError("pas possible de multiplier 2 vecteurs/coordonnées")
            
           
        
    def __rmul__(self,value):
        return self.__mul__(value)




class vector(coordinate):
    """class permettant d'utiliser des vecteurs pour faire des opérations mathématiques, cette class est dépendante de la class coordinate """

    def create(self,x,y,z):
        """ méthode permettant de créer un objet du même type que celui utilisé pour faire les opérations, grâce à sa surcharge """
        
        return vector(x,y,z)
        
    

    def __str__(self):
        return self.__repr__()
        
    def __repr__(self):
        return f"vector({self.x}, {self.y}, {self.z})"

    def norm(self):
        return math.sqrt((self.x)**2+(self.y)**2+(self.z)**2)
    
    def scalar_product(self,vect):
        return self.x*vect.x + self.y*vect.y + self.z*vect.z
        
    def normalize(self):
        return self / abs(self)
    
    def vector_product(self,vect):
        return vector(self.y*vect.z-self.z*vect.y,self.z*vect.x-self.x*vect.z,self.x*vect.y-self.y*vect.x)


    def __abs__(self):
        """moyen plus simple d'obtenir la norme"""
        
    

        
        return self.norm()




class ray:
    def __init__(self,origin,direction):
        self.origin = origin
        self.direction = direction.normalize()

    def __str__(self):
        self.__repr__()
        
    def __repr__(self):
        return f"ray(ori: ({self.origine.x}, {self.origine.y}, {self.origine.z}),dire: ({self.direction.x}, {self.direction.y}, {self.direction.z}))"
    
    
    
    def __call__(self,t):
        return self.get_pos(t)
    
    def get_pos(self,t):
        return self.origine+t*self.direction
