
# No other modules apart from 'math' need to be imported
# as they aren't required to solve the assignment

# Import required module/s
import math


def computeDistance(x1, y1, x2, y2):
	val1=(x2-x1)**2
	val2=(y2-y1)**2
	res = math.sqrt(val1+val2)
	return format(res, '.3f')


if __name__ == "__main__":
	"""Main function, code begins here
	"""
	x1 = 1.0; y1 = 1.3
	x2 = 4.2; y2 = 4.6
	temp = computeDistance(x1, y1, x2, y2)
	print("Distance computed:  ",temp)