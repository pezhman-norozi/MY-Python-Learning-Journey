class Circle() :
    pi = 3.1415
    
    def __init__(self , r ):
        self.r = r
    def masahat(self):
        m = self.r * self.r * Circle.pi
        return m
    
c1 = Circle ( int ( input()))
print (c1.masahat()) 