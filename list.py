import sys
grades = []

def detString(countString):
    if countString[-1] == "1" and len(countString) == 1:	    
        a = raw_input("Please enter the %sst grade.\n" % (countString))
        grades.append(float(a))
    elif countString[-1] == "1" and not countString[-2] == "1" and len(countString)>1:
        a = raw_input("Please enter the %sst grade.\n" % (countString))
        grades.append(float(a))
    elif countString[-1] == "1" and countString[-2] == "1" and len(countString)>1:
        a = raw_input("Please enter the %sth grade.\n" % (countString))
        grades.append(float(a))
    elif countString[-1] == "2":
	    a = raw_input("Please enter the %snd grade.\n" % (countString))
	    grades.append(float(a))
    elif countString[-1] == "3":
	    a = raw_input("Please enter the %srd grade.\n" % (countString))
	    grades.append(float(a))
    else:
        a = raw_input("Please enter the %sth grade.\n" % (countString))
        grades.append(float(a))
	

count = 0
gradeNumber = input("How many grades do you have to input?\n")
for x in range(gradeNumber):
    count += 1
    countString = str(count)
    detString(countString)
    grades.sort()

print "The lowest grade is %.2f." % (grades[0])
print "The highest grade is %.2f." % (grades[-1])
sys.exit("The average grade is %.2f!" % (sum(grades)/len(grades)))