from functions import calculateFolding
from Algorithms import helpers

def randomizer (Protein, tries):

    aminoCoordinates = [(0,0),(0,1)]

    tries = tries
    success = 0
    stuck = 0
    loops = 0

    bestScore = 0
    bestFolding = []

    while success != tries:

        for amino in range(2,len(Protein.proteinChain)):

            # Generate possibilities for neighboring locations
            left, right, up, down = helpers.possibilityCheck(amino, aminoCoordinates)

            # Randomly picks one of the directions, checks if it's valid, and adds it to 'aminoCoordinates'
            valid = helpers.validityCheck(left, right, up, down, aminoCoordinates, 'randomizer')
            if valid != None:
                aminoCoordinates.append(valid)
            else:
                stuck = 1
                break

        if stuck == 0:
            # Calculates the folding score
            oneScore = calculateFolding(aminoCoordinates, Protein.proteinChain)

            # Updates 'bestScore' and 'bestFolding' if the folding is better, and
            # resets the coordinates
            if success == 0:
                bestScore = oneScore
                bestFolding = aminoCoordinates
            elif oneScore > bestScore:
                bestScore = oneScore
                bestFolding = aminoCoordinates

            # Add one succes
            success += 1

        # Resets values for a new try
        loops += 1
        stuck = 0
        aminoCoordinates = [(0,0),(0,1)]

    # print(loops)
    return [bestFolding, bestScore]
