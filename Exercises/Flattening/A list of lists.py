# use this algorithm for one level depth
from collections import Iterable
l = [1,[0,1],[2,3]]

flatten_list = []


flat_list = []
for item in l:
    if isinstance(item, Iterable):
        flatten_list.extend(item)
    else:
        flatten_list.append(item)


print(flatten_list)