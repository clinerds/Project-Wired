import math

# --- settings ---
WORLD_MIN = -10
WORLD_MAX = 10
THREAT_SPEED = 0.1
# FLY_SPEED = 0.5
DASH_SPEED = 1.5       # NEW: must beat the threat's top speed (about 1.0) so the fly can overtake it
STEPS = 200
MOVE_PER_SPIKE = 1.0    # how far the fly moves each time a motor neuron spikes
SENSE_GAIN = 2.0     # NEW in settings


fly_position = 0
dashing = False        # NEW: is a dash in progress?
dash_side = None       # NEW: side the threat was on when the dash started

TAU = 20
THRESH = 1.0

class Neuron:
    def __init__(self):
        self.voltage = 0
        self.count = 0
        self.spiked = False

    def spike(self, push):
        self.voltage = self.voltage - self.voltage / TAU + push
        self.spiked = False

        if self.voltage >= THRESH:
            self.voltage = 0
            self.spiked = True
            self.count += 1

left_Eye = Neuron()     # sees threat on the left, drives the right motor
right_Motor = Neuron()
right_Eye = Neuron()    # sees threat on the right, drives the left motor
left_Motor = Neuron()

left_W = 1.0
right_W = 1.0



for step in range(STEPS):
    threat_position = 10 * math.sin(step * THREAT_SPEED)

    distance = abs(threat_position - fly_position)

    if threat_position > fly_position:
        side = "right"
    elif threat_position < fly_position:
        side = "left"
    else:
        side = "same spot"


    # NEW: turn the threat position into two sensor signals
    left_strength = 0
    right_strength = 0

    if side == "right":
        right_strength = 1 / (1 + distance)
    elif side == "left":
        left_strength = 1 / (1 + distance)


    # NEW: strengths push the eyes, eyes drive the opposite motors
    left_Eye.spike(left_strength * SENSE_GAIN)
    right_Motor.spike(left_W if left_Eye.spiked else 0)
    right_Eye.spike(right_strength * SENSE_GAIN)
    left_Motor.spike(right_W if right_Eye.spiked else 0)

    # NEW: cornered at a wall with the threat on the open side? start a dash
    if not dashing:
        dash_steps = 0    # how many steps the fly spent dashing
        if side == "right" and fly_position <= WORLD_MIN:
            dashing = True
            dash_side = "right"
        elif side == "left" and fly_position >= WORLD_MAX:
            dashing = True
            dash_side = "left"

    # NEW: the dash is over once the threat is no longer on the side it started from
    if dashing and side != dash_side:
        dashing = False

    # move the fly: ONE movement block only
    if dashing:
        dash_steps += 1
        # run TOWARD the threat until we are past it
        if side == "right":
            fly_position = fly_position + DASH_SPEED
        else:
            fly_position = fly_position - DASH_SPEED
    else:
        # neural flee: the motors decide, not the side check
        if right_Motor.spiked:
            fly_position = fly_position + MOVE_PER_SPIKE
        if left_Motor.spiked:
            fly_position = fly_position - MOVE_PER_SPIKE

    # clamp: never go past the walls
    fly_position = max(WORLD_MIN, min(WORLD_MAX, fly_position))

    print(step, "threat", round(threat_position, 2),
          "| fly", round(fly_position, 2),
          "| dash", dashing,
          "| dash steps:", dash_steps,
          "| distance", round(distance, 2),
          "| L", round(left_strength, 2),
          "| R", round(right_strength, 2),
          "| threat is on the", side,
          "| LE", int(left_Eye.spiked), "RE", int(right_Eye.spiked),
          "| LM", int(left_Motor.spiked), "RM", int(right_Motor.spiked))
          
         

           
          
        