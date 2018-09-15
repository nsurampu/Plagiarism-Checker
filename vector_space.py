import nltk
import os
import pickle


file_path = input("Enter path of file: ")

with open(file_path,'rb') as input_file:
    input_data = input_file.read()
    input_data.decode('utf-8','ignore')
    input_data = str(input_data)
    input_tokens = nltk.word_tokenize(input_data)

input_freq = {}

for i in range(0, len(input_tokens)):
    if input_tokens[i] not in input_freq:
        input_freq[input_tokens[i]] = 1
    else:
        input_freq[input_tokens[i]] = input_freq[input_tokens[i]] + 1

scores = {}
length = []

corpus_path = "D:\\studies\\3-1\\ir\\ir_project_1\\Plagiarism-Checker\\corpus-original"
corpus = os.listdir(corpus_path)

for i in range(0, len(corpus)):
    doc_path = corpus_path + "\\" + corpus[i]
    doc_file = open(doc_path,'rb')
    doc_content = doc_file.read()
    doc_content.decode('utf-8','ignore')
    doc_content = str(doc_content)
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
    for doc in data_keys:
        scores[doc] = 0
        temp_term = data_dict[doc]
        term_keys = temp_term.keys()
        for term_key in tfidf_keys:
            tfidf = tfidf_dict[term_key ]
            scores[doc] = scores[doc] + (tfidf * input_freq[input_tokens[i]])

print(len(scores))
print(len(length))
score_keys = scores.keys()
i = 0
for score_key in score_keys:
    scores[score_key] = scores[score_key] / length[i]
    i += 1

sorted_scores = {t: scores[t] for t in sorted(scores, key=scores.get, reverse=True)}

# print(sorted_scores)
sorted_score_keys = sorted_scores.keys()
count = 0
top_docs = []
for sorted_score in sorted_score_keys:
    top_doc_scores = sorted_scores[sorted_score]
    top_docs.append(sorted_score)
    count += 1
    if count == 10:
        break
# top_docs = top_doc_scores.keys()

checker_obj = Checker()
for i in range(0, len(top_docs)):
    top_doc_path = "D:/Plagiarism-Checker/corpus-original/" + top_docs[i]
    checker_obj.plag_check(top_doc_path ,file_path)
