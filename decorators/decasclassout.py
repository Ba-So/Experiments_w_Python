#!/usr/bin/env python
# coding=utf-8
# this way the decorator behaviour unusual, self becomes accessible.
class time_this(object):
    @classmethod
    def time_this(self, decorated):
        def decorate(*args, **kwargs):
            print(args)
            import datetime
            before = datetime.datetime.now()
            x = decorated(*args, **kwargs)
            after = datetime.datetime.now()
            print("Elapsed Time: {}".format(after - before))
            return x
        return decorate

class operations(object):

    def __init__(self) :
        self.a = 2

    @time_this.time_this
    def add_two(self, a):
        return self.a + 2

if __name__ == '__main__':

    a = operations()
    print(a.add_two(2))
