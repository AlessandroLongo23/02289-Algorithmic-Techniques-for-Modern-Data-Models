import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from lib.reservoir import Reservoir

if __name__ == "__main__":
    n = 10
    k = 3
    num_simulations = 10000

    # Track frequency of each number appearing in the reservoir
    frequency_counter: Counter = Counter()
    last_index_counter: Counter = Counter()

    # Run simulations
    for sim in range(num_simulations):
        last_index: int = 0
        reservoir: Reservoir = Reservoir(n=n, k=k)
        stream: list[int] = [i for i in range(n)]
        for i in range(len(stream)):
            if reservoir.add(stream[i]):
                last_index = i
        
        # Count which numbers are in this reservoir
        for num in reservoir.get_reservoir():
            frequency_counter[num] += 1

        last_index_counter[last_index] += 1
    
    # Prepare data for plotting
    numbers: list[int] = list(range(n))
    frequencies: list[int] = [frequency_counter[i] for i in numbers]
    # Calculate expected frequency (theoretical)
    expected_frequency: float = (k / n) * num_simulations
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(numbers, frequencies, alpha=0.7, edgecolor='black')
    plt.axhline(y=expected_frequency, color='r', linestyle='--', linewidth=2, 
                label=f'Expected frequency: {expected_frequency:.1f}')
    
    plt.xlabel('Number', fontsize=12)
    plt.ylabel('Frequency in reservoir', fontsize=12)
    plt.title(f'Distribution of numbers in reservoir over {num_simulations} simulations\n(n={n}, k={k})', fontsize=14)
    plt.xticks(numbers)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    # Add text with statistics
    plt.text(0.02, 0.98, f'Mean: {sum(frequencies)/len(frequencies):.2f}\nStd: {(sum([(f - expected_frequency)**2 for f in frequencies])/len(frequencies))**0.5:.2f}',
             transform=plt.gca().transAxes, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()


    last_indices = [last_index_counter[i] for i in range(n)]
    last_index = np.mean(list(last_index_counter.keys()))


    # Create the plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(range(n), last_indices, alpha=0.7, edgecolor='black')
    plt.axvline(x=last_index, color='r', linestyle='--', linewidth=2, 
                label=f'Expected last index: {last_index:.1f}')
    plt.xlabel('Last index', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title(f'Distribution of last indices over {num_simulations} simulations\n(n={n}, k={k})', fontsize=14)
    plt.xticks(range(n))
    plt.legend()
    plt.tight_layout()
    plt.show()