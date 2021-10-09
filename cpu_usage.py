#!/usr/bin/env python3
import os
import sys
import time
import winsound

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
	if used_memory >= memory_limit:
		#playsound('erro.mp3')
        # create status report
        

                                                # generate sound
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
