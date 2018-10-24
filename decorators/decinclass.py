#!/usr/bin/env python
# coding=utf-8
# this way the usual decorator behaviour is maintained.
# however no access to self. functions need to be defined without self.
# I think this is desirable. => explicit passing. especially for
# parallelization
class operations(object):

    def __init__(self) :
        self.a = 2

    class time_this_arg(object):
        def __init__(self, more):
            self.more = more
            print(more)
        def __call__(self, fun):
            def timeit(*args, **kwargs):
                import datetime
                before = datetime.datetime.now()
                x = fun(*args, **kwargs)
                after = datetime.datetime.now()
                print("Elapsed Time: {}".format(after - before))
                return x
            return timeit

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

    @staticmethod
    @time_this_arg('a string')
    @time_this
    def add_two(a):
        return a + 2

    @staticmethod
    @time_this
    def add_three(a):
        return a + 3

    @staticmethod
    def add_four(a):
        return a + 4

if __name__ == '__main__':

    a = operations()
    print(a.add_two(2))
    print(a.add_three(2))
    print(a.add_four(2))
