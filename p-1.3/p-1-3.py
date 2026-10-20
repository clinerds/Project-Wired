TAU = 20.0       # leak: bigger = drains slower - The Smaller the TAU, the faster the leak. The bigger the TAU, the slower the leak.
THRESH = 1.0     # the line on the bucket
push = 0.08      # constant input each step
v = 0.0          # water level, starts empty

for t in range(200):
    v = v - v / TAU + push    # leak, then integrate
    if v >= THRESH:           # fire?
        print("spike at", t)
        v = 0.0               # reset


