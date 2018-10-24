#!/usr/bin/env python
# coding=utf-8
import numpy as np
from multiprocessing import Process, Array, Queue

class Operations(object):
    self.mp = self.Mp(1, False)


    @time_this
    @parallel_np_array
    def add_arrays(a, b):
        result = []
        for i, x_a in a:
            x_b = b[i]
            result.append(add_skalars(x_a, x_b))
        return result

    def add_skalars(a, b):
        '''the tidier version, since I clearly hand over the information to be processed'''
        result = a + b
        return(result)

class Data(Operations):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = 0

class DataStack(object):

    def __init__(self, num_sets):
        self.num_sets = num_sets
        self.num_procs = 3
        self.mp = False
        self.prepare()

    def prepare(self):
        self.data_list = []
        for i in range(self.num_sets):
            self.data_list.append(data(i, i + 1))

    def print_all(self):
        for i, thing in enumerate(self.data_list):
            if thing.result:
                print(thing.result)
            else:
                print('nothing here {}'.format(i))

if __name__ == '__main__':

    states = [False, True]
    for j in [10, 100, 1000, 10000, 100000, 1000000]:
        for state in states:
            print(state)
            ds = DataStack(j)
            ds.mp = state
            ds.execute()
            #ds.print_all()


