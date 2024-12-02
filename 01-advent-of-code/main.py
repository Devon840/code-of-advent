#day one of advent of code


list1 = [1,2,4,6]
list2 = [2,2,5,7]

list1.sort()
list2.sort()

distance = []

index = 0

for x in range(len(list2)):
    added = list1[index]+list2[index]
    subtract = list1[index]-list2[index]
    #print(added)
    print(subtract)
    distance.append(subtract)
    index +=1


print(distance)
