import numpy as np

def lorenz_step(state, sigma=10, rho=28, beta=8/3, dt=0.01):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return (x + dx*dt, y + dy*dt, z + dz*dt)

def generate_trajectory(n_steps=1000):
    state = (0.1, 0.0, 0.0)
    traj = []
    for _ in range(n_steps):
        traj.append(state)
        state = lorenz_step(state)
    return np.array(traj)