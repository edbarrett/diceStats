"""
TO DO LIST:
- Check for empty list
- Implement matplotlib for distribution graph
- finish getMode
"""

import random


"""
roll is used to gather data. Simulates rolling a dice.
Returns a number from 1-6
"""
def roll():
    return int((random.random()*6)+1)

"""
getMean prints and returns the mean of the data
"""
def getMean(data):
    N = len(data)
    mean = sum(data)/N
    print('Mean: ' + str(mean))
    return mean

"""
getMode prints the element that occurs the most in the data and
returns it.
"""
def getMode(data):
    return

"""
getMedian sorts a list from smallest to largest then
computed the median.
The median is printed and returned.
"""
def getMedian(data):
    N = len(data)
    data.sort()
    if(N%2 == 0):
        median = (data[(int(N/2)-1)] + data[int(N/2)])/2
    else:
        median = data[int(N/2)]
    print('Median: ' + str(median))
    return median


list = []
sample_size = 10
print('Rolling...')
for n in range(sample_size):
    list.append(roll())
print('Sample data has been gathered.')
list.sort() #Not needed, but good for visuals
print(list) #Not needed, but good for visuals
getMedian(list)
getMean(list)
