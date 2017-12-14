import timeit
import copy
from functions import calculateFolding
from Algorithms.helpers import possibilityCheck
from Algorithms.helpers import validityCheck
from functions import calculateFolding
from classes import Protein

<<<<<<< HEAD
=======

>>>>>>> 3754943f54d3169243cb12d17bf1e090c92297fa
def depthFirst(inputPro):

    succes = 0
    bestScore = 0
    bestFolding = []

    # 0 == staigth; 1 == up; 2 == down; 3 == left; 4 == right;
    options = []
<<<<<<< HEAD
    counter = len(inputPro.proteinChain)
    for aminos in range(1,counter):
=======

    counter = len(inputPro.proteinChain)
    for aminos in range(counter):
>>>>>>> 3754943f54d3169243cb12d17bf1e090c92297fa
        options.append(0)
    counter -= 2

    while options[0] != 1:
        options[counter] += 1
        if options[counter] == 5:
            cancel = 0
            while True:
                if options[counter - cancel] == 5:
                    options[counter - cancel] = 0
                    options[(counter - cancel) - 1] += 1
                else:
                    break
                cancel += 1
        if not ('1,1,1,1' in str(options)) and not ('2,2,2,2' in str(options)) \
        and not ('3,3,3,3' in str(options)) and not ('4,4,4,4' in str(options)):
            solution = folder(options, inputPro)
            if solution != None:
                # Calculates the folding score
                oneScore = calculateFolding(solution, inputPro.proteinChain)

                # Updates 'bestScore' and 'bestFolding' if the folding is better, and
                # resets the coordinates
                if succes == 0:
                    bestScore = oneScore
                    bestFolding = solution
                elif oneScore > bestScore:
                    bestScore = oneScore
                    bestFolding = solution

                # Add one succes
                succes += 1

    print (bestFolding)
    print (bestScore)
    bestPro = Protein(inputPro.proteinChain)
    bestPro.strength = bestScore
    bestPro.aminoCoordinates= bestFolding
    return bestPro

<<<<<<< HEAD
def folder(directions, Protein):
    aminoCoordinates = [[0,0,0],[1,0,0]]
    span = len(directions)
    for aminozuur in range(1,span):
        direction = ((aminoCoordinates[aminozuur][0] - aminoCoordinates[aminozuur - 1][0]),\
        (aminoCoordinates[aminozuur][1] - aminoCoordinates[aminozuur - 1][1]),\
        (aminoCoordinates[aminozuur][2] - aminoCoordinates[aminozuur - 1][2]))
=======
def folder(directions, inputProtein):
    aminoCoordinates = [[0,0,0]]
    # print(directions)
    for aminozuur in range(len(directions)):
        if aminozuur == 0:
            direction = (0,1,0)
        else:
            direction = ((aminoCoordinates[aminozuur][0] - aminoCoordinates[aminozuur - 1][0]),\
            (aminoCoordinates[aminozuur][1] - aminoCoordinates[aminozuur - 1][1]),\
            (aminoCoordinates[aminozuur][2] - aminoCoordinates[aminozuur - 1][2]))
            # print (direction)
>>>>>>> 3754943f54d3169243cb12d17bf1e090c92297fa
        aminoCoordinates.append(copy.copy(aminoCoordinates[aminozuur]))
        if directions[aminozuur] == 0: # straight
            aminoCoordinates[aminozuur+1][0] += direction[0]
            aminoCoordinates[aminozuur+1][1] += direction[1]
            aminoCoordinates[aminozuur+1][2] += direction[2]
        elif directions[aminozuur] == 1 or directions[aminozuur] == 2: # up # down
            if direction == (1,0,0) or direction == (-1,0,0):
                if directions[aminozuur] == 1:
                    aminoCoordinates[aminozuur+1][0] += direction[0]
                else:
                    aminoCoordinates[aminozuur+1][0] -= direction[0]
            elif direction == (0,1,0) or direction == (0,-1,0) or direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminozuur] == 1:
                    aminoCoordinates[aminozuur+1][1] -= direction[1]
                else:
                    aminoCoordinates[aminozuur+1][1] += direction[1]
        elif directions[aminozuur] == 3 or directions[aminozuur] == 4: # left, right
            if direction == (1,0,0) or direction == (-1,0,0) or direction == (0,1,0) or direction == (0,-1,0):
                if directions[aminozuur] == 3:
                    aminoCoordinates[aminozuur+1][2] += direction[0]
                else:
                    aminoCoordinates[aminozuur+1][2] -= direction[0]
            elif direction == (0,0,1) or direction == (0,0,-1):
                if directions[aminozuur] == 3:
                    aminoCoordinates[aminozuur+1][0] -= direction[2]
                else:
                    aminoCoordinates[aminozuur+1][0] += direction[2]

    tuples = []
    tuples.append([tuple(l) for l in aminoCoordinates])
    # print (tuples)

    if len(set(tuples[0])) == len(aminoCoordinates):
        print (aminoCoordinates)
        return aminoCoordinates
    else:
        return None

    # scipy en numpy
