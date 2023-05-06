import numpy as np

class PolyNorm:
    def __init__(self, theta0, omega0, k):
        self.theta0 = theta0
        self.omega0 = omega0
        self.k = k

    def c2(self):
        return -1/2 * self.k * np.sin(self.theta0)

    def c3(self):
        return -1/6 * self.k * self.omega0 * np.cos(self.theta0)

    def c4(self):
        return 1/24 * self.k * np.sin(self.theta0) * (self.k * np.cos(self.theta0) + self.omega0**2)

    def phi(self, t):
        return self.theta0 + self.omega0 * t + self.c2() * t**2 + self.c3() * t**3 + self.c4() * t**4
