import os
from functions.write_file import write_file

print (f"Result for not ipsum")
not_ipsum = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print (not_ipsum)

print (f"Result for lorem ipsum")
lorem_ipsum = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(lorem_ipsum)

print (f"Result for not allowed")
not_allowed = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(not_allowed)
