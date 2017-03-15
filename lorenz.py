#Euler's method to solve initial value problems
#import Tkinter for graphics
from Tkinter import *
from math import *
from array import *
\
#define the step size, smaller=more accurate (float)
dt = 0.001
#define the maximum x value
t_max = 60.0
#define Initial conditions theta=
x0 = 1.0
y0 = 0.0
z0 = 0.0
r = 20.0

sigma = 10
b = 8.0/3.0

#calculate where the last increment is based on the specified domain
max_increments = int(t_max/dt)
#Arrays to store calculated x and y coordinates
tArray=array('d',range(0,max_increments))
xArray=array('d',range(0,max_increments))
yArray=array('d',range(0,max_increments))
zArray=array('d',range(0,max_increments))


#Graphics stuff:
#create root and canvas
root = Tk()
width = 600
height = 600
canvas = Canvas(root,width=600,height=600)
canvas.pack()
root.canvas = canvas.canvas = canvas # Store canvas in root and in canvas itself for callbacks
#converts a cartesian coordinate to on screen coordinate for drawing (x)
def get_x_coord(x):
	center = width/2
	return x+center
#converts a cartesian coordinate to on screen coordinate for drawing (y)
def get_y_coord(y):
	center = height/2
	return center-y

#performs all of the scaling and drawing of points from xArray,yArray
# r is the radius of the dots for plotting
def draw(r):
	xMax = -float("inf")
	zMax = -float("inf")
	#find maximum value for plot scaling
	for j in range(0,max_increments):
		if(xArray[j]>xMax):
			xMax = xArray[j]
		if(zArray[j]>zMax):
			zMax = zArray[j]
	#draw axis
	canvas.create_line(0,height/2,width,height/2,dash=(3,2),fill="#a3a3a3")
	canvas.create_line(width/2,0,width/2,height,dash=(3,2),fill="#a3a3a3")
	canvas.create_text(width/2, 12, anchor=W, font="Times",text=int(round(zMax)))
	canvas.create_text(width-30, height/2+12, anchor=W, font="Times",text=int(round(xMax)))
	#print xMax
	#draw points
	for k in range(0,max_increments):
		u = get_x_coord(xArray[k]*(width/2)/xMax)
		v = get_y_coord(zArray[k]*(height/2)/zMax)
		canvas.create_oval(u-r,v-r, u+r,v+r)
	canvas.pack(fill=BOTH,expand=1)


def main():
    xArray[0] = x0
    yArray[0] = y0
    zArray[0] = z0
    
    for i in range(1,max_increments):
        tArray[i] = tArray[i-1] + dt
        xArray[i] = xArray[i-1] + sigma*(yArray[i-1]-xArray[i-1])*dt
        yArray[i] = yArray[i-1] + (-xArray[i-1]*zArray[i-1]+r*xArray[i-1]-yArray[i-1])*dt
        zArray[i] = zArray[i-1] + (xArray[i-1]*yArray[i-1] - b*zArray[i-1])*dt
    draw(0.01)
    root.mainloop()  # wait until window gets closed so graphics are displayed

main()
