from lib.P3C import P3C
from lib.PMISC import PMISC
from lib.FastP3C import FastP3C
from lib.FastPMISC import FastPMISC
from lib.RandomP3C import RandomP3C
from lib.RandomPMISC import RandomPMISC
from lib.FastUP3C import FastUP3C

def get_algorithm(algorithm_name, n):
    if algorithm_name == "P3C":
        return P3C(n=n)
    elif algorithm_name == "PMISC":
        return PMISC(n=n)
    elif algorithm_name == "FastP3C":
        return FastP3C(n=n)
    elif algorithm_name == "FastPMISC":
        return FastPMISC(n=n)
    elif algorithm_name == "RandomP3C":
        return RandomP3C(n=n)
    elif algorithm_name == "RandomPMISC":
        return RandomPMISC(n=n)
    elif algorithm_name == "FastUP3C":
        return FastUP3C(n=n)
    else:
        raise ValueError(f"Algorithm {algorithm_name} not found")

def single_run(algorithm, debug=False):
    return algorithm.run(debug=debug)

def simulate(n, algorithm_name, simulations, debug=False):
    algorithm = get_algorithm(algorithm_name, n)
    steps = []
    for _ in range(simulations):
        steps.append(single_run(algorithm, debug))
    return steps