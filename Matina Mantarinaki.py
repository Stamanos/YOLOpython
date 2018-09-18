
import sys
import random
import os

list_phrase = []
phrase = "Μαγκα μου εισαι για μια νυχτα που δεν θα ξεχασει ποτέ κανείς"       #παράδειγμα, εδω θα βάλεις το string που πήρες απο το API αγάπη μου
list_phrase = phrase.split(" ")
random.shuffle(list_phrase)
for i in range(0,len(list_phrase)-1):
    print(list_phrase[i], end=" ")






