with open("liczby.txt") as file:
    liczby = file.read().splitlines()

wiecej_zer = 0

for i in liczby:
    if i.count('0') > i.count('1'):
        wiecej_zer += 1

print(wiecej_zer)

podzielne_przez_dwa = 0
podzielne_przez_osiem = 0

for i in liczby:
    if i[-1] == '0':
        podzielne_przez_dwa += 1
    if i[-1] == '0' and i[-2] == '0' and i[-3] == '0':
        podzielne_przez_osiem += 1

print(podzielne_przez_dwa)
print(podzielne_przez_osiem)

dziesietne = []

for i in liczby:
    dziesietne.append(int(i, 2))


minimum = float("inf")
maksimum = float("-inf")

wiersz_min = 0
wiersz_max = 0

for index, x in enumerate(dziesietne):
    if x > maksimum:
        maksimum = x
        wiersz_max = index + 1
    if x < minimum:
        minimum = x
        wiersz_min = index + 1

print("{} jest minimum w wierszu {}".format(minimum, wiersz_min))
print("{} jest maksimum w wierszu {}".format(maksimum, wiersz_max))

#Czas wykonania: 21 minut