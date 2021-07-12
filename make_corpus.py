import os
corpus_url = "Shahnameh/shahname"
corpus = ""
for filename in os.listdir(corpus_url):
   with open(os.path.join(corpus_url, filename), 'r') as f:
      text = f.read()
      corpus += text

file_corpus = open("shahname.txt", "a")
file_corpus.write(corpus)
file_corpus.close()