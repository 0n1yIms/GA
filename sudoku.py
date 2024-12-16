import random





board = [
    5, 3, -1, -1, 7, -1, -1, -1, -1,
    6, -1, -1, 1, 9, 5, -1, -1, -1,
    -1, 9, 8, -1, -1, -1, -1, 6, -1,
    8, -1, -1, -1, 6, -1, -1, -1, 3,
    4, -1, -1, 8, -1, 3, -1, -1, 1,
    7, -1, -1, -1, 2, -1, -1, -1, 6,
    -1, 6, -1, -1, -1, -1, -1, 2, 8,
    -1, -1, -1, 4, 1, 9, -1, -1, 5,
    -1, -1, -1, -1, 8, -1, -1, 7, 9
]

def getBoard(i):
    for j in range(81):
        if board[j] == -1:
            i--
        if i == 0:
            return board[j]



individualSize = 51
populationSize = 100
i = [0] * 51

def fitness(x):
    error = 0

    # checkcolumn
    for i in range(9):
        for j in range(9):
            if getBoard(i * 9 + j) != x[i * 9 + j]:
                error += 1
            


    return 


def individuals():
    individuals = []

    for i in range(populationSize):
        individuals.append([random.randint(0, 9) for _ in range(individualSize)])

    return individuals


def sort(ev, individuals):
    individuals.sort(key=ev, reverse=True)


def cross(individuals):


def calculate():
    generation = 100

    currentGeneration = individuals()

    for i in range(generation):
        ev = fitness(currentGeneration)

        bestIndividual = sort(currentGeneration, ev)

        newGeneration = cross(bestIndividual)

        mutate(newGeneration)

        currentGeneration = newGeneration




