#!/usr/bin/env python
# coding=utf-8
import numpy as np
from multiprocessing import Process, Array, Queue
from debugdecorators import TimeThis, PrintArgs, PrintReturn
from paralleldecorators import Mp, ParallelNpArray, shared_array_1D

mp = Mp(8, False)

@TimeThis
@ParallelNpArray(mp)
def add_arrays(a, b):
    result = []
    for i, x_a in enumerate(a):
        x_b = b[i]
        result.append(add_skalars(x_a, x_b))
    return result

def add_skalars(a, b):
    result = a + b
    return(result)

class DataStack(object):

    def __init__(self, num_sets):
        super(DataStack, self).__init__()
        self.num_sets = num_sets
        self.prepare('a')
        self.prepare('b')

    def prepare(self, name):
        data_list = []
        for i in range(self.num_sets):
            data_list.append(i)
        shrd_list = shared_array_1D([self.num_sets])
        shrd_list[:] = data_list[:]
        setattr(self, name, shrd_list)

    def print_all(self):
        for i, thing in enumerate(self.result):
            print(thing)

    def execute(self):
        result = add_arrays(self.a, self.b)
        setattr(self, "result", result)

if __name__ == '__main__':

    states = [False, True]
    for j in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
        for state in states:
            print(mp.switch)
            if mp.switch:
                for num_procs in [2,4,8,16]:
                    print("procs: {}".format(num_procs))
                    mp.change_num_procs(num_procs)
                    ds = DataStack(j)
                    ds.execute()
                mp.toggle_switch()
            else:
                ds = DataStack(j)
                ds.execute()
                mp.toggle_switch()


