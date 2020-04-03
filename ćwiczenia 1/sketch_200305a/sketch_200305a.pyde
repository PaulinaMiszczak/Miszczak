def setup():
    size(400,600)
    #point(50,50)
    #rectMode(CORNER)
    
    
def draw():
    print(mouseX,mouseY,mousePressed)
    #line(mouseX,mouseY,mouseX,mouseY)
    #rect(width/2,height/2,mouseX,mouseY)
    if mousePressed:
        rect(40,20,55,55)
    else:circle(50,50,60)
