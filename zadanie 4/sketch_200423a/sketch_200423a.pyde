def setup():
    global img
    size(500,500) # to nie są proporcje zdjęcia dokumentowego
    img = loadImage("portret.jpg")
    
    
    
def draw():
    background(255,239,213)
    global img
    image(img, 0,0, height/2, width/2)
    
    s = createShape()
    s.beginShape()
    s.fill(255,150,200,100)
    s.stroke(0,0,0,20)
    s.vertex(200, height/2-15)
    s.vertex(200, height/2+15)
    s.vertex(width/2, height/2-15)
    s.vertex(width/2, height/2+15)
    s.vertex(width/2, height/2+15)
    s.endShape(CLOSE) 
    shape(s, -146, -120)
     
      
        
def mousePressed():
    exit()
    
# gdzie eksport do pdf'a?

# 0,75pkt
