import numpy as np
import matplotlib.pyplot as plt

# Define the time step and time interval
h = 0.1
t = np.arange(0, 15, h)

# Define the initial velocity function v_0
v_0 = (40 / (1 + np.exp(-t))) - 20
V_n = v_0.copy()

# Create an array for the position using Euler's Method
X_n = np.cumsum(v_0 * 0.1)


#Plotting 1st vehicle
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
V_n = V_n[:len(t)]
X_n = X_n[:len(t)]
plt.plot(t,V_n)
plt.subplot(1, 2, 2)
plt.plot(t,X_n)
time_step = 10

for iter in range(6):
    
    v_n = np.concatenate((np.zeros(time_step), v_0))
    v_np1 = np.concatenate((np.zeros(time_step), v_0))

    # Calculating v_np1 using Range-Kutta method
    for i in range(time_step - 1, len(t) - 1):
        k1 = h * (v_n[i] - v_np1[i]) / (1 + np.exp(v_n[i] - v_np1[i]))
        k2 = h * (v_n[i] + 0.5 * k1 - v_np1[i] - 0.5 * k1) / (1 + np.exp(v_n[i] + 0.5 * k1 - v_np1[i] - 0.5 * k1))
        k3 = h * (v_n[i] + 0.5 * k2 - v_np1[i] - 0.5 * k2) / (1 + np.exp(v_n[i] + 0.5 * k2 - v_np1[i] - 0.5 * k2))
        k4 = h * (v_n[i] + k3 - v_np1[i] - k3) / (1 + np.exp(v_n[i] + k3 - v_np1[i] - k3))

        v_np1[i + 1] = v_n[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

    # Calculate X_n_plus_1 by the Euler's method
    X_n_plus_1 = np.cumsum(v_np1 * 0.1)

    # Remove the beginning zeros from v_n
    v_n = v_n[10:]
    v_np1 = v_np1[:len(v_n)]
    v_n = v_np1.copy()
    time_step += 10
    
    plt.subplot(1, 2, 1)
    v_np1 = v_np1[:len(t)]
    X_n_plus_1 = X_n_plus_1[:len(t)]
    plt.plot(t,v_np1)
    plt.subplot(1, 2, 2)
    plt.plot(t,X_n_plus_1)

plt.subplot(1, 2, 1)
plt.xlabel('Time (t)')
plt.ylabel('Velocity')
plt.legend()
plt.grid(True)
plt.title('Velocity of (i)th vehicle vs. Time')

plt.subplot(1, 2, 2)
plt.grid(True)
plt.xlabel('Time(t)')
plt.ylabel('Position')
plt.legend()
plt.title('Position of (i)th vehicle vs. Time')

plt.tight_layout()
plt.show()
