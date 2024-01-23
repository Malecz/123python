import os, random

def kulonbség(orszag1, orszag2):
    if(orszag1>orszag2):
        return orszag1-orszag2
    else:
        return orszag2-orszag1

os.system("cls")
o1=random.randrange(0,21)
o2=random.randrange(0,21)
print("1. ország: ", o1,"millió fő")
print("2. ország: ",o2,"millió fő")