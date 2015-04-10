def caesar(infile, outfile, shift):
	file_in = open(infile, "r")
	file_out = open(outfile, "w")
	while True:
		character = file_in.read(1)
		if not character:
			break
		elif 97 <= ord(character.lower()) <= 123:
			num = ord(character.lower())
			num += shift - 97
			new_char = (num%26) + 97
			file_out.write(chr(new_char))
	file_in.close()
	file_out.close()

#caesar("my_file.txt", "out1.txt", 88)