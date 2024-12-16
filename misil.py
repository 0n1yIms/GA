import math
import random

pi = math.pi
g = 9.81
dx = 0.01

# x = x0 + vix * t
# y = y0 + viy * t + 1/2 * g * t^2

class Misil:
    def __init__(self):
        self.vi = 0
        self.ang = 45

    @classmethod
    def create(cls, vi, ang):
        m = cls()
        m.vi = vi
        m.ang = ang
        return m



def getExplosionPos(misil):
    x0 = 0
    y0 = 0.01

    vix = misil.vi * math.cos(misil.ang)
    viy = misil.vi * math.sin(misil.ang)

    x = x0
    y = y0
    t = 0
    while (y > 0):
        x += vix * dx
        y += viy * dx - 1/2 * g * (dx)**2

        viy -= g * dx
        t += dx

    # print(x, y, t)
    return x

misil = Misil()
misil.vi = 10
misil.ang = 45

xpos = getExplosionPos(misil)
print (xpos)


XWanted = 8

popSize = 100

def population():
    pop = []
    for i in range(popSize):
        misil = Misil()
        misil.vi = random.uniform(0, 10.0)
        misil.ang = random.uniform(0, 90)
        pop.append(misil)

    return pop

def fitness(pop):
    fit = []
    for misil in pop:
        fit.append(abs(getExplosionPos(misil) - XWanted))

    return fit

def sortPop(pop, fit):
    for i in range(len(pop)):

        idx = i
        for j1 in range(len(pop) - i):
            j = i + j1
            if fit[idx] > fit[j]:
                idx = j

        pop[i], pop[idx] = pop[idx], pop[i]
                
    # return pop
    

    # for i in range(len(pop)):
        # for j in range(len(pop) - i - 1):
            # if fit[j] > fit[j + 1]:
                # fit[j], fit[j + 1] = fit[j + 1], fit[j]
                # pop[j], pop[j + 1] = pop[j + 1], pop[j]

def cross(pop):
    newPop = pop[: len(pop) // 2]
    for i in range(len(pop) // 2):
        cross = Misil()
        idx1 = random.randint(0, len(pop) // 2 - 1)
        idx2 = random.randint(0, len(pop) // 2 - 1)
        cross.vi = pop[idx1].vi
        cross.ang = pop[idx2].ang
        newPop.append(cross)

    return newPop

def mutate(pop):
    for i in range(len(pop)):
        if random.uniform(0, 1) < 0.1:
            pop[i].vi = random.uniform(0, 100)
            pop[i].ang = random.uniform(0, 90)

pop = population()
generations = 100
for i in range(generations):
    fit = fitness(pop)
    sortPop(pop, fit)
    pop = cross(pop)
    mutate(pop)
    print(i * 100 // generations)

sortPop(pop, fitness(pop))
print(pop[0].vi, pop[0].ang)
print(getExplosionPos(pop[0]))

# pop = [Misil.create(10, 25), Misil.create(10, 45)]
# print([getExplosionPos(p) for p in pop])
# print(fitness(pop))
# sortPop(pop, fitness(pop))
# print([getExplosionPos(p) for p in pop])
# newPop = cross(pop)
# print([getExplosionPos(p) for p in newPop])
# mutate(newPop)
# print([getExplosionPos(p) for p in newPop])