from collections import defaultdict

def findFriends(friends,search):
    dictFriends=defaultdict(set)
    for i in friends:
        if len(i)==2:
            dictFriends[i[0].upper()].add(i[1].upper())
            dictFriends[i[1].upper()].add(i[0].upper())
        if len(i)==1:
            dictFriends[i[0].upper()].add(set)
    
    print(dictFriends)

    if search.upper() in dictFriends:
        return dictFriends[search.upper()]
    else:
        return "Not Found"

input_list = [['A','B'],['B','C'],['D']]
print(findFriends(input_list,'B'))









