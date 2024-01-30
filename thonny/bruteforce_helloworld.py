import random
import sys
import time
import timeit
import matplotlib.pyplot as plt
anzahlen=[]
zeiten=[]
targetArray = ["H","e","l","l","o"," ","w","o","r","l","d","!" ]
stringArray = ["","","","","","","","","","","",""]
i=0
count = 0
while i < len(targetArray):
    global start
    start=timeit.default_timer()
    if stringArray[i] != targetArray[i]:
        stringArray[i] = chr(random.randint(0,256))

    if stringArray[i] == targetArray[i]:
        i += 1


    x = 0
    print("\n")
    while x< len(stringArray):
        print(stringArray[x]  , end = "" , flush = True)
        x += 1
        count += 1
    time.sleep(.01)
    global stop
    stop=timeit.default_timer()
    zeit=stop-start
    anzahlen.append(count)
    zeiten.append(zeit)

print("\nTotal Gusses is :",count)
plt.plot(anzahlen,zeiten)
plt.show()
print(anzahlen)
print(zeiten)





