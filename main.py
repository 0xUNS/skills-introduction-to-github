import time
from contextlib import contextmanager

@contextmanager
def timer(name: str = 'Block'):
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f'{name} took {end - start:.4f}s')

# Usage
with timer('Heavy computation'):
    # place code to time here
    sum(i*i for i in range(10_000_000))
