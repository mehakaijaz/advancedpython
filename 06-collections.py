#collections : counter,namedtuple(similar to struct) ,ordereddict(less important now,way of using dictionary),defaultdict,deque
"""from collections import Counter
a="aaabbbbcccccddd"
my_counter=Counter(a)
print(my_counter)
print(my_counter.elements())#this will give itertool obkject
print(list(my_counter.elements()))#this will give list
print(my_counter.most_common(3))
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])
print(my_counter.values())
print(my_counter.keys())
print(my_counter.items())"""
"""from collections import namedtuple
point=namedtuple('point','x,y')
pt=point(1,-4)
print(pt)
print(pt.x,pt.y)"""
#orderedDict= is a dictionary subclass in Python that maintains the order of the 
# items based on the order of their insertion. In a regular dictionary (dict), the order of items is not guaranteed, 
# but OrderedDict remembers the order in which items were added.
from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict()

# Adding items
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])


#defaultdict= is another dictionary subclass that provides a default value 
# for a nonexistent key. When creating a defaultdict, you specify a default factory function for the dictionary. 
# This function is used to provide a default value whenever a new key is accessed for the first time.
from collections import defaultdict

# Creating a defaultdict with default value 0
default_dict = defaultdict(int)

# Adding items without explicit initialization
default_dict['a'] += 1
default_dict['b'] += 2
default_dict['c'] += 3

print(default_dict)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3})

#deque= stands for "double-ended queue," and it is a class in Python's collections module. 
# A deque is a data structure that allows for fast and efficient append and pop operations 
# from both ends of the queue. It is implemented as a doubly-linked list,
# which means that each element in the deque contains a reference to the next and previous element

from collections import deque

# Creating a deque
my_deque = deque([1, 2, 3, 4, 5])

# Appending elements
my_deque.append(6)          # append to the right end
my_deque.appendleft(0)      # append to the left end

print(my_deque)  # Output: deque([0, 1, 2, 3, 4, 5, 6])

# Popping elements
right_end = my_deque.pop()       # pop from the right end
left_end = my_deque.popleft()    # pop from the left end

print(right_end, left_end)  # Output: 6 0
print(my_deque)  # Output: deque([1, 2, 3, 4, 5])

