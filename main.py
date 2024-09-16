import matplotlib.pyplot as plt
import numpy as np
def trajectory(x, y):
    plt.title("Траектория движения")
    plt.xlabel("Время (с)")
    plt.ylabel("Расстояние (м)")
    plt.grid(True)
    plt.plot(x, y)
    plt.show()

def dependenceSpeedTime(t, v):
    plt.title("Зависимость скорости от времени")
    plt.xlabel("Время (с)")
    plt.ylabel("Скорость (м/с)")
    plt.grid(True)
    plt.plot(t, v)
    plt.show()

def dependenceCoordinateTime(x, y, t):
    plt.title("Зависимость координат от времени")
    plt.xlabel("Время (с)")
    plt.ylabel("Координата (м)")
    plt.grid(True)
    plt.plot(t, x, label="Координата X")
    plt.plot(t, y, label="Координата Y")
    plt.legend()
    plt.show()

h0 = float(input("Начальная высота (м) = "))
v0 = float(input("Начальная скорость (м/с) = "))
angles = float(input("Угол броска (градусы) = "))

angle_rad = np.radians(angles)

vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

t_max = (vy + np.sqrt(vy ** 2 + 2 * 9.8 * h0)) / 9.8
time = np.linspace(0, t_max, num = 1000)

v = np.sqrt(vx ** 2 + (vy - 9.8 * time) ** 2)

x = vx * time
y = h0 + vy * time - 0.5 * 9.8 * time ** 2

trajectory(x, y)
dependenceSpeedTime(time, v)
dependenceCoordinateTime(x, y, time)