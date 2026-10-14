# # def add_input(voltage, amount):
# #     return voltage + amount

# # v = add_input(2, 3)

# # print(v)

# # for t in range(5):
# #     print(t)

# # for t in range(5):
# #     print("time step", t)

# voltage = []
# threshold = 5

# for t in range(100):
#     voltage.append(t*0.1)

# print(voltage)

# if voltage >= threshold:
#     result = "spike"
# else:
#     result = "no spike (Quiet)"

# print(result)

class Neuron:
    def __init__(self, threshold):
        self.voltage = 0
        self.threshold = threshold

    def receive(self, amount):
        self.voltage = self.voltage + amount

    def step(self):
        if self.voltage >= self.threshold:
            self.voltage = 0
            return True      # spiked
        return False         # stayed quiet

a = Neuron(10)   # build neuron a
b = Neuron(10)   # build neuron b
a.receive(4)     # only a changes