# -*- coding:utf-8 -*-
import threading
import time



def FuncTest(tdata):
    print(tdata)


class mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self)

    def run(self):
        lock.acquire()
        FuncTest(ft)
        lock.release()


def MutiThread(num):
    threads = []
    i = 0
    global ft
    for x in range(num):
        # print(num)
        threads.append(mythread(num))
    for t in threads:
        time.sleep(0.5)
        lock.acquire()
        ft = GetThreadParam(datafile, num, i)
        print ('[%s]Thread:%s,Testdata:%s'%(time.ctime(),t,ft))
        i = i + 1
        t.start()
        lock.release()
    for t in threads:
        t.join()


def GetThreadParam(datafile, num, curthread):
    # 线程数需要小于文件行数
    f = open(datafile, 'r')
    lines = f.readlines()
    divres = divmod(len(lines), num)
    if curthread < (num - 1):
        res = lines[curthread * divres[0]:(curthread + 1) * divres[0]]
    elif curthread == (num - 1):
        res = lines[curthread * divres[0]:((curthread + 1) * divres[0] + divres[1])]
    return res
    f.close()


if __name__ == '__main__':
    global num, lock
    datafile = 'E:a.txt'

    num = 3  # num 并发数

    lock = threading.Lock()
    MutiThread(num)