import sys
my_input= sys.argv

first=set(my_input[1].upper())

try:
    first.remove(' ')
except:
    pass


print first
print len(first)
