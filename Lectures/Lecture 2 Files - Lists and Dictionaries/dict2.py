my_dict = {"word": "hello", "number": 7, "number_list": [3, 2, 5]}

my_dict["more junk"] = "and stuff"

print(my_dict)

if "word" in my_dict:
    print("It is")

print(my_dict.items())

print(my_dict.keys())

print(my_dict.values())

for key, value in my_dict.items():
    print("The key", key, "is set to value", value)
    
my_dict.update({"more": "to", "be": "added"})
print(my_dict)