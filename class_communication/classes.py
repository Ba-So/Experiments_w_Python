#!/usr/bin/env python
# coding=utf-8
from decorators import *

# MetaClass Containing Operations
class Operations:

    def add_next(self):
        b = self.ask_from(self.name + 1, "a", self.name)
        self.resulta = self.a + b
        self.resultb = self.a + self.inbox.a

class Inbox:

    def __init__(self, data):
        self._data = data
# Data Points on a grid, need to communicate
class Data(Operations):

    def __init__(self, a, name):
        self.a = a
        self.name = name
        self.inbox = Inbox(self)

    def setDS(self, stack):
        self._ds = stack

    def ask_from(self, who, what, me):
        return self._ds.communicate(who, what, me)

    def send(self, what):
        return getattr(self, what)

    def recv(self, what, value):
        setattr(self.inbox, what, value)


# Containor holding the datapoints, managing multithreading.
class DataStack():

    def __init__(self, num_sets):
        self.num_sets = 0
        self.data_list = []
        self.prepare(num_sets)

    def add(self):
        i = self.num_sets
        self.data_list.append(Data(i, i))
        self.data_list[i].setDS(self)
        self.num_sets += 1

    def prepare(self, num_sets):
        for i in range(num_sets):
            self.add()

    def print_all(self):
        for i, thing in enumerate(self.data_list):
            if thing.resulta:
                print(thing.resulta)
            else:
                print('nothing here {}'.format(i))
            if thing.resultb:
                print(thing.resultb)
            else:
                print('nothing here {}'.format(i))

    def communicate(self, who, what, to):
        if who < self.num_sets:
            package = self.data_list[who].send(what)
        else:
            package = 0

        self.data_list[to].recv(what, package)
        return package

    def execute(self, who, what):
        if who < self.num_sets:
            getattr(self.data_list[who], what)()


class UseCase:
    def __init__(self):
        self.num_procs = 3
        self.mp = False

    @time_this
    @multithread
    def execute(self, x_slice):
        list_of = []
        for i in x_slice:
            self._ds.execute(i, "add_next")

    @time_this
    @multithread
    def execute2(self, x_slice):
        list_of = []
        for i in x_slice:
            self._ds.execute(i, "add_next")
            self._ds.execute(i, "add_next")

    @time_this
    @multithread
    def execute4(self, x_slice):
        list_of = []
        for i in x_slice:
            self._ds.execute(i, "add_next")
            self._ds.execute(i, "add_next")
            self._ds.execute(i, "add_next")
            self._ds.execute(i, "add_next")

    def setDS(self, ds):
        self._ds = ds



if __name__ == '__main__':
    for i in [1000000]:
        print(i)
        ds = DataStack(i)
        uc = UseCase()
        uc.setDS(ds)
        uc.execute(i)
        uc.execute2(i)
        uc.execute4(i)
        uc.mp = True
        for j in [16]:
            uc.num_procs = j
            uc.execute(i)
            uc.execute2(i)
            uc.execute4(i)
