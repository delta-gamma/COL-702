# Author: Mahima Manik
# Date: 01-08-2017
import random
from heapq import heappush, heappop
from random import randint

number_of_lists = randint(0,50)     #number of lists is randomly generated number between 0 to 50
random_data = []
orderedL = []
heap = []

# maximum length of each list can be 100
#random.sample returns a list of length list_length and appends it to random_data. So at the end of the for loop, random_data becomes list of lists
for number in range(0, number_of_lists):
    list_length = randint(0, 100)         
    random_data.append(random.sample(range(1, 1001), list_length))  

#sorting the data in the list
for lists in range(0,len(random_data)):
    random_data[lists].sort()

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
