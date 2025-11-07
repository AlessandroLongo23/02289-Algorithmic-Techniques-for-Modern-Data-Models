from lib.utils import get_algorithm, single_run, simulate
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":  
    n = 10
    algorithm_name = "FastUP3C"
    simulations = 100
    debug = True

    # Test single run
    # algorithm = get_algorithm(algorithm_name, n)
    # print(f"Steps: {single_run(algorithm, debug)}")
    
    # Run multiple simulations
    steps = simulate(n, algorithm_name, simulations, debug)

    print(f"Mean: {np.mean(steps)}\nMedian: {np.median(steps)}\nStd: {np.std(steps)}")

    plt.hist(steps)
    plt.savefig("histogram.png")
    plt.show()
