#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:39:53 2020

@author: Jose
"""

# -*- coding: cp1252 -*-

#Jose ramos
#171448
# chilerismo

import random, simpy

def simulation(processName,x,waiting,CPU):

    global wholeProcess 
 
    yield x.timeout(waiting)
    
 
    ready = x.now


    running = random.randint(1, 10)
    print ('%s  is ready on %f , it also needs %d of RAM to complete process' % (processName,ready,running))
    

    with CPU.request() as CPUturn:
        yield CPUturn     
        yield x.timeout(running) 
        print ('%s  get out of the CPU %f'% (processName, x.now))
        
        
    totalTime = x.now - ready
    print ('%s  takes %f'% (processName, totalTime))
    wholeProcess = wholeProcess + totalTime
    
env = simpy.Environment()
RAM = simpy.Container(env, init=100, capacity=100)