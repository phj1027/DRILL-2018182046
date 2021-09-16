from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while 1:
        
    x=0
    while (x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)

    y=90
    while (y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y)
        y = y + 2
        delay(0.01)

    x=800
    while (x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x = x - 2
        delay(0.01)

    y=600
    while (y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y = y - 2
        delay(0.01)
          
  
    a = 0
    while (a > -360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400+ math.cos(a/ 360*2*math.pi) * 270, 350+ math.sin(a / 360*2*math.pi)*270 )
        a = a - 2
        delay(0.01)

    
    #다하고돌아오면 다시 그자리에서 사각형그리러가기 x=400에서 마저가는걸
    
close_canvas()
