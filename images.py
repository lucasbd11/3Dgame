from colors import color

class image:

    def __init__(self, lenght = 1, width = 1):
        self.lenght = lenght
        self.width = width
        #self.pixels = [[couleur(0,0,0) for i in range(width)] for i in range(lenght)]
        self.pixels = [[None for i in range(lenght)] for i in range(width)]
    
    def set_color(self,x,y,color_value):
        self.pixels[-(y+1)][x] = color_value
    
    def write_img(self,file):
        
        def redim_value(x): 
            return round(max(min(x,1),0)*255)
        
        
        file.write("P3\n{} {}\n255\n".format(self.lenght,self.width))
        
        
        
        for ligne in self.pixels:
            for pixel in ligne:
                try:
                    file.write("{}\n{}\n{}\n".format(redim_value(pixel.r),redim_value(pixel.g),redim_value(pixel.b)))
                except:
                    print(pixel)
                    print(ligne)
                    print(self.pixels.index(ligne))
                    file.write("{}\n{}\n{}\n".format(redim_value(pixel.r),redim_value(pixel.g),redim_value(pixel.b)))
                    raise "error"
            #file.write("\n")
    
        return file
