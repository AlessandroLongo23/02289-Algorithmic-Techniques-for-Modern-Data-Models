import numpy as np
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

from lib.oracle import Oracle
from lib.point import Point

if __name__ == "__main__":
    num_points: int = 1000
    k: int = 3
    p: float = np.power(num_points, -1 / k)

    ratios: list[float] = []
    simulations: int = 1000
    for i in tqdm(range(simulations)):
        if i % 50 == 0:
            oracle: Oracle = Oracle(num_points, k, p)

        u, v = random.sample(oracle.points, 2)
        estimated_dist: float = oracle.distance(u, v)
        true_dist: float = Point.distance(u, v)
        ratios.append(estimated_dist / true_dist)

    print(f"""
Mean: {np.mean(ratios):.3f}
Median: {np.median(ratios):.3f}
Std: {np.std(ratios):.3f}
Min: {np.min(ratios):.3f}
Max: {np.max(ratios):.3f}
""")

    plt.hist(ratios, bins=100)
    plt.show()