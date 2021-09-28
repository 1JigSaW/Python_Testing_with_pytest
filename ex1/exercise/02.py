import pytest
from collections import namedtuple

Task = namedtuple('Task', ['a', 'b', 'c', 'd'])
Task.__new__.__defaults__ = (None, None, None, None)

def test_equal():
	t_task = Task('do something', 'okken', 'f', '21')
	t_before = Task('finish book', 'brian', '22')
	assert t_task == t_before