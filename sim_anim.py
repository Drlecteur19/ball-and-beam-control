# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:02:00 2026

@author: DR lecteur

"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


m = 0.1      #  (kg)
R = 0.02     # (m)
g = 9.81     #  (m/s^2)
J = (2/5) * m * R**2 # 
L = 0.5   # beam length = 50 cm
# diff equation: [r', r'']
def ball_beam(y, t, theta):
    r, v = y
    drdt = v
    # d2rdt2 = -(mg * sin(theta)) / (m + J/R^2)
    # note:using theta like an an canstant input
    c = 0.8 # friction
    d2rdt2 = -(5/7)*g*np.sin(theta) - c*v
    if abs(r) >= L/2:
        v = 0
        drdt = 0
        d2rdt2 = 0
    return [drdt, d2rdt2]

#
t = np.linspace(0, 5, 100) # 5s sim
theta = np.radians(5)      #  5 degree of beam
y0 = [0.1, 0]              # the ball start at pos=0.1 at 0s

#solution
sol = odeint(ball_beam, y0, t, args=(theta,))

#plot
plt.plot(t, sol[:, 0])
plt.savefig("results.png", dpi=300)
plt.xlabel('Time (s)')
plt.ylabel('Ball Position (m)')
plt.title('Ball Motion on Beam (Open Loop)')
plt.grid()
plt.show()
