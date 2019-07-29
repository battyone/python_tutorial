
# In a heap, the heap[0], aka first element, is always the
# smallest element. heappop() will remove first element and
# make sure the new first element is the smallest.
# 
# use min() or max() when only looking for the smallest or
# highest value. 

# %%

# find the 4 smallest and highest numbers in a collection of
# random values

import heapq
from random import randint

r = [randint(1, 1000) for i in range(0, 10)]
print(r)
print(heapq.nsmallest(4, r))
print(heapq.nlargest(4, r))

#%%
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s:s['price'])
print(cheap)


#%%
# building a priority queue with heapq. We want the 
# item returned (popped) with the highest priority

# heapq always stores smallest to highest (heap ordering). Therefore,
# we -1 * priority

class PriorityQueue:
    def __init__(self):
        
        self.queue = []
        # keep an increasing index to preserve the
        # order of items with the same priority
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index =+ 1
    
    def pop(self):
        return heapq.heappop(self.queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item({self.name})'

p = PriorityQueue()
p.push(Item('foo'), 1)
p.push(Item('miow'), 5)
p.push(Item('bar'), 8)
p.push(Item('moo'), 2)

# should print bar
print(p.pop())




