import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from scipy.integrate import solve_ivp
from math import cos 
from math import sin
from math import tan 

L = 1.0
g = 9.81
m = 1.0
M = 5.0

def fddtita(dtita, tita, dx, gamma):
    costita = cos(tita)
    sintita = sin(tita)
    t0 = g*sintita
    t1 = - (m/(M-m))*L*costita*sintita*((M * dx)/(m*L))**2
    t2 = -costita * gamma/(M-m)
    t3 = (1 + (m/(m-M))*L*costita**2)
    return (t0 + t1 + t2) / t3

def fddx(dtita, tita, dx, gamma):
    costita = cos(tita)
    sintita = sin(tita)
    t0_0 = ((M * dx)/(m*L))
    t0 =  -m * L * sintita * t0_0*t0_0
    t1 = m * L * costita * fddtita(dtita, tita, dx, gamma)
    t2 = -gamma
    t3 = M - m
    return (t0 + t1 + t2) / t3


def solve(dtita, tita, dx, x, gamma, time, h):
    res = []

    for i in range(int(time * (1 / h))):
        res.append((dtita, tita, dx, x))
        ddtita = fddtita(dtita, tita, dx, gamma)
        dtita = dtita + ddtita * h
        tita = tita + dtita * h

        ddx = fddx(dtita, tita, dx, gamma)
        dx = dx + ddx * h
        x = x + dx * h

        dtita = min(dtita, 1E10)
        tita = min(tita, 1E10)
        dx = min(dx, 1E10)
        x = min(x, 1E10)

    res.append((dx, x))

    return res

gamma = 0
tita0 = np.pi / 4
dtita0 = 0
x0 = 0
dx0 = 0
h = 0.01
time = 50
res = solve(dtita0, tita0, dx0, x0, gamma, time, h)


# Tiempo de integración
# t_span = (0, 10)  # Integrar desde 0 hasta 10 segundos
# t_eval = np.linspace(0, 10, 300)  # Muestras para la animación

# Resolver las ecuaciones diferenciales
# solution = solve_ivp(pendulum_eq, t_span, y0, t_eval=t_eval)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

ax.set_xlim(-4, 4)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

line, = ax.plot([], [], 'o-', lw=2)
anchor, = ax.plot(0, 0, 'ko')

def update(frame):
    theta = res[frame][1]
    x1 = res[frame][3]
    
    x = L * np.sin(theta) + x1
    y = L * np.cos(theta)
    
    line.set_data([x1, x], [0, y])
    
    return line,

interv = h * 100
ani = FuncAnimation(fig, update, frames=len(res), interval=interv, blit=True)
# ani = FuncAnimation(fig, update, frames=len(res), interval=50, blit=True)

ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])  # [izq, abajo, ancho, alto]
slider = Slider(ax_slider, 'Frame', -10, 10, valinit=0, valstep=1)
def on_slider_update(val):
    gamma = val
    # frame = int(slider.val)
    # update(frame)
    # fig.canvas.draw_idle()

slider.on_changed(on_slider_update)

plt.title("Simulación del Péndulo Simple")
plt.show()


'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
from math import cos 
from math import sin
from math import tan 

L = 1.0
g = -9.81
m = 5.0
M = 5.0

def fddtita(dtita, tita, dx, gamma):
    costita = cos(tita)
    sintita = sin(tita)
    t0 = -g*sintita
    t1 = (m/(M+m))*L*costita*sintita*((M * dx)/(m*L))**2
    t2 = gamma
    t3 = (1 + (m/(m+M))*L*costita**2)
    return (t0 -t1 + t2) / t3

def fddx(dtita, tita, dx, gamma):
    t0 = m * L * sin(tita)*((M * dx)/(m*L))**2
    t1 = m * L * cos(tita)*fddtita(dtita, tita, dx, gamma)
    t2 = gamma
    t3 = M + m
    return (t0 - t1 + t2) / t3

def solve(dtita, tita, dx, x, gamma, time, h):
    res = []

    for i in range(int(time * (1 / h))):
        res.append((dtita, tita, dx, x))
        ddtita = fddtita(dtita, tita, dx, gamma)
        dtita = dtita + ddtita * h
        tita = tita + dtita * h

        ddx = fddx(dtita, tita, dx, gamma)
        dx = dx + ddx * h
        x = x + dx * h

        dtita = min(dtita, 1E10)
        tita = min(tita, 1E10)
        dx = min(dx, 1E10)
        x = min(x, 1E10)

    res.append((dx, x))

    return res

gamma = 1
tita0 = 2 * np.pi
dtita0 = 0
x0 = 0
dx0 = 0
h = 0.01
time = 50
res = solve(dtita0, tita0, dx0, x0, gamma, time, h)


# Tiempo de integración
# t_span = (0, 10)  # Integrar desde 0 hasta 10 segundos
# t_eval = np.linspace(0, 10, 300)  # Muestras para la animación

# Resolver las ecuaciones diferenciales
# solution = solve_ivp(pendulum_eq, t_span, y0, t_eval=t_eval)

fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
line, = ax.plot([], [], 'o-', lw=2)

anchor, = ax.plot(0, 0, 'ko')

def update(frame):
    theta = res[frame][1]
    x1 = res[frame][3]
    
    x = L * np.sin(theta) + x1
    y = L * np.cos(theta)
    
    line.set_data([x1, x], [0, y])
    
    return line,

interv = h * 100
ani = FuncAnimation(fig, update, frames=len(res), interval=interv, blit=True)
# ani = FuncAnimation(fig, update, frames=len(res), interval=50, blit=True)

plt.title("Simulación del Péndulo Simple")
plt.show()

'''