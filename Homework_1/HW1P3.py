def my_function(my_list):
	my_list.sort()
	results1 = []
	results2 = []
	i = 0
	for element in my_list:
		if i % 2 != 0:
			results1.append(element)
		else:
			results2.append(element)
		i += 1
	results2.reverse()
	results = results1 + results2
	return results

for element in random.randint(1, 10)
	my_list=[4,3,6,7,4,3,9]
print(my_function(my_list))