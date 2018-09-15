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

tfidf_file = open("D:/Plagiarism-Checker/tfidf.py")
tfidf_scores = tfidf.read()

for i in range(0, len(input_freq)):
    for j in range(0, len(tfidf_scores)):
        scores[i] = scores[i] + tfidf[j]

for i in range(0, len(scores)):
    scores[i] = scores[i] / length[i]

top_docs -> docs with top 10 scores

checker_obj = Checker()

for i in range(0, len(top_docs)):
    checker.plag_check(top_docs[i] ,input_file)
