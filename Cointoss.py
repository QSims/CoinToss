####################################

#Created by: Simsarul Haq Vengasseri
#Date: 30/10/2017

# This program is for experimenting the randomness. This program uses pyquil and reference-qvm to simulate the quantum computation.
# Please specify the path to the referenceqvm directory to import the api library.



import sys
sys.path.insert(0, '/home/infinitylabs/Documents/QSimulations/QSims/reference-qvm/referenceqvm')
import api
import pyquil.quil as pq
from pyquil.gates import *

qvm = api.SyncConnection()

p = pq.Program().inst(H(0)).measure(0,0)

def coin_toss(iteration_count):
    results = qvm.run(p, [0],iteration_count)
    print results


if __name__ == '__main__':
    if (len(sys.argv)>1):
        try:
            iteration_count = int(sys.argv[1])
        except ValueError:
            print ("Enter an integer as argument.")
            sys.exit(1)
    else:
        iteration_count = 1
    coin_toss(iteration_count)
