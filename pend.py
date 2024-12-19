import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
from math import cos 
from math import sin
from math import tan 

L = 1.0
g = 9.81
m = 1.0


def ddf(dtita, tita):
    return -g*sin(tita)


def solve(dx, x, time, h):
    res = []

    for i in range(int(time * (1 / h))):
        res.append((dx, x))
        ddx = ddf(dx, x)
        dx = dx + ddx * h
        x = x + dx * h

    res.append((dx, x))

    return res


tita0 = np.pi / 4
dtita0 = 0
h = 0.01
res = solve(dtita0, tita0, 10, h)


# Tiempo de integración
# t_span = (0, 10)  # Integrar desde 0 hasta 10 segundos
# t_eval = np.linspace(0, 10, 300)  # Muestras para la animación

# Resolver las ecuaciones diferenciales
# solution = solve_ivp(pendulum_eq, t_span, y0, t_eval=t_eval)

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
line, = ax.plot([], [], 'o-', lw=2)

anchor, = ax.plot(0, 0, 'ko')

def update(frame):
    theta = res[frame][1]
    
    x = L * np.sin(theta)
    y = -L * np.cos(theta)
    
    line.set_data([0, x], [0, y])
    
    return line,

interv = h * 100
ani = FuncAnimation(fig, update, frames=len(res), interval=50, blit=True)

plt.title("Simulación del Péndulo Simple")
plt.show()
