from nltk.tokenize import word_tokenize
import string
import re

text = open('/Users/purnendu/Documents/test1/data.txt').read()

tokens = [s.strip().split(': ') for s in text.splitlines()]


#print tokens


speaker1 = tokens[0][0]
speaker2 = tokens[1][0]

print 'Speaker 1 is: ', speaker1
print 'Speaker 2 is: ', speaker2

s1 = []     # List to store things said by speaker 1
s2 = []     # List to store things said by speaker 2

for i in tokens:
    if i[0] == speaker1:
        s1.append(i[1])
    elif i[0] == speaker2:
        s2.append(i[1])
    else:
        continue


#print 'The things spoken by speaker 1 : ', s1
#print 'The stuff speaker 2 said : ', s2

print '\n\nThe number of turns taken by ',speaker1,' :',len(s1)
print '\nThe number of turns taken by ',speaker2,' :',len(s2)


s1str = ' '.join(s1)
s2str = ' '.join(s2)
s1str= re.sub('--',' ', s1str)
s2str= re.sub('--',' ', s2str)
s1str=s1str.translate(None, string.punctuation)

#print s1str
s2str=s2str.translate(None, string.punctuation)


s1w = word_tokenize(s1str)
s2w = word_tokenize(s2str)
print '\n\nTotal words said by ',speaker1,' :',len(s1w)
print '\nTotal words said by ',speaker2,' :',len(s2w)


s1AvgW = float(len(s1w))/float(len(s1))
s2AvgW = float(len(s2w))/float(len(s2))
print '\n\nWords per turn on average by ',speaker1,' :',s1AvgW
print '\nWords per turn on average by ',speaker2,' :',s2AvgW


s1AvgLW = float(len(''.join(s1w))) / float(len(s1w))
s2AvgLW = float(len(''.join(s2w))) / float(len(s2w))
print '\n\nAverage length of word by ',speaker1,' :',s1AvgLW
print '\nAverage length of word by ',speaker2,' :',s2AvgLW



'''
x = text.splitlines()

for s in text.splitlines():
    if s == '':
        continue
    else:
        tokens = [s.strip().split(': ')]

'''
