import sys

# Count number of words in an input text file.
input_file = sys.argv[1]
text = open(input_file).read()
word_count = len(text.split(' '))

print('Word count in %s: %d' % (input_file, word_count))