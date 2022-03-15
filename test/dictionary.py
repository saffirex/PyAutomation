dictionary = {
    "raju" : 55
    ,"babu" :56
    ,"magar" :67
}

# get(), setdefault()

y= dictionary.get("rajjiu", 20)
print(y)
print(dictionary)

dictionary.append("mamy", 66)
y=dictionary.setdefault("ratomato", 555)
print(y)
print(dictionary)