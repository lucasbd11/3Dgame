import copy

class matrix:
    def __init__(self,matr):
        
        self.matr = copy.deepcopy(matr)
        self.dim = (len(matr),len(matr[0]))
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        
        str_repr = "|"
        
        for y in range(self.dim[0]):
            
            for x in range(self.dim[1]):
                
                flat_matr = self[:,x].flat()
                longest_str = len(str(flat_matr[0]))
                
                for i in flat_matr[1:]:
                    if len(str(i)) > longest_str:
                        longest_str = len(str(flat_matr[i]))
                
                longest_str += 1

                str_repr += str(self[y,x].matr[0][0]) + " "*(longest_str-(len(str(self[y,x].matr[0][0]))))
            
            
            str_repr += "|\n|"
        
        return str_repr[:-1]
    
    
    
    
    def __getitem__(self,key):
        
        if str(type(key[0])) == "<class 'int'>":
            key = (slice(key[0],key[0]+1,None),key[1])
        
        if str(type(key[1])) == "<class 'int'>":
            key = (key[0],slice(key[1],key[1]+1,None))
            
        selected_lines = self.matr[key[0]]
        

        for selected_column_index in range(len(selected_lines)):
            selected_lines[selected_column_index] = selected_lines[selected_column_index][key[1]]
        
        return matrix(selected_lines)
    
    
    def __delitem__(self,key):
        
        if str(type(key[0])) == "<class 'int'>":

            key = (slice(key[0],key[0]+1,None),key[1])
        
        if str(type(key[1])) == "<class 'int'>":
            key = (key[0],slice(key[1],key[1]+1,None))
            
        del self.matr[key[0]]
        

        for selected_column_index in range(len(self.matr)):
            del self.matr[selected_column_index][key[1]]

    def __mul__(self,value):
        matr_bis = copy.deepcopy(self.matr)
        for y in range(len(self.matr)):
            for x in range(len(self.matr[0])):
                matr_bis[y][x] *= value
        return matrix(matr_bis)
    
    def __rmul__(self,value):
        return self.__mul__(value)


    def __add__(self,value):
        matr_bis = copy.deepcopy(self.matr)

        for y in range(len(self.matr)):
            for x in range(len(self.matr[0])):
                if type(value) == matrix:
                    matr_bis[y][x] += value.matr[y][x]
                else:
                    matr_bis[y][x] += value
        return matrix(matr_bis)
    
    def __radd__(self,value):
        return self.__add__(value)
    
    def __sub__(self,value):
        matr_bis = copy.deepcopy(self.matr)
        for y in range(len(self.matr)):
            for x in range(len(self.matr[0])):
                if type(value) == matrix:
                    matr_bis[y][x] -= value.matr[y][x]
                else:
                    matr_bis[y][x] -= value
        return matrix(matr_bis)
    
    def __truediv__(self,value):
        matr_bis = copy.deepcopy(self.matr)
        for y in range(len(self.matr)):
            for x in range(len(self.matr[0])):
                matr_bis[y][x] /= value
        return matrix(matr_bis)
    
    
    def transpose(self):
        
        
        new_matr = [[None for i in range(self.dim[0])] for n in range(self.dim[1])]
        
        for y in range(len(self.matr)):
            for x in range(len(self.matr[0])):
                new_matr[x][y] = self.matr[y][x]
        return matrix(new_matr)
    
    def __setitem__(self,key,other):
        
        if str(type(key[0])) == "<class 'int'>":

            key = (slice(key[0],key[0]+1,None),key[1])
        
        if str(type(key[1])) == "<class 'int'>":
            key = (key[0],slice(key[1],key[1]+1,None))
        
        
        matr_bis = copy.deepcopy(self.matr)
        
        matr_lines_selected = self.matr[key[0]]
        

        for i in range(len(other.matr)):
            matr_lines_selected[i][key[1]] = other.matr[i]
        

        
        matr_bis[key[0]] = matr_lines_selected
        
        
        
        self.matr = matr_bis
    
    def flat(self):
        list_elements = []
        for y in self.matr:
            for x in y:
                list_elements += [x]
        return list_elements
    
    def echelon_reduce(self):
        
        pivot_rank = 0
        
        for x in range(self.dim[0]):
            y = pivot_rank

            pivot = self[y,x]
            
            
            while pivot.matr[0][0] == 0 and y < self.dim[0]-1:
                y += 1
                
                pivot = self[y,x]
            
            
            
            if pivot.matr[0][0] != 0:
                
                self[y,x:] = self[y,x:]/self[y,x].matr[0][0]
                
                self[pivot_rank,:],self[y,:] = self[y,:],self[pivot_rank,:]
                
                for y_bis in range(x+1,self.dim[0]):
                    self[y_bis,:] = self[y_bis,:]-self[y_bis,x].matr[0][0]*self[x,:]
                
                pivot_rank += 1
        
        for x in range(self.dim[0]-1,-1,-1):
            y_pivot = 0
            flat_column = self[:,x].flat()
            for y in range(len(flat_column)):
                if flat_column[y] != 0:
                    y_pivot = y
            if self[y_pivot,:x].flat().count(0) == len(self[y_pivot,:x].flat()):
                for y in range(y_pivot-1,-1,-1):
                    self[y,:] = self[y,:]-self[y,x].matr[0][0]*self[y_pivot,:]
                
                
                
