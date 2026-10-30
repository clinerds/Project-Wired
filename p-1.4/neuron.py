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

        if self.voltage >= thresh:
            self.spiked = True
            self.voltage = 0
            self.count +=1
      
n = Neuron()

for t in range(200):
    n.step(0.08)
    if n.spiked:
        print("spike at time", t, "total spikes", n.count)