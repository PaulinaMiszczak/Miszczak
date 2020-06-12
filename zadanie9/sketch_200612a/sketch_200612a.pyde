def setup ():
    size (700,700)
    global kotek
    kotek = loadImage("kotek.jpeg")


def draw ():
    global kotek 
    try:
        rect(250,250,400,266)
        stroke(0,0,255)
        strokeWeight(8)
        image(kotek, 250,250,400,266)
    except:
        text("Nie ma zdjecia", 200,200)
        stroke(255,0,0)
        strokeWeight(8)
        
