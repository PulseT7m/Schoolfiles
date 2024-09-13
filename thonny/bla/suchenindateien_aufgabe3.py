import matplotlib.pyplot as p
var = 97
buchstabenanzahl = []
buchstabe = []
with open("text_klein.txt","w") as file:
    file.write("")
with open("text_klein.txt","a") as file_neu:
    with open("text.txt","r") as file:
        for _ in file:
            k1 = _.lower()
            k2 = k1.replace("ä","ae")
            k3 = k2.replace("ö","ue")
            k4 = k3.replace("ü","ue")
            k5 = k4.replace("ß","s")
            file_neu.write(f"{k5}")

for i in range(26):
    with open("text_klein.txt","r") as file_neu:
        anzahl = 0
        for _ in file_neu:
            anzahl += _.count(f"{chr(var)}")
        buchstabenanzahl.append(anzahl)
        buchstabe.append(f"{chr(var)}")
        var += 1
with open("text_klein.txt","r") as file:
    ger = file.read()
print(ger)
print(buchstabenanzahl)
print(buchstabe)
p.bar(buchstabe,buchstabenanzahl,linewidth=0.5)
p.show()
