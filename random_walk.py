
import random
def randomwalk_list():
    last, rand = 1, random.random() # init candidate elements
    nums = []                       # empty list
    while rand > 0.1:                # threshhold terminator
        if abs(last-rand) >= 0.4:    # accept the number
            last = rand
            nums.append(rand)       # add latest candidate to nums
        else:
            print( '*',)               # display the rejection
        rand = random.random()      # new candidate
    nums.append(rand)               # add the final small element
    return nums

for num in randomwalk_list():
    print (num,)

