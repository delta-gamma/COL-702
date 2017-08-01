import random
from heapq import heappush, heappop
from random import randint

number_of_lists = randint(0,5)
random_data = []
orderedL = []
heap = []

for number in range(0,number_of_lists):
    list_length = randint(0,10)         # maximum list length is limited by 10
    random_data.append(random.sample(range(1, 101), list_length))

for lists in range(0,len(random_data)):
    random_data[lists].sort()

for lists in range(0,len(random_data)):
    print random_data[lists]
    print len(random_data[lists])

for i in range(0,10):
    for lists in range(0, len(random_data)):
        if i < len(random_data[lists]):
            heappush(heap, random_data[lists][i])
    if heap:
        x = heappop(heap)
        orderedL.append(x)

while heap:
    orderedL.append(heappop(heap))

print "The output list is: \n"
print orderedL
