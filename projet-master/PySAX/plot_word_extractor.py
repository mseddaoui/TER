"""
==============
Word Extractor
==============

Time series are often transformed into sequences of symbols. Bag-of-words
approaches are then used to extract features from these sequences.
Identical back-to-back words can be discarded or kept using the
``numerosity_reduction`` parameter.

This example illustrates the transformation and the impact of this parameter.
It is implemented as :class:`pyts.bag_of_words.WordExtractor`.
"""
# Author: Johann Faouzi <johann.faouzi@gmail.com>
# License: BSD-3-Clause

import numpy as np
import matplotlib.pyplot as plt
from plot_sax import X_sax
from pyts.bag_of_words import WordExtractor
# Parameters
n_samples, n_timestamps = 100, 48
n_bins = 26
alphabet = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z'])
# Toy dataset
word=[]
word=X_sax
liste=''
X_bow=[]
words=[]
for i in range (len(word[0])-1):
    liste+=(word[0][i])
    liste+=(word[0][i+1])
    liste+=' '
X_bow.append(liste)
words = np.asarray(X_bow[0].split(' '))
different_words_idx = np.r_[True, words[1:] != words[:-1]]
alphabet1=['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z']
X_ordinal=[]
for i in range(len(word[0])):
    for j in range(len(alphabet1[0])):
        if(word[0][i]==alphabet1[0][j]):
            X_ordinal.append(j)
# Show the results
plt.figure(figsize=(16, 7))
plt.suptitle('Extracting words from a discretized time series',
             fontsize=20, y=0.9)
plt.subplot(121)
plt.plot(X_ordinal, 'o', scalex=0.2)
plt.yticks(np.arange(n_bins), alphabet)
plt.xticks([], [])
plt.yticks(fontsize=16)
plt.title('Without numerosity reduction', fontsize=16)
for i, word in enumerate(words):
    plt.text(i, - n_bins/10 - (i % (n_bins+1)) / n_bins, word, fontsize=17, color='C0')
plt.subplot(122)
plt.plot(X_ordinal, 'o')
plt.yticks(np.arange(n_bins), alphabet)
plt.xticks([], [])
plt.yticks(fontsize=16)
plt.title('With numerosity reduction', fontsize=16)
for i, (word, different_word) in enumerate(zip(words, different_words_idx)):
    if different_word:
        plt.text(i, - n_bins/10 - (i % (n_bins+1)) / n_bins, word, fontsize=17, color='C0')
    else:
        plt.text(i, - n_bins/10 - (i % (n_bins+1)) / n_bins, word, fontsize=17, color='C0',
                 alpha=0.2)
plt.tight_layout()
plt.subplots_adjust(bottom=0.3, top=0.8)
plt.show()