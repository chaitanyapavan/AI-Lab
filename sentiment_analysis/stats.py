#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:28:33 2019

@author: nikhil
"""
import numpy as np
import load_data
import explore_data

# ((train_texts, train_labels), (validation_texts, validation_labels)) = load_data.load_imdb_sentiment_analysis_dataset("./data/")
# explore_data.get_num_classes(train_labels)
# explore_data.get_num_words_per_sample(train_texts)
# explore_data.plot_frequency_distribution_of_ngrams(train_texts)
# explore_data.plot_sample_length_distribution(train_texts)
# explore_data.plot_class_distribution(train_labels)



((train_texts, train_labels), (validation_texts, validation_labels)) = load_data.load_rotten_tomatoes_sentiment_analysis_dataset("./data/")


count = 0
for i in train_labels:
	if i == 1:
		count+=1
c2=0
c3=0
train_labels_final = []
train_texts_final = []
for i in range(len(train_labels)):
	if train_labels[i]==0 or train_labels[i]==4:
		continue
	elif train_labels[i]==1:
		train_labels_final.append(1)
		train_texts_final.append(train_texts[i])
	elif train_labels[i]==2 and c2<count:
		c2+=1
		train_labels_final.append(2)
		train_texts_final.append(train_texts[i])
	elif train_labels[i]==3 and c3<count:
		c3+=1
		train_labels_final.append(3)
		train_texts_final.append(train_texts[i])

train_labels_final = [x - 1 for x in train_labels_final]
explore_data.get_num_classes(train_labels_final)
explore_data.get_num_words_per_sample(train_texts_final)
explore_data.plot_frequency_distribution_of_ngrams(train_texts_final)
explore_data.plot_sample_length_distribution(train_texts_final)
explore_data.plot_class_distribution(train_labels_final)

count = 0
for i in validation_labels:
	if i == 1:
		count+=1
c2=0
c3=0
validation_labels_final = []
validation_texts_final = []
for i in range(len(validation_labels)):
	if validation_labels[i]==0 or validation_labels[i]==4:
		continue
	elif validation_labels[i]==1:
		validation_labels_final.append(1)
		validation_texts_final.append(validation_texts[i])
	elif validation_labels[i]==2 and c2<count:
		c2+=1
		validation_labels_final.append(2)
		validation_texts_final.append(validation_texts[i])
	elif validation_labels[i]==3 and c3<count:
		c3+=1
		validation_labels_final.append(3)
		validation_texts_final.append(validation_texts[i])
validation_labels_final = [x - 1 for x in validation_labels_final]

def vishal():
	return ((np.array(train_texts_final), np.array(train_labels_final)), (np.array(validation_texts_final), np.array(validation_labels_final)))