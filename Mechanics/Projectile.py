from vpython import *
canvas(width=1900, height=930, background=color.black)

ball = sphere(pos=vector(0,.1,0), radius=0.05, color=color.yellow, make_trail= True)
ground = box(pos=vector(0,0,0), size=vector(3,0.01,0.5))

g = vector(0,-9.81,0)
ball.m = 0.5
v0 = 3
theta = 75*pi/180
ball.v = vec(cos(theta),sin(theta),0)*v0

vscale =0.08
varrow = arrow(pos=ball.pos, axis=ball.v*vscale, color=color.red)

t = 0
dt = 0.01

while ball.pos.y-ball.radius >= ground.pos.y+ground.size.y:
   rate(100)
   F = g*ball.m
   a = F/ball.m
   ball.v = ball.v + a*dt
   ball.pos = ball.pos + ball.v*dt
   varrow.pos = ball.pos
   varrow.axis = ball.v*vscale
   t = t + dt
