#!/usr/bin/env python
# coding=utf-8
import ctypes
import numpy as np
from multiprocessing import Process, Queue, Array
from debugdecorators import TimeThis, PrintArgs, PrintReturn

class Mp(object):
    def __init__(self, num_procs, switch):
        self.num_procs = num_procs
        self.switch = switch
    def toggle_switch(self):
        self.switch = not(self.switch)
    def change_num_procs(self, num_procs):
        self.num_procs = num_procs

class ParallelNpArray(object):
    """do parallelisation using shared memory"""
    def __init__(self, mp=None):
        self._mp = mp
    def __call__(self, func):
        def _parall(*args, **kwargs):
            if self._mp.switch:
                slices = self.prepare_slices(args[0], self._mp)
                result_queue = []
                processes = []
                for i in range(self._mp.num_procs):
                    q = Queue()
                    p = Process(target=self.array_worker, args=(func, args, slices[i], q,))
                    processes.append(p)
                    result_queue.append(q)
                for p in processes:
                    p.run()
                results = []
                for i, p in enumerate(processes):
                    results.append(result_queue[i].get())
                    #p.join()
                return results
            else:
                return func(*args)
        return _parall

    @staticmethod
  # @DebugDecorator.PrintArgs
    def array_worker(func, fargs, x_slice, result_queue):
        """worker to do the slicing and all"""
        args = [arg[x_slice] for arg in fargs]
        result = func(*args)
        result_queue.put(result)

    @staticmethod
    # @DebugDecorator.PrintArgs
    def prepare_slices(x_list, mp):
        """returns appropriate slices for worker"""
        l_shape = np.shape(x_list)
        if mp.num_procs > 1:
            len_slice = l_shape[0] % (mp.num_procs - 1)
        else:
            len_slice = l_shape[0]
        slices = []
        for proc in range(mp.num_procs):
            slices.append(slice(proc * len_slice, (proc + 1) * len_slice))
        return slices

# @DebugDecorator.PrintReturn
# @DebugDecorator.PrintArgs
def shared_array_1D(shape):
    """Form shared memory 1D numpy array"""
    from multiprocessing import Array
    shared_array_base = Array(ctypes.c_double, shape[0])
    shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
    shared_array = shared_array.reshape(*shape)
    return shared_array



