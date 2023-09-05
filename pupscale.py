import random
import pupdatabase as pupdb

def MeasureWeight():

    randomweight = random.random()

    pupdb.AddWeight(randomweight)

    print(f'Measured random weight: {randomweight}')

    return randomweight