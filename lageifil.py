frukt1 = "Eple"
frukt2 = "Plomma"
frukt3 = "Nektarin"
frukt4 = "Små grøn plomma"
frukt5 = "Banan"

with open('c:/users/emrey/documents/github/pythontests/frukt.txt', 'w') as file:
    file.write(frukt1 + '\n')
    file.write(frukt2 + '\n')
    file.write(frukt3 + '\n')
    file.write(frukt4 + '\n')
    file.write(frukt5 + '\n')

with open('c:/users/emrey/documents/gitHub/pythontests/frukt.txt', 'r') as file:
    content = file.read()
    print(content)