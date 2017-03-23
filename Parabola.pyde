"""
    Map values from cartesian mathematics to screen resolution

    x_screen = w_screen / 2 + (w_screen * x_mathematics) / w_mathematics
    y_screen = h_screen / 2 - (h_screen * y_mathematics) / h_mathematics
"""
x = -3
xf = 3

def setup():
    size(500, 500)
    
def draw():
    global x
    global xf
    a = 1
    b = -3
    c = 0
    i = 0
    
    #X and Y axes
    stroke('#000000')
    strokeWeight(1)
    line(0, height/2, width, height/2)
    line(width/2, 0, width/2, height)
    
    i = x
    for i in range(int(x) , int(xf)):
        draw_x_marker(i)
        draw_y_marker(i)
        i+=1
    
    draw_parabola(a, b, c)
              
def draw_point(x, y):
    point(map(x, -3, 3, 0, 500), map(-y, -3, 3, 0, 500))
    
def draw_x_marker(a):
    line(map(a, -3, 3, 0, 500), height/2 - height*0.025, map(a, -3, 3, 0, 500),  height/2 + height*0.025)
    
def draw_y_marker(a):
    line(width/2 - width*0.025, map(a, -3, 3, 0, 500),  width/2 + width*0.025, map(a, -3, 3, 0, 500))
    
def draw_parabola(a, b, c):
    global x
    global xf
    
    #Parabola
    strokeWeight(1)
    stroke('#000000')
    noFill()
    beginShape()
    while(x < xf):
        y = a*x**2 + b*x  + c
        vertex(map(x, -3, 3, 0, 500), map(-y, -3, 3, 0, 500))
        x += 0.01   
    endShape()
    
    #if you don't force float cast, it might return an int. So, 2.0 or float(2*a)
    delta = b**2 - 4*a*c
    x1 = (-b + sqrt(delta))/(2.0*a)
    x2 = (-b - sqrt(delta))/(2.0*a)
    
    #Critical points
    strokeWeight(5)
    stroke('#FF0000')
    draw_point(x1, 0)
    draw_point(x2, 0)
    x0 = (-b)/(2.0*a) #if you don't force float cast, it might return an int. So, 2.0 or float(2*a)
    draw_point(x0, quadratic_equation(x0, a, b, c))
    
def quadratic_equation(x0, a, b, c):
    return a*(x0**2) + b*x0 + c
    
