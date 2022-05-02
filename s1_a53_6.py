list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

list_length = len(list)

letztes = list[list_length - 1]
vorletztes = list[list_length - 2]
vorvorletztes = list[list_length - 3]

print(list)

for x in list: 
    if (list[x] == letztes):
        pass
    elif (list[x] == vorletztes):
        pass
    elif (list[x] == vorvorletztes):
        pass

    if (vorvorletztes == list[0]):
        break

    temp = list[0]
    list.append(temp)
    del list[0]


print(list)