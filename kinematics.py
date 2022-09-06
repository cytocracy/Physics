from vpython import *

scene.width = scene.height = 600
scene.title = "Basic Kinematics equation"

g = 9.8

#initialposition
x0 = 0
y0 = 200
v0 = 0



# Create a ball
ball = sphere(pos=vec(x0, y0, 0), radius=10, color=color.red)

#create floor
floor = box(pos=vec(0, 0, 0), size=vec(600, 10, 50), color=color.blue)



t=0
dt = 0.01



while True:

    ball.pos.y -= 1
    
    # ball.pos.y = y0 + v0 + 0.5 * -1* g * t**2

    # rate(100)

    # x0 = ball.pos.x
    # y0 = ball.pos.y

    # v0 = v0 + g * t
    # # print("Running")
    # t += dt    



