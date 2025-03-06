import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6, step_size=0.1, restarts=5):
    best_solution = None
    best_value = float("inf")

    for _ in range(restarts):
        current_solution = [random.uniform(b[0], b[1]) for b in bounds]
        current_value = func(current_solution)

        for _ in range(iterations):
            neighbor = [xi + random.uniform(-step_size, step_size) for xi in current_solution]
            neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]  # Keep in bounds
            neighbor_value = func(neighbor)

            if neighbor_value < current_value:
                current_solution, current_value = neighbor, neighbor_value
                step_size *= 0.99 

            elif random.random() < 0.1:
                step_size *= 1.05  

            if abs(neighbor_value - current_value) < epsilon:
                break

        if current_value < best_value:
            best_solution, best_value = current_solution, current_value

    return best_solution, best_value

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_solution = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

        if best_value < epsilon:
            break

    return best_solution, best_value

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    
    for _ in range(iterations):
        candidate = [xi + random.uniform(-0.5, 0.5) for xi in current_solution]
        candidate = [max(min(candidate[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]  
        candidate_value = func(candidate)

        delta = candidate_value - current_value
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_solution, current_value = candidate, candidate_value

        temp *= cooling_rate

        if temp < epsilon:
            break

    return current_solution, current_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)] 

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Solution:", hc_solution, "Value:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Solution:", rls_solution, "Value:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Solution:", sa_solution, "Value:", sa_value)
