input = open("./inputs/1a.txt", "r").read().split()

nums = [int(n) for n in input]

for n in nums:
	for o in nums:
		for p in nums:
			if n + o + p == 2020:
				print(n * o * p)
				break


