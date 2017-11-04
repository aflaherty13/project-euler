#!/usr/bin/env python3

# From  https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print ("")

print (bcolors.OKBLUE + "project-euler.net:" + bcolors.ENDC + " Problem 1")
print ("")
print ("	" + bcolors.UNDERLINE + "Multiples of 3 and 5:" + bcolors.ENDC);
print ("	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.");
print ("");
print ("	Find the sum of all the multiples of 3 or 5 below 1000");

# Problem Code

y=0;
for x in range(0, 1000):
	if (x/3.0)%1 == 0 or (x/5.0)%1 == 0:
		y+=x;

print ("")
print ("	" + bcolors.BOLD + "Answer is %d"  % y);
print (bcolors.ENDC);

