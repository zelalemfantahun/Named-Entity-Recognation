# -*- coding: utf-8 -*-
# Natural Language Toolkit: Interface to the CRFSuite Tagger
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Long Duong <longdt219@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
A module for POS tagging using CRFSuite
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import unicodedata
import re
from nltk.tag.api import TaggerI

try:
    import pycrfsuite
except ImportError:
    pass



class crf_tagger(TaggerI):

    def __init__(self, feature_func=None, verbose=False, training_opt={}):
        self._model_file = ''
        self._tagger = pycrfsuite.Tagger()

        if feature_func is None:
            self._feature_func = self._get_features
        else:
            self._feature_func = feature_func

        self._verbose = verbose
        self._training_options = training_opt
        self._pattern = re.compile(r'\d')
        print ('============================================================')
    def set_model_file(self, model_file):
        self._model_file = model_file
        self._tagger.open(self._model_file)

    def _get_features(self, tokens, idx):

        token = tokens[idx]
        print (token)
        feature_list = []
        # Capitalization
        if token[0].isupper():
            feature_list.append('CAPITALIZATION')

        # Number
        if re.search(self._pattern, token) is not None:
            feature_list.append('HAS_NUM')

            # Punctuation
        punc_cat = set(["Pc", "Pd", "Ps", "Pe", "Pi", "Pf", "Po"])
        if all(unicodedata.category(x) in punc_cat for x in token):
            feature_list.append('PUNCTUATION')

        # Suffix up to length 3
        if len(token) > 1:
            feature_list.append('SUF_' + token[-1:])
        if len(token) > 2:
            feature_list.append('SUF_' + token[-2:])
        if len(token) > 3:
            feature_list.append('SUF_' + token[-3:])

        feature_list.append('WORD_' + token)
        print (feature_list)

        return feature_list

    def tag_sents(self, sents):

        if self._model_file == '':
            raise Exception(' No model file is found !! Please use train or set_model_file function')

        # We need the list of sentences instead of the list generator for matching the input and output
        result = []
        for tokens in sents:
            features = [self._feature_func(tokens, i) for i in range(len(tokens))]
            labels = self._tagger.tag(features)

            if len(labels) != len(tokens):
                raise Exception(' Predicted Length Not Matched, Expect Errors !')

            tagged_sent = list(zip(tokens, labels))
            result.append(tagged_sent)

        return result

    def train(self, train_data, model_file):
        trainer = pycrfsuite.Trainer(verbose=self._verbose)
        trainer.set_params(self._training_options)

        for sent in train_data:
            tokens, labels = zip(*sent)
            features = [self._feature_func(tokens, i) for i in range(len(tokens))]
            trainer.append(features, labels)

        # Now train the model, the output should be model_file
        trainer.train(model_file)
        # Save the model file
        self.set_model_file(model_file)

    def tag(self, tokens):

        return self.tag_sents([tokens])[0]
