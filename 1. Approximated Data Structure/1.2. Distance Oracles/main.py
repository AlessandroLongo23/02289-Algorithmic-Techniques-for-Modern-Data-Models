import numpy as np
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
from lib.Oracle import Oracle

if __name__ == "__main__":
    num_points = 1000
    k = 3
    p = np.power(num_points, -1 / k)

    ratios = []
    simulations = 1000
    for i in tqdm(range(simulations)):
        if i % 50 == 0:
            oracle = Oracle(num_points, k, p)

        u, v = random.sample(oracle.points, 2)

        ratios.append(oracle.dist(u, v))

    print(f"Mean: {np.mean(ratios)}\nMedian: {np.median(ratios)}")

    plt.hist(ratios, bins=100)
    plt.show()