import sys
words=sys.argv[1:]
words.sort()

print words
final=words[-1]
words= words[:-1]

words = ', '.join(words)
print words
words+=(' and '+final+'.')
words=words[0].upper() + words[1:]
print words
