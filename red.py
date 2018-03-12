from operator import itemgetter
import sys

dic = {}
current_name = None
wordPerDoc = {}

for line in sys.stdin:
    line = line.strip()
    customKey, count = line.split('\t',1)
    filename, word = customKey.split(';',1)
    try:
        count = int(count)
    except ValueError:
        continue
    dic[customKey]=count
    if current_name == filename:
        wordPerDoc[current_name] = wordPerDoc.get(current_name,0) + count
    else:
        if current_name:
            current_name = filename

wordPerDoc[current_name] = wordPerDoc.get(current_name,0) + count

for key, val in dic:
    filename, word = key.split(';',1)
    print '%s\t%s;%s' % (key,val,wordPerDoc[filename])