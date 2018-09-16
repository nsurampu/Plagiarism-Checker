import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import os

class Checker:
    def plag_score(self,sents, words):
        sent_score = sents * 0.8
        word_score = words * 0.2
        score = sent_score + word_score
        return score

    def plag_check(self,orig_file, plag_file):
        stop_words = stopwords.words('english')
        tokenizer = RegexpTokenizer(r'\w+')
        
        orig_doc = open(orig_file, 'rb')
        plag_doc = open(plag_file, 'rb')
        orig_content = orig_doc.read()
        plag_content = plag_doc.read()
        orig_content.decode('utf-8', 'ignore')
        plag_content.decode('utf-8', 'ignore')
        orig_content = str(orig_content)
        plag_content = str(plag_content)

        orig_word_tokens = nltk.word_tokenize(orig_content)
        plag_word_tokens = nltk.word_tokenize(plag_content)
        orig_sent_tokens = nltk.sent_tokenize(orig_content)
        plag_sent_tokens = nltk.sent_tokenize(plag_content)

        word_match = 0  # for uniqueness
        sent_match = 0  # for plagiarism score

        for i in range(0, len(plag_sent_tokens)):
            if plag_sent_tokens[i] in orig_sent_tokens:
                sent_match = sent_match + 1

        sent_percent = (len(plag_sent_tokens) - sent_match)  # zero score implies highest plagiarism

        filtered_orig = [word for word in orig_word_tokens if word not in stop_words]
        filtered_plag = [word for word in plag_word_tokens if word not in stop_words]

        for i in range(0, len(filtered_plag)):
            if filtered_plag[i] in filtered_orig:
                word_match = word_match + 1

        word_percent = (len(filtered_plag) - word_match)

        score = self.plag_score(sent_percent, word_percent)

        uniqueness = 100 - ((word_match / len(filtered_plag)) * 100)
        uniqueness = float(uniqueness)

        print("Document compared with: " + orig_file.split('/')[-1])
        print("Uniqness: " + str(uniqueness) + "%")
        print("Plagiarism score: " + str(score))
        print("\n")

        orig_doc.close()
        plag_doc.close()
