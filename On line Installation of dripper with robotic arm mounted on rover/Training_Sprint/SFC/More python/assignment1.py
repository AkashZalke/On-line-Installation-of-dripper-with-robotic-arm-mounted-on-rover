
# No other modules apart from 'argparse' need to be imported
# as they aren't required to solve the assignment

# Import required module/s
import argparse

def raise_power_of_N(value):
	"""Computes square of positional argument (N) and cube as well if optional argument 'c' or 'cube' is passed.

	Example
	-------
	$ python3 assignment1.py -h
	
	usage: assignment1.py [-h] [-c] N
	
	Calculate square and/or cube of N

	positional arguments:
		N           input the number

	optional arguments:
		-h, --help  show this help message and exit
		-c, --cube  calculate cube of N as well
	
	Week-5 Assignment-1

	=======

	$ python3 assignment1.py 5

	Square of N: 25

	=======

	$ python3 assignment1.py 5 -c
	OR
	$ python3 assignment1.py 5 --cube

	Square of N: 25
	Cube of N: 125
	"""

	##############	ADD YOUR CODE HERE	##############
	if args.cube:
		print(value**2)
		print(value**3)
	else:
		print(value**2)
		
	

	##################################################


if __name__ == "__main__":
	"""Main function, code begins here
	"""
	
	parser = argparse.ArgumentParser()
	parser.add_argument('square',type=int, help='Square of a number')
	parser.add_argument('-c','--cube',action='store_true', help='cube of a number')
	args = parser.parse_args()
	raise_power_of_N(args.square)
