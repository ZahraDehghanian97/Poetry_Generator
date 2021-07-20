import os
import random
import pickle

corpus_address = "./shahname"
data_path = "my_shahname_represntation.txt"

corpus = ""
test = []
list_dir = random.sample(os.listdir(corpus_address), len(os.listdir(corpus_address)))
num_text = len(list_dir)
num_test = int(0.1 * num_text)
counter = 0
for filename in list_dir:
    with open(corpus_address + "/" + filename, encoding='utf-8') as f:
        if counter < num_test:
            temp = ""
            for line in f:
                temp += line
            test.append(temp)
        else:
            for line in f:
                corpus += line
    counter += 1
with open(data_path, 'wb') as f:
    pickle.dump((corpus, test), f)
print(num_text)
print(len(test))
print(test[0])
