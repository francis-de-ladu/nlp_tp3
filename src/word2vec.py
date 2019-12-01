import os
import pandas as pd
import spacy
import sys
import time

from tqdm import tqdm

from gensim import models, utils
from gensim.models.phrases import Phrases, Phraser


# command line arguments
FOLDER, THRESHOLD, SIZE = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
os.makedirs(FOLDER, exist_ok=True)

with open('data/train_posts.txt', 'r') as file:
	sentences = file.readlines()

sentences = [utils.simple_preprocess(sent) for sent in sentences]

start = time.time()
phrases = Phrases(sentences, threshold=THRESHOLD)
bigram = Phraser(phrases)
sentences = [bigram[sent] for sent in sentences]

test = utils.simple_preprocess("i'm from the united states of america.")
print(test)
print(bigram[test])

test2 = utils.simple_preprocess("an airplane is a nice mean to travel to another country.")
print(test2)
print(bigram[test2])

test3 = utils.simple_preprocess("Chris Johnson was the best friend i even had.")
print(test3)
print(bigram[test3])

test4 = utils.simple_preprocess("We're not the ones that are goint to save this queen's selfish interests.")
print(test4)
print(bigram[test4])

test5 = utils.simple_preprocess("I'd prefer to drink green tea over black tea.")
print(test5)
print(bigram[test5])

print('phraser:', time.time() - start)

start = time.time()
model = models.Word2Vec(sentences=sentences, size=SIZE)
model.wv.save_word2vec_format(f'{FOLDER}/word2vec_T-{THRESHOLD}_S-{SIZE}.txt')
print('word2vec:', time.time() - start)
