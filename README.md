# 🚗 Traffic Signal Optimization using Deep Q-Learning



---

## 📅 Project Overview
As urban populations grow, traffic congestion presents serious challenges to efficiency and quality of life. Traditional traffic light systems struggle with real-time adaptation. This project proposes a scalable, intelligent alternative by using reinforcement learning to control signal phases based on real-time traffic conditions.

---

## 🪀 Key Features
- Intelligent traffic light control using Deep Q-Learning (DQL)
- SUMO-based simulation environment
- Emergency vehicle prioritization
- Real-time traffic flow optimization
- Comparison with traditional Q-Learning

---

## 🔄 Algorithms Used
- **Q-Learning**: For simple environments with reduced state spaces
- **Deep Q-Networks (DQN)**: For complex, dynamic traffic scenarios

---

## 💡 Technologies & Tools
- Python
- SUMO (Simulation of Urban Mobility)
- TraCI (Traffic Control Interface)
- TensorFlow / Keras
- NumPy, Matplotlib

---

## 📈 Results Summary
| Model              | Reward   | Vehicles Waiting | Avg Speed (m/s) | Avg Wait Time (s) |
|--------------------|----------|------------------|------------------|--------------------|
| Baseline Simulation | -15255.36 | 405              | 4.2              | 3493.33            |
| Q-Learning         | -2327.62 | 5                | 4.6              | 79.22              |
| Deep Q-Learning    | 2774.90  | 0                | 6.5              | 15.66              |

---

## 🌐 How to Run
```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run environment simulation
python RL_env.py

# or use Jupyter Notebooks for step-by-step walkthrough
jupyter notebook dql-simulation-1.ipynb
```

---

## 🚀 Future Enhancements
- Train on larger datasets like Kinetics or real-world city data
- Optimize the model for real-time, on-device deployment
- Deploy as a web application for live simulations and demos

---

## 🤝 Contributors
- Aryan Patil ([GitHub](https://github.com/aryanator))
- Harsh Anilkumar Ramani
- Saiteja Kalam
- Chandra Mourya

---
