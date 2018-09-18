import sys
import random
import os


n = int(input("Καλημέρα κύριε Σταματάκη. Παρακαλώ εισάγετε την ηλικία του ανθρώπου: "))
hight = int(input("Παρακαλώ εισάγετε ύψος(χωρίς κόμμα): "))
weight = int(input("Παρακαλώ εισάγεται βάρος: "))
dis = (hight - 100 - weight)
if  ((dis < 20) and (dis > -10)):
    cal = 2000
elif (dis > 20):
    cal = 2200
elif (dis < -10):
    cal = 1700

flag = True
extra = 0
if (n < 12):
    extra = 400
elif (n < 18):
    extra = 300
elif (n < 26):
    extra = 200
elif (n < 34):
    extra = 0
else:
    extra = -250

training = int(input("Πόσες ώρες γυμνάζεται την εβδομάδα; "))
if(training < 35):
    extra = extra + training*20
else:
    print("Σιγά ρε μεγάλε που γυμνάζεσαι τόσο")
    flag = False
    print("Η Συνιστώμενη ημερήσια κατανάλωση σε θερμίδες για εσένα είναι όσο τρώει ο Superman")

if (flag):
    rightCal = cal + extra
    print("Η Συνιστώμενη ημερήσια κατανάλωση σε θερμίδες για εσένα είναι", rightCal)