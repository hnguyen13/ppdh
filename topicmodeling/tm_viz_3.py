'''
Vizualize the topic weights within a given document
'''

import matplotlib.pyplot as plt

import os

doc_to_viz = "1_Hamilton"

# create a set of ignore files
ignore = {".DS_Store", ".txt"}

# a list for the labels
titles = []

for root, dirs, files in os.walk("fedpapers"):
    for filename in files:
        titles.append(filename[:-4])

with open('fed_doctopics.txt','r', encoding='utf8') as rf:
    topic_info = rf.read().split("\n")
    topic_info = [item for item in topic_info if item != ""]

doc_topic_info = {}

total_topics = 0
for title, line in zip(titles, topic_info):
    info = line.split("\t")
    doc_topic_info[title] = [float(weight) for weight in info[2:]]
    total_topics = len(info[2:])

doc_weight_per_topic = [[] for _ in range(total_topics)]

for title in titles:
    weights = doc_topic_info[title]

    for i, weight in enumerate(weights):
        doc_weight_per_topic[i].append(weight)

index = range(len(doc_topic_info))

labels = [f"T:{i+1}" for i in range(total_topics)]

plt.stackplot(index, doc_weight_per_topic, labels=labels)

plt.xticks(index, titles, rotation = 90)

plt.legend()

plt.plot()

plt.show()