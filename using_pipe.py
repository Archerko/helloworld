# -*- coding: utf-8 -*-
# Filename:using_queue.py
from multiprocessing import Process, Pipe
import time
import random


def sendmsg(conn):
    for value in ['A', 'B', 'C']:
        print 'Send %s to Pipe' % value
        conn.send(value)
        time.sleep(random.random())


def recvmsg(conn):
    while True:
        value = conn.recv()
        print 'Recv %s from Pipe' % value

if __name__ == '__main__':
    conn1, conn2 = Pipe()
    ps = Process(target=sendmsg, args=(conn1,))
    pr = Process(target=recvmsg, args=(conn2,))

    ps.start()
    pr.start()

    ps.join()
    pr.terminate()
