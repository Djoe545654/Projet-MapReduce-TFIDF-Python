import sys, re, os

stopwords = []
stopword = open('stopwords_en.txt','rb')
for stw in stopword.readlines():
    stw = stw.strip()
    stopwords.append(stw)
    
for line in sys.stdin:
    line = line.strip().lower()
    line = re.sub('[^a-z]',' ',line)
    words = line.split(' ')
    current_filename = os.environ['mapreduce_map_input_file'].rsplit('/',1)[-1]
    for word in words:
        if len(word)>2 and (word not in stopwords):
            print '%s;%s\t%s' % (word,current_filename,1)