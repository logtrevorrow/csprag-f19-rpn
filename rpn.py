#!/usr/bin/env python3

def calculate(string):
	stack = list()
	for token in string.split():
		if token == '+':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		elif token == '-':
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = arg1 - arg2
			stack.append(result)
		elif token == '^':
			arg2 = stack.pop()
			arg1 = stack.pop()
			i = 0
			result = 1
			while i < arg2:
				result = result * arg1
				i += 1
			stack.append(result)
		else:
			stack.append(int(token))
		print(stack)
	if len(stack) != 1:
		raise TypeError('Malformed input: ' + string)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__': 
	main()