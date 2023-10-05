"""
Takes in file path and prints out content in that file
@author :Dharma Teja
GitHub:https://github.com/dharmateja03
"""
with open("data.txt") as file:
    # replace data.txt with actual file path
    line = file.readline()
    while line:
        print(line, end=" ")
        line = file.readline()
