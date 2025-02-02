import os
import gymnasium as gym
import sumo_rl
from stable_baselines3 import PPO

# Define paths to your SUMO network and route files
net_file = 'C:\AMS Project\AMS_sim\my_network.net.xml'
route_file = 'C:\AMS Project\AMS_sim\my_routes.rou.xml'

# Create a SUMO-RL environment
env = gym.make('sumo-rl-v0',
               net_file=net_file,
               route_file=route_file,
               use_gui=False,  # Set to False if you don't need GUI
               num_seconds=1000)  # Simulation time in seconds

# Initialize PPO agent
model = PPO('MlpPolicy', env, verbose=1)

# Train the agent
model.learn(total_timesteps=10000)

# Save the trained model
model.save("ppo_sumo_rl")

# Evaluate the trained agent
obs = env.reset()
done = False
while not done:
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)

env.close()