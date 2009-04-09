import sys
from time import sleep
runs = int(sys.argv[1])
for i in xrange(runs):
    print i
    #sys.stdout.flush()
    sleep(2)
