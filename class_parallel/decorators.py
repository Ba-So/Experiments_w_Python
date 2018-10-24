#!/usr/bin/env python
# coding=utf-8
class Decorator_par(object):
    class Mp(object):
        def __init__(self, num_procs, switch):
            self.num_procs = num_procs
            self.switch = switch
        def toggle_switch(self):
            self.switch = not(self.switch)
        def change_num_procs(self, num_procs):
            self.num_procs = num_procs

    class time_this(object):
        def __init__(self, decorated):
            self._decorated = decorated
        def __call__(self, *args, **kwargs):
            print(args)
            import datetime
            before = datetime.datetime.now()
            x = self._decorated(*args, **kwargs)
            after = datetime.datetime.now()
            print("Elapsed Time: {}".format(after - before))
            return x

    class parallel_np_array(object):
        """do parallelisation using shared memory"""
        def __init__(self, mp=None):
            self._mp = mp
        def __call__(self, func):
            def _parall(*args, **kwargs):
                if self._mp.switch:
                    from multiprocessing import Process, Queue
                    slices = Slicer(self._mp.num_procs)
                    arr = [self.shared_array_1D(np.shape(arg)) for arg in args]
                    arr = tuple(arr)
                    result_queue = Queue()
                    for i in self._mp.num_procs:
                        p = Process(target=array_worker, args=(func, arr, x_slice, result_queue,))
                    for p in processes:
                        p.run()
                    result = [result_queue.get()]
                    for p in processes:
                        p.join()
                    return result
                else:
                    return func(*args)
            return _parall

        @staticmethod
        def shared_array_1D(shape):
            """Form shared memory 1D numpy array"""
            from multiprocessing import Array
            shared_array_base = Array(ctypes.c_double, shape[0])
            shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
            shared_array = shared_array.reshape(*shape)
            return shared_array

        @staticmethod
        def array_worker(func, fargs, x_slice, result_queue):
            """worker to do the slicing and all"""
            # finish
            result_queue.put(result)

        @staticmethod
        def Slicer():

class DebugDecorator
    class time_this(object):
        def __init__(self, decorated):
            self._decorated = decorated
        def __call__(self, *args, **kwargs):
            import datetime
            print(args)
            before = datetime.datetime.now()
            x = self._decorated(*args, **kwargs)
            after = datetime.datetime.now()
            print("Elapsed Time: {}".format(after - before))
            return x


