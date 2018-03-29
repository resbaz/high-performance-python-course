from multiprocessing import Pool


def count_words(filename):
    text = open(filename).read()
    return len(text.split(' '))

pool = Pool(processes=4)
input_files = ['input_1.txt', 'input_2.txt', 'input_3.txt', 'input_4.txt', 'input_5.txt']
word_counts = pool.map(count_words, input_files)
print('Total word count: %d' % sum(word_counts))