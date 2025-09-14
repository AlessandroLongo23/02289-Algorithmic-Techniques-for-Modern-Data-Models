import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from tqdm import tqdm

class Point:
    def __init__(self, i, x, y):
        self.i = i
        self.x = x
        self.y = y

    def distance(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return f"{self.i}"


def setup(num_points, k, p):
    points = [Point(i, random.random(), random.random()) for i in range(num_points)]

    Vs = [[] for _ in range(k)]

    Vs[0] = points
    for i in range(1, len(Vs)):
        for point in Vs[i-1]:
            if random.random() < p:
                Vs[i].append(point)

    return points, Vs

def create_bunch(p: Point, Vs: list[list[Point]]):
    bunch = [[] for _ in range(len(Vs))]
    
    for i in range(len(Vs) - 1):
        p_next_layer = min(Vs[i + 1], key=lambda x: p.distance(x))

        for v in Vs[i]:
            if p.distance(v) <= p.distance(p_next_layer):
                bunch[i].append(v)

    for v in Vs[-1]:
        bunch[-1].append(v)

    for layer in bunch:
        layer.sort(key=lambda x: p.distance(x))

    bunch_flattened = [v for layer in bunch for v in layer]

    return bunch, bunch_flattened


def dist(u: Point, v: Point, Vs: list[list[Point]]):
    bunch_u, bunch_flattened_u = create_bunch(u, Vs)
    bunch_v, bunch_flattened_v = create_bunch(v, Vs)

    # colors = ['black', 'red', 'blue', 'green', 'orange', 'purple']

    # for i in range(len(Vs)):
    #     plt.scatter([point.x for point in Vs[i]], [point.y for point in Vs[i]], color=colors[i], s=i + 1)

    # plt.plot([u.x, v.x], [u.y, v.y], color='purple')

    # for v in bunch_flattened:
    #     plt.plot([u.x, v.x], [u.y, v.y], color='#00000044')

    # for i in range(len(bunch)):
    #     if len(bunch[i]) == 0:
    #         continue

    #     closest = bunch[i][0]
    #     circle = patches.Circle((u.x, u.y), radius=u.distance(closest), edgecolor=colors[i], fill=False)
    #     plt.gca().add_patch(circle)



    # if q in bunch_flattened_p or p in bunch_flattened_q:
    #     sum_distance = u.distance(v)
    # else:
    #     layer_index = 1
    #     while layer_index < len(bunch_u):
    #         if bunch_u[layer_index][0] == bunch_v[layer_index][0]:
    #             break
            
    #         layer_index += 1

    #     distance = u.distance(bunch_u[layer_index][0]) + v.distance(bunch_v[layer_index][0])

    w = u
    i = 0
    while w not in bunch_flattened_v:
        i += 1
        u, v = v, u
        w = bunch_u[i][0]

    distance = u.distance(w) + v.distance(w)

    plt.show()
    return distance / u.distance(v)


if __name__ == "__main__":
    num_points = 10000
    k = 2
    p = np.power(num_points, -1 / k)

    # colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'brown', 'pink', 'gray', 'black']

    # for i in range(len(Vs)):
    #     plt.scatter([point.x for point in Vs[i]], [point.y for point in Vs[i]], color=colors[i])

    # plt.show()

    ratios = []
    simulations = 10000
    for _ in tqdm(range(50)):
        points, Vs = setup(num_points, k, p)
    
        for _ in range(simulations // 50):
            u, v = points[random.randint(0, len(points)-1)], points[random.randint(0, len(points)-1)]
            while u.i == v.i:
                u, v = points[random.randint(0, len(points)-1)], points[random.randint(0, len(points)-1)]
            
            ratios.append(dist(u, v, Vs))

    print(np.median(ratios))

    plt.hist(ratios, bins=100)
    plt.show()

