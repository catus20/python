hemmeleg_nummer = 7

while True:
    guess = int(input("Gjett et tall mellom 1 og 10: "))

    if guess == hemmeleg_nummer:
        print("Gratulerer! Du gjettet riktig tall.")
        break
    else:
        print("Feil svar. Prøv igjen.")