#!/usr/bin/env python3
import os
import sys
import time

memory_limit, minutes = sys.argv[1:]

if memory_limit[-1] == 'G':
    # convert memory_limit from GB to B
    memory_limit *= 10 ** 9  
    
if memory_limit[-1] == 'M':
    # convert memory_limit from MB to B
    memory_limit *= 10 ** 6

while True:
    time.sleep(int(minutes) + 60)
    used_memory = os.popen('free -t -m').readlines()[-1].split()[2]
    if used_memory => memory_limit:
        # create status report
        # generate sound

