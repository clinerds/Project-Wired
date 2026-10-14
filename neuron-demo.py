# neuron_demo.py  -  Project WIRED, P1.1
# Run with:  python neuron_demo.py   (inside your .venv)


class Neuron:
    """A very simple neuron: it collects voltage, and spikes at a threshold."""

    def __init__(self, threshold):
        # Runs once, when you write Neuron(10). Sets the starting state.
        self.voltage = 0              # every neuron starts at rest
        self.threshold = threshold    # the voltage needed to spike

    def receive(self, amount):
        # Another neuron (or the outside world) pushes voltage in.
        self.voltage = self.voltage + amount

    def step(self):
        # One tick of time. Did we reach the threshold?
        if self.voltage >= self.threshold:
            self.voltage = 0          # reset after spiking
            return True               # spiked
        return False                  # stayed quiet


# ---------------------------------------------------------------
# PART 1: the original example, now with prints so you can watch it
# ---------------------------------------------------------------
print("=== PART 1: two neurons, one blueprint ===")
a = Neuron(10)   # build neuron a
b = Neuron(10)   # build neuron b
print("start      -> a:", a.voltage, " b:", b.voltage)

a.receive(4)     # only a changes
print("a.receive(4) -> a:", a.voltage, " b:", b.voltage)


# ---------------------------------------------------------------
# PART 2: step() on a neuron that has NOT reached threshold
# ---------------------------------------------------------------
print("\n=== PART 2: step() below threshold ===")
print("a.step() returned:", a.step())          # 4 < 10, so False
print("a voltage is still:", a.voltage)        # unchanged


# ---------------------------------------------------------------
# PART 3: push a over the threshold and watch it spike and reset
# ---------------------------------------------------------------
print("\n=== PART 3: crossing the threshold ===")
a.receive(8)                                   # 4 + 8 = 12
print("a voltage before step:", a.voltage)
print("a.step() returned:", a.step())          # 12 >= 10, so True
print("a voltage after step:", a.voltage)      # reset to 0


# ---------------------------------------------------------------
# PART 4: a real loop. A neuron gets +3 every tick for 12 ticks.
# This is the shape every later WIRED simulation will have.
# ---------------------------------------------------------------
print("\n=== PART 4: loop simulation (input +3 per tick) ===")
n = Neuron(10)
spike_times = []                               # we record when spikes happen

for t in range(12):
    n.receive(3)                               # input arrives
    voltage_before = n.voltage                 # peek before step() resets it
    spiked = n.step()                          # did it fire this tick?
    if spiked:
        spike_times.append(t)
    label = "SPIKE" if spiked else "quiet"     # ternary
    print("t =", t, "| voltage =", voltage_before, "|", label)

print("\nSpikes happened at ticks:", spike_times)