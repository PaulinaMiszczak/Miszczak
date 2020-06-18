def setup ():
    size (700,700)
    global kotek
    kotek = loadImage("kotek.jpeg")
    strokeWeight(8)
    noFill()


def draw ():
    global kotek 
    try:
        image(kotek, 250,250,400,266)
    except:
        text("Nie ma zdjecia", 200,200)
        stroke(255,0,0)
    else:
        stroke(0,0,255)
    finally:
        rect(250,250,400,266)
        
# 1,25pkt 
        
