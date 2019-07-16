#Percentage of a pair of corrdinates making a line or triangle
import random

out = []

def IsPoints():
	cord1 = []
	cord2 = []
	cord3 = []
	for i in range(0,3):
		x = random.randint(0,100)
		y = random.randint(0,100)
		if i == 0:
			cord1.append(x)
			cord1.append(y)
		elif i == 1:
			cord2.append(x)
			cord2.append(y)
		elif i == 2:
			cord3.append(x)
			cord3.append(y)
	slope = cord1[0] * (cord2[1] - cord3[1]) + cord2[0] * (cord3[1] - cord1[1]) + cord3[0] * (cord1[1] - cord2[1])
	if cord1[0] == cord2[0] == cord3[0]:
		return "Line"
	elif cord1[1] == cord2[1] == cord3[1]:
		return "Line"
	if slope == 0:
		return "Line"
	else:
		return "Tri"

for x in range(0,10000):
	out.append(IsPoints())

tri = out.count('Tri')
line = out.count('Line')


if tri < line:
	dec = tri/line
	percent = dec*100
	tri = "Tri: {0}".format(tri)
	line = "Line: {0}".format(line)
	perc = "Percentage: {0}".format(percent)
else:
	dec = line/tri
	percent = dec*100
	tri = "Tri: {0}".format(tri)
	line = "Line: {0}".format(line)
	perc = "Percentage: {0}".format(percent)

print(tri)
print(line)
print(perc)


