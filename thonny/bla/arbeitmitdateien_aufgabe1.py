with open("mein_satz.txt","w") as file:
    file.write("Dies ist ein Test.")
    
with open("mein_satz.txt","r") as file:
    inhalt = file.read()
print(inhalt)