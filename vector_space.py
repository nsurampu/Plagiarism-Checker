import nltk
import os

file_path = input("Enter path of file: ")

input_file = open(input_file)
input_data = input_file.read()

input_tokens = nltk.word_tokenize(input_data)
input_freq = {}

for i in range(0, len(input_tokens)):
    if input_tokens[i] not in input_freq:
        input_freq[input_tokens[i]] = 1
    else:
        input_freq[input_tokens[i]] = input_freq[input_tokens[i]] + 1

scores = {}
length = []

corpus_path = "D:/Plagiarism-Checker/corpus-original"
corpus = os.listdir(corpus_path)

for i in range(0, len(corpus)):
    doc_path = corpus_path + "/" + corpus[i]
    doc_file = open(doc_path)
    doc_content = doc_file.read()
    doc_tokens = nltk.word_tokenize(doc_content)
    length.append(len(doc_tokens))
    doc_file.close()

data_pickle = open('data.txt', 'rb')
data_dict = pickle.load(data_pickle)
data_keys = data_dict.keys()

tfidf_pickle = open('tfidf.txt', 'rb')
tfidf_dict = pickle.load(tfidf_pickle)
tfidf_keys = tfidf_dict.keys()

for i in range(0, len(input_tokens)):
    for j in range(0, len(data_dict):
        doc = data_keys[j]
        scores[doc] = 0
        temp_term = data_dict[doc]
        term_keys = temp_term.keys()
        for k in range(0, len(term_keys)):
            tfidf = tfidf_dict[(term_keys[k], doc)]
            scores[doc] = scores[doc] + (tfidf * input_freq[input_tokens[i]])

for i in range(0, len(scores)):
    scores[i] = scores[i] / length[i]

sorted_scores = [(t, scores[t]) for t in sorted(scores, key=scores.get, reverse=True)]

top_doc_scores = sorted_scores[1:10]
top_docs = top_doc_scores.keys()

checker_obj = Checker()

for i in range(0, len(top_docs)):
    top_doc_path = "D:/Plagiarism-Checker/corpus-original/" + top_docs[i]
    checker.plag_check(top_doc_path ,file_path)
