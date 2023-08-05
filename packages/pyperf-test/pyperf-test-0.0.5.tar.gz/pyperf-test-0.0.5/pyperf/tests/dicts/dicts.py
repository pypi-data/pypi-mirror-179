from pyperf.base import profile

xs = {str(i): i for i in range(0, 1_000_000)}


@profile()
def get_keys1():
	return list(xs.keys())


@profile()
def get_keys2():
	return [key for key in xs]

@profile()
def get_keys3():
	return [*xs]