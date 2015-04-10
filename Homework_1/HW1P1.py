def palindrome(my_string):
	lstring = my_string.lower()
	i = 0
	j = len(lstring)-1
	while i<=j:
		if lstring[i] != lstring[j]:
			return False
		i += 1
		j -= 1
	return True

#print(palindrome('Rats live on no evil star'))
#print(palindrome('No ab On'))
#print(palindrome('abcd efg gfed cba'))
#print(palindrome('abcdefghijklmnopqrstuvwxyz zyxwvutsrqponmlkjihgfedcba'))