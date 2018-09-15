import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
import os
import pickle


stop_words = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')

ps = PorterStemmer()

def parseAndStore(folder, files):
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





<<<<<<< HEAD
folder = 'D:\\studies\\3-1\\ir\\ir_project_1\\corpus-original\\'
=======
folder = 'D:\\studies\\3-1\\ir\\ir_project_1\\Plagiarism-Checker\\corpus-20090418\\'
>>>>>>> efef2ee08f74957b6c32a651b75e175d43f6fe40



files = os.listdir(folder)
if parseAndStore(folder,files):
    print('success')


# read data
with open(os.getcwd() +'\\' + 'data.txt','rb') as f:
        data = pickle.load(f)
        keys = data.keys()
        for key in keys:
            print(key)
