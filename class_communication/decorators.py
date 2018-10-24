#!/usr/bin/env python
# coding=utf-8

def multiprocess(fn):
    def decorated(*args, **kwargs):
        if args[0].mp:
            from multiprocessing import Pool
            from functools import partial
            pool = Pool(processes = args[0].num_procs)
            result = pool.map(partial(fn, self=args[0]), args[1])
        else:
            fn(*args)
    return decorated

def multithread(fn):
    def decorated(*args, **kwargs):
        len_data = args[0]._ds.num_sets
        args = list(args)
        if args[0].mp:
            chunk_len = (len_data // args[0].num_procs) + (len_data % args[0].num_procs > 0)
            from threading import Thread
            threads = []
            for i in range(args[0].num_procs):
                args[1] = range(i*chunk_len, (i+1)*(chunk_len))
                t = Thread(target = fn, args=args, kwargs=kwargs)
                threads += [t]
                t.start()
            for t in threads:
                t.join()
        else:
            args[1] = range(len_data)
            fn(*args, **kwargs)

    return decorated


def do_for(these):
    def decorator(fn):
        def decorated(*args, **kwargs):
            for i, these in enumerate(these):
                fn(these)
        return decorated
    return decorator

def time_this(fn):
    def decorated(*args, **kwargs):
        import datetime
        before = datetime.datetime.now()
        x = fn(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time: {}".format(after - before))
        return x
    return decorated


