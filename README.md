# Tree Containers

Asymptotically-efficient tree-based containers in pure Python. Licensed under the [Apache License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## PriorityMap

A combination between a heap and a map that stores key:priority mappings.

### Operations
| Operation | Description | Runtime Complexity |
|---|---|---|
| `__getitem__(key)` | Get priority of key | O(1) |
| `__setitem__(key, priority)` | Set priority of key | O(log n) |
| `__delitem__(key)` | Remove a key | O(log n) |
| `__contains__(key)` | Check whether a key is contained | O(1) |
| `__len__()` | Return the number of keys contained | O(1) |
| `peek()` | Get lowest-priority key and its priority | O(1) |
| `pop()` | Get and remove lowest-priority key and its priority | O(log n) |

### Example Console Output
```py
>>> from prioritymap import PriorityMap
>>> pm = PriorityMap()
>>> pm["first"] = 1
>>> pm["second"] = 2
>>> pm["underdog"] = 5
>>> pm.peek()
('first', 1)
>>> pm["underdog"] = 0
>>> len(pm)
3
>>> pm.pop()
('underdog', 0)
>>> pm.pop()
('first', 1)
>>> pm.pop()
('second', 2)
>>> len(pm)
0
```
## PriorityQueue

Like Java's PriorityQueue, but with O(log(n)) arbitrary removal and O(1) containment check (versus linear for both in Java).

### Operations
| Operation | Description | Runtime Complexity |
|---|---|---|
| `__init__(key=None)` | Key is a function determining priority of an item, identity function by default. | O(1) |
| `add(item)` | Add an item | O(log n) |
| `remove(item)` | Remove an item, erroring if it doesn't exist | O(log n) |
| `discard(item)` | Remove an item if it exists | O(log n) |
| `peek()` | Get the lowest-priority item | O(1) |
| `pop()` | Get and remove the lowest-priority item | O(log n) |
| `__contains__(item)` | Check whether an item is contained | O(1) |
| `__len__()` | Return the number of items contained | O(1) |

## PrioritySet

Exactly like the PriorityQueue above, but slightly optimized and not tracking multiples of items. (Adding an existing item does nothing).

Roughly, PrioritySet is to PriorityMap as set is to dict.

## TreeMap

To be implemented.