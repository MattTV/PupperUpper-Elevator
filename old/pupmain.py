import pupdatabase as db
import pupalgo as algo

import time
import random

def main():
    for x in range(10):
        randomweight = random.random()
        print(f"Random Weight: {randomweight}, Time of Print: {time.time()}\nDate and Time from database: ")
        db.AddWeight(randomweight)

    print("Added items:\n")
    db.DumpAll()

    algo.CalculateBaseline()
    baseline = db.GetBaseline()

    print(f"Baseline: {baseline}\n")

    print(f"Exact: {algo.Warn(baseline)}\n")
    print(f"Above: {algo.Warn(baseline * 1.1)}\n")
    print(f"Below: {algo.Warn(baseline * 0.9)}\n")

if __name__ == "__main__":
    main()