from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.model import build_vocabulary
from nltk.model import count_ngrams

from nltk.model import LaplaceNgramModel

from nltk.corpus import gutenberg

#text = open('/Users/purnendu/Desktop/Nat_Lang_HW3/Lin.txt').read()
#utext = unicode(text, "utf8")

sents = gutenberg.sents('/Users/purnendu/Desktop/Nat_Lang_HW3/LB-Train.txt')

words = [w.lower() for s in sents for w in s]

words_train_LB = words

vocab = build_vocabulary(3, words)

#print(sents[:6])

bigram_counts = count_ngrams(2, vocab, sents)

#print(bigram_counts.unigrams)


LB_model = LaplaceNgramModel(bigram_counts)

#ex_score = LB_model.score("administration", ["of"])

#print ex_score

sents_test = gutenberg.sents('/Users/purnendu/Desktop/Nat_Lang_HW3/LB-Test.txt')
words_test = [w.lower() for s in sents_test for w in s]
print "1.b) perplexity of LB on LB-Test) : ",  LB_model.perplexity(words_test)




#perplexity of MB on MB-test
# -------------------------
# -------------------------
# -------------------------
# -------------------------
# -------------------------
# -------------------------
sents = gutenberg.sents('/Users/purnendu/Desktop/Nat_Lang_HW3/MB_train.txt')

words = [w.lower() for s in sents for w in s]

words_train_MB = words

vocab = build_vocabulary(3, words)

#print(sents[:6])

bigram_counts = count_ngrams(2, vocab, sents)

#print(bigram_counts.unigrams)


MB_model = LaplaceNgramModel(bigram_counts)

#ex_score = LB_model.score("administration", ["of"])

#print ex_score

sents_test = gutenberg.sents('/Users/purnendu/Desktop/Nat_Lang_HW3/MB_test.txt')
words_test = [w.lower() for s in sents_test for w in s]

print "1.d) Perplexity of MB on MB-test : ",  MB_model.perplexity(words_test)




#perplexities of LB on LB-train and MB on MB-train
# -------------------------
# -------------------------
# -------------------------
# -------------------------
# -------------------------
# -------------------------

print "Perplexity of LB on LB-train : ",  LB_model.perplexity(words_train_LB)

print "Perplexity of MB on MB-train : ",  MB_model.perplexity(words_train_MB)

#perplexity of MB on LB-train and the perplexity of LB on MB-train.

print "Perplexity of MB on LB-train : ",  MB_model.perplexity(words_train_LB)

print "Perplexity of LB on MB-train : ",  LB_model.perplexity(words_train_MB)


