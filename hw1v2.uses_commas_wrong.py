import random

print """
===========================================================================
The computer will ask for your input, and compare it with a pre-generated number.
It will then tell you if you were too high, too low, or exactly right.
===========================================================================
"""

def get_input():
	keepgoing = True
	while keepgoing:
		b = int(raw_input("Enter a number between 1 and 100 \n >"))
		if b < 1:
			print "Smaller than expected."
		elif b > 100:
			print "Larger than expected."
		else:
			return b
			keepgoing = False
			
keepgoing = True
a = random.randint(1,100)

while keepgoing:
	b = get_input()
	if a == b:
		print "Numbers matched. Neato!\n"
		keepgoing = False
	elif a > b:
		print "Too Low. Try again.\n"
	else:
		print "Too high. Try again. \n"
