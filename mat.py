import matplotlib.pyplot as plt
import re

patron1 = re.compile("1")

patron2 = re.compile("2")

patron3 = re.compile("3")

patron4 = re.compile("4")

patron5 = re.compile("5")

one = 0

two = 0

three = 0

four = 0


for line in open("numbers"):
    for match in re.finditer(patron1, line):
        one += 1

for line in open("numbers"):
    for match in re.finditer(patron2, line):
        two += 1

for line in open("numbers"):
    for match in re.finditer(patron3, line):
        three += 1

for line in open("numbers"):
    for match in re.finditer(patron4, line):
        four += 1

plt.plot([one, two, three, four])
plt.ylabel('some numbers')
plt.show()