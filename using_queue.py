# -*- coding: utf-8 -*-
# Filename:using_queue.py

import time
import random
from multiprocessing import Process, Queue


def write(item):
    for value in ['A', '2', '100']:
        print "Put %s to queue..." % value
        item.put(value)
        time.sleep(random.random())


def read(item):
    while True:
        value = item.get()
        print 'Get %s from queue.' % value


if __name__ == '__main__':
    # 父进程创建Queue，并传给各子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
