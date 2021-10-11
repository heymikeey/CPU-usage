#!/usr/bin/env python3
import os
import sys
import time

memory_limit, minutes = sys.argv[1:]

if memory_limit[-1] == 'G':
    memory_limit = float(memory_limit[:-1])
    memory_limit *= 10 ** 9     # convert memory_limit from GB to B


elif memory_limit[-1] == 'M':
    memory_limit = float(memory_limit[:-1])
    memory_limit *= 10 ** 6     # convert memory_limit from MB to B

while True:
    time.sleep(int(minutes) * 2)
    used_memory = os.popen('free -t').readlines()[-1].split()[2]
    
    if float(used_memory) > memory_limit:
        print("Då")
        
            # create status report
        

  # To Do:
  
  # Service filen ska endast kolla RAM tröskeln som angetts, och köra .pyfilen 
  # om Ram minnet är över tröskeln
  
