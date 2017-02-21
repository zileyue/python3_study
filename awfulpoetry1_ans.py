#/usr/bin/python3
#coding=utf-8

import random

articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
         "heard", "felt", "slept", "hopped", "hoped", "cried",
         "laughed", "walked"]
adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]

i = 0
while i < 5:
    line = ""
    line += random.choice(articles) + " "
    line += random.choice(subjects) + " "
    line += random.choice(verbs) + " "
    j = random.randint(1,2)
    if j == 2:
        line += random.choice(adverbs) + " "
    print(line)
    i += 1
