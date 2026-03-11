import numpy as np
import gymnasium as gym
from gymnasium import spaces

class DrivingEnv(gym.Env):
    def __init__(self, grid_size=5):
        super(DrivingEnv, self).__init__()
        self.grid_size = grid_size
        self.action_space = spaces.Discrete(5)  # 0: accelerate, 1: brake, 2: turn left, 3: turn right, 4: continue
        self.observation_space = spaces.Box(low=0, high=grid_size-1, shape=(2,), dtype=np.float32)
        
        self.state = np.array([0, 0], dtype=np.float32)
        self.goal = np.array([grid_size-1, grid_size-1], dtype=np.float32)
        self.sign = None
        self.objects = []

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = np.array([0, 0], dtype=np.float32)
        return self.state, {}

    def step(self, action):
        # Simplified movement logic
        if action == 2:  # turn left
            self.state[1] = max(0, self.state[1] - 1)
        elif action == 3:  # turn right
            self.state[1] = min(self.grid_size - 1, self.state[1] + 1)
        elif action == 0 or action == 4:  # accelerate or continue
            self.state[0] = min(self.grid_size - 1, self.state[0] + 1)
        
        reward = 0
        done = np.array_equal(self.state, self.goal)
        if done:
            reward = 10
            
        return self.state, reward, done, False, {}

if __name__ == "__main__":
    env = DrivingEnv()
    print("Environment initialized.")
