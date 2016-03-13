from functions import *

class test():
    def __init__(self, value):
        self.value = value

objs = []

item1 = test(3)
item2 = test(4)
item3 = test(1)

objs.extend((item1, item2, item3))
sorted_objects = sort_objects(objs)


for i in range(len(sorted_objects) - 1):
    if sorted_objects[i].value < sorted_objects[i + 1].value:
        raise RuntimeError('Sorting not performing')
    else:
        pass
