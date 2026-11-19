# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 12
# Date: 19 November 2026

# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material

import matplotlib.pyplot as plt
import numpy as np

# 1
x = np.linspace(-2, 2, 100)
f1 = 2
f2 = 6
y1 = (1 / (4 * f1)) * x ** 2
y2 = (1 / (4 * f2)) * x ** 2

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y1, c="r", linewidth=f1, label=f"f={f1}")
plt.plot(x, y2, c="b", linewidth=f2, label=f"f={f2}")
plt.title("Parabola plots with varying focal length")
plt.legend()
plt.show()

# 2
x = np.linspace(-4, 4, 25)
y = 2 * x ** 3 + 3 * x ** 2 - 11 * x - 6

plt.scatter(x, y, marker="*", color='yellow', edgecolors='black', s=100)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Plot of cubic polynomial")
plt.show()

# 3

x = np.linspace(-2*np.pi, 2*np.pi, 100)
c = np.cos(x)
s = np.sin(x)

plt.subplot(212)
plt.plot(x, s, color='grey', label= 'sin(x)')
plt.yticks([-1,0,1])
plt.ylabel(' y=sin(x)')
plt.xlabel('x')
plt.grid(True)
plt.legend()

plt.subplot(211)
plt.plot(x, c, color='r', label='cos(x)')
plt.yticks([-1,0,1])
plt.ylabel('y=cos(x)')
plt.tick_params(labelbottom=False)
plt.title('Plot of cos(x) and sin(x)')
plt.grid(True)
plt.legend(loc="lower right")

plt.show()