#!/usr/bin/env python
# coding=utf-8
import global_var as gv
import update as up
import numpy as np
import multiprocessing


def printx():
    print(gv.a)
    return None

def update():
    update = up.Updater()
    update.value(gv.a + 3)
    return None

def addone(chunk):
    update = up.Updater()
    x = gv.b[gv.mp['chunks'][chunk]]
    print chunk
    update.insert_array(chunk, chunk)
    return np.add(x, 1)

def print_hi(i):
    print('this is process {}, printing {}').format(multiprocessing.current_process(), i)
    return None


