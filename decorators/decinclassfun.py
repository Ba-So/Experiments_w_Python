#!/usr/bin/env python
# coding=utf-8

# this way the decorator behaviour unusual, self becomes accessible.
class operations(object):

    def __init__(self) :
        self.a = 2

    def time_this(decorated):
        def decorate(*args, **kwargs):
            print(args)
            import datetime
            before = datetime.datetime.now()
            x = decorated(*args, **kwargs)
            after = datetime.datetime.now()
            print("Elapsed Time: {}".format(after - before))
            return x
        return decorate

    @time_this
    def add_two(self):
        return self.a + 2

if __name__ == '__main__':

    a = operations()
    print(a.add_two())
