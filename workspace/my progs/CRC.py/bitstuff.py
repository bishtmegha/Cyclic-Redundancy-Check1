input, i = raw_input('Enter bit stream:\n'), 0;
while 1:
	i = input.find('00000',i)
	if i == -1: break
	input, i = input[:i+5] + '1' + input[i+5:], i + 4
print input