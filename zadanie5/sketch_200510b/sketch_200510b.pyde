class kolo():
    ilosc_klikniec = 0 

    
    def __init__ (self,arg_x, arg_y, arg_r):
    
        self.obrot = 0
        self.klikniety = False
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r
    
        
    def rysuj(self):
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+90), PI+ radians(self.obrot+90)) 
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+100), PI+ radians(self.obrot+100))
    def obroty(self,stopnie):
        self.obrot += stopnie
    def wcisnij(self): 
        kolo.ilosc_klikniec +=1 
        self.kilkniety = not self.klikniety 
        if self.klikniety:
            fill(255)
        else:
            fill(0)

def setup():
    size (300,300)
    global przycisk
    przycisk = kolo(width/2, height/2, 50)
    
def mouseClicked():
    przycisk.wcisnij()    
    
def draw():
    background(0)
    przycisk.rysuj()
    print(kolo.ilosc_klikniec)
    circle(50,60,50)
    fill(255)

# bardzo mocno wzorowane z mojego kodu, widać brak głębszego zrozumienia, do tego literóki uniemożliwiające działanie
# 0,5p
