"""Генерация аттрактора Лоренца (v4)."""
from core.lorenz import generate_trajectory
import matplotlib.pyplot as plt

def run():
    traj = generate_trajectory(2000)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(traj[:,0], traj[:,1], traj[:,2], lw=0.5)
    plt.savefig("lorenz.png")
    print("Аттрактор сохранён в lorenz.png")

if __name__ == '__main__':
    run()