def setup():
    size(300, 400)
    textSize(40)
    global k_zaznaczenia, k_bialy # warto czasem stworzyć zmienną po prostu dla czytelności :)
    k_zaznaczenia = (220, 130, 30, 50) 
    k_bialy = (255) # w przypadku białego, czarnego i szarości wystarczy jedna wartość
    
def draw():
    background(0)
    if keyPressed:
        if (key == CODED):
            if (keyCode == 37):
                fill(*k_zaznaczenia)
            if (keyCode == 39):
                fill(k_bialy)
        if (key == 'm'):
            fill(k_bialy)
    elif (mouseX > width/2-40) and (mouseX < width/2-20) and (mouseY > 160) and (mouseY < 200):
        fill(*k_zaznaczenia)
    else:
        fill(k_bialy)
        
    text("P", width/2-40, height/2)
    
    
    if keyPressed:
        if (key == CODED):
            if (keyCode == 39):
                fill(*k_zaznaczenia)
            if (keyCode == 37):
                fill(k_bialy)
        if (key == 'm'):
            fill(*k_zaznaczenia)
    else:
        fill(k_bialy)
            
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
    
# mały mankament: strzałki działają również, gdy nic nie jest zaznaczone, ale to było tricky ;)
# 2pkt
