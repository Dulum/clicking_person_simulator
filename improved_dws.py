import os
import time
import random
import sys

def sleep(t):
    noise = (random.gauss(0,t/4)) ** 2
    noise = noise ** .5
    time.sleep(t + noise)

def presskey(key, wait=0.3):

    os.system("xdotool key " + key)
    sleep(wait)




instructions_file = sys.argv[1]

with open(instructions_file, 'r') as f:
    instructions = f.read().split('\n')

instructions = [line.split(': ') for line in instructions]
first_time = int(instructions[0][0])
instructions = [(int(time) - first_time, command) for time, command in instructions]

instructions = [(time / 1000, command) for time, command in instructions]

sleep(5)


for time, command in instructions:
    presskey(command, sleep=time)