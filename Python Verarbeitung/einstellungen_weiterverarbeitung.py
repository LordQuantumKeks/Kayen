import re
import os


with open('../webseite/changes.txt', 'r') as currentfile:
    change = currentfile.read()
    change = re.sub('[{}" ]', '', change)
    print(change)

print('writing ' + change + ' to general_settings.txt\n')

with open('../PipeData/general_settings.txt', 'r+') as currentfile:
    data = currentfile.readlines()
    for line in data:
        print(line)


