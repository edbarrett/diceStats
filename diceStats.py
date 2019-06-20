import random

def roll():
    return int((random.random()*6)+1)

def getMean(data):
    return sum(data)

def getMode(data):
    return

def getMedian(data, N):
    data.sort()
    if N%2 = 0:
        median = (data[(N/2)-1] + data[N/2])/2
    else:
        median = data[int(N/2)]
    return median
