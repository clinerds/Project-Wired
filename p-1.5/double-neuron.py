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
W = 1.0 # strength of the wire from a to b

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


test = 0.95 ** 20
print('Charge remaining:', test)

test2 = (W / (1 - test))
print('Max B can reach:', test2)



#NOTES

# W = 0.7 and W = 1.0 counts (3 and 10)

#ok so change w = 1.0 and noticed its now firing the same as a gap of 20 because we defined only take w value which acts as a push in neuron b when a fires so a fires at the gap of 20 so its takes value at the gap of 20 and as its valye is 1.0 which is the threshold so it just fires

# You’ve done this. Your A is the eye neuron, B is the output neuron, and W = 0.7 is the wire.
#so our output b is dependent on a

# ----------------------------------------
# QUESTIONS AND ANSWERS

# Question 1:

# How we are defining 0.95 as its a static value?

# Answer 1:
# Where does 0.95 come from?

# It isn’t a fixed number. It comes from TAU. Your own line does the work: Taking away voltage / TAU is the same as multiplying the voltage by (1 - 1/TAU).

# With TAU = 20, that’s 1 - 1/20 = 0.95.

# If you change TAU to 10, it becomes 1 - 1/10 = 0.9, a faster leak. If you change it to 100, it becomes 0.99, a very slow leak.

# Question 2:

# Also why B is spiking at 0.7 but not at 0.08 as it has the same value as A?

# Answer 2:

# A’s push = 0.08 is poured in on every step. That’s 20 pours between A’s spikes, and the charge builds up to a ceiling of 0.08 × 20 = 1.6, so A fires.

# B’s W = 0.08 would be added only once, on the single step when A spikes. For the other 19 steps B gets nothing, and the leak eats the charge away.

# Put numbers on B with W = 0.08:

# Right after a kick, B holds about 0.08.
# Over the next 20 steps it keeps only about 36% of that, so about 0.03 is left.
# The next kick adds 0.08 on top of that leftover. The most B can ever reach is 0.08 / 0.64, which is about 0.125, nowhere near the threshold of 1.