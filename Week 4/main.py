import random
import numpy as np
import matplotlib.pyplot as plt
from P3C import P3C
from PMISC import PMISC
from FastP3C import FastP3C
from FastPMISC import FastPMISC
from RandomP3C import RandomP3C
from RandomPMISC import RandomPMISC
from FastUP3C import FastUP3C

def single_run(n, algorithm, debug=False):
    if algorithm == "P3C":
        p3c = P3C(n=n)
        return p3c.run(debug=debug)
    elif algorithm == "PMISC":
        pmisc = PMISC(n=n)
        return pmisc.run(debug=debug)
    elif algorithm == "FastP3C":
        fastp3c = FastP3C(n=n)
        return fastp3c.run(debug=debug)
    elif algorithm == "FastPMISC":
        fastpmisc = FastPMISC(n=n)
        return fastpmisc.run(debug=debug)
    elif algorithm == "RandomP3C":
        randomp3c = RandomP3C(n=n)
        return randomp3c.run(debug=debug)
    elif algorithm == "RandomPMISC":
        randompmisc = RandomPMISC(n=n)
        return randompmisc.run(debug=debug)
    elif algorithm == "FastUP3C":
        fastup3c = FastUP3C(n=n)
        return fastup3c.run(debug=debug)

def simulate(n, algorithm, simulations):
    steps = []
    for _ in range(simulations):
        steps.append(single_run(n, algorithm))
    return steps

if __name__ == "__main__":  
    n = 10

    # Test single run
    # print(f"Steps: {single_run(n, 'FastUP3C', debug=True)}")
    
    # Run multiple simulations
    simulations = 100
    steps = simulate(n, "FastUP3C", simulations)

    print(f"Mean: {np.mean(steps)}\nMedian: {np.median(steps)}\nStd: {np.std(steps)}")

    plt.hist(steps)
    plt.savefig("histogram.png")
    plt.show()
