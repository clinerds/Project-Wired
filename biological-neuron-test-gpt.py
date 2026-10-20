
import matplotlib.pyplot as plt

# 1. Neuron parameters
V_rest = -70.0       # Resting potential (mV)
V_threshold = -55.0  # Firing threshold (mV)
V_reset = -70.0      # Voltage after a spike (mV)

R = 100.0            # Membrane resistance (MOhm)
C = 0.1              # Membrane capacitance (nF)

dt = 0.1             # Time step (ms)
refractory = 2.0     # Refractory period after a spike (ms)

# 2. Simulation settings
duration = 500.0     # Total simulation time (ms)
steps = int(duration / dt)

V = V_rest           # Initial membrane voltage
spike_times = []     # Store when the neuron fires

voltages = []
times = []

last_spike = -1000.0

# 3. Run the simulation
for step in range(steps):
    t = step * dt

    # Incoming current changes over time
    if 100 <= t < 300:
        I = 0.2        # Input current (nA)
    else:
        I = 0.0

    # 4. Update voltage using the LIF equation
    if t - last_spike < refractory:
        V = V_reset
    else:
        dV = dt / (R * C) * (
            -(V - V_rest) + R * I
        )
        V = V + dV

    # 5. Fire if the threshold is reached
    if V >= V_threshold:
        spike_times.append(t)
        last_spike = t
        V = V_reset

    # 6. Save values for plotting
    times.append(t)
    voltages.append(V)

# 7. Display the results
print("Number of spikes:", len(spike_times))
print("Spike times (ms):", spike_times)

plt.plot(times, voltages)
plt.axhline(
    V_threshold,
    linestyle="--",
    label="Firing threshold"
)
plt.axhline(
    V_rest,
    linestyle=":",
    label="Resting potential"
)

plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
plt.title("Leaky Integrate-and-Fire Neuron")
plt.legend()
plt.show()
