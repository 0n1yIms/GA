import os
import math
import time

g = 9.81        # Gravedad (m/s^2)
dt = 0.01       # Intervalo de tiempo (s)
stiffness = 0.9 # Rigidez de la cuerda
numParticles = 10  # Número de partículas en la cuerda
segmentLength = 2.0 # Longitud entre partículas

class Particle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.fixed = False

def aplicarGravedad(p):
    if (p.fixed == False):
        p.vy += g * dt;
    
def actualizarParticula(p):
    if (p.fixed == False):
        p.x += p.vx * dt;
        p.y += p.vy * dt;
    
def aplicarRestriccion(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    L = math.sqrt(dx * dx + dy * dy)
    diff = L - segmentLength
    a = (dx / L) * diff
    b = (dy / L) * diff

    if (p2.fixed == False):
        p2.x -= a
        p2.y -= b

    # dist = math.sqrt(dx * dx + dy * dy)
    # diff = (dist - segmentLength) / dist
    # if (p1.fixed == False):
        # p1.x += stiffness * diff * dx
        # p1.y += stiffness * diff * dy
    # if (p2.fixed == False):
        # p2.x -= stiffness * diff * dx
        # p2.y -= stiffness * diff * dy

def dibujarCuerda(particles):
    os.system("cls")
    for j in range(20):
        for i in range(40):
            particleFound = False
            for p in particles:
                if (int(p.x) + 10 == i and int(p.y) == j):
                    print("O", end="")
                    particleFound = True
                    break
            
            if (particleFound == False):
                print(".", end="")
        
        print()
    

particles = []

# Inicializamos la cuerda en posición horizontal
for  i in range(numParticles):
    part = Particle()
    part.x = i * segmentLength
    part.y = 0
    part.fixed = i == 0
    particles.append(part)
    

while (True):
    # Aplicamos la gravedad y actualizamos las partículas
    for p in particles:
        aplicarGravedad(p);
        actualizarParticula(p);

    # Aplicamos restricciones de distancia entre partículas adyacentes
    for i in range(numParticles - 1):
        aplicarRestriccion(particles[i], particles[i + 1]);

    # Dibujamos la cuerda
    dibujarCuerda(particles);

    # Pausa
    time.sleep(0.001)
