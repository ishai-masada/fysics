from fysics import *
import matplotlib.pyplot as plt

bodies = [Point(Vector2(0, 5), Vector2(0, 100))]
altitudes = []

duration = 100
steps_per_sec = 2
gravity = Vector2(0, -9.8)
time = 0
while time < duration:
    time += 1 / steps_per_sec
    for body in bodies:
        altitudes.append(body.position.y)
        body.step(steps_per_sec, gravity) 

# plot
plt.plot(altitudes)
plot.show()
