def my_function(w, x, y, z):
	my_range = range(w, x)
	result = []
	for element in my_range:
		if element**y %z == 0:
			result.append(element**y)
	return result

#print(my_function(1,20,2,3))
#print(my_function(1,20,3,2))