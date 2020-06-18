class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _xLinii_ = 0  
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class InnyKwadrat(Kwadrat): # trochę mało się różni jak na inny
    def sketchInny(self, x, y, linie):
        Kwadrat.sketch(self,x, y)
        przestrzen = self.bok/linie
        _xLinii_ = 0
        for linia in range(0, linie):
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=przestrzen
    
            
def setup():
    size(500, 500)
    malyKwadrat = InnyKwadrat (100.0)
    malyKwadrat.sketchInny(300,100,10)
    duzyKwadrat = InnyKwadrat(100.0)
    duzyKwadrat.sketchInny(50,200,20)
    malyInnyKwadrat = InnyKwadrat(10.0)
    malyInnyKwadrat.sketchInny(120,100,40)

# 1 pkt, nie liczę rzezy, które są tak jak w mojej klasie, bo mogły być skopiowane bez zrozumienia, jedynie ze zmianą nazw
