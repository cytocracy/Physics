from vpython import *

scene.width = scene.height = 600
scene.title = "Basic Kinematics equation"

x0 = 0
y0 = 10
v0 = 0

ball = sphere(pos=vec(x0, y0, 0), radius=0.5, color=color.red)
ball.velocity = vec(0, v0, 0)
floor = box(pos=vec(0, 0, 0), size=vec(30, 1, 1), color=color.blue)

t=0
dt = 0.005
g = 9.8

while True:
    rate(400)
    if ball.pos.y < floor.pos.y + ball.radius*2:
        ball.pos.y = floor.pos.y + ball.radius*2
        ball.velocity.y = -ball.velocity.y * 0.9


    ball.velocity.y = ball.velocity.y - g*dt
    ball.pos = ball.pos + ball.velocity*dt
    t+=dt

