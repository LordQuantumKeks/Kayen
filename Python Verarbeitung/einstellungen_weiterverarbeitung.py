import re
import os

with open('../webseite/changes.txt', 'r') as currentfile:
    change = currentfile.read()
    change = re.sub('[{}" ]', '', change)
    changeName, seperator, changeValue = change.rpartition(":")

with open('../PipeData/general_settings.txt', 'r+') as currentfile:
    data = currentfile.readlines()
    x = -1
    for line in data:
        x += 1
        if changeName in line:
            print(changeName, ' ', changeValue)
            replacementline = changeName + "=" + changeValue + "\n"
            data[x] = replacementline
    currentfile.seek(0)
    currentfile.truncate(0)
    currentfile.writelines(data)






# luft_rpm=280
# bodenfeuchteschwelle=12
# licht_takt=43200
# temp=22.5
