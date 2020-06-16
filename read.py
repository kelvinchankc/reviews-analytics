data = []
with open('reviews', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))
