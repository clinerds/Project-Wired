TAU = 20
THRESH = 1.0

class Neuron:
    def __init__ (self):
        self.voltage=0
        self.count=0
        self.spiked=False

    def spike(self, push):
        self.voltage = self.voltage - self.voltage/TAU + push
        self.spiked = False
        
        if self.voltage >= THRESH:
            self.voltage = 0
            self.spiked=True
            self.count+=1


left_Eye = Neuron() # Drives the right motor
left_Motor = Neuron() 

right_Eye = Neuron() # Drives the left motor
right_Motor = Neuron()

left_W = 1.0
right_W = 1.0

left_Eye_input = 0.0
right_Eye_input = 0.0

for t in range(200):
    left_Eye.spike(left_Eye_input)
    right_Motor.spike( left_W if left_Eye.spiked else 0)
    right_Eye.spike(right_Eye_input)
    left_Motor.spike(right_W if right_Eye.spiked else 0)

    if left_Eye.spiked:
        print("Left Eye spiked at", t, "total spikes", left_Eye.count)
    if right_Motor.spiked:
        print("Right Motor spiked at", t, "total spikes", right_Motor.count)
    if right_Eye.spiked:
        print("Right Eye spiked at", t, "total spikes", right_Eye.count)   
    if left_Motor.spiked:
        print("Left Motor spiked at", t, "total spikes", left_Motor.count)
    


