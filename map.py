import sys, re, os

for line in sys.stdin:
    line = line.strip()
    line = re.sub('[^a-z]',' ',line)
    customKey, count = line.split('\t',1)
    word, filename = customKey.split(';',1)
    print '%s;%s\t%s' % (filename,word,count)