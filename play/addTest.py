import multiprocessing as mp
import sys

def add_print(num):
    total.value += 1
    print total.value
    #print "\r" + str(total.value)
    # sys.stdout.write("Num: " + str(total.value) + "\r")
    # sys.stdout.flush()

def setup(t):
    global total
    total = t

if __name__ == "__main__":
    total = mp.Value('i', 0)
    nums = range(20)
    pool = mp.Pool(processes=20, initializer=setup, initargs=[total])
    pool.map(add_print, nums)
    print "final: " + str(total.value)