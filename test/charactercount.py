message = 'It was a bright cold day in april, and the clocks were striking thirteen'

count= {} #this is the declaration of a dictionary with name count

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] +1 #assessing the value of key 'charcater' of the count dictionaary

print(count)