import sys
import random
import os

def Counting(square):
    result = 1
    while square>1:
        result = square**2 + result
        square = square - 1
    return result

n = int(input("Εισάγετε αριθμό μικρών τετραγώνων διατεταγμένα σε τέλειο τετράγωνο:  "))
mult = int(input("πόσες φορές επαναλαμβάνεται το μοτίβο του τετραγώνου;  "))
result = Counting(n)*mult

useless = int(input("πόσα είναι τα περιττά μικρά τετράγωνα;  "))
mult = int(input("πόσες φορές επαναλαμβάνεται το μοτίβο των περιττών τετραγώνων;  "))

useless_result = Counting(useless)*mult

print("όλα τα τετράγωνα είναι", result - useless_result)