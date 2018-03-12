import sys, re, os

for line in sys.stdin:
    line = line.strip()
    line = re.sub('[^a-z]',' ',line)
    customKey, customValue = line.split('\t',1)
    word, filename = customKey.split(';',1)
    count, wordPerDoc = customValue.split(';',1)
    print '%s\t%s;%s;%s' % (word,filename,count,wordPerDoc)