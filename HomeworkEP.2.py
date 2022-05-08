import turtle   
tao = turtle.Pen()  
tao.shape('turtle')
def RTG(x):   
    for i in range(4):  
        tao.forward(x)    
        tao.left(90)    

def Go(x,y): 
    tao.penup() 
    tao.goto(x,y) 
    tao.pendown() 

def CC(x):
    tao.circle(x)
Go(0,-50)
CC(50)
Go(-100,-100)
RTG(200)



    
