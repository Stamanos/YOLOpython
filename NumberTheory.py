import sys
import random
import os

#Εισαγωγή Μ bits
M = int(input("Παρακαλώ εισάγετε τα Bits > 1: "))

DoNotFound = True #Λογική μεταβλητή που μας δείχνει αν βρέθηκε πρώτος ή όχι
while DoNotFound: #Ο βρόγχος δεν θα σταματήσει μέχρι να βρει έναν πρώτο αριθμό
    DoNotFound = False #Έστω πως ο αριθμός που θα διαλεχτεί τυχαία είναι πρώτος, μέχρι να αποδειχτεί το αντίθετο
    Pass = True  # Λογική μεταβλητή για να μην περνάει σε κωδικα ξέροντας πως είναι σύνθετος

    # Εύρεση τυχαίου αριθμού n στο όπου 2^(Μ-1) < n < 2^Μ
    from random import randint  # συνάρτηση τυχαίας αναζήτησης
    Down = 2 ** (M - 1)  # Κάτω όριο
    Top = 2 ** M  # Πάνω όριο
    n = randint(Down, Top)
    while True:  # και ελέγχω αν ειναι περιττός γιατί δεν γίνεται να είναι πρώτος και άριος > 2
        if (n % 2 == 1) or (n == 2):
            break
        else:
            n = randint(Down, Top)

    # Απλός αλγόριθμος που ελέγχω αν δεν είναι πρώτος ο αριθμός διαιρώντας τον με μερικούς πρώτους για να δω αν το υπόλοιπο κάνει 0
    if ((n % 3 == 0) or (n % 5 == 0) or (n % 7 == 0) or (n % 11 == 0) or (n % 13 == 0) or (n % 17 == 0) or (
                    n % 19 == 0) or (n % 23 == 0)):
        Pass = False
        DoNotFound = True
        print(n, "Είναι Σύνθετος")

    if Pass: #Για βελτιστοποίηση
        # Εύρεση αριθμού k και u όπου n-1= u*(2^k)
        k = 0
        m = n - 1
        Flag = True
        while Flag:
            if (m % 2 == 0):
                k = k + 1
                m = m / 2
            else:
                Flag = False
        m = round(m)
        # Άλλαξα τον τύπο μεταβλητής σε int από float γιατί δεν θα γίνονται παρακάτω πράξεις μεταξύ int και float

        # Εύρεση τυχαίου αριθμού a όπου 1 < a < n-1
        from random import randint  # συνάρτηση τυχαίας αναζήτησης
        a = randint(1, n-1) #Τελείως τυχαίο ακέραιο


        b = ((a ** m) % n)
        if ((b != 1) or (b != -1)):
            DoNotFound = False #Δηλαδή βρέθηκε ο πρώτος
        else:
            F = True
            for x in range(0, k - 1):
                b = (b ** 2) % n
                if ((b - 1) % n == 0):
                    #Ο gcd(b-1, n) δίνει μη τετριμένο παράγοντα του n)
                    DoNotFound = True
                if ((b + 1) % n == 0):
                    print(n, "Πιθανά πρώτος")
                    DoNotFound = False
                    F = False #Για να δω άν μπηκε να κανει την εντολή break
                    break

            if F:
                DoNotFound = True
                print("O", n, "σύνθετος")



print("Ο αριθμός ", n, "πέρασε τον έλεγχο και είναι πρώτος με μεγάλη πιθανότητα")