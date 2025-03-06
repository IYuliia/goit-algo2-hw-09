### **Task Description**  

Implement a program to **minimize the Sphere function**:  

\[
f(x) = \sum_{i=1}^{n} x_i^2
\]

using three different approaches to local optimization:  

1. **Hill Climbing Algorithm**  
2. **Random Local Search**  
3. **Simulated Annealing**  

---

### **Technical Requirements**  

1. **Function Boundaries:**  
   Each parameter \( x_i \) must be within the range:  
   \[
   x_i \in [-5,5]
   \]

2. **Expected Output:**  
   Each algorithm must return:  
   - The optimal point (a list of coordinates \( x \)).  
   - The function value at that point.  

3. **Methods to Implement:**  
   - `hill_climbing(iterations, epsilon)`: Hill Climbing algorithm.  
   - `random_local_search(iterations, epsilon)`: Random Local Search.  
   - `simulated_annealing(iterations, epsilon)`: Simulated Annealing.  

4. **Iterations Parameter:**  
   Each algorithm should accept a parameter `iterations`, which sets the **maximum number of iterations** to run.  

5. **Termination Conditions:**  
   The algorithms should stop if **either** of these conditions is met:  

   - **Small Change Condition:** If the **change in the objective function value** or the **position in the solution space** between two consecutive iterations is smaller than `epsilon`,** the algorithm stops.  
   - **Simulated Annealing Temperature Condition:** For **Simulated Annealing**, if the **temperature decreases below `epsilon`**, the algorithm terminates, as this indicates the search has lost its ability to explore new solutions.  