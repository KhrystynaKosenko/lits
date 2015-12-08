#! /usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import os
from nltk.corpus import PlaintextCorpusReader

#creating corpus with 3 texts in 3 files
txt_fawles= os.path.abspath('/home/khrystyna/python/course_project/The_Magus.txt') 
txt_hemingway= os.path.abspath('/home/khrystyna/python/course_project/.Hemingway_The_Old_Man_and_the_Sea.txt')
txt_merdock= os.path.abspath('/home/khrystyna/python/course_project/Murdoch_Iris_The_Black_Prince.txt')
corpus= [txt_fawles, txt_hemingway, txt_merdock]

corpusdir = 'newcorpus/'
if not os.path.isdir(corpusdir):
    os.mkdir(corpusdir)

filename = 0
for text in corpus:
    filename= filename + 1
    open(corpusdir+str(filename)+'.txt','w): n
   

newcorpus = PlaintextCorpusReader('newcorpus/', '.*')



import nltk
from nltk.corpus import gutenberg
nltk.corpus.gutenberg.fileids()
for fileid in gutenberg.fileids():
	num_chars = len(gutenberg.raw(fileid))
	num_words = len(gutenberg.words(fileid))
	num_sents = len(gutenberg.sents(fileid))
	num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
	average_word_length = int(num_chars/num_words)
	average_sent_length = int(num_words/num_sents)
	lexical_diversity = int(num_words/num_vocab)
	print average_sent_length, average_word_length, lexical_diversity, fileid
