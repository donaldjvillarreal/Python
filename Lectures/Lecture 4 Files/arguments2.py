import sys

def my_function(param1, param2):
    print(param1)
    print(param2)
    
if __name__ == "__main__":
    my_function(sys.argv[1], sys.argv[2])