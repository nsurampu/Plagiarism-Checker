import nltk
import os
import pickle
import checker


file_path = input("Enter path of file: ")

print("Reading file and tokenizing...")
with open(file_path,'rb') as input_file:
    input_data = input_file.read()
    input_data.decode('utf-8','ignore')
    input_data = str(input_data)
    input_tokens = nltk.word_tokenize(input_data)

input_freq = {}

print("Calculating term frequencies...")
for i in range(0, len(input_tokens)):
    if input_tokens[i] not in input_freq:
        input_freq[input_tokens[i]] = 1
    else:
        input_freq[input_tokens[i]] = input_freq[input_tokens[i]] + 1

scores = {}
length = []

corpus_path = "D:/Plagiarism-Checker/corpus-original"
corpus = os.listdir(corpus_path)

print("Calculating lengths of corpus documents...")
for i in range(0, len(corpus)):
    doc_path = corpus_path + "/" + corpus[i]
    doc_file = open(doc_path,'rb')
    doc_content = doc_file.read()
    doc_content.decode('utf-8','ignore')
    doc_content = str(doc_content)
    doc_tokens = nltk.word_tokenize(doc_content)
    length.append(len(doc_tokens))
    doc_file.close()

print("Unpickling tokenized corpus data...")
data_pickle = open('data.txt', 'rb')
data_dict = pickle.load(data_pickle)
data_keys = data_dict.keys()

print("Unpickling tf-idf data...")
tfidf_pickle = open('tfidf.txt', 'rb')
tfidf_dict = pickle.load(tfidf_pickle)
tfidf_keys = tfidf_dict.keys()

print("Calculating document scores...")
for i in range(0, len(input_tokens)):
    for doc in data_keys:
        scores[doc] = 0
        temp_term = data_dict[doc]
        term_keys = temp_term.keys()
        for term_key in tfidf_keys:
            tfidf = tfidf_dict[term_key]
            if term_key[0] in input_tokens:
                scores[doc] = scores[doc] + (tfidf * input_freq[term_key[0]])


score_keys = scores.keys()
i = 0

for score_key in score_keys:
    scores[score_key] = scores[score_key] / length[i]
    i += 1

sorted_scores = {t: scores[t] for t in sorted(scores, key=scores.get, reverse=True)}
sorted_score_keys = sorted_scores.keys()
count = 0
top_docs = []

print("Fetching top 10 matching documents...")
for sorted_score in sorted_score_keys:
    top_doc_scores = sorted_scores[sorted_score]
    top_docs.append(sorted_score)
    count += 1
    if count == 3:
        break

checker_obj = checker.Checker()

print("\nPlagiarism Results:\n")
print("Document being checked: " + file_path.split('/')[-1])

for i in range(0, len(top_docs)):
    input("\nPress enter to continue...")
    top_doc_path = "D:/Plagiarism-Checker/corpus-original/" + top_docs[i]
    checker_obj.plag_check(top_doc_path ,file_path)

print("\nEnd of result")
