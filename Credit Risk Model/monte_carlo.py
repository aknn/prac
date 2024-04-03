
import numpy as np
import math



def simulate_secretary_problem(n_simulations, n_candidates):
    success_count = 0

    # Define the cutoff point as the optimal stopping rule
    cutoff = int(n_candidates / math.e)

    for _ in range(n_simulations):
        # Generate random permutation of candidate ranks
        candidates = np.random.permutation(n_candidates) + 1

        # Find the best candidate in the first 'cutoff' candidates
        best_of_seen = max(candidates[:cutoff])

        # Assume we didn't find the best candidate yet
        chosen_candidate = None

        # Go through the rest of the candidates
        for candidate in candidates[cutoff:]:
            # If this candidate is better than all we've seen, choose them
            if candidate > best_of_seen:
                chosen_candidate = candidate
               break

        # If we ended up choosing the best candidate, it's a success
        if chosen_candidate == n_candidates:
            success_count += 1

    # Calculate the probability of success
    probability_of_success = success_count / n_simulations
    return probability_of_success


# Parameters
n_simulations = 1000
n_candidates = 100

# Run the simulation
probability_of_success = simulate_secretary_problem(n_simulations, n_candidates)

# Show the results
print(f"Probability of successfully selecting the best candidate: {probability_of_success:.4f}")