multiline_string = """xyz
xyz
xyz"""

also_a_multiline_string = '''
            __
           / _)
    .-^^^-/ /
 __/       /
<__.|_|-|_|'''

print(multiline_string)
print(also_a_multiline_string)

"""
This is a multiline comment.
Since I didn't assign the string
to any binding, the compiler ignores
the string and it is just a comment.
Python docstrings are made this way
as well, but we'll get to that later.
"""
