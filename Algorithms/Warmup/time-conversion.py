#!/bin/python

import sys


time = raw_input().strip()

def convertTime(time):
    ampm = time[-2:].upper()
    time = time[0:-2].split(':')
    if ampm == 'PM':
        if time[0] !='12':
            militaryHour = int(time[0]) + 12
            time[0] = str(militaryHour)
        return ':'.join(time)
    elif ampm == 'AM':
        if time[0] == '12':
            time[0] = '00'
        return ':'.join(time)
    
print convertTime(time)