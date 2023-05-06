import numpy as np

def dtheta_dt(t, theta, omega):
    return omega

def domega_dt(t, theta, omega, k):
    return -k * np.sin(theta)

def rk4_step(f, t, y, z, h, k=None):
    k1 = h * f(t, y, z) if k is None else h * f(t, y, z, k)
    k2 = h * f(t + h / 2, y + k1 / 2, z + k1 / 2) if k is None else h * f(t + h / 2, y + k1 / 2, z + k1 / 2, k)
    k3 = h * f(t + h / 2, y + k2 / 2, z + k2 / 2) if k is None else h * f(t + h / 2, y + k2 / 2, z + k2 / 2, k)
    k4 = h * f(t + h, y + k3, z + k3) if k is None else h * f(t + h, y + k3, z + k3, k)
    return (k1 + 2 * k2 + 2 * k3 + k4) / 6

def rk4_integrate(dtheta_dt, domega_dt, theta0, omega0, t0, tf, dt, k):
    t = np.arange(t0, tf + dt, dt)
    theta = np.zeros_like(t)
    omega = np.zeros_like(t)
    theta[0] = theta0
    omega[0] = omega0

    for i in range(1, len(t)):
        theta[i] = theta[i - 1] + rk4_step(dtheta_dt, t[i - 1], theta[i - 1], omega[i - 1], dt)
        omega[i] = omega[i - 1] + rk4_step(domega_dt, t[i - 1], theta[i - 1], omega[i - 1], dt, k)

    return t, theta, omega
