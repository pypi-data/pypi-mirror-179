from pyperf.base import profile
from dataclasses import dataclass

class NoSlots:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = (1, 2, 34)

class Slots:
    __slots__ = ['a', 'b', 'c']
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = (1, 2, 34)

@dataclass
class DataclassNoSlots:
    a: int = 1
    b: int = 2
    c: tuple = (1, 2, 34)

@dataclass(slots=True)
class DataclassSlots:
    a: int = 1
    b: int = 2
    c: tuple = (1, 2, 34)

@profile()
def class_slots():
    xs = [Slots() for _ in range(0, 100_000)]
    return xs

@profile()
def class_no_slots():
    xs = [NoSlots() for _ in range(0, 100_000)]
    return xs

@profile()
def dataclass_no_slots():
    xs = [DataclassNoSlots() for _ in range(0, 100_000)]
    return xs

@profile()
def dataclass_slots():
    xs = [DataclassSlots() for _ in range(0, 100_000)]
    return xs
