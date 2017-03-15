import Tkinter as tk 
from math import *
from array import *

#step size
dt = 0.05
#total time
t_max = 600.0
#initial conditions
theta0 = 6*pi/8
omega0 = 0.0
#gravity, mass, length, velocity, drag, driving frequency, driving force
g = 9.8
m = 10.0
l = 98.0
v = 0.0
q = 0.05
dfreq = 1.0/3.0
dforce = .003

radius = 10

#window dimensions
width = 600
height = 600

#calculate where the last increment is based on the specified domain
max_increments = int(t_max/dt)
#Arrays to store calculated x and y coordinates
time = array('d',range(0,max_increments))
omega = array('d',range(0,max_increments))
theta = array('d',range(0,max_increments))
length = array('d',range(0,max_increments))

class Pendulum(object):
    def __init__(self, canvas, *args, **kwargs):
        self.canvas = canvas
        self.mid = canvas.create_oval(*args, **kwargs)
        self.sid = canvas.create_line(width/2, height/2, sin(theta0)*l + width/2, cos(theta0)*l + height/2)
        self.vx = 5
        self.vy = 0
    def move(self, t):
        x = sin(theta[t])*length[t] + width/2.0
        y = cos(theta[t])*length[t] + height/2.0
        self.canvas.coords(self.mid, x-radius, y-radius, x+radius, y+radius)
        self.canvas.coords(self.sid, width/2, width/2, x, y)

class App(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.canvas = tk.Canvas(self.master, width = 600, height = 600)
        self.canvas.pack()
        self.pendulums = [
            Pendulum(self.canvas, sin(theta0)*l + width/2 - radius, cos(theta0)*l + height/2 -radius, sin(theta0)*l + width/2 + radius, cos(theta0)*l + height/2 +radius, outline = 'white', fill = 'blue')
            ]
        self.canvas.pack()
        self.canvas.create_oval(width/2-5,height/2-5,width/2+5,height/2+5)
        self.t = 0
        self.master.after(0, self.calculate)
        self.master.after(0, self.animation)

    def calculate(self):
        omega[0] = omega0
        theta[0] = theta0
        length[0] = l
        for i in range(1, max_increments):
            time[i] = time[i-1] + dt
            #length[i] = length[i-1] + sin(time[i])*1.6
            length[i] = length[i-1] + .1
            omega[i] = omega[i-1] - (g/length[i])*sin(theta[i-1])*dt
            #forcing
            omega[i] = omega[i] + dforce*sin(dfreq*time[i-1])*dt
            omega[i] = omega[i] - q*omega[i-1]*dt
            theta[i] = theta[i-1] + omega[i]*dt
            #keep -pi<theta<pi
            if(theta[i]>pi):
                theta[i] = theta[i] - 2*pi
            if(theta[i]<-pi):
                theta[i] = theta[i] + 2*pi

    def animation(self):
        self.t = self.t+1
        if(self.t>max_increments):
            self.t = 0
        for p in self.pendulums:
            p.move(self.t)
            self.master.after(12, self.animation)

root = tk.Tk()
app = App(root)
root.mainloop()
