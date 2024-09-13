with open("mein_satz2.txt","w") as file:
    file.write("Dies ist ein Test.")
with open("mein_satz2.txt","r") as file:
    inhalt = file.read()
print(inhalt)

with open("mein_satz2.txt","a") as file:
    file.write("Dies ist ein Test.2")
with open("mein_satz2.txt","r") as file:
    inhalt2 = file.read()
print(inhalt2)