#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime


def log_processes():
    processes_raw = os.popen('ps aux').read().splitlines()
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    log_file = "/tmp/cpu_usage_rapport.txt"
    log_body = ["*******{}*******".format(timestamp),
            "[PID]\t[name]\t[memory]"]

    #adds running processes to 'log_body' with pid, name and memory usage in K
    for p in processes_raw[1:-2]:
        elements = p.split()
        pid = elements[1]
        name = elements[10]
        log_body.append(pid + "\t" + name + "\t" + os.popen('sudo pmap ' + pid).readlines()[-1].split()[1])

    #writes items in 'log_body' to textfile referenced in 'log_file'
    with open(log_file, 'a') as out:
        for item in log_body:
            out.write("%s\n" % item)
        return

def main():

    memory_limit, minutes = sys.argv[1:]
    if memory_limit[-1] == 'G':
        memory_limit = float(memory_limit[:-1])
        memory_limit *= 1024                         # convert memory_limit from GB to MB

    if memory_limit[-1] == 'M':
        memory_limit = int(memory_limit[:-1])


    while True:
        time.sleep(int(minutes) * 6)                                        #wait x minutes before proceeding
        used_memory = os.popen('free -t -m').readlines()[-1].split()[2]     #get used memory in MB

        if float(used_memory) > memory_limit:
            log_processes()

if __name__ == "__main__":
	main()
