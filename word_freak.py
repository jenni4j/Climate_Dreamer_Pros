# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:43:25 2020

@author: white
"""

import functools
import operator
import ignored


def frequency(some_df, column):

    word_list_block = []
    answers = list(some_df[column])
    for i in range(len(answers)):
        answers[i] = answers[i].lower().split()
    for word in answers:
        # print(word)
        word_list_block.append(word)
    
    Words_list = functools.reduce(operator.iconcat, word_list_block, [])
    
    # return Words
    
    unique_words = {}
    prep = ignored.ignore_these_words()
    for W in Words_list:
        if W in prep:
            pass
        else:
            if W in unique_words:
                unique_words[W] += 1
            else:
                unique_words[W] = 1
    
    for key, value in sorted(unique_words.items(), key=operator.itemgetter(1)):
        print(key, value)