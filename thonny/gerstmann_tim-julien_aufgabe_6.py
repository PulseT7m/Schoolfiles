zins=int(input("Wie lautet der Jahreszins in Prozent? "))
z=zins/100+1
kapital=int(input("Wieviel Geld wird am Anfang eingezahlt? "))
jahre=int(input("Wieviel Jahre soll das Geld drinnen bleiben? "))
def zins_reku(kapital,jahre):
    if jahre <= 0:
        return kapital
    else:
        return round(zins_reku(kapital,jahre-1)*z,2)
print(f"Mit einem Startguthaben von {kapital}€ und einem Jahreszins von {zins}% beträgt nach {jahre} Jahren das Guthaben {zins_reku(kapital,jahre)}€.")
