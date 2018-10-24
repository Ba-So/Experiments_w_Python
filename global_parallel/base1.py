#!/usr/bin/env python
# coding=utf-8
import base2 as b2
import global_var as gv
import update as up
from multiprocessing import Pool



class moretest():
    def __init__(self):
        self.update = up.Updater()
    def changea(self):
        global poop
        self.update.value(gv.a + 1 + poop)
        return None

def reassemble(x):
    update = up.Updater()



if __name__ == '__main__':
    update = up.Updater()
    b2.printx()
    global poop
    poop = 3
    moretest().changea()
    print gv.a
    b2.printx()
    b2.update()
    b2.printx()
    print gv.a
    up.prep_mp(5)

    pool = Pool(processes = gv.mp['n_procs'])
    print(gv.mp['chunks'])
    helper = [i for i in range(gv.mp['n_procs'])]
    update.part_of_array(pool.map(b2.addone, helper), gv.mp['chunks'])
    print gv.b
    print gv.c
    pool.map(b2.print_hi, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 3)



