import turtle
def draw_sword():
    turtle.setup(800,600)
    turtle.pensize(2)
    turtle.title("sword")
    turtle.speed(10)
    #circulo
    turtle.up()
    turtle.goto(10,-70)
    turtle.down()
    turtle.circle(7)
    turtle.up()
    turtle.goto(10,-66)
    turtle.down()
    turtle.circle(3)
    #punho
    turtle.up()
    turtle.goto(7,-55)
    turtle.down()
    turtle.goto(7,-40)
    turtle.goto(13,-40)
    turtle.goto(13,-55)
    #guarda
    turtle.up()
    turtle.goto(2,-40)
    turtle.down()
    turtle.goto(20,-40)
    turtle.goto(0,-40)
    #lâmina
    turtle.up()
    turtle.goto(5,30)
    turtle.down()
    turtle.goto(5,-40)
    turtle.goto(15,-40)
    turtle.goto(15,30)
    turtle.goto(10,35)
    turtle.goto(5,30)
    #pegada
    turtle.up()
    turtle.goto(7,-50)
    turtle.down()
    turtle.goto(13,-50)
    turtle.up()
    turtle.goto(7,-45)
    turtle.down()
    turtle.goto(13,-45)
    turtle.up()
    turtle.goto(7,-42)
    turtle.down()
    turtle.goto(13,-42)
    #meio da lâmina
    turtle.up()
    turtle.goto(10,30)
    turtle.down()
    turtle.goto(10,-40)
    #marcas na lâmina
    turtle.up()
    turtle.goto(7,-45)
    turtle.down()
    turtle.goto(7.5,-45.5)
    
    turtle.up()
    turtle.goto(12,-20)
    turtle.down()
    turtle.goto(11.5,-20.5)
    
    turtle.up()
    turtle.goto(7,-11)
    turtle.down()
    turtle.goto(7.5,-11.5)

    turtle.up()
    turtle.goto(12, 4)
    turtle.down()
    turtle.goto(11.5, 4.5)
    
    turtle.up()
    turtle.goto(7,8)
    turtle.down()
    turtle.goto(7.7,7.3)
    
    turtle.up()
    turtle.goto(12,17)
    turtle.down()
    turtle.goto(11.5,17.5)
    pass

#FUNÇÃO ZOOM
def sword_zoom(zoom:float):
    turtle.setup(800,600)
    turtle.pensize(zoom*2)
    turtle.title("sword")
    turtle.speed(20)
    #circulo
    turtle.up()
    turtle.goto(zoom*10,zoom*-70)
    turtle.down()
    turtle.circle(zoom*7)
    turtle.up()
    turtle.goto(zoom*10,zoom*-66)
    turtle.down()
    turtle.circle(zoom*3)
    #punho
    turtle.up()
    turtle.goto(zoom*7,zoom*-55)
    turtle.down()
    turtle.goto(zoom*7,zoom*-40)
    turtle.goto(zoom*13,zoom*-40)
    turtle.goto(zoom*13,zoom*-55)
    #guarda
    turtle.up()
    turtle.goto(zoom*2,zoom*-40)
    turtle.down()
    turtle.goto(zoom*20,zoom*-40)
    turtle.goto(0,zoom*-40)
    #lâmina
    turtle.up()
    turtle.goto(zoom*5,zoom*30)
    turtle.down()
    turtle.goto(zoom*5,zoom*-40)
    turtle.goto(zoom*15,zoom*-40)
    turtle.goto(zoom*15,zoom*30)
    turtle.goto(zoom*10,zoom*35)
    turtle.goto(zoom*5,zoom*30)
    #pegada
    turtle.up()
    turtle.goto(zoom*7,zoom*-50)
    turtle.down()
    turtle.goto(zoom*13,zoom*-50)
    turtle.up()
    turtle.goto(zoom*7,zoom*-45)
    turtle.down()
    turtle.goto(zoom*13,zoom*-45)
    turtle.up()
    turtle.goto(zoom*7,zoom*-42)
    turtle.down()
    turtle.goto(zoom*13,zoom*-42)
    #meio da lâmina
    turtle.up()
    turtle.goto(zoom*10,zoom*30)
    turtle.down()
    turtle.goto(zoom*10,zoom*-40)
    #marcas na lâmina
    turtle.up()
    turtle.goto(zoom*7,zoom*-45)
    turtle.down()
    turtle.goto(zoom*7.5,zoom*-45.5)
    
    turtle.up()
    turtle.goto(zoom*12,zoom*-20)
    turtle.down()
    turtle.goto(zoom*11.5,zoom*-20.5)
    
    turtle.up()
    turtle.goto(zoom*7,zoom*-11)
    turtle.down()
    turtle.goto(zoom*7.5,zoom*-11.5)

    turtle.up()
    turtle.goto(zoom*12, zoom*4)
    turtle.down()
    turtle.goto(zoom*11.5,zoom* 4.5)
    
    turtle.up()
    turtle.goto(zoom*7,zoom*8)
    turtle.down()
    turtle.goto(zoom*7.7,zoom*7.3)
    
    turtle.up()
    turtle.goto(zoom*12,zoom*17)
    turtle.down()
    turtle.goto(zoom*11.5,zoom*17.5)
    pass

#FUNÇÃO POSIÇÃO
def pos_sword(x:int,y:int):
    turtle.setup(800,600)
    turtle.pensize(2)
    turtle.title("sword")
    turtle.speed(10)
    #circulo
    turtle.up()
    turtle.goto(x + 10,y-70)
    turtle.down()
    turtle.circle(7)
    turtle.up()
    turtle.goto(x + 10,y-66)
    turtle.down()
    turtle.circle(3)
    #punho
    turtle.up()
    turtle.goto(x + 7,y-55)
    turtle.down()
    turtle.goto(x + 7,y-40)
    turtle.goto(x + 13,y-40)
    turtle.goto(x + 13,y-55)
    #guarda
    turtle.up()
    turtle.goto(x + 2,y-40)
    turtle.down()
    turtle.goto(x + 20,y-40)
    turtle.goto(x + 0,y-40)
    #lâmina
    turtle.up()
    turtle.goto(x + 5,y + 30)
    turtle.down()
    turtle.goto(x + 5,y-40)
    turtle.goto(x + 15,y-40)
    turtle.goto(x + 15,y + 30)
    turtle.goto(x + 10,y + 35)
    turtle.goto(x + 5,y + 30)
    #pegada
    turtle.up()
    turtle.goto(x + 7,y-50)
    turtle.down()
    turtle.goto(x + 13,y-50)
    turtle.up()
    turtle.goto(x + 7,y-45)
    turtle.down()
    turtle.goto(x + 13,y-45)
    turtle.up()
    turtle.goto(x + 7,y-42)
    turtle.down()
    turtle.goto(x + 13,y-42)
    #meio da lâmina
    turtle.up()
    turtle.goto(x + 10,y + 30)
    turtle.down()
    turtle.goto(x + 10,y-40)
    #marcas na lâmina
    turtle.up()
    turtle.goto(x + 7,y-45)
    turtle.down()
    turtle.goto(x + 7.5,y-45.5)
    
    turtle.up()
    turtle.goto(x + 12,y-20)
    turtle.down()
    turtle.goto(x + 11.5,y-20.5)
    
    turtle.up()
    turtle.goto (x +7,y-11)
    turtle.down()
    turtle.goto(x + 7.5,y-11.5)

    turtle.up()
    turtle.goto(x + 12, y + 4)
    turtle.down()
    turtle.goto(x + 11.5, y + 4.5)
    
    turtle.up()
    turtle.goto(x + 7,y + 8)
    turtle.down()
    turtle.goto(x + 7.7,y + 7.3)
    
    turtle.up()
    turtle.goto(x + 12,y + 17)
    turtle.down()
    turtle.goto(x + 11.5,y + 17.5)
    pass

#FUNÇÃO COR
def sword_color(cor:int):
    turtle.color(cor)
    turtle.setup(800,600)
    turtle.pensize(2)
    turtle.title("sword")
    turtle.speed(10)
    #circulo
    turtle.up()
    turtle.goto(10,-70)
    turtle.down()
    turtle.circle(7)
    turtle.up()
    turtle.goto(10,-66)
    turtle.down()
    turtle.circle(3)
    #punho
    turtle.up()
    turtle.goto(7,-55)
    turtle.down()
    turtle.goto(7,-40)
    turtle.goto(13,-40)
    turtle.goto(13,-55)
    #guarda
    turtle.up()
    turtle.goto(2,-40)
    turtle.down()
    turtle.goto(20,-40)
    turtle.goto(0,-40)
    #lâmina
    turtle.up()
    turtle.goto(5,30)
    turtle.down()
    turtle.goto(5,-40)
    turtle.goto(15,-40)
    turtle.goto(15,30)
    turtle.goto(10,35)
    turtle.goto(5,30)
    #pegada
    turtle.up()
    turtle.goto(7,-50)
    turtle.down()
    turtle.goto(13,-50)
    turtle.up()
    turtle.goto(7,-45)
    turtle.down()
    turtle.goto(13,-45)
    turtle.up()
    turtle.goto(7,-42)
    turtle.down()
    turtle.goto(13,-42)
    #meio da lâmina
    turtle.up()
    turtle.goto(10,30)
    turtle.down()
    turtle.goto(10,-40)
    #marcas na lâmina
    turtle.up()
    turtle.goto(7,-45)
    turtle.down()
    turtle.goto(7.5,-45.5)
    
    turtle.up()
    turtle.goto(12,-20)
    turtle.down()
    turtle.goto(11.5,-20.5)
    
    turtle.up()
    turtle.goto(7,-11)
    turtle.down()
    turtle.goto(7.5,-11.5)

    turtle.up()
    turtle.goto(12, 4)
    turtle.down()
    turtle.goto(11.5, 4.5)
    
    turtle.up()
    turtle.goto(7,8)
    turtle.down()
    turtle.goto(7.7,7.3)
    
    turtle.up()
    turtle.goto(12,17)
    turtle.down()
    turtle.goto(11.5,17.5)
    pass
draw_sword()
sword_zoom(zoom=2)
pos_sword(x=-50,y=-50)
sword_color("red")    

turtle.done()

    