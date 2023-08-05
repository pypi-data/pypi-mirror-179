from statistics import mean
import pyperf.tests as ptests
from pyperf.base import decorated, TestColored, get_tests
import inspect
from colorama import Fore
from tqdm import tqdm

def remove_prof(src: str):
    f = src.find('@profile')
    if f >= 0:
        d = src.find('def', f)
        src = src[d:]
    return src

def _apply_internal(name: str):
    func_obj = decorated[name]
    func = getattr(ptests, name.split('.')[-1])
    return func

def apply_one(name: str, test_name='', print_src: bool=False):
    func = _apply_internal(name)
    src_code = inspect.getsource(func)
    with TestColored(test_name=test_name, test_src=None if not print_src else remove_prof(src_code)):
        return func()

def apply_group(name: str, test_name=''):
    print(f'---- TESTGROUP {{{test_name}}} ----')
    funcs = [x for x in get_tests() if x.split('.')[0] == name]
    outs = []
    for i in tqdm(range(len(funcs))):
        outs.append(_apply_internal(funcs[i])())
    outs.sort(key=lambda x: x[0])

    m = mean([x[0] for x in outs])
    print(f'{Fore.BLUE}avg: {m:.4f}')

    for i, test in enumerate(outs):
        print(f'TOP {i+1}/{len(outs)}: \'{test.name}\'')
        print(f'  time: {test.time:.4f}')
        clr = Fore.GREEN if test.time <= m else Fore.RED
        avg = f'{clr}{int(m * 100 / test.time) - 100}%{Fore.RESET}'
        print(f'  avg: {avg}')
        if i != len(outs) - 1:
            tm_next = outs[i+1].time
            better = int(tm_next * 100 / test.time - 100)
            print(f'  better: {Fore.YELLOW}{better}%')

def get_src(name: str) -> str:
    func = _apply_internal(name)
    src_code = inspect.getsource(func)
    return remove_prof(src_code)
