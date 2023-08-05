import time
from functools import wraps
import inspect
from dataclasses import dataclass
from colorama import Fore, init
from collections import namedtuple

init(autoreset=True)

class TestColored:
    def __init__(self, test_name, test_src=None):
        self.test_name = test_name
        self.test_src = test_src

    def __enter__(self):
        print(f'**** {Fore.GREEN}TEST [{self.test_name}]{Fore.RESET} ****')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.test_src is not None:
            print(f'{Fore.LIGHTBLACK_EX}SOURCE CODE:')
            print(f'{Fore.LIGHTBLACK_EX}{self.test_src}')

@dataclass(slots=True)
class ProfiledFunc:
    src: str

RetTuple = namedtuple('INFO', ('time', 'pcs', 'name',))

decorated: dict[str, ProfiledFunc] = {}


def profile(number: int = 100):
    def _profile(func):
        module = inspect.getmodule(inspect.stack()[1][0])
        newname = f'{module.__name__.split(sep=".")[-2]}.{func.__name__}'
        #newname = func.__name__
        decorated[newname] = ProfiledFunc(src='')

        @wraps(func)
        def wrapper(*args, **kwargs):
            all_time = 0.0
            for _ in range(number):
                start = time.perf_counter()
                func(*args, **kwargs)
                end = time.perf_counter()
                all_time += end - start
            all_time /= number

            return RetTuple(all_time, number, func.__name__)

        return wrapper
    return _profile

def get_tests() -> list[str]:
    return list(decorated.keys())

def get_groups() -> list[str]:
    return list(set([x.split(sep='.')[0] for x in decorated]))