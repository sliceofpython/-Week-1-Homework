import random

print """
Enter a number between 1 and 100.
This script will tell you if you were too high, too low, or exactly right.
"""

a = random.randint(1,100)
b = int(raw_input("Enter a number between 1 and 100 \n >"))

if b < 1:
	print "Between 1 and 100 dummy. Exiting program."
elif b > 100:
	print "Between 1 and 100 dummy. Exiting program."
	
if a == b:
	print "Numbers matched. Neato!"
elif a > b:
	print "Too Low."
	print "Number was %d." % a
else:
	print "Too high."
	print "Number was %d." % a
