cycle = 1

def MeasureWeight():

    weight = 0
    global cycle

    match(cycle):
        case 1:
            weight = 24
            cycle += 1
        case 2:
            weight = 26
            cycle += 1
        case 3:
            weight = 30
            cycle = 1

    print(f'Measured weight: {weight}')

    return weight