import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
import os
import pickle
import math


"""
This file Contains Classes for processing data.

"""
class ParseAndStore:
    """
    This class is used to handle the processing of text files encoded in ASCII and processes them, created a dictionary of terms and their
    frequencies and stores it as a pickle file (.pkl)
    """
    def parseAndStore(self,folder, files):
        """
        Creates a dictionary having the terms with their term-frequencies.
        This takes two parameters viz folder- folder where the files lie the and files- the
        list of files that need to be processed. The processed data will be stored as a pickled file.

        @type folder: string
        @param folder: folder to access files.

        @type files: list
        @param files: the list of files which will be read.

        @rtype: string
        @return: success after the process terminates successfully

        """
        ps = PorterStemmer()
        stop_words = stopwords.words('english')
        tokenizer = RegexpTokenizer(r'\w+')
        # print(files)
        file_data = {}
        for file in files:
        # for i in range(1):
            data_with_tf = {}
            with open(folder + file,'rb') as f:
                data = f.read()
                data = data.decode('utf-8','ignore')
                # print(data)
                data = str(data)
                data = data.lower()
                tokens = tokenizer.tokenize(data)
                # print(tokens)
                filtered = [w for w in tokens if w not in stop_words]
                filtered.sort()
                keys = list(set(filtered))
                keys.sort()
                for i in range(len(keys)):
                    data_with_tf[keys[i]] = filtered.count(keys[i])
                # print(data_with_tf)
            file_data[file] = data_with_tf
        cwd = os.getcwd()
        with open(cwd +'\\' + 'data.txt','wb') as f:
            pickle.dump(file_data,f)
        return True



folder = 'D:\\Plagiarism-Checker\\corpus-original\\'
parse = ParseAndStore()
files = os.listdir(folder)
if parse.parseAndStore(folder,files):
    print('success')



class TF_IDF:

    """
    The class calculates the tf-idf value while parsing each term of each document
    and calculating the document frequency fo each word. Then the idf value is calculated
    using document frequency and is multiplied with term frequency to produce tf-idf.
    """

    def tf_idf(self,file_path):
        """
        The function calculates the tf-idf value while parsing each term of each document
        and calculating the document frequency fo each word. Then the idf value is calculated
        using document frequency and is multiplied with term frequency to produce tf-idf

        @type folder: string
        @param folder: folder to access files.

        @type files: string
        @param files: the path of the data.txt dictionary

        @rtype: string
        @return: path path of pickled dictionary containing tf-idf values

        """

        with open(file_path,'rb') as f:
            corpus_dict = pickle.load(f)
            keys = corpus_dict.keys()
        tfidf = {}
        N = len(corpus_dict)
        for doc in corpus_dict:
            for term in corpus_dict[doc]:
                # print(term)
                tf = corpus_dict[doc][term]
                df = 0
                for eachdoc in corpus_dict:
                    if term in (corpus_dict[eachdoc]):
                        df += 1
                val = tf * math.log((N // df),10)
                tfidf[(term,doc)] = val
                # (term,document) is the key

        # print(tfidf)
        cwd = os.getcwd()
        path = cwd+'\\' + 'tfidf.txt'
        with open(path,'wb') as f:
            pickle.dump(tfidf,f)
        return path
