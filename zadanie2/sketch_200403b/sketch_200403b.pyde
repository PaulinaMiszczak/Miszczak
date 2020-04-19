def setup():
    size (800, 600)
    frameRate(60)
    
    global x 
    x = 400
    global y 
    y = 300
    global Speedx
    Speedx = 5
    global Speedy
    Speedy = 5
    
    global slownik_kolorow
    slownik_kolorow = {"czerwony":(255,0,0,120), "niebieski":(0,0,255,120), "zielony":(0,255,0,120)} # ostatnia liczba odpowiada za przeźroczystość - jeśli ustawizs ją na zero, kolor nie będzie widoczny.
    global lista_kolorow
    lista_kolorow = []
    for klucz, wartosc in slownik_kolorow.items(): 
        lista_kolorow.append(wartosc)
    global iteracja_programu
    iteracja_programu = 0 
    
def draw():

    global x
    global y 
    global Speedx
    global Speedy
    x += Speedx
    if (x> width or x <0):
        Speedx = Speedx * -1
        
    y += Speedy
    if (y> width or y <0):
        Speedy = Speedy * -1
    
    ellipse(x,y,50,50)
    global iteracja_programu
    iteracja_programu +=1 

    fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    
    if mousePressed:
        exit()
        
#1,75
    
    

    

    
