#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#
import pandas as pd
import numpy as np

def calcMissing(readings):
    # Write your code here
    time =[]
    mecury = []
    for row in readings:
        x = row.split('\t')
        time.append(x[0])
        mecury.append(x[1])
    new_readings = list(zip(time,mecury))
    df = pd.DataFrame(new_readings)
    df = df.rename(columns={'0':'time', '1':'mecury'})
    #print(df)
        #print(df)
    for idx in range(len(df['time'])):
        if idx==0 and 'missing' in df['mercury'][idx]:
            cnt = 1
            while True:
                if 'missing' in df['mercury'][cnt]:
                    cnt+=1
                else:
                    break
            cnt2 = cnt+1
            while True:
                if 'missing' in df['mercury'][cnt2]:
                    cnt2+=1
                else:
                    break
            x = (df['mercury'][cnt2]-df['mercury'][cnt])/(cnt2-cnt)
            x = x*cnt
            df['mercury'][0]=df['mercury'][cnt]-x
            missing.append(x)
        elif idx==len(df['time'])-1 and 'missing' in df['mercury'][idx]:
            cnt=len(df['time'])-2
            while True:
                if 'missing' in df['mercury'][cnt]:
                    cnt-=1
                else:
                    break
            cnt2=cnt-1
            while True:
                if 'missing' in df['mercury'][cnt2]:
                    cnt2-=1
                else:
                    break
            x = (df['mercury'][cnt2]-df['mercury'][cnt])/(cnt2-cnt)
            x = x*cnt
            df['mercury'][len(df['time']-1)]=df['mercury'][cnt]-x
            missing.append(x)
        elif 'missing' in df['mercury'][idx]:
            
            
    
    #print(readings[21].split('\t'))
    return 
if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []
    

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)
