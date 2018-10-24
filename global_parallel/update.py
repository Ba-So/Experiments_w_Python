#!/usr/bin/env python
# coding=utf-8
import global_var as gv

class Updater():

    def __init__(self):
        self.globals_dict = {
            'a' : gv.a
        }

    def value(self, x):
        self.globals_dict['a'] = x
        self.finish()
        return None

    def finish(self):
        gv.a = self.globals_dict['a']
        return None

    def part_of_array(self, x, chunks):
        for i, y in enumerate(x):
            gv.b[chunks[i]] = y

    def insert_array(self, x, i):
        gv.c[i] = x
        return None

def prep_mp(n_procs):
    n_procs = 5
    chunk_l = len(gv.b)/n_procs
    chunks = []
    for i in range(n_procs):
        chunks.append(slice(i*chunk_l, (i+1)*chunk_l))

    gv.mp = {
        'n_procs' : n_procs,
        'chunks'  : chunks
    }
    return None




