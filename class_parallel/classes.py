#!/usr/bin/env python
# coding=utf-8
import numpy as np
from multiprocessing import Process, Array, Queue
from decorators import ParallelDecorator, DebugDecorator

mp = ParallelDecorator.Mp(8, False)

@DebugDecorator.time_this
@ParallelDecorator.parallel_np_array(mp)
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
        shrd_list = ParallelDecorator.parallel_np_array.shared_array_1D([self.num_sets])
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
    for j in [10, 100, 1000, 10000, 100000, 1000000]:
        for state in states:
            print(mp.switch)
            ds = DataStack(j)
            ds.execute()
           #ds.print_all()
            mp.toggle_switch()


