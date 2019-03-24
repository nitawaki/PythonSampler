# coding:utf-8
import time

def heavy( i ):
    time.sleep(0.1)
    print(i)

def StopWatch( func, count ):
    start = time.time()
    func(count)
    print(time.time() - start)

def normalFunction(count):
    for i in range(count):
        heavy(i)

import multiprocessing as mp

# processを利用
from multiprocessing import Process
def process(count):
    jobs = []
    for data in range(count):
        job = Process(target=heavy, args=(data,))
        jobs.append(job)
        job.start()
    [job.join() for job in jobs]


# Poolを利用
from multiprocessing import Pool
def mapPool(count):
    p = Pool(mp.cpu_count())
    p.map( heavy , list(range(count)))
    p.close()

count = 10
print('normal')
StopWatch( normalFunction, count )
print('Process')
StopWatch( process, count )
print('Pool(cpu:{0})'.format(mp.cpu_count()))
StopWatch( mapPool, count )
