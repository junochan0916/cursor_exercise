import numpy as np
import matplotlib.pyplot as plt

g = 9.81

def fall_time(height):
    t = np.sqrt(2 * height / g)
    return t

height = input("Enter height in meters: ")

time = fall_time(height)

print("Fall time =", time, "seconds")

t = np.linspace(0, time, 100)

y = height - 0.5 * g * t**2

plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Free Fall")

plt.show()

print("Final height =", y[100])
