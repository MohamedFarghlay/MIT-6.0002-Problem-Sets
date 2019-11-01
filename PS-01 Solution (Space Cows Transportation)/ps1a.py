###########################
# 6.0002 Problem Set 1a: Space Cows 
###########################

from ps1_partition import get_partitions
import time
import operator

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    CowData = {}
    for line in filename:
        key,value = line.split(',')
        value = str(value).strip("\n")
        CowData[str(key)] = int(value)
    return CowData

# Problem 2
def greedy_cow_transport(cows,limit=10):

    start = time.time()
    spaceship = [] 
    take = []
    NumberOfTransport = 0
    
    cows = sorted(cows.items(), key = operator.itemgetter(1),reverse=True)
    cows = dict(cows)
    while len(cows) > 0:
        maxCows = limit
        for cow in cows:
            if cows[cow] <= maxCows:
                take.append(cow)
                maxCows -= cows[cow]
            if maxCows < 1 :
                break
        spaceship.append(take)
        NumberOfTransport += 1
        for item in take:
            del cows[item]
        take=[] 
    end = time.time()
    timeTakeForGreedy = end - start
    return spaceship,NumberOfTransport, timeTakeForGreedy


# Problem 3    
def brute_force_cow_transport(cows,limit=10):
    start = time.time()
    spaceship = []
    NumberOfTransport = 0
    
    for partition in get_partitions(cows):
        if (len(cows) < 1 ):
            break

        for cow in partition:
            flag = True
            maxCowsWeight = limit
            SumOfWeights = 0
            take = []

            for item in cow:
                if item in cows:
                    SumOfWeights += cows[item]
                    take.append(item)
                    if(SumOfWeights > limit):
                        flag = False
                        break

            if(flag != False):
                if len(take) > 0:
                    spaceship.append(take)
                    NumberOfTransport += 1
                    for item in take:
                        del cows[item]
                
                
    end = time.time()
    timeTakeForBruteForce = end - start
    return spaceship, NumberOfTransport, timeTakeForBruteForce
             
        
        
# Problem 4
def compare_cow_transport_algorithms():

    filename = open(r"E:\My courses\Path Course\MIT Courses\MIT 6.0002 Introduction to Computational\Assignments & Codes\Soultion\PS1\ps1_cow_data.txt")
    cows = load_cows(filename)
    spaceshipUsingGreedy,numberOfTransUsingGreedy, TimeTakeForGreedy = greedy_cow_transport(cows)
    print(spaceshipUsingGreedy,"\n","Number Of Trans Using Greedy : ",numberOfTransUsingGreedy,"\n","Time Take : ",TimeTakeForGreedy)
    spaceshipUsingBrute, numberOdTransUsingBrute, TImeTakeUsingBrute = brute_force_cow_transport(cows)
    print(spaceshipUsingBrute,"\n","Number Of Transtion Using Brute : ",numberOdTransUsingBrute,"\n","Time Take Using Brute : ",TImeTakeUsingBrute)    


if __name__ == "__main__":
   compare_cow_transport_algorithms()
   