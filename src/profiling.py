#!/usr/bin/env python3

from mathematica import Math
import sys
import cProfile

### Help message
print("Enter numbers. Ctrl+D to continue.")

### global variables ###
x=sys.stdin.readlines()
N=len(x)

pr = cProfile.Profile()
pr.enable()

def avrg(): 
    # average of input numbers  

    def sumerino_1():
        # sum of input numbers
        global x
        sum=0
        for i in range(len(x)):
            x[i]=x[i].replace('\n','')
            sum = Math(sum) + Math(x[i])
        return sum 

    def dividing_1():
        # 1/N
        global N
        div = Math(1.0) / Math(N)
        return div

    def mult_1(a,b):
        m = a * b
        return m

    average = mult_1(sumerino_1(), dividing_1())
    return average

av = avrg()
def rootino():
    def dividing_2():
        global N
        div = Math(1.0) / (Math(N) - Math(1))
        return div

    def bracket():
        def sumerino_2():
            global x
            sum=0
            for i in range(len(x)):
                x[i]=x[i].replace('\n','')
                sum = Math(sum) + (Math(x[i]) ** Math(2))
            return sum 

        def mult_2():
            global N, av
            m = Math(N) * (av ** Math(2))
            return m

        def sub(a,b):
            s = a - b
            return s
        
        brac = sub(sumerino_2(), mult_2())
        return brac

    def mult_3(a,b):
        m = a * b
        return m
    
    multRes = mult_3(dividing_2(),bracket())
    root = multRes.root()
    return root
avrg()
rootino()
pr.disable()
pr.print_stats(sort='time')
pr.dump_stats("profiling-v1.prof")