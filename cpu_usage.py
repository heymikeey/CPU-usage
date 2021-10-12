#!/usr/bin/env python3
import os
import sys
import time

memory_limit, minutes = sys.argv[1:]
logfile = "/tmp/cpu_usage_rapport.txt"

if memory_limit[-1] == 'G':
    memory_limit = int(memory_limit[:-1])
    memory_limit *= 1024    # convert memory_limit from GB to MB

if memory_limit[-1] == 'M':
    memory_limit = int(memory_limit[:-1])


print(memory_limit)                                 #debug
while True:
    time.sleep(int(minutes) * 1)
    used_memory = os.popen('free -t -m').readlines()[-1].split()[2]
    
    if float(used_memory) > memory_limit:
        print("Writing to log")                     #debug
        with open(logfile, 'a') as out:
             out.write("threshold exceeded" + '\n') #test to write to location (works) //MJ
        
        

  # To Do:
  
  # Service filen ska endast kolla RAM tröskeln som angetts, och köra .pyfilen 
  # om Ram minnet är över tröskeln
  
