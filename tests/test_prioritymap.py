import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")


from prioritymap import PriorityMap  # noqa: E402


def test_priority_map_set_get():
    pm = PriorityMap()
    pm["first"] = 1
    assert pm["first"] == 1


def test_priority_map_contains_delete_truthiness():
    pm = PriorityMap()
    pm["first"] = 1
    assert pm
    assert "first" in pm
    del pm["first"]
    assert not pm
    assert "first" not in pm
    assert "second" not in pm


def test_priority_map_peek_pop():
    pm = PriorityMap()
    pm["first"] = 1
    pm["second"] = 2
    pm["third"] = 3
    pm["fourth"] = 4
    assert pm.peek() == ("first", 1)
    assert pm.pop() == ("first", 1)
    assert pm.peek() == ("second", 2)
    assert pm.pop() == ("second", 2)
    assert pm.peek() == ("third", 3)
    assert pm.pop() == ("third", 3)
    assert pm.peek() == ("fourth", 4)
    assert pm.pop() == ("fourth", 4)
    assert not pm
