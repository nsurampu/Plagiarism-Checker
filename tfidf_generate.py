import math
import pickle 
import os 

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

tf = TF_IDF()
tf.tf_idf(os.getcwd()+'\\data.txt')        