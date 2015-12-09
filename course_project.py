#! /usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import os
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
reader = CategorizedPlaintextCorpusReader('/home/khrystyna/python/course_project1/', r'author_.*\.txt', cat_pattern=r'author_(\w+)\.txt')
print reader.categories()
#print reader.fileids(categories=['murdoch'])

for fileids in reader.fileids():
	num_chars = len(reader.raw(fileids))
	num_words = len(reader.words(fileids))
	num_sents = len(reader.sents(fileids))
	num_vocab = len(set([w.lower() for w in reader.words(fileids)]))
	average_word_length = int(num_chars/num_words)
	average_sent_length = int(num_words/num_sents)
	lexical_diversity = int(num_words/num_vocab)
	print average_sent_length, average_word_length, lexical_diversity, fileids

