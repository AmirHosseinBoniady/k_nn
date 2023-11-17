import numpy as np
import pandas as pd
import copy
from scipy.stats import stats

file  = pd.read_excel("HW1_AUT_MLPR_4021-Ar-Fa.xlsx")
bow = file.values.tolist()
sentenses = [b[0] for b in bow]
sentences_vector = [s.split() for s in sentenses]
all_words = copy.deepcopy(sentences_vector)

dict = {}
for i in all_words:
    for j in i:
        dict[j] = j

word_vector = []
for key in dict:
    word_vector.append(key)

# print(word_vector)

binary_bows = []
for sentens in sentences_vector:
    binary_bow = []
    for word in word_vector:
        binary_bow.append(1 if word in sentens else 0)
    binary_bows.append(binary_bow)

# print(binary_bows)

def cal_number_rep_words(word,sentence):
    conter = 0
    if word not in sentence:
        pass
    else:
        for w in sentence:
            if str(w) == str(word):
                conter +=1
    return conter

weighted_bows = []
for sentens in sentences_vector:
    binary_bow = []
    for word in word_vector:
        binary_bow.append(cal_number_rep_words(word,sentens))
    weighted_bows.append(binary_bow)

print("weighted_bows[10]", weighted_bows[10])

normalized_weighted_bows = []

for vector in weighted_bows:
    len = 0
    for i in vector:
         len = len + i
    print("sum_vector", len)

    resualt = [s/len for s in vector]
    normalized_weighted_bows.append(resualt)
        
    print("vector", vector)

# print(normalized_weighted_bows)


all_zscores = []
for vector in weighted_bows:
    data = np.array(vector)
    zscore = stats.zscore(data)
    all_zscores.append(zscore)

print("all_zscores", all_zscores[1])
