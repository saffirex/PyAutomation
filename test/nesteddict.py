allguests= {
    'Alice': {'apples': 5, 'bread': 15, 'brownie': 20}
    ,'Ram' : {'mango': 10, 'bread':55, 'brownie': 5}
    ,'Raju': {'ham': 6, 'apples':6, 'bread':6, 'banana': 6}
}
print('\n -----snip-----\n')

def totaller(itemname): #a function that receives the whole dictionary and the name of item
    count=0 #the total number of items 
    for i,j in allguests.items():  # i iterates through the keys and j iterates through the values after .items separates the dictionary items in key:value(inner dictionary) pair
        count= count+ j.get(itemname,0) # j has the inner dictionary. so .get is used for j to get the key's value from inner dictionary.
    return count
print('Number of items: \n')
print('1. Apples:' + str(totaller('apples')) )
print('1. bread:' + str(totaller('bread')) )
print('1. brownie:' + str(totaller('brownie')) )
print('1. ham:' + str(totaller('ham')) )
print('1. banana:' + str(totaller('banana')) )
print('1. mango:' + str(totaller('mango')) )


