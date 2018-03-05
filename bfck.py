#BrainF*ck Interpreter

def isNum(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

stack = [0]*30000

instructions = raw_input()
length = len(instructions)
cur_pointer = 0
prev_open = -1
i = 0
while 1:
	#print "processing " + instructions[i]
	if instructions[i] == '+':
		stack[cur_pointer] = stack[cur_pointer] + 1
		i = i + 1
	elif instructions[i] == '-':
		stack[cur_pointer] = stack[cur_pointer] - 1
		if stack[cur_pointer] < 0:
			print("Stack value goes below zero. This is not allowed. Exiting")
			break
		i = i + 1
	elif instructions[i] == '>':
		cur_pointer = cur_pointer + 1
		if cur_pointer == 30000:
			print("Exceeded max stack value aka overflow. Exiting")
			break
		i = i + 1
	elif instructions[i] == '<':
		cur_pointer = cur_pointer - 1
		if cur_pointer < 0:
			print("Underflow!!!. Exiting")
			break
		i = i + 1
	elif instructions[i] == '[':
		prev_open = i
		if stack[cur_pointer] == 0:
			print("stack value is 0 so no looping")
			while instructions[i] != ']':
				i = i + 1
		else:
			i = i + 1
	elif instructions[i] == ']':
		if prev_open == -1:
			print("Syntax Error")
			break
		elif stack[cur_pointer] == 0:
			i = i + 1
		else:
			i = prev_open
			continue
	elif instructions[i] == ',':
		temp = raw_input("Input : ")
		if isNum(temp):
			stack[cur_pointer] = (int)(temp)
		else:
			stack[cur_pointer] = ord(temp)
		i = i + 1
	elif instructions[i] == '.':
		print(chr(stack[cur_pointer]))
		i = i + 1
	if i == length:
		break