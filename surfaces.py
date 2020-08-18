from euclidean_space import *
from colors import color
from matrices import matrix

class surface:
    
    def __init__(self,point,vect1,vect2,col):
        self.point = point
        self.vect1 = vect1
        self.vect2 = vect2
        
        self.color_surface = col
    
    def intersection(self,Lray):
        system = matrix([[self.vect1.x , self.vect2.x , -Lray.direction.x , Lray.origin.x-self.point.x],
                         [self.vect1.y , self.vect2.y , -Lray.direction.y , Lray.origin.y-self.point.y],
                         [self.vect1.z , self.vect2.z , -Lray.direction.z , Lray.origin.z-self.point.z]])
        
        system.echelon_reduce()
        
        
        if 1 in system[:,2].flat():
            index_value = system[:,2].flat().index(1)
        else:
            return False,0
        
        if 1 in system[:,0].flat():
            a_index = system[:,0].flat().index(1)
            a = system[a_index,3].flat()[0]
        else:
            a = 0
        
        if 1 in system[:,1].flat():
            b_index = system[:,1].flat().index(1)
            b = system[b_index,3].flat()[0]
        else:
            b = 0
        
        if abs(a) <= 1 and abs(b) <= 1:
            
            t_value = system[index_value,3].flat()[0]
            
            return True,t_value
        else:
            return False,0
