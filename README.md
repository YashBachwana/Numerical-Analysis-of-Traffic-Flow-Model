# Traffic Flow Model Simulation

## Overview
This project implements a **microscopic traffic flow model** for simulating vehicle dynamics using **Runge-Kutta** and **Euler's methods**. The traffic model follows a **car-following approach**, focusing on the interaction between vehicles in a single lane. Each vehicle adjusts its velocity based on the behavior of the car ahead, maintaining a safe following distance.

## Key Features
- Simulates the **velocity** and **position** of vehicles over time.
- Uses **Runge-Kutta** for velocity calculation and **Euler's method** for position updates.
- Includes visualizations of **velocity vs time** and **position vs time** for multiple vehicles.
- Designed for the analysis of **microscopic traffic flow** and potential improvements to **traffic signal systems**.

## Problem Statement
This simulation addresses **traffic congestion** at traffic signals. The project models how vehicles accelerate after a green light and how their velocities converge to a maximum speed. The results can aid in optimizing **signal timings** to enhance traffic flow.

## Models
1. **OVM (Optimal Velocity Model)**: Based on nonlinear dynamic equations to model vehicle interactions.
2. **Our Model**: Inspired by car-following models, this model introduces a **Sigmoid function** to adjust the sensitivity based on the difference in velocities between consecutive cars.

## Methodology
1. **Initial Conditions**: 
    - Vehicles start from rest at a traffic signal.
    - The leader vehicle's velocity is modeled using a **Sigmoid function**.
  
2. **Velocity Update**:
    - The velocity of the vehicles is updated using the **Runge-Kutta method**:
    ```python
    k1 = h * f(v_n, v_n-1)
    k2 = h * f(v_n + 0.5 * k1, v_n-1)
    ...
    v_n+1 = v_n + (k1 + 2*k2 + 2*k3 + k4) / 6
    ```

3. **Position Update**:
    - Positions are updated using **Euler’s method**:
    ```python
    X_n+1 = X_n + h * V_n
    ```

4. **Simulations**:
    - Simulates the traffic flow dynamics with multiple iterations of vehicles following the leader.
    - Uses increasing time steps to model each vehicle's delay in responding to the signal change.

## Usage
1. **Prerequisites**: Ensure you have Python installed along with the following libraries:
   - `numpy`
   - `matplotlib`
   
2. **Run the Simulation**: 
   Execute the Python script to simulate vehicle dynamics:
   ```bash
   python traffic_simulation.py
