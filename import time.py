import time
import numpy as np

# Generate sample arrays
def generate_data(n):
    a = np.random.randint(1, 100, n)
    b = np.random.randint(1, 100, n)
    return a, b

# Simulate the algorithm
def algorithm(n):
    a, b = generate_data(n)
    total_sum = 0
    j = 2
    while j < n:
        k = j
        while k < n:
            total_sum += a[j] * b[k]
            k = k * k
        j = 2 * j
    return total_sum

# Theoretical time complexity: O(log2(n) * log(log(n)))
def theoretical_time(n):
    return np.log2(n) * np.log(np.log(n))

# List of n values
n_values = [10, 100, 1000, 10000, 100000]

# Measure experimental execution times
times = []
for n in n_values:
    start_time = time.time()
    algorithm(n)
    end_time = time.time()
    times.append((n, (end_time - start_time) * 1e9))  # Convert time to nanoseconds

# Calculate theoretical results
theoretical_results = [theoretical_time(n) for n in n_values]

# Scaling constant to match theoretical and experimental values
scaling_constant = times[-1][1] / theoretical_results[-1]

# Adjust theoretical results by the scaling constant
adjusted_theoretical = [t * scaling_constant for t in theoretical_results]

# Display the results in a table
print(f"{'n':<8} {'Experimental Time (ns)':<25} {'Theoretical Result':<20} {'Adjusted Theoretical Result':<30}")
for i, n in enumerate(n_values):
    print(f"{n:<8} {times[i][1]:<25.2f} {theoretical_results[i]:<20.6f} {adjusted_theoretical[i]:<30.2f}")