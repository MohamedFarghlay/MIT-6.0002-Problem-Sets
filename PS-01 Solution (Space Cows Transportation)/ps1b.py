###########################
# 6.0002 Problem Set 1b: Space Change
###########################

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):

    egg_weights =  sorted(egg_weights)
    count = 0
    for egg in reversed(egg_weights):
        memo[egg] = 0        
        while egg <= target_weight:
            target_weight -= egg 
            memo[egg] += 1
            if target_weight < 0:
                return count
        count += memo[egg]

    #remove zeros from memo using dictionary comprehension
    memo = {x:y for x,y in memo.items() if y != 0}
    return count,memo

if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25,30,40,50,60,66,70,72,75,78,79,80,56,21,45,24,52,85,35,69,71,98,14,58,89,90,99,96,93,92,91,95,94,97,73,76)
    n = 1000
   
    print("Egg weights = ",egg_weights)
    print("n = ",n)
    #print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("minimum number of eggs fit for ship :", dp_make_weight(egg_weights, n))
    print()