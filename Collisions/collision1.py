from vpython import *
canvas(width=1900, height=930, background=color.black)

R = 100
mass = 1

shell = sphere(pos=vec(0,0,0), radius=R, color=color.white, opacity=0.25)
ball = sphere(pos=vec(0,0,0), radius=R*0.01, m = mass, color = color.yellow, make_trail = True)

v0 = 20
ball.p = vec(1,1,0)*ball.m*v0
t = 0
dt = 0.01

while t < 50:
    rate(100)
    # ball.p = ball.p + 0
    ball.pos = ball.pos + ball.p*dt/ball.m

    if mag(ball.pos) + ball.radius >= shell.radius:
         ball.p = ball.p*(-1)
    t = t + dt
