import re

string = input("Digite uma palavra: ")

quantidade = len(string)

for i in range(quantidade-1, -1, -1):
    print(string[i], end="")