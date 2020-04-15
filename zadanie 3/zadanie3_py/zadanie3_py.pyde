def setup():
    size(300, 400)
    textSize(40)

def draw():
    background(0)
    if keyPressed:
        if (key == CODED):
            if (keyCode == 37):
                fill(220, 130, 30, 50)
        if (key == CODED):
            if (keyCode == 39):
                fill(255, 255, 255, 255)
    if keyPressed:
        if (key == 'm'):
            fill(255, 255, 255, 255)
    elif (mouseX > width/2-40) and (mouseX < width/2-20) and (mouseY > 160) and (mouseY < 200):
        fill(220, 130, 30, 50)
    else:
        fill(255,255,255,255)
        
    text("P", width/2-40, height/2)
    
    
    if keyPressed:
        if (key == CODED):
            if (keyCode == 39):
                fill(130,220,30,80)
            if (keyCode == 37):
                fill(255, 255, 255, 255)
        if (key == 'm'):
            fill(130,220,30,80)
    else:
        fill(255,255,255,255)
        
        
    text("M", width/2, height/2)
    
    s = createShape()
    s.beginShape()
    s.fill(0,0,255,255)
    s.stroke(0,0,255,255)
    s.vertex(300, height/2+80)
    s.vertex(330, height/2+90)
    s.vertex(width/2-40, height/2+40)
    s.vertex(width/2-10, height/2+40)
    s.vertex(width/2+120, height/2+110)
    s.endShape(CLOSE) 
    shape(s, 15, 0)
