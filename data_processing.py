import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
import os
import pickle
import math

stop_words = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')

ps = PorterStemmer()
class ParseAndStore:
    def parseAndStore(self,folder, files):
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
        with open(cwd+'\\' + 'data.txt','wb') as f:
            pickle.dump(file_data,f)
        return True

folder = 'D:\\Plagiarism-Checker\\corpus-original\\'


parse = ParseAndStore()
files = os.listdir(folder)
if parse.parseAndStore(folder,files):
    print('success')


# # read data
# with open(os.getcwd() +'\\' + 'data.txt','rb') as f:
#         data = pickle.load(f)
#         keys = data.keys()
#         for key in keys:
#             print(key)

class TF_IDF:
    def tf_idf(self,file_path):
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
