def RepeatingFunc(myStr):
	char_order = []
	counts = {}

	for c in myStr:
		if c in counts:
			counts[c] += 1
		else:
			counts[c] = 1
			char_order.append(c)
	for c in char_order:
		if counts[c] == 1:
			return c
	return None

print("First Non-Repeating Character = ",RepeatingFunc('vivian'))