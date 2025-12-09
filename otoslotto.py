import random

tipp=[]
#tippek bekerese es listaba tetele, hibakod kiirasa adott esetekben
while len(tipp) < 5:
    try:
        szam = int(input(f"Adj meg egy számot 1-90 között, még {5 - len(tipp)} kell: "))
        if 1 <= szam <= 90 and szam not in tipp:
            tipp.append(szam)
        else:
            print(f"Ez már volt vagy túl nagy szám!!")
    except ValueError:
        print(f"Csak számot adj meg!")

#tippek szortirozasa kesobbi vizsgalatokhoz
tipp.sort()

#szamok soroslasa
sors = sorted(random.sample(range(1, 91), 5))

#talalatok megkeresese
talalatok = [i for i in tipp if i in sors]

print(f"\n EREDMÉNYEID:")
print(f"Tipped:  {tipp}")
print(f"Sorsolt: {sors}")
print(f"Találat: {len(talalatok)} db")
if talalatok:
    print(f"Talált számok: {talalatok}")