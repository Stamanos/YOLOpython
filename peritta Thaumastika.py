import sys

print("Παρακαλώ εισάγετε πρόταση")
long_string = sys.stdin.readline()
for i in range(1,len(long_string)-2):
    if ((long_string[i-1:i])== "!" and ((long_string[i+1:(i+2)] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") and (long_string[i+1:(i+2)] not in "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΩ"))):
        #Αν ο Χαρακτήρας αυτος ειναι θαυμαστικό και το παραεπόμενος χαρακτήρας δεμν ειναι κεφαλαίο απο τα Ελληνικά και τα Αγγλικα
        long_string = long_string[:i-1] + long_string[i:] #διεγραψε το θαμαστικό
print(long_string)


#Fo!r ex!ample! My na!me !is M!anos! I am !beautiful! and adorable!
#Γει!α σας μαγκ!ες! Ε!ιμαι ο Μανος! Αντε! γεια!






