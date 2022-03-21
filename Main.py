#text
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

#users
users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

#welcome
move = 25
pomlcek = 40
oddelovac = ("-" * pomlcek)
print("-*" * 40)
print(" "* move, "Welcome in text analyzer"," "* move )
print("-*" * 40)

#lists
slova_text = []
velke = []
mala = []
caps = []
cisla = []
suma = []
delka = []
symbol = "*"
vysledek = []
hvezdicky = {}

#verification
print(oddelovac)
username = input("Username: ".lower())
password = input("password: ".lower())
print(oddelovac)

if users.get(username) == password:
    print("Welcome in to the application, ", username.title())

else:
    print("Unregistered user, termination the program...")

print(oddelovac)
choice = int(input("We have 3 texts to be analyzed. 1 and 3 to select: "))
print(oddelovac)
if choice == 1:
    text1 = TEXTS[0].split()

elif choice == 2:
    text1 = TEXTS[1].split()

elif choice == 3:
    text1 = TEXTS[2].split()
else:
    print("Did not choice the number from range, program is closed...")
for slovo in text1:
    slovo_text1 = slovo.strip(".,")
    slova_text.append(slovo_text1)
    pocet = len(slova_text)
for slovo in slova_text:
    velka = slovo.istitle()
    velke.append(velka)
for slovo in slova_text:
    male = slovo.islower()
    mala.append(male)
for slovo in slova_text:
    capse = slovo.isupper() and slovo.isalpha()
    caps.append(capse)
for slovo in slova_text:
    cislo = slovo.isdigit()
    cisla.append(cislo)
for celkem in slova_text:
    if celkem.isdigit():
        suma.append(int(celkem))
    deset = sum(suma)
for i in slovo_text1:
  delko=len(i)
  delka.append(delko)
delka = [int(i) for i in delka]



print("There are", pocet, "word in the selected text.")
print("There are", velke.count(True), "titlecase words.")
print("There are", caps.count(True), "uppercase words.")
print("There are", mala.count(True), "lowercase words.")
print("There are", cisla.count(True), "numeric strings.")
print("The sum of all the numbers", deset)

for i in slova_text:
  delko=len(i)
  delka.append(delko)
delka = [int(i) for i in delka]

for i in delka:
  vysledek1 = symbol * i
  vysledek.append(vysledek1)

for hvezda in vysledek:
  hvezdicky[hvezda] = vysledek.count(hvezda)

seradit = sorted(hvezdicky, key=hvezdicky.get, reverse=True)
print(oddelovac)
print("LEN| OCCURENCES |NR.")
print(oddelovac)
for i,_ in enumerate(range(len(seradit), 0, -1), 1):
  print(f"{i}", end=",")
  for v in seradit:
    print(f"|{v}       bob|{hvezdicky[v]}x")
    seradit.remove(v)
    break