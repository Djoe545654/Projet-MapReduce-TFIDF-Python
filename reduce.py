from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
total_count = 0

for line in sys.stdin:
    line = line.strip()
    customKey, count = line.split('\t',1)
    word, filename = customKey.split(';',1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print '%s;%s\t%s' % (filename, current_word, current_count)
        current_count = count
        current_word = word

if current_word == word:
    print '%s;%s\t%s' % (filename, current_word, current_count)

