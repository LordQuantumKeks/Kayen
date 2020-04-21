import re
import os

while True:
    with open('../webseite/changes.txt', 'r') as currentfile:
        change = currentfile.read()
        change = re.sub('[{}" ]', '', change)
        changeName, seperator, changeValue = change.rpartition(":")

    with open('../PipeData/general_settings.txt', 'r+') as recentfile:
        data = recentfile.readlines()
        x = -1
        for line in data:
            x += 1
            if changeName in line:
                print(changeName, ' ', changeValue)
                replacementline = changeName + "=" + changeValue + "\n"
                data[x] = replacementline
        recentfile.seek(0)
        recentfile.truncate(0)
        recentfile.writelines(data)


# luft_rpm=280
# bodenfeuchteschwelle=12
# licht_takt=43200
# temp=22.5
