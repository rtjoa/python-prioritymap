from typing import Any, Callable, DefaultDict, List, Optional

from collections import Counter
from collections.abc import Hashable

from prioritymap import PriorityMap


class Comparable:
    def __lt__(self, other: Any) -> bool:
        raise NotImplementedError


class PrioritySet:
    def __init__(self, key: Optional[Callable[[Hashable], Comparable]] = None):
        self.key = key
        self.pm = PriorityMap()

    def add(self, item: Hashable) -> None:
        if item not in self.pm:
            priority = item if self.key is None else self.key(item)
            self.pm[item] = priority

    def remove(self, item: Hashable) -> None:
        if item not in self.pm:
            raise KeyError(f"Item {item} not in PrioritySet")
        del self.pm[item]

    def discard(self, item: Hashable) -> None:
        if item in self.pm:
            del self.pm[item]

    def peek(self) -> Hashable:
        return self.pm.peek()[0]

    def pop(self) -> Hashable:
        return self.pm.pop()[0]

    def __contains__(self, key: Hashable) -> bool:
        return key in self.pm

    def __len__(self) -> int:
        return len(self.pm)


class PriorityQueue:
    def __init__(self, key: Optional[Callable[[Hashable], Comparable]] = None):
        self.key = key
        self.pm = PriorityMap()
        self.item_count: Counter[Hashable] = Counter()

    def add(self, item: Hashable) -> None:
        if item not in self.pm:
            priority = item if self.key is None else self.key(item)
            self.item_count[item] += 1
            # Key of each item is (item, id)
            # If N of item exist, then all (item, i) for i in [1, N] exist
            self.pm[item, self.item_count[item]] = priority

    def remove(self, item: Hashable) -> None:
        if item not in self:
            raise KeyError(f"Item {item} not in PriorityMultiSet")

        del self.pm[item, self.item_count[item]]

        self.item_count[item] -= 1
        if self.item_count[item] == 0:
            del self.item_count[item]

    def discard(self, item: Hashable) -> None:
        if item in self:
            self.remove(item)

    def peek(self) -> Hashable:
        return self.pm.peek()[0][0]

    def pop(self) -> Hashable:
        item = self.pm.peek()[0][0]
        self.remove(item)
        return item

    def __contains__(self, item: Hashable) -> bool:
        return item in self.item_count

    def __len__(self) -> int:
        return len(self.pm)
