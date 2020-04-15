def setup():
    size(400,600)
    #point(50,50)
    #rectMode(CORNER)
    
    
def draw():
    print(mouseX,mouseY,mousePressed)
    #line(mouseX,mouseY,mouseX,mouseY)
    #rect(width/2,height/2,mouseX,mouseY)
    if mousePressed:
        rect(width/10,20,55,55) # tam gdzie się da, warto stosować zmienne zależne
    else:
        circle(50,50,height/10)
# 1,5pkt
