# Dict main called corpus_dict
# len(dict)

import math
# corpus_dict = {"test1": {"hello": 3, "hi": 4, "why" : 7},
#                "test2": {"hello": 7, "to": 5}}
with open(os.getcwd() +'\\' + 'data.txt','rb') as f:
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
                df +=1
        val = tf * math.log((N // df),10)
        tfidf[(term,doc)] = val


with open(cwd+'\\' + 'tfidf.txt','wb') as f:
    pickle.dump(tfidf,f)
