import pupdatabase as db

def CalculateBaseline():
    weights = db.GetTen()
    baseline = sum(weights[0]) / len(weights)
    db.SetBaseline(baseline)

def Warn(weight):
    if weight > db.GetBaseline() * 1.05 or weight < db.GetBaseline() * 0.95:
        return True
    else:
        return False