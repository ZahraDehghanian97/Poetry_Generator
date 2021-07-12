import os
corpus_address = "./shahname"
corpus = ""
for filename in os.listdir(corpus_address):
   with open( corpus_address+"/"+filename, encoding='utf-8') as f:
      for line in f :
         corpus += line

file_corpus = open("shahname.txt", "a")
file_corpus.write(corpus)
file_corpus.close()