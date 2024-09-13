import random as r
wort = []
with open("abc_wort.txt","w") as file:
    file.write("")
with open("abc_wort.txt","a") as file:
    for i in range(50):
        wort = []
        for x in range(10):
            wort.append(r.randint(97,99))
        for _ in range(len(wort)-1):
            u = chr(wort[_])
            file.write(f"{u}")
        file.write("\n")
with open("aaa_woerter.txt","w") as file:
    file.write("")
with open("aaa_woerter.txt","a") as file_neu:
    with open("abc_wort.txt","r") as file:
        for i in file:
            b = i.strip()
            if "aaa" in b:
                file_neu.write(f"{b} \n")
with open("aaa_woerter.txt","r") as file:
    ger = file.read()
print(ger)