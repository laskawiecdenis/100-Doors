doors = [None] * 100
for i in range(1,101):
    doors[i-1] = "X"

for i in range(1,101):
    for j in range(i,101,i):
        if doors[j-1] == "X":
            doors[j-1] = "O"
        else:
            doors[j-1] = "X"

def wypisujemy(lista):
    OpenDoors = []
    for i in range(len(lista)):
        if lista[i] == "O":
            opened = str(i+1)
            OpenDoors.append(opened)
    numbers = ','.join(OpenDoors)
    OpenDoorsText = "Following doors are open: "
    print(OpenDoorsText+numbers)



print(wypisujemy(doors))
