from operator import itemgetter
import sys, math

dic = {}
data = {}
current_word = None
occurence = 0

for line in sys.stdin:
    line = line.strip()
    word, custom = line.split('\t',1)
    data[word] = custom
    if current_word == word:
        occurence += 1
    else:
        dic[current_word] = occurence
        if current_word:
            current_word = word
            occurence = 1

dic[current_word] = occurence

for key, val in data:
    filename, count, wordPerDoc = val.split(';',2)
    try:
        count = float(count)
        wordPerDoc = float(wordPerDoc)
    except ValueError:
        continue
    tfidf = (count/wordPerDoc)*math.log10(2.0/float(dic[word]))
    print '%s;%s\t%s' % (filename,word,tfidf)