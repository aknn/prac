# Table lookup is a special case of linear value function approximation where each state-action pair
# has a corresponding unique feature. This can be explained and illustrated using a simple example in Python.

import numpy as np


# Define the grid world environment
class GridWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.n_states = width * height
        self.n_actions = 4  # up, down, left, right
        self.state = 0  # starting state (top-left corner)

    def state_to_position(self, state):
        return state // self.width, state % self.width

    def position_to_state(self, pos):
        return pos[0] * self.width + pos[1]

    def step(self, action):
        x, y = self.state_to_position(self.state)
        if action == 0:  # up
            x = max(0, x - 1)
        elif action == 1:  # down
            x = min(self.height - 1, x + 1)
        elif action == 2:  # left
            y = max(0, y - 1)
        elif action == 3:  # right
            y = min(self.width - 1, y + 1)
        self.state = self.position_to_state((x, y))
        return self.state


# Define the feature vectors
def get_feature_vector(state, action, n_states, n_actions):
    feature_vector = np.zeros(n_states * n_actions)
    index = state * n_actions + action
    feature_vector[index] = 1
    return feature_vector


# Linear value function approximation
class LinearValueFunction:
    def __init__(self, n_states, n_actions):
        self.weights = np.zeros(n_states * n_actions)
        self.n_states = n_states
        self.n_actions = n_actions

    def get_value(self, state, action):
        feature_vector = get_feature_vector(state, action, self.n_states, self.n_actions)
        return np.dot(self.weights, feature_vector)

    def update_value(self, state, action, target, alpha=0.1):
        feature_vector = get_feature_vector(state, action, self.n_states, self.n_actions)
        prediction = np.dot(self.weights, feature_vector)
        error = target - prediction
        self.weights += alpha * error * feature_vector


# Example usage
env = GridWorld(4, 4)
value_function = LinearValueFunction(env.n_states, env.n_actions)

# Example update: suppose we observed a target value of 10 for state 5 and action 2
state = 5
action = 2
target_value = 10
value_function.update_value(state, action, target_value)

# Retrieve updated value
updated_value = value_function.get_value(state, action)
print(f"Updated value for state {state} and action {action}: {updated_value}")
