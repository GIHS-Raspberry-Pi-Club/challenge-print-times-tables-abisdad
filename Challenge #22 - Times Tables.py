# Challenge #22 - Times Tables up to 12...
# Challenge #22 - Times Tables.py
# By Rob Thomas
# 18/9/2017
# Ver 1.0

def timesTables():
    for i in range (1,13):
        for j in range (1,13):
            print(i*j,"", end="")
        print()

timesTables()
