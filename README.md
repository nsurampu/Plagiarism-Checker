# Plagiarism Checker

This project implements a plagiarism checker using Python3.


## Description

The project uses the Vector Space model along with tf-idf to generate a score for each document, and accordingly pass it through a checker which returns uniqueness of each document and assigns a plagiarism level, based on the number of matching sentences and words. Preference is given to sentences.  


### Prerequisites

Python3 along with nltk library is required to run this program.

### Structure of project

data_processing.py : Access the corpus-original folder and processes the documents and generates the tf-idf score for every (term,document) pair.

vector_space.py : Implements the vector space model and calculates the cosine score for every document in the corpus.

checker.py : Calculates uniqueness and assigns plagiarism level to every document.

corpus-original : Folder that contains the corpus for the project.

data.txt : The picked dictionary containing the term frequencies for every document.

tfidf.txt : The picked dictionary containing the tfidf scores.

### Running

Run this in your project folder.
```
$ python data_processing.py
$ python vector_space.py
```

## Built With

The project uses
- Python3
- NLTK

## Authors

Chandrahas Aroori [https://github.com/Exorust]
Naren Surampudi [https://github.com/nsurampu]
Aditya Srikanth [https://github.com/aditya-srikanth]

## Acknowledgments

We'd like to thank our Information Retrieval instructor to give us this opportunity to make such a project.
