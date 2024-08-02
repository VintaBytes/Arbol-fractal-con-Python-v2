from turtle import *
import time
import random

speed(10) 
rt(-90) 
angle = 10

def y(sz, level): 
    final_level = level   
    if level > 0: 
        colormode(255)

        #Según sea el nivel, realizo modificaciones los parametros de las ramas
        if level < 7:
            #Ramas mas cercanas a la copa
            if level == 1:
                pensize(6)
            else:
                pensize(level*1.5)
            largo  = 0.8 * (sz + random.randrange(-2,15))
            colorR = 200 - level*15
            colorG = 100 + level*15
            colorB =  47 - level 
            angulo = angle + random.randrange(0,int(8-level)*3) # Mayor valor, mas ángulo en las ramas altas
        else:
            #Ramas mas cercanas a la base
            pensize(level) # Grosor de las ramas
            largo  = 0.9 * sz + random.randrange(-12,15)
            colorR = 141 - level*4
            colorG =  70 - level*2
            colorB =  47 - level     
            angulo = angle + level* random.randrange(0,15)/15   # Mayor valor, mas ángulo en las ramas bajas

        #Determino si se realiza o no la rama:
        #Si está por encima de determinado nivel, puede que la rama no esté.
        if  (random.randrange(1,100) > (level*4) ) or (level > random.randrange(7,12)):
            print (level)
            # Rama 1
            pencolor(colorR, colorG, colorB) 
            fd(largo) 
            rt(angulo) 
            y(largo, level-1) 

            # Rama 2, 50% de posibilidad de ser dibujada.
            if  (random.randrange(1,100) > 50):
                penup()
            pencolor(colorR, colorG, colorB) 
            lt( 2 * angulo ) 
            y(largo, level-1) 
            pendown()
            
            pencolor(colorR, colorG, colorB)   
            rt(angulo) 
            fd(-largo) 

setup(1024, 800, 0, 0)
penup()
goto(0,-350)
pendown()
time.sleep(8)          
y(80, 14) 
exitonclick()