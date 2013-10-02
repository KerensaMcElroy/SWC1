import sys
num=int(sys.argv[1])

rem = int(num) % 2
if rem == 0:
    print "Even"
else:
    print "Odd"
    

if num < 50:
    print "Minor"
elif num < 1000:
    print "Major"
else:
    print "Severe"
