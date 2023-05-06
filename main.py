import numpy as np
from matplotlib import pyplot as plt
import rk4
from poly_norm import PolyNorm

# initial conditions
pi = np.pi
theta0 = pi/10
omega0 = 0
k = 1

t0 = 0  # Initial time (s)
tf = 50  # Final time (s)
dt = 0.01  # Time step (s)

pendulum = PolyNorm(theta0, omega0, k)
t = np.arange(t0, tf + dt, dt)
phi_values = pendulum.phi(t)

# Plot results
plt.plot(t, phi_values, label='θ(t)')
# plt.plot(t, omega, label="ω(t)")
plt.xlabel('Time (s)')
plt.ylabel('Values')
plt.title('Pendulum motion using RK4 with k = g/L')
plt.grid()

plt.plot(t,phi(t),label='approximation')

#plot cos over the same time period
#plt.plot(t,theta0*np.cos(np.sqrt(k)*t),label='cos')
plt.ylim(-pi,pi)

# add legend    
plt.legend()
plt.show()