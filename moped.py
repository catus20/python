alder = int(input("Skriv inn alderen din: "))

if alder >= 16 and alder < 18:
    print("Du kan ta moped og motorsykkel-lappen.")
elif alder >= 18:
    print("Du kan ta både motorsykkel- og bil-lappen.")
else:
    print("Du vart ikkje kvalifisert for noko førarkort.")