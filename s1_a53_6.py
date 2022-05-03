from lib2to3.pytree import convert


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

list_length = len(list1)

letztes = list1[list_length - 1]
vorletztes = list1[list_length - 2]
vorvorletztes = list1[list_length - 3]

print(list1)

for x in list1: 
    if (list1[x] == letztes):
        pass
    elif (list1[x] == vorletztes):
        pass
    elif (list1[x] == vorvorletztes):
        pass

    if (vorvorletztes == list1[0]):
        break

    temp = list1[0]
    list1.append(temp)
    del list1[0]


print(list1)






wort = "Donaudampfschiffahrtsgesellschaftsstewardess"

def string_to_char_list(string):
    list1=[]
    list1[:0]=string
    return list1

string_list = string_to_char_list(wort)

print(string_list)
print(len(string_list))

def delete_double(x):
    return list(dict.fromkeys(x))


print(delete_double(string_list))
print(len(delete_double(string_list)))

l3 = [[1, 2, 3,], [2,1,3], [4,0,1]]

#def sort_list(x):
#    if (l3[0][1] < l3[1][1] & l3[2][1] > l3[0][1]):
#        smallest = l3[0]
#        if (l3[1][1] < l3[2][1]):
#            mid = l3[1]
#        elif (l3[1][1] > l3[2][1]):
#            top = l3[2]
#            mid = l3[3]
#            l3[2] = mid
#            l3[3] = top
#    elif (l3[1][1] < l3[0][1] & l3[2][1] > l3[0][1]):
#        smallest = l3[1]
#        if (l3[1][1] < l3[2][1]):
#           mid = l3[1]
#        elif (l3[1][1] > l3[2][1]):
#            top = l3[2]
#            mid = l3[3]
#            l3[2] = mid
#           l3[3] = top




sound = {
    'Hund' : 'Bellt',
    'Katze' : 'Miaut',
    'Vogel' : 'Zwitschert'
}

print(sound)
print(sound['Hund'])


