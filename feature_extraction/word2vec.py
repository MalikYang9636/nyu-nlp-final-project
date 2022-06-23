# Python program to generate word vectors using Word2Vec

# importing all necessary modules
import sys
import re
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action = 'ignore')

import gensim
from gensim.models import Word2Vec


# Reads ‘alice.txt’ file
# sample = open("/Users/peiwentang/Downloads/Partitive-Files/%-dev")
# s = sample.read()

# Replaces escape character with space
# f = s.replace("\n", " ")

data = []
og_file = []
name = "/Users/peiwentang/Downloads/Partitive-Files/%-training"
with open(name, 'r') as f:
    temp = []
    for line in f:
        no_arg = True
        every_line = []
        tokens = line.split()
        if len(tokens) == 0 and len(temp) != 0:
            data.append(temp)
            temp = []
        if len(tokens) != 0:
            if len(tokens) == 6:
                no_arg = False
            temp.append(tokens[0])
            every_line.append(tokens[0])
        if no_arg == True:
            new_line = line[:-1] + '\t' + "NOARG"
        else:
            new_line = line[:-1]
        every_line.append(new_line)
        og_file.append(every_line)
        

if len(temp) != 0:
    data.append(temp)
    

# Create CBOW model
model1 = gensim.models.Word2Vec(data, min_count = 1, vector_size = 100, window = 5)

# Print results
	
with open("%-training_new", 'w') as o:
    for line in og_file:
        if len(line) == 2:
            o.write(line[1] + "\t" + str(model1.wv.similarity('%', line[0])) + '\n')
        else:
            o.write('\n')
        