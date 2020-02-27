import json

current_file = open(r"2020-02-02T17.40.26.txt","r+")
n = 0

while n != 10:
    print(current_file.readlines())
    n += 1