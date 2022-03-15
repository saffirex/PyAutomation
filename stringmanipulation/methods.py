# join and ssplit methods
list1 = ['parrot', 'carrot', 'chariot', 'kharibot']
print(list2 := ('.pa.'.join(list1)))
print(list2.split('.pa.'))

# multiple_Assignment trick with partition method

before, separator, after = ' '.join(list1).partition('carrot')
print(before+'...'+separator+"..."+after)


# alignment or text justification
str1 = 'WELCOME TO THE GAME'
length = len(str1)
print(length)
print(str1.rjust(19+10).ljust(19+10*2))
#          WELCOME TO THE GAME
print(str1.rjust(19+10, "*").ljust(19+10*2, "*"))
# **********WELCOME TO THE GAME**********

""" or you can simply use .center(10,"*") """
