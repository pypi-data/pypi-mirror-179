from pyperf.base import get_tests, get_groups
from pyperf.apply import apply_one, apply_group

if __name__ == '__main__':
	print(get_tests())
	print(get_groups())
	#apply_one('classes.class_no_slots', print_src=True)
	apply_group('lists')

