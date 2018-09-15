import nltk
import os

def sigmoid(number):
    result = 1 / (1 + (2.71 ** -number))
    return result


def plag_level(sents, words):
    print(str(sents))
    print(str(words))
    sent_score = sents * 0.8
    word_score = words * 0.2
    score = sent_score + word_score
    return score

orig_doc = open('D:/Hello_1.txt', 'r')  # Original document (from  corpus)
plag_doc = open('D:/Hello_2.txt', 'r')  # Plagiarised document (from query)

orig_content = orig_doc.read()
plag_content = plag_doc.read()

orig_word_tokens = nltk.word_tokenize(orig_content)
plag_word_tokens = nltk.word_tokenize(plag_content)
orig_sent_tokens = nltk.sent_tokenize(orig_content)
plag_sent_tokens = nltk.sent_tokenize(plag_content)

print(orig_word_tokens)
print(plag_word_tokens)
print(orig_sent_tokens)
print(plag_sent_tokens)

word_match = 0  # for uniqueness
sent_match = 0  # for plagiarism score

for i in range(0, len(plag_sent_tokens)):
    if plag_sent_tokens[i] in orig_sent_tokens:
        sent_match = sent_match + 1

sent_percent = (len(plag_sent_tokens) - sent_match)  # zero score implies highest plagiarism

for i in range(0, len(plag_word_tokens)):
    if plag_word_tokens[i] in orig_word_tokens:
        word_match = word_match + 1

word_percent = (len(plag_word_tokens) - word_match)

plag_score = plag_level(sent_percent, word_percent)

uniqueness = 100 - ((word_match / len(plag_word_tokens)) * 100)

print("Uniqness: " + str(uniqueness) + "%")
print("Plagiarism score: " + str(plag_score))
