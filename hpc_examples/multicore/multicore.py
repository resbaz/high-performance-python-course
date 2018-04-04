from multiprocessing import Pool


def count_words(filename):
    text = open(filename).read()
    return len(text.split(' '))

# Start four processes.
# The operating system will work to distribute these across available cores.
# We could request more than four processes if need be, but it probably won't be any faster.
pool = Pool(processes=4)

# Run our word count function across five input files, and return result as an array.
# Note that there are more input files than processes, but that's okay; multiprocessing will work to distribute the
# work evenly.
input_files = ['input_1.txt', 'input_2.txt', 'input_3.txt', 'input_4.txt', 'input_5.txt']
word_counts = pool.map(count_words, input_files)

# Sum the array to get our final result.
print('Total word count: %d' % sum(word_counts))