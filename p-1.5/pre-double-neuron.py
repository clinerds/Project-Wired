TAU = 20
THRESH = 1   # Always write constants in ALL CAPS. This is a Python convention.


class Neuron:
    def __init__(self):
        self.voltage = 0
        self.spiked = False
        self.count = 0

    def step(self, push):
        self.voltage = self.voltage - self.voltage / TAU + push
        self.spiked = False

        if self.voltage >= THRESH:
            self.spiked = True
            self.voltage = 0
            self.count += 1
      
n = Neuron()

for t in range(200):
    n.step(0.08)
    if n.spiked:
        print("spike at time", t, "total spikes", n.count)
    # else:
    #     print("no spike at time", t, "voltage", n.voltage)



# Double Neuron: two neurons, one wire
a = Neuron()
b = Neuron()
W = 0.7 # strength of the wire from a to b

for t in range(200):
    a.step(0.08)                    # a gets the outside push
    b.step(W if a.spiked else 0)    # b gets a kick only when a just spiked
    if a.spiked:
        print("A spiked at", t, "total spikes", a.count)
    if b.spiked:
        print("B spiked at", t, "total spikes", b.count)


# Work out how much of B’s charge survives between A’s spikes (0.95 ** gap of A).
# Find the max B can reach (W / (1 - that number)).
# If it’s at least 1, B fires. If not, it stays silent.


#Question: How we are defining 0.95 as its a static value? Also why B is spiking at 0.7 but not at 0.08 as it has the same value as A

# BELOW IS THE METHOD TO TEST IF B WILL SPIKE

test = 0.95 ** 20
print('Charge remaining:', test)

test2 = (W / (1 - test))
print('Max B can reach:', test2)