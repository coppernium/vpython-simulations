from vpython import *
canvas(width=1900, height=930, background=color.black)


# Constantes

R = 1
rpt = 0.01
N = 1000
n = 0

inside_shell = sphere(radius=R, color=color.blue, opacity=0.2)
while n < N:
    ptp = vector(R*(2*random()-1),R*(2*random()-1),R*(2*random()-1))
    if mag(ptp)<=(R-rpt/2):
        sphere(pos=ptp,radius=rpt)
        n = n+1


